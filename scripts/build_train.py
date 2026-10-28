#!/usr/bin/env python3
"""Build the v4 fine-tuning set: whole rap songs cut into <= 28 s chunks
labelled from LRCLIB's synced lyrics (DESIGN.md v4).

    python scripts/build_train.py plan  --artists scripts/train_artists.txt
    python scripts/build_train.py fetch [--workers 4]
    python scripts/build_train.py chunk
    python scripts/build_train.py check     # leak + size report, exits 1 on a leak

plan   MusicBrainz albums per artist -> tracks -> LRCLIB synced lyrics,
       screened by peak syllable rate. Writes train/candidates.jsonl.
fetch  yt-dlp audio for each candidate, kept only if its duration is within
       3 s of LRCLIB's (sync stamps are album-relative). train/audio/<id>.wav,
       16 kHz mono, whole song.
chunk  Consecutive lyric lines grouped into windows of at most 28 s (whisper
       sees 30 s), broken at blank stamps and long gaps. train/manifest.jsonl.

The leak rule is enforced here, not remembered: no track whose MusicBrainz
artist credit or title names an artist credited on any exhibition or fresh
segment (EVAL_ARTISTS below, built from segments.yaml plus the features on
the exhibition tracks). `check` re-verifies the finished manifest against
the same list and also refuses any track title that matches an eval track.

Labels are community lyrics: timing drifts and fast passages lose words.
That's accepted training noise. 5% of songs (by hash) are held out as a
validation split so training loss has an in-distribution check; the real
evaluation is the fresh tier, which nothing here can touch.

Everything under train/ is gitignored (whole-song audio and whole-song
lyrics), but rsync ships it to the GPU box with the working tree.
"""

import argparse
import hashlib
import json
import random
import re
import subprocess
import sys
import tempfile
import time
import unicodedata
import urllib.error
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from rapbench import REPO_ROOT, load_segments
from scout import LRC_LINE, get, mb, peak_rate
from select_fresh import YTDLP, youtube
from synth import count_syllables

TRAIN = REPO_ROOT / "train"
CANDIDATES = TRAIN / "candidates.jsonl"
MANIFEST = TRAIN / "manifest.jsonl"
AUDIO = TRAIN / "audio"

# Guests on exhibition tracks that segments.yaml doesn't credit. Worldwide
# Choppers and Speedom are posse cuts; every voice on them is held out.
EXHIBITION_FEATURES = [
    "Krizz Kaliko", "Ceza", "D-Loc", "JL", "Yelawolf", "Twisted Insane", "U$O",
    "Juice WRLD",  # Godzilla
    "Lil Wayne",   # Look at Me Now (the clip is Busta's verse; every voice on the track is held out)
]
MAX_CHUNK = 28.0
MIN_CHUNK = 4.0
MAX_LINE = 10.0     # a "line" longer than this has swallowed an instrumental gap
MIN_PEAK = 5.0      # syl/s screen, same as scout.py
PER_ARTIST = 12
VAL_SHARE = 0.05


def fold(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9$]+", " ", s).strip()
    # "J.I.D" folds to "j i d"; join runs of single letters so it matches "jid"
    return re.sub(r"\b(?:[a-z] )+[a-z]\b", lambda m: m.group().replace(" ", ""), s)


def eval_artists() -> list[str]:
    names = set(EXHIBITION_FEATURES)
    for s in load_segments():
        if s.get("population") in ("exhibition", "fresh"):
            names.add(s["artist"])
            names.add((s.get("lrclib") or {}).get("artist", s["artist"]))
    out = set()
    for n in names:
        # "Chris Brown, track: Look at Me Now}" style leftovers, and "A & B"
        for part in re.split(r",|&| feat\.? | ft\.? | x ", n.split("track:")[0]):
            if fold(part):
                out.add(fold(part))
    return sorted(out)


def eval_titles() -> set[str]:
    return {fold(re.sub(r"\s*[\(\[].*?[\)\]]", "", s["track"])) for s in load_segments()
            if s.get("population") in ("exhibition", "fresh") and s.get("track")}


def names_held_out(text: str, held: list[str]) -> str | None:
    t = f" {fold(text)} "
    for h in held:
        if f" {h} " in t:
            return h
    return None


