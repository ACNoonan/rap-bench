#!/usr/bin/env python3
"""Extract vocal stems from fetched audio with demucs (htdemucs).

    pip install demucs
    python scripts/separate.py

Output: stems/<id>_vocals.wav (16 kHz mono, matching audio/).
Stems stay local — the stems/ directory is gitignored.
"""

import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from rapbench import AUDIO_DIR, STEMS_DIR, load_segments


def separate(segment_id: str) -> None:
    src = AUDIO_DIR / f"{segment_id}.wav"
    out = STEMS_DIR / f"{segment_id}_vocals.wav"
    if not src.exists():
        print(f"  {segment_id}: no audio (run scripts/fetch.py first), skipping")
        return
    if out.exists():
        print(f"  {segment_id}: already separated, skipping")
        return
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(
            ["demucs", "--two-stems", "vocals", "-n", "htdemucs", "-o", tmp, str(src)],
            check=True,
        )
        vocals = Path(tmp) / "htdemucs" / segment_id / "vocals.wav"
        subprocess.run(
            [
                "ffmpeg", "-hide_banner", "-loglevel", "error",
                "-i", str(vocals), "-ac", "1", "-ar", "16000", str(out),
            ],
            check=True,
        )
    print(f"  {segment_id}: wrote {out}")


def main() -> None:
    STEMS_DIR.mkdir(exist_ok=True)
    for seg in load_segments():
        separate(seg["id"])


if __name__ == "__main__":
    main()
