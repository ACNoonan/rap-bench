#!/usr/bin/env python3
"""Run an ASR model over the benchmark segments.

    python scripts/transcribe.py --model faster-whisper:large-v3 --source raw
    python scripts/transcribe.py --model faster-whisper:large-v3 --source vocals
    python scripts/transcribe.py --model whisper:turbo --source vocals
    python scripts/transcribe.py --model hf:distil-whisper/distil-large-v3 --source raw

Backends (install what you use):
    faster-whisper:<size>   pip install faster-whisper
    whisper:<size>          pip install openai-whisper
    hf:<model-id>           pip install transformers torch  (any HF ASR pipeline
                            model: distil-whisper, wav2vec2, moonshine, ...)

Adding a backend (nemo/parakeet, kyutai, voxtral, your own service): write a
load(variant) -> model and a transcribe(model, audio_path) -> str, register
the pair in BACKENDS.

Output per segment:
    outputs/<model-slug>__<source>/<segment_id>.txt    transcript
    outputs/<model-slug>__<source>/<segment_id>.time   inference wall seconds

Timing excludes model load (loaded once, before the clock starts) — it
answers "could this model have kept up live?", the benchmark's golden
standard (RTF < 1 while staying accurate).
"""

import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from rapbench import OUTPUTS_DIR, audio_path, load_segments


def load_faster_whisper(variant: str):
    from faster_whisper import WhisperModel

    return WhisperModel(variant)


def run_faster_whisper(model, path: Path) -> str:
    segments, _ = model.transcribe(str(path), language="en")
    return " ".join(s.text.strip() for s in segments)


def load_openai_whisper(variant: str):
    import whisper

    return whisper.load_model(variant)


def run_openai_whisper(model, path: Path) -> str:
    return model.transcribe(str(path), language="en")["text"].strip()


def load_hf_pipeline(variant: str):
    from transformers import pipeline

    return pipeline("automatic-speech-recognition", model=variant)


def run_hf_pipeline(pipe, path: Path) -> str:
    return pipe(str(path), return_timestamps=True)["text"].strip()


BACKENDS = {
    "faster-whisper": (load_faster_whisper, run_faster_whisper),
    "whisper": (load_openai_whisper, run_openai_whisper),
    "hf": (load_hf_pipeline, run_hf_pipeline),
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True, help="backend:variant, e.g. faster-whisper:large-v3")
    parser.add_argument("--source", choices=["raw", "vocals"], default="raw")
    parser.add_argument("segments", nargs="*", help="segment ids (default: all)")
    args = parser.parse_args()

    backend, _, variant = args.model.partition(":")
    if backend not in BACKENDS:
        sys.exit(f"unknown backend {backend!r}; available: {', '.join(BACKENDS)}")
    load, transcribe = BACKENDS[backend]

    slug = args.model.replace(":", "-").replace("/", "-")
    out_dir = OUTPUTS_DIR / f"{slug}__{args.source}"
    out_dir.mkdir(parents=True, exist_ok=True)

    model = None
    for seg in load_segments():
        if args.segments and seg["id"] not in args.segments:
            continue
        path = audio_path(seg["id"], args.source)
        if not path.exists():
            print(f"  {seg['id']}: missing {path}, skipping")
            continue
        if model is None:
            model = load(variant)
        t0 = time.perf_counter()
        text = transcribe(model, path)
        elapsed = time.perf_counter() - t0
        (out_dir / f"{seg['id']}.txt").write_text(text + "\n")
        (out_dir / f"{seg['id']}.time").write_text(f"{elapsed:.3f}\n")
        audio_secs = seg["end"] - seg["start"]
        print(f"  {seg['id']}: {len(text.split())} words, RTF {elapsed / audio_secs:.2f}")


if __name__ == "__main__":
    main()