def song_id(artist: str, title: str) -> str:
    s = fold(f"{artist} {title}").replace(" ", "-")[:60]
    return f"{s}-{hashlib.sha1((artist + title).encode()).hexdigest()[:6]}"


def plan(args) -> None:
    held = eval_artists()
    titles = eval_titles()
    artists = [a.strip() for a in Path(args.artists).read_text().splitlines()
               if a.strip() and not a.startswith("#")]
    TRAIN.mkdir(exist_ok=True)
    done = set()
    if CANDIDATES.exists():
        for l in CANDIDATES.read_text().splitlines():
            r = json.loads(l)
            done.add(r["query_artist"])
    with open(CANDIDATES, "a") as out:
        for artist in artists:
            if artist in done:
                continue
            if names_held_out(artist, held):
                print(f"{artist}: held out (eval artist), skipping")
                continue
            q = urllib.parse.quote(f'artist:"{artist}" AND primarytype:album AND status:official')
            try:
                groups = mb(f"release-group?query={q}&fmt=json&limit=40").get("release-groups", [])
            except Exception as e:
                print(f"{artist}: musicbrainz failed ({e})")
                continue
            kept, seen = 0, set()
            for g in groups:
                credit = " ".join(c.get("name", "") + c.get("joinphrase", "") for c in g.get("artist-credit", []))
                if g.get("score", 0) < 90 or fold(artist) not in fold(credit) or not g.get("releases"):
                    continue
                if set(g.get("secondary-types", [])) & {"Compilation", "Live", "Remix", "DJ-mix"}:
                    continue
                if kept >= PER_ARTIST:
                    break
                try:
                    rel = mb(f"release/{g['releases'][0]['id']}?inc=recordings+artist-credits&fmt=json")
                except Exception:
                    continue
                todo = []
                for medium in rel.get("media", []):
                    for t in medium.get("tracks", []):
                        title = t["title"]
                        tcredit = " ".join(c.get("name", "") + c.get("joinphrase", "")
                                           for c in t.get("artist-credit", [])) or credit
                        key = fold(re.sub(r"\s*[\(\[].*?[\)\]]", "", title))
                        if key in seen:
                            continue
                        seen.add(key)
                        leak = names_held_out(f"{tcredit} {title}", held)
                        if leak:
                            print(f"  skip {title}: credits {leak}")
                            continue
                        if key in titles:
                            print(f"  skip {title}: eval title")
                            continue
                        todo.append((title, tcredit))
                # LRCLIB lookups in parallel; MusicBrainz above stays serial at 1/s.
                with ThreadPoolExecutor(2) as ex:
                    synced_all = list(ex.map(lambda tc: lrclib_get(artist, tc[0]), todo))
                for (title, tcredit), hit in zip(todo, synced_all):
                    synced = (hit or {}).get("syncedLyrics")
                    if not synced or kept >= PER_ARTIST:
                        continue
                    rate = peak_rate(synced)[0]
                    if rate < MIN_PEAK:
                        continue
                    r = {"query_artist": artist, "artist": artist, "title": title, "credit": tcredit,
                         "album": g["title"], "released": g.get("first-release-date", ""),
                         "peak": round(rate, 2), "id": song_id(artist, title)}
                    out.write(json.dumps(r) + "\n")
                    out.flush()
                    kept += 1
                    print(f"  {rate:5.1f}  {artist} — {title}")
            # a marker row so a resumed plan skips artists with zero keepers
            out.write(json.dumps({"query_artist": artist, "marker": True}) + "\n")
            print(f"{artist}: {kept} kept", flush=True)
    print(f"plan done; LRCLIB gave up on {len(GAVE_UP)} lookups")


GAVE_UP = []


def lrclib_get(artist: str, title: str) -> dict | None:
    """Exact-match LRCLIB lookup. LRCLIB answers about half of requests with
    503 ServerOverloaded under load (2026-10-28), so retry up to 10 times
    with jittered backoff. A lookup that still fails is logged and counted
    (LRCLIB-GAVE-UP), never dropped silently as scout.lrclib_synced does."""
    q = urllib.parse.urlencode({"artist_name": artist, "track_name": title})
    for attempt in range(10):
        try:
            hit = get(f"https://lrclib.net/api/get?{q}")
            return hit if isinstance(hit, dict) else None
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code not in (429, 500, 502, 503, 504):
                raise
        except (urllib.error.URLError, TimeoutError):
            pass
        time.sleep(min(60, 3 * 2 ** attempt * 0.5) + random.random() * 2)
    GAVE_UP.append(f"{artist} — {title}")
    print(f"  LRCLIB-GAVE-UP {artist} — {title}", flush=True)
    return None


