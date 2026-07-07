#!/usr/bin/env python3
"""Forced log-prob membership inference on whisper's decoder (BLOG appendix).

    python scripts/prior_logprob.py

The free-run probe (prior_probe.py) showed the decoder won't rap over
silence. This is the stronger test: teacher-force the TRUE continuation
tokens with the audio ablated (silence) and measure mean per-token log
probability under a MATCHED prompt (the verse's real preceding words,
placed in whisper's previous-context slot) vs MISMATCHED prompts (openings
of the other verses in the same population).

    memorization lift = LP(continuation | matched) - LP(continuation | mismatched)

The lift controls for each continuation's intrinsic probability; what
remains is how much the decoder's prior expects THESE words after THOSE
words. Famous lift >> synthetic lift = lyric memorization demonstrated in
the weights, no dataset access required.
"""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from rapbench import LYRICS_DIR, REPO_ROOT
from rapbench.normalize import normalize

PROMPT_WORDS = 15
CONT_WORDS = 40

VERSES = [
    ("rap-god", LYRICS_DIR / "rap-god-fast.txt", "famous", 0),
    ("godzilla", LYRICS_DIR / "godzilla-v3.txt", "famous", 0),
    ("lose-yourself", LYRICS_DIR / "lose-yourself-v1.txt", "famous", 0),
    ("speedom", LYRICS_DIR / "speedom-em.txt", "famous", 0),
    ("synthetic-a", REPO_ROOT / "synthetic" / "verse-01.txt", "control", 0),
    ("synthetic-b", REPO_ROOT / "synthetic" / "verse-01.txt", "control", 50),
]


def main() -> None:
    import torch
    import whisper

    model = whisper.load_model("turbo")
    model.eval()
    tok = whisper.tokenizer.get_tokenizer(
        multilingual=True, num_languages=model.num_languages, language="en", task="transcribe"
    )

    audio = whisper.pad_or_trim(np.zeros(16000 * 5, dtype=np.float32))
    mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).unsqueeze(0)
    with torch.no_grad():
        audio_features = model.encoder(mel)

    def continuation_logprob(prompt: str, continuation: str) -> float:
        prev = [tok.sot_prev] + tok.encode(" " + prompt)
        main = list(tok.sot_sequence_including_notimestamps)
        cont_tokens = tok.encode(" " + continuation)
        seq = prev + main + cont_tokens
        tokens = torch.tensor([seq])
        with torch.no_grad():
            logits = model.decoder(tokens, audio_features)
        logprobs = torch.log_softmax(logits.float(), dim=-1)
        start = len(prev) + len(main)
        lp = 0.0
        for i in range(start, len(seq)):
            lp += logprobs[0, i - 1, seq[i]].item()
        return lp / len(cont_tokens)

    data = []
    for name, path, kind, offset in VERSES:
        text = " ".join(l for l in path.read_text().splitlines() if not l.startswith("#"))
        words = normalize(text).split()
        data.append((name, kind,
                     " ".join(words[offset: offset + PROMPT_WORDS]),
                     " ".join(words[offset + PROMPT_WORDS: offset + PROMPT_WORDS + CONT_WORDS])))

    print(f"{'verse':<14} {'kind':<8} {'matched':>9} {'mismatched':>11} {'lift (nats/token)':>18}")
    lifts = {}
    for name, kind, prompt, cont in data:
        matched = continuation_logprob(prompt, cont)
        others = [p for n, k, p, c in data if n != name and not (kind == "control" and k == "control")]
        mismatched = sum(continuation_logprob(p, cont) for p in others) / len(others)
        lift = matched - mismatched
        lifts.setdefault(kind, []).append(lift)
        print(f"{name:<14} {kind:<8} {matched:>9.3f} {mismatched:>11.3f} {lift:>18.3f}")

    print()
    for kind, vals in lifts.items():
        print(f"{kind}: mean lift {sum(vals)/len(vals):+.3f} nats/token over {len(vals)} verses")


if __name__ == "__main__":
    main()
