#!/usr/bin/env python3
"""Build the synthetic speed-swept tier from a TTS-rendered verse (DESIGN.md).

    python scripts/synth.py synthetic/verse-01.txt synthetic/verse-01.wav

For each target syllable rate, time-stretches the render (pitch-preserving
ffmpeg atempo), producing an a cappella and a beat-mixed variant:

    audio/<stem>-acap-r<rate>.wav
    audio/<stem>-beat-r<rate>.wav

plus lyrics/<id>.txt (exact ground truth by construction) and manifest
entries appended to segments.yaml. The beat is synthesized numerically
(kick/snare/hat), so the whole tier is distributable.

Caveats encoded here on purpose: syllable counts use CMU-style heuristics
(±a few %), and the beat is NOT tempo-locked to the voice — it is a masking
control, not music.
"""

import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from rapbench import AUDIO_DIR, LYRICS_DIR, REPO_ROOT

TARGET_RATES = [5.0, 6.5, 8.0, 9.5, 11.0]
BEAT_BPM = 96
BEAT_GAIN = 0.35  # beat amplitude relative to voice


def count_syllables(text: str) -> int:
    total = 0
    for word in re.findall(r"[a-zA-Z']+", text.lower()):
        groups = len(re.findall(r"[aeiouy]+", word))
        if word.endswith("e") and not word.endswith(("le", "ee", "ye")) and groups > 1:
            groups -= 1
        total += max(1, groups)
    return total


def duration_of(path: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True, check=True,
    )
    return float(out.stdout.strip())


def atempo_chain(factor: float) -> str:
    """ffmpeg atempo accepts 0.5-2.0 per instance; chain for larger factors."""
    stages = []
    while factor > 2.0:
        stages.append("atempo=2.0")
        factor /= 2.0
    while factor < 0.5:
        stages.append("atempo=0.5")
        factor /= 0.5
    stages.append(f"atempo={factor:.6f}")
    return ",".join(stages)


def make_beat(path: Path, seconds: float) -> None:
    import numpy as np

    sr = 16000
    beat_len = 60 / BEAT_BPM
    n = int(sr * seconds)
    t = np.arange(n) / sr
    audio = np.zeros(n)

    def add(onset: float, sig: "np.ndarray") -> None:
        i = int(onset * sr)
        j = min(n, i + len(sig))
        if i < n:
            audio[i:j] += sig[: j - i]

    tk = np.arange(int(0.12 * sr)) / sr
    kick = np.sin(2 * np.pi * (50 + 60 * np.exp(-tk * 30)) * tk) * np.exp(-tk * 18)
    rng = np.random.default_rng(0)
    snare = rng.standard_normal(int(0.08 * sr)) * np.exp(-np.arange(int(0.08 * sr)) / sr * 40) * 0.5
    hat = rng.standard_normal(int(0.03 * sr)) * np.exp(-np.arange(int(0.03 * sr)) / sr * 120) * 0.25

    step = 0.0
    while step < seconds:
        add(step, kick)
        add(step + beat_len, snare)
        add(step + 3 * beat_len, snare)
        for k in range(8):
            add(step + k * beat_len / 2, hat)
        step += 4 * beat_len

    audio /= max(1e-9, np.abs(audio).max())
    pcm = (audio * 32767 * 0.9).astype(np.int16)
    import wave

    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(pcm.tobytes())


def main() -> None:
    verse_txt, verse_wav = Path(sys.argv[1]), Path(sys.argv[2])
    stem = verse_wav.stem.replace("verse-", "synth")
    text = verse_txt.read_text()
    syllables = count_syllables(text)
    base_dur = duration_of(verse_wav)
    base_rate = syllables / base_dur
    print(f"{verse_txt.name}: {syllables} syllables / {base_dur:.1f}s = {base_rate:.2f} syl/s base")

    entries = []
    for rate in TARGET_RATES:
        factor = rate / base_rate
        acap = AUDIO_DIR / f"{stem}-acap-r{rate}.wav"
        beat_mix = AUDIO_DIR / f"{stem}-beat-r{rate}.wav"
        subprocess.run(
            ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(verse_wav),
             "-filter:a", atempo_chain(factor), "-ac", "1", "-ar", "16000", str(acap)],
            check=True,
        )
        dur = duration_of(acap)
        beat_wav = acap.with_suffix(".beat-only.tmp.wav")
        make_beat(beat_wav, dur)
        subprocess.run(
            ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(acap), "-i", str(beat_wav),
             "-filter_complex", f"[1:a]volume={BEAT_GAIN}[b];[0:a][b]amix=inputs=2:duration=first:normalize=0",
             "-ac", "1", "-ar", "16000", str(beat_mix)],
            check=True,
        )
        beat_wav.unlink()
        actual = syllables / dur
        tier = "baseline" if actual < 7 else ("fast" if actual < 9.3 else "insane")
        for variant, path in (("acap", acap), ("beat", beat_mix)):
            seg_id = f"{stem}-{variant}-r{rate}"
            (LYRICS_DIR / f"{seg_id}.txt").write_text(text)
            entries.append(
                f"\n  - id: {seg_id}\n"
                f"    artist: synthetic\n"
                f'    track: "{verse_txt.stem} TTS {variant} @ {actual:.1f} syl/s"\n'
                f"    url: null\n"
                f"    start: 0\n"
                f"    end: {dur:.2f}\n"
                f"    syl_per_sec: {actual:.1f}\n"
                f"    tier: {tier}\n"
                f"    timing_verified: true\n"
                f"    lyrics_verified: true\n"
                f"    notes: synthetic tier (DESIGN.md) — exact ground truth by construction\n"
            )
        print(f"  r{rate}: {dur:.1f}s, actual {actual:.2f} syl/s -> {acap.name}, {beat_mix.name}")

    with open(REPO_ROOT / "segments.yaml", "a") as f:
        f.writelines(entries)
    print("manifest entries appended")


if __name__ == "__main__":
    main()
