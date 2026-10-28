#!/usr/bin/env python3
"""Draft ground-truth lyrics from LRCLIB's time-synced lyrics.

    python scripts/draft_lyrics.py            # all segments missing drafts
    python scripts/draft_lyrics.py godzilla-v3 --force

For each segment, searches lrclib.net (open API, no auth) for synced lyrics,
keeps the lines whose sync timestamps fall in the segment's [start, end]
window, and writes them to lyrics/<id>.txt as a DRAFT.

Drafts are NOT ground truth: LRC timing drifts, community lyrics have errors,
and fast passages are exactly where they're wrong. Read along with the audio
once, fix discrepancies, then delete the TODO-VERIFY line — the scorer
ignores the file until you do.
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
from rapbench import LYRICS_DIR, load_segments

LRC_LINE = re.compile(r"\[(\d+):(\d+(?:\.\d+)?)\](.*)")
# Sync timestamps mark line starts; a line beginning slightly before the
# window can still be mostly inside it.
PAD_BEFORE = 3.0


def lrclib(path: str) -> object:
    """GET with retries: LRCLIB answers bursts with 429/503."""
    for attempt in range(4):
        try:
            with urllib.request.urlopen(f"https://lrclib.net/api/{path}") as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code not in (429, 503) or attempt == 3:
                raise
            time.sleep(5 * (attempt + 1))


def search_lrclib(artist: str, track: str) -> dict | None:
    """Exact-match lookup first: it is the entry select_fresh.py chose the
    window from, so the stamps agree. Search is the fallback."""
    query = urllib.parse.urlencode({"artist_name": artist, "track_name": track})
    hit = lrclib(f"get?{query}")
    if isinstance(hit, dict) and hit.get("syncedLyrics"):
        return hit
    for r in lrclib(f"search?{query}") or []:
        if r.get("syncedLyrics"):
            return r
    return None


def window_lines(synced: str, start: float, end: float) -> list[str]:
    lines = []
    for raw in synced.splitlines():
        m = LRC_LINE.match(raw.strip())
        if not m:
            continue
        t = int(m.group(1)) * 60 + float(m.group(2))
        text = m.group(3).strip()
        if text and start - PAD_BEFORE <= t < end:
            lines.append(text)
    return lines


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("segments", nargs="*", help="segment ids (default: all)")
    parser.add_argument("--force", action="store_true", help="overwrite existing lyric files")
    args = parser.parse_args()

    for seg in load_segments():
        if args.segments and seg["id"] not in args.segments:
            continue
        out = LYRICS_DIR / f"{seg['id']}.txt"
        existing = out.read_text() if out.exists() else "TODO"
        if not args.force and "TODO" not in existing:
            print(f"  {seg['id']}: already has lyrics, skipping (--force to overwrite)")
            continue

        lrclib = seg.get("lrclib") or {}
        artist = lrclib.get("artist", seg["artist"])
        track = lrclib.get("track", seg["track"])
        hit = search_lrclib(artist, track)
        if not hit:
            print(f"  {seg['id']}: no synced lyrics on lrclib for {artist} — {track}")
            continue

        lines = window_lines(hit["syncedLyrics"], seg["start"], seg["end"])
        if not lines:
            print(f"  {seg['id']}: synced lyrics found but empty window, check timestamps")
            continue

        header = (
            f"# DRAFT from lrclib.net (id {hit['id']}: {hit['artistName']} — "
            f"{hit['trackName']}, {hit['duration']:.0f}s), trimmed to "
            f"{seg['start']}-{seg['end']}s.\n"
            f"# Read along with audio/{seg['id']}.wav, fix what's actually rapped,\n"
            f"# then delete the TODO-VERIFY line below.\n"
            f"TODO-VERIFY\n"
        )
        out.write_text(header + "\n".join(lines) + "\n")
        print(f"  {seg['id']}: drafted {len(lines)} lines from lrclib id {hit['id']}")


if __name__ == "__main__":
    main()
