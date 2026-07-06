#!/usr/bin/env python3
"""Download and trim benchmark audio from the URLs in segments.yaml.

The published repo ships no audio and no URLs — fill in `url:` for each
segment with your own source, then:

    python scripts/fetch.py            # all segments with a url
    python scripts/fetch.py rap-god-fast

Requires yt-dlp and ffmpeg on PATH. Output: audio/<id>.wav, 16 kHz mono,
trimmed to [start, end] from the manifest.
"""

import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from rapbench import AUDIO_DIR, load_segments


def fetch(segment: dict) -> None:
    out = AUDIO_DIR / f"{segment['id']}.wav"
    if out.exists():
        print(f"  {segment['id']}: already fetched, skipping")
        return
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "full.wav"
        subprocess.run(
            ["yt-dlp", "-x", "--audio-format", "wav", "-o", str(src), segment["url"]],
            check=True,
        )
        subprocess.run(
            [
                "ffmpeg", "-hide_banner", "-loglevel", "error",
                "-ss", str(segment["start"]), "-to", str(segment["end"]),
                "-i", str(src), "-ac", "1", "-ar", "16000", str(out),
            ],
            check=True,
        )
    print(f"  {segment['id']}: wrote {out}")


def main() -> None:
    only = set(sys.argv[1:])
    AUDIO_DIR.mkdir(exist_ok=True)
    failed = []
    for seg in load_segments():
        if only and seg["id"] not in only:
            continue
        if not seg.get("url"):
            print(f"  {seg['id']}: no url in segments.yaml, skipping")
            continue
        try:
            fetch(seg)
        except subprocess.CalledProcessError as e:
            failed.append(seg["id"])
            print(f"  {seg['id']}: FAILED ({e})")
    if failed:
        sys.exit(f"failed: {', '.join(failed)}")


if __name__ == "__main__":
    main()
