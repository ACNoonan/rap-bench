#!/usr/bin/env python3
"""Scout post-cutoff fast rap: tracks the ASR roster cannot have trained on.

    python scripts/scout.py "Eminem" "Tech N9ne" ...      # artists to scan
    python scripts/scout.py --file scripts/scout_artists.txt --after 2025-06-01

For each artist, lists the tracks of every MusicBrainz release group first
released on or after --after, fetches each track's time-synced lyrics from
LRCLIB by exact artist and title, and estimates the peak syllable rate from the sync stamps:
syllables in a run of consecutive lines divided by the time from the first
line's stamp to the stamp after the last. Writes results/scout.md, fastest
first.

The rate is a screen, not a measurement. LRC stamps drift and community
lyrics drop words in exactly the fast passages, so a candidate's rate is
re-measured from verified lyrics before it goes in segments.yaml. Window
minimum is 12 s so one mistimed line can't fake a 20 syl/s burst.
"""

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from rapbench import RESULTS_DIR
from synth import count_syllables

LRC_LINE = re.compile(r"\[(\d+):(\d+(?:\.\d+)?)\](.*)")
UA = "rap-bench/0.1 (research; adamcnoonan@gmail.com)"
MIN_WINDOW = 12.0
MAX_WINDOW = 45.0


def get(url: str) -> object:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def mb(path: str) -> dict:
    """MusicBrainz asks for at most one request a second."""
    for attempt in range(4):
        time.sleep(1.1 * (attempt + 1))
        try:
            return get(f"https://musicbrainz.org/ws/2/{path}")
        except urllib.error.HTTPError as e:
            if e.code not in (429, 503) or attempt == 3:
                raise
    return {}


def post_cutoff_tracks(artist: str, after: str) -> list[tuple[str, str, str]]:
    """(track title, release title, first release date) for every track on a
    release group by `artist` first released on or after `after`."""
    q = urllib.parse.quote(f'artist:"{artist}" AND firstreleasedate:[{after} TO *]')
    groups = mb(f"release-group?query={q}&fmt=json&limit=50").get("release-groups", [])
    out, seen = [], set()
    for g in groups:
        credit = " ".join(c.get("name", "") for c in g.get("artist-credit", []))
        if g.get("score", 0) < 90 or artist.lower() not in credit.lower() or not g.get("releases"):
            continue
        rel = mb(f"release/{g['releases'][0]['id']}?inc=recordings&fmt=json")
        for medium in rel.get("media", []):
            for t in medium.get("tracks", []):
                key = t["title"].lower()
                if key not in seen:
                    seen.add(key)
                    out.append((t["title"], g["title"], g.get("first-release-date", "")))
    return out


def earliest_recording(artist: str, track: str) -> str | None:
    """Earliest first-release-date of any recording with this artist and
    title. Release-group dates aren't enough: compilations and reissues
    (STANS 2025, Music To Be Murdered By [Epilogue] 2026) carry old songs,
    sometimes as new recording entities with the reissue's date."""
    clean = re.sub(r"\s*[\(\[].*?[\)\]]", "", track).replace('"', "")
    q = urllib.parse.quote(f'recording:"{clean}" AND artist:"{artist}"')
    res = mb(f"recording?query={q}&fmt=json&limit=50")
    dates = [r["first-release-date"] for r in res.get("recordings", [])
             if r.get("score", 0) >= 90 and r.get("first-release-date")]
    return min(dates) if dates else None


def lrclib_synced(artist: str, track: str) -> str | None:
    q = urllib.parse.urlencode({"artist_name": artist, "track_name": track})
    time.sleep(0.5)
    try:
        r = get(f"https://lrclib.net/api/get?{q}")
    except Exception:
        return None
    return r.get("syncedLyrics") if isinstance(r, dict) else None


def peak_rate(synced: str) -> tuple[float, float, float]:
    """(syl/s, window start s, window length s) of the fastest run of lines."""
    lines = []
    for raw in synced.splitlines():
        m = LRC_LINE.match(raw.strip())
        if m:
            lines.append((int(m.group(1)) * 60 + float(m.group(2)), m.group(3).strip()))
    best = (0.0, 0.0, 0.0)
    for i in range(len(lines)):
        syl = 0
        for j in range(i, len(lines) - 1):
            syl += count_syllables(lines[j][1])
            dur = lines[j + 1][0] - lines[i][0]
            if dur > MAX_WINDOW:
                break
            if dur >= MIN_WINDOW and syl / dur > best[0]:
                best = (syl / dur, lines[i][0], dur)
    return best


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("artists", nargs="*")
    p.add_argument("--file", type=Path)
    p.add_argument("--after", default="2025-06-01", help="keep first releases on or after this date")
    p.add_argument("--min-rate", type=float, default=5.0)
    args = p.parse_args()
    artists = list(args.artists)
    if args.file:
        artists += [a.strip() for a in args.file.read_text().splitlines() if a.strip() and not a.startswith("#")]

    rows = []
    for artist in artists:
        try:
            tracks = post_cutoff_tracks(artist, args.after)
        except Exception as e:
            print(f"{artist}: musicbrainz failed ({e})")
            continue
        print(f"{artist}: {len(tracks)} post-cutoff tracks")
        for title, album, released in tracks:
            synced = lrclib_synced(artist, title)
            if not synced:
                continue
            rate, start, dur = peak_rate(synced)
            if rate < args.min_rate:
                continue
            earliest = earliest_recording(artist, title)
            if earliest and earliest < args.after:
                print(f"  drop {title}: earlier recording {earliest}")
                continue
            rows.append((rate, artist, title, album, released, start, dur))
            print(f"  {rate:5.1f} syl/s  {title}  ({released})")

    rows.sort(reverse=True)
    lines = [
        "# Post-cutoff scout",
        "",
        f"Tracks first released on or after {args.after} (MusicBrainz), with LRCLIB synced lyrics, "
        f"peak rate ≥ {args.min_rate} syl/s over a {MIN_WINDOW:.0f}–{MAX_WINDOW:.0f} s window. "
        "Rates are a screen from community sync stamps, not measurements. "
        "Written by `scripts/scout.py`.",
        "",
        "| peak syl/s | artist | track | album | first release | window |",
        "|---|---|---|---|---|---|",
    ]
    for rate, artist, track, album, released, start, dur in rows:
        lines.append(f"| {rate:.1f} | {artist} | {track} | {album} | {released} | "
                     f"{int(start // 60)}:{start % 60:04.1f} +{dur:.0f}s |")
    RESULTS_DIR.mkdir(exist_ok=True)
    (RESULTS_DIR / "scout.md").write_text("\n".join(lines) + "\n")
    print(f"wrote {RESULTS_DIR / 'scout.md'} ({len(rows)} candidates)")


if __name__ == "__main__":
    main()
