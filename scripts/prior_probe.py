#!/usr/bin/env python3
"""Membership-inference probe of whisper's decoder prior (BLOG.md appendix).

    python scripts/prior_probe.py

Feeds the model SILENCE (and low-level noise) with an initial_prompt
containing the opening words of a verse, and measures whether the decoder
completes the lyrics with no acoustic evidence. Famous verses (from the
verified exhibition references) vs our synthetic verse (which no model can
have trained on) as control.

Score per probe: fraction of the true continuation's normalized 4-grams
that appear in the emitted text. Famous >> synthetic = memorization
demonstrated in the model itself, not inferred from WER.

Anti-hallucination thresholds are disabled (no_speech/logprob/compression)
so the decoder is free to emit whatever its prior wants.
"""

import re
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from rapbench import LYRICS_DIR, REPO_ROOT
from rapbench.normalize import normalize

REPO = "mlx-community/whisper-large-v3-turbo"
SR = 16000
PROMPT_WORDS = 15
CONT_WORDS = 40

PROBES = [
    ("rap-god-fast", LYRICS_DIR / "rap-god-fast.txt", "famous"),
    ("godzilla-v3", LYRICS_DIR / "godzilla-v3.txt", "famous"),
    ("lose-yourself-v1", LYRICS_DIR / "lose-yourself-v1.txt", "famous"),
    ("speedom-em", LYRICS_DIR / "speedom-em.txt", "famous"),
    ("synthetic-a", REPO_ROOT / "synthetic" / "verse-01.txt", "control"),
    ("synthetic-b", REPO_ROOT / "synthetic" / "verse-01.txt", "control"),
]


def words_of(path: Path) -> list[str]:
    text = " ".join(l for l in path.read_text().splitlines() if not l.startswith("#"))
    return normalize(text).split()


def ngrams(words: list[str], n: int = 4) -> set:
    return {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}


def main() -> None:
    import mlx_whisper

    audios = {
        "silence": np.zeros(5 * SR, dtype=np.float32),
        "noise": (np.random.default_rng(0).standard_normal(5 * SR) * 0.005).astype(np.float32),
    }
    # warm up
    mlx_whisper.transcribe(audios["silence"], path_or_hf_repo=REPO)

    print(f"{'probe':<18} {'kind':<8} {'audio':<8} {'4-gram completion':<18} emitted (first 120 chars)")
    results = {}
    for name, path, kind in PROBES:
        words = words_of(path)
        offset = 50 if name.endswith("-b") else 0
        prompt = " ".join(words[offset: offset + PROMPT_WORDS])
        continuation = words[offset + PROMPT_WORDS: offset + PROMPT_WORDS + CONT_WORDS]
        target = ngrams(continuation)
        for audio_name, audio in audios.items():
            result = mlx_whisper.transcribe(
                audio,
                path_or_hf_repo=REPO,
                language="en",
                initial_prompt=prompt,
                temperature=0.0,
                no_speech_threshold=None,
                logprob_threshold=None,
                compression_ratio_threshold=None,
            )
            emitted = normalize(result["text"]).split()
            hit = len(ngrams(emitted) & target) / max(1, len(target))
            results.setdefault(kind, []).append(hit)
            snippet = " ".join(emitted)[:120]
            print(f"{name:<18} {kind:<8} {audio_name:<8} {hit:<18.0%} {snippet}")

    print()
    for kind, vals in results.items():
        print(f"{kind}: mean 4-gram completion {sum(vals)/len(vals):.0%} over {len(vals)} probes")


if __name__ == "__main__":
    main()
