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
function (audio_path: Path, variant: str) -> str and register it in BACKENDS.

Output: outputs/<model-slug>__<source>/<segment_id>.txt
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from rapbench import OUTPUTS_DIR, audio_path, load_segments


def run_faster_whisper(path: Path, variant: str) -> str:
    from faster_whisper import WhisperModel

    model = _cached("fw" + variant, lambda: WhisperModel(variant))
    segments, _ = model.transcribe(str(path), language="en")
    return " ".join(s.text.strip() for s in segments)


def run_openai_whisper(path: Path, variant: str) -> str:
    import whisper

    model = _cached("ow" + variant, lambda: whisper.load_model(variant))
    return model.transcribe(str(path), language="en")["text"].strip()


def run_hf_pipeline(path: Path, variant: str) -> str:
    from transformers import pipeline

    pipe = _cached(
        "hf" + variant,
        lambda: pipeline("automatic-speech-recognition", model=variant),
    )
    return pipe(str(path), return_timestamps=True)["text"].strip()


BACKENDS = {
    "faster-whisper": run_faster_whisper,
    "whisper": run_openai_whisper,
    "hf": run_hf_pipeline,
}

_MODELS: dict = {}


def _cached(key: str, build):
    if key not in _MODELS:
        _MODELS[key] = build()
    return _MODELS[key]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True, help="backend:variant, e.g. faster-whisper:large-v3")
    parser.add_argument("--source", choices=["raw", "vocals"], default="raw")
    parser.add_argument("segments", nargs="*", help="segment ids (default: all)")
    args = parser.parse_args()

    backend, _, variant = args.model.partition(":")
    if backend not in BACKENDS:
        sys.exit(f"unknown backend {backend!r}; available: {', '.join(BACKENDS)}")

    slug = args.model.replace(":", "-").replace("/", "-")
    out_dir = OUTPUTS_DIR / f"{slug}__{args.source}"
    out_dir.mkdir(parents=True, exist_ok=True)

    for seg in load_segments():
        if args.segments and seg["id"] not in args.segments:
            continue
        path = audio_path(seg["id"], args.source)
        if not path.exists():
            print(f"  {seg['id']}: missing {path}, skipping")
            continue
        text = BACKENDS[backend](path, variant)
        (out_dir / f"{seg['id']}.txt").write_text(text + "\n")
        print(f"  {seg['id']}: {len(text.split())} words")


if __name__ == "__main__":
    main()