def candidates() -> list[dict]:
    """Planned songs, deduplicated by id (a plan interrupted mid-artist
    replays that artist on resume)."""
    rows = {}
    for r in map(json.loads, CANDIDATES.read_text().splitlines()):
        if not r.get("marker"):
            rows.setdefault(r["id"], r)
    return list(rows.values())


def fetch_one(r: dict) -> str:
    out = AUDIO / f"{r['id']}.wav"
    lrc_path = AUDIO / f"{r['id']}.lrc.json"
    if out.exists() and lrc_path.exists():
        return f"  {r['id']}: have"
    try:
        hit = lrclib_get(r["artist"], r["title"])
    except Exception as e:
        return f"  {r['id']}: lrclib failed ({e})"
    if not hit or not hit.get("syncedLyrics"):
        return f"  {r['id']}: lrclib has no synced lyrics now"
    yt = youtube(r["artist"], r["title"], hit["duration"])
    if not yt:
        return f"  {r['id']}: no upload within 3 s of {hit['duration']:.0f} s"
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "full.wav"
        p = subprocess.run([YTDLP, "-q", "--no-warnings", "-x", "--audio-format", "wav",
                            "-o", str(src), yt[0]], capture_output=True, text=True)
        if p.returncode or not src.exists():
            return f"  {r['id']}: download failed ({p.stderr.strip().splitlines()[-1][:120] if p.stderr.strip() else p.returncode})"
        subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(src),
                        "-ac", "1", "-ar", "16000", str(out)], check=True)
    lrc_path.write_text(json.dumps({"lrclib_id": hit["id"], "duration": hit["duration"],
                                    "url": yt[0], "synced": hit["syncedLyrics"]}))
    return f"  {r['id']}: ok ({yt[1]:.0f}s)"


def fetch(args) -> None:
    AUDIO.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(args.workers) as ex:
        for msg in ex.map(fetch_one, candidates()):
            print(msg, flush=True)
    print(f"fetch done; LRCLIB gave up on {len(GAVE_UP)} lookups")


TAG = re.compile(r"^\s*[\[\(][^\]\)]*[\]\)]\s*$")   # "[Chorus]" on its own line


def chunks(synced: str, duration: float) -> list[tuple[float, float, list]]:
    """[(start, end, [[line_start, line_end, text], ...])], absolute seconds.
    Per-line times let finetune_lora.py write timestamp-token labels."""
    lines = []
    for raw in synced.splitlines():
        m = LRC_LINE.match(raw.strip())
        if m:
            lines.append((int(m.group(1)) * 60 + float(m.group(2)), m.group(3).strip()))
    lines.append((duration, ""))
    out, cur = [], []
    def close():
        if cur:
            s, e = cur[0][0], cur[-1][1]
            text = " ".join(t for _, _, t in cur)
            if e - s >= MIN_CHUNK and len(text.split()) >= 5:
                out.append((round(max(s - 0.2, 0), 2), round(e, 2), [[round(a, 2), round(b, 2), t] for a, b, t in cur]))
            cur.clear()
    for (t, text), (t_next, _) in zip(lines, lines[1:]):
        end = min(t_next, t + MAX_LINE)
        real = text and not TAG.match(text)
        if real and cur and end - cur[0][0] > MAX_CHUNK:
            close()
        if real:
            cur.append((t, end, text))
        if not real or t_next - t > MAX_LINE:   # blank stamp, tag, or a gap: break
            close()
    close()
    return out


