#!/usr/bin/env python3
"""Turn scouted tracks into fresh-population segments in segments.yaml.

    python scripts/select_fresh.py            # the PICKS below
    python scripts/select_fresh.py --dry-run  # print, don't write

For each pick: fetch LRCLIB synced lyrics, choose the densest window of
25-40 s by syllables per second (line-start stamps, so bounds land on line
boundaries), find an official-audio upload with yt-dlp, and keep it only if
its duration is within 3 s of LRCLIB's (sync stamps are album-relative; a
music-video cut with an intro would shift every bound). Appends entries
with population: fresh, timing_verified: false, lyrics_verified: false and
syl_per_sec as the draft's mean rate. Both flags stay false until Adam
checks the clip by ear; draft_lyrics.py then writes the TODO-VERIFY draft.

Picks were chosen from results/scout.md (2026-10-28) for rate spread and
artist spread: at most three per artist.
"""

import argparse
import json
import subprocess
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import yaml
from rapbench import REPO_ROOT, load_segments
from scout import LRC_LINE, get
from synth import count_syllables

PICKS = [
    ("GAWNE", "TITANIC"),
    ("GAWNE", "Nightmares"),
    ("JID", "Animals (Pt. I)"),
    ("JID", "Sk8"),
    ("JID", "Behold"),
    ("Token", "Never Me"),
    ("Token", "The Ropes"),
    ("Token", "Kumquat"),
    ("Joyner Lucas", "GTA 6"),
    ("Joyner Lucas", "One of Them"),
    ("Joyner Lucas", "Monsters"),
    ("Tech N9ne", "Black Walt Street (The New Breed)"),
    ("Tech N9ne", "The Nice One"),
    ("Logic", "Call Them Less"),
    ("NF", "GIVE ME A REASON"),
    ("Merkules", "Bad News"),
    ("Ren", "Richard’s Tale: Set the Scene"),
    ("Dax", "Caught You in the Bed"),
    ("King Iso", "Crash Out"),
    ("Chris Webby", "Raw Thoughts VII"),
    ("Doja Cat", "Jealous Type"),
]
MIN_WIN, MAX_WIN = 25.0, 40.0
DURATION_TOL = 3.0


def slug(artist: str, track: str) -> str:
    s = f"{track}-{artist}".lower().replace("’", "").replace("'", "")
    return "fresh-" + "-".join("".join(c if c.isalnum() else " " for c in s).split())


def densest(synced: str) -> tuple[float, float, float, list[str]] | None:
    lines = []
    for raw in synced.splitlines():
        m = LRC_LINE.match(raw.strip())
        if m:
            lines.append((int(m.group(1)) * 60 + float(m.group(2)), m.group(3).strip()))
    best = None
    for i in range(len(lines)):
        syl = 0
        for j in range(i, len(lines) - 1):
            syl += count_syllables(lines[j][1])
            dur = lines[j + 1][0] - lines[i][0]
            if dur > MAX_WIN:
                break
            if dur >= MIN_WIN and (best is None or syl / dur > best[0]):
                best = (syl / dur, lines[i][0], lines[j + 1][0], [l for _, l in lines[i:j + 1] if l])
    return best


def youtube(artist: str, track: str, want: float) -> tuple[str, float] | None:
    """Official-audio search first, then a broader one; first upload whose
    duration matches LRCLIB's wins."""
    out = ""
    for query in (f"ytsearch5:{artist} {track} official audio", f"ytsearch10:{artist} {track}"):
        out += subprocess.run(
            ["yt-dlp", query, "--print", "%(id)s\t%(duration)s\t%(title)s", "--skip-download", "--no-warnings"],
            capture_output=True, text=True, timeout=300,
        ).stdout
    for row in out.splitlines():
        vid, dur, title = (row.split("\t") + ["", ""])[:3]
        try:
            d = float(dur)
        except ValueError:
            continue
        if abs(d - want) <= DURATION_TOL:
            return f"https://www.youtube.com/watch?v={vid}", d
    return None


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    have = {s["id"] for s in load_segments()}
    entries = []
    for artist, track in PICKS:
        sid = slug(artist, track)
        if sid in have:
            print(f"  {sid}: already in segments.yaml")
            continue
        q = urllib.parse.urlencode({"artist_name": artist, "track_name": track})
        try:
            hit = get(f"https://lrclib.net/api/get?{q}")
        except Exception as e:
            print(f"  {sid}: lrclib failed ({e})")
            continue
        win = densest(hit.get("syncedLyrics") or "")
        if not win:
            print(f"  {sid}: no {MIN_WIN:.0f}-{MAX_WIN:.0f} s window")
            continue
        rate, start, end, _ = win
        yt = youtube(artist, track, hit["duration"])
        if not yt:
            print(f"  {sid}: no upload within {DURATION_TOL:.0f} s of lrclib's {hit['duration']:.0f} s")
            continue
        url, dur = yt
        start, end = round(max(start - 0.3, 0), 1), round(end, 1)
        entries.append({
            "id": sid, "population": "fresh", "artist": artist, "track": track,
            "lrclib": {"artist": hit["artistName"], "track": hit["trackName"]},
            "url": url, "start": start, "end": end, "syl_per_sec": round(rate, 2),
            "tier": "baseline" if rate < 6 else "fast" if rate < 8 else "insane",
            "timing_verified": False, "lyrics_verified": False,
            "notes": f"fresh tier (DESIGN.md v3). Window and rate from lrclib id {hit['id']} sync stamps; "
                     f"upload {dur:.0f}s vs lrclib {hit['duration']:.0f}s. Re-measure rate after verification.",
        })
        print(f"  {sid}: {rate:.2f} syl/s mean, {start}-{end}s, {url}")

    if args.dry_run or not entries:
        return
    block = yaml.safe_dump(entries, sort_keys=False, allow_unicode=True, width=100)
    block = "\n".join("  " + l if l else l for l in block.splitlines())
    with open(REPO_ROOT / "segments.yaml", "a") as f:
        f.write("\n  # --- fresh tier: released after every roster model (DESIGN.md v3) ---\n" + block + "\n")
    print(f"appended {len(entries)} segments")


if __name__ == "__main__":
    main()