def chunk(args) -> None:
    rows, val_songs = [], 0
    held = eval_artists()
    for r in candidates():
        wav, lrc_path = AUDIO / f"{r['id']}.wav", AUDIO / f"{r['id']}.lrc.json"
        if not (wav.exists() and lrc_path.exists()):
            continue
        if names_held_out(f"{r['credit']} {r['artist']} {r['title']}", held):
            continue   # planned before the hold-out list grew
        lrc = json.loads(lrc_path.read_text())
        split = "val" if int(hashlib.sha1(r["id"].encode()).hexdigest(), 16) % 1000 < VAL_SHARE * 1000 else "train"
        val_songs += split == "val"
        for s, e, lines in chunks(lrc["synced"], lrc["duration"]):
            text = " ".join(t for _, _, t in lines)
            rows.append({"song": r["id"], "artist": r["artist"], "title": r["title"], "split": split,
                         "audio": f"train/audio/{r['id']}.wav", "start": s, "end": e, "text": text,
                         "lines": [[round(a - s, 2), round(b - s, 2), t] for a, b, t in lines],
                         "syl_per_sec": round(count_syllables(text) / (e - s), 2)})
    MANIFEST.write_text("".join(json.dumps(r) + "\n" for r in rows))
    hours = sum(r["end"] - r["start"] for r in rows) / 3600
    print(f"wrote {MANIFEST}: {len(rows)} chunks, {hours:.1f} h, "
          f"{len({r['song'] for r in rows})} songs ({val_songs} val), "
          f"{len({r['artist'] for r in rows})} artists")


def check(args) -> None:
    held, titles = eval_artists(), eval_titles()
    rows = [json.loads(l) for l in MANIFEST.read_text().splitlines()]
    cands = {r["id"]: r for r in candidates()}
    leaks = []
    for song in {r["song"] for r in rows}:
        c = cands[song]
        hit = names_held_out(f"{c['credit']} {c['artist']} {c['title']}", held)
        if hit or fold(re.sub(r"\s*[\(\[].*?[\)\]]", "", c["title"])) in titles:
            leaks.append((song, hit or "eval title"))
    by_split = {}
    for r in rows:
        by_split.setdefault(r["split"], []).append(r["end"] - r["start"])
    for k, v in sorted(by_split.items()):
        print(f"{k}: {len(v)} chunks, {sum(v) / 3600:.2f} h")
    if not rows:
        sys.exit("empty manifest")
    rates = sorted(r["syl_per_sec"] for r in rows)
    print(f"chunk rate p10/p50/p90: {rates[len(rates)//10]}/{rates[len(rates)//2]}/{rates[9*len(rates)//10]} syl/s")
    longest = max(r["end"] - r["start"] for r in rows)
    print(f"longest chunk: {longest:.1f} s")
    if longest > 30.0:
        leaks.append(("chunk length", f"{longest:.1f} s > 30 s: whisper would see truncated audio with full labels"))
    print(f"held-out artists checked: {len(held)}")

    # Independent of the name filter (D1): any 8 consecutive words shared
    # between a training chunk and any lyric reference in lyrics/, drafts
    # included. Catches an eval song under another title or artist credit.
    # One shared 8-gram can be a stock phrase; three or more from one song
    # against one reference is a leak.
    from rapbench.normalize import normalize
    def grams(text):
        w = normalize(text).split()
        return {tuple(w[i:i + 8]) for i in range(len(w) - 7)}
    refs = {p.stem: grams(" ".join(l for l in p.read_text().splitlines()
                                   if not l.startswith("#") and "TODO" not in l))
            for p in sorted((REPO_ROOT / "lyrics").glob("*.txt"))}
    song_grams = {}
    for r in rows:
        song_grams.setdefault(r["song"], set()).update(grams(r["text"]))
    flagged = 0
    for song, g in song_grams.items():
        for ref, rg in refs.items():
            n = len(g & rg)
            if n:
                flagged += 1
                print(f"  8-gram overlap: {song} ~ {ref}: {n}")
            if n >= 3:
                leaks.append((song, f"{n} 8-grams shared with lyrics/{ref}.txt"))
    print(f"8-gram check: {len(song_grams)} songs x {len(refs)} references, {flagged} pairs with any overlap")
    if leaks:
        for s, h in leaks:
            print(f"LEAK {s}: {h}")
        sys.exit(1)
    print("no leaks")


def main() -> None:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("plan"); a.add_argument("--artists", default="scripts/train_artists.txt")
    a = sub.add_parser("fetch"); a.add_argument("--workers", type=int, default=4)
    sub.add_parser("chunk")
    sub.add_parser("check")
    args = p.parse_args()
    {"plan": plan, "fetch": fetch, "chunk": chunk, "check": check}[args.cmd](args)


if __name__ == "__main__":
    main()
