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
    mlx-whisper:<hf-repo>   pip install mlx-whisper  (Apple-GPU whisper;
                            default mlx-community/whisper-large-v3-turbo)
    parakeet:<hf-repo>      pip install parakeet-mlx  (NVIDIA Parakeet on
                            Apple GPU; default mlx-community/parakeet-tdt-0.6b-v2)
    openrouter:<model-id>   hosted models through OpenRouter's speech-to-text
                            endpoint, e.g. openrouter:elevenlabs/scribe-v2.
                            Paid. Reads OPENROUTER_API_KEY from the environment
                            or .env. Sends the clip's audio to the provider.
                            The .time file includes the network round trip, so
                            RTF is not comparable with the local backends.

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
    try:
        # Whisper-family needs timestamps for >30s inputs...
        return pipe(str(path), return_timestamps=True)["text"].strip()
    except ValueError:
        # ...but e.g. moonshine rejects the flag outright.
        return pipe(str(path))["text"].strip()


def load_mlx_whisper(variant: str):
    import mlx_whisper
    import numpy as np

    repo = variant or "mlx-community/whisper-large-v3-turbo"
    # Warm up so weight loading + Metal kernel compilation don't land in the
    # first segment's timing.
    mlx_whisper.transcribe(np.zeros(16000, dtype=np.float32), path_or_hf_repo=repo)
    return repo


def run_mlx_whisper(repo, path: Path) -> str:
    import mlx_whisper

    return mlx_whisper.transcribe(str(path), path_or_hf_repo=repo, language="en")["text"].strip()


def load_parakeet(variant: str):
    from parakeet_mlx import from_pretrained

    return from_pretrained(variant or "mlx-community/parakeet-tdt-0.6b-v2")


def run_parakeet(model, path: Path) -> str:
    return model.transcribe(str(path)).text.strip()


def load_openrouter(variant: str):
    import os

    key = os.environ.get("OPENROUTER_API_KEY")
    env = Path(__file__).resolve().parent.parent / ".env"
    if not key and env.exists():
        for line in env.read_text().splitlines():
            if line.startswith("OPENROUTER_API_KEY="):
                key = line.split("=", 1)[1].strip().strip("'\"")
    if not key:
        sys.exit("OPENROUTER_API_KEY not set (environment or .env)")
    return {"model": variant, "key": key, "cost": 0.0}


def run_openrouter(model, path: Path) -> str:
    import base64
    import json
    import urllib.error
    import urllib.request

    body = json.dumps({
        "model": model["model"],
        "input_audio": {"data": base64.b64encode(path.read_bytes()).decode(), "format": "wav"},
        "language": "en",
    }).encode()
    for attempt in range(4):
        req = urllib.request.Request(
            "https://openrouter.ai/api/v1/audio/transcriptions", data=body,
            headers={"Authorization": f"Bearer {model['key']}", "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                out = json.loads(r.read())
            break
        except urllib.error.HTTPError as e:
            msg = e.read().decode(errors="replace")[:400]
            if e.code not in (429, 500, 502, 503, 504, 524, 529) or attempt == 3:
                sys.exit(f"openrouter {e.code} for {model['model']}: {msg}")
            time.sleep(5 * (attempt + 1))
    usage = out.get("usage") or {}
    model["cost"] += float(usage.get("cost") or 0)
    model["usage"] = usage
    return (out.get("text") or "").strip()


BACKENDS = {
    "faster-whisper": (load_faster_whisper, run_faster_whisper),
    "whisper": (load_openai_whisper, run_openai_whisper),
    "hf": (load_hf_pipeline, run_hf_pipeline),
    "mlx-whisper": (load_mlx_whisper, run_mlx_whisper),
    "parakeet": (load_parakeet, run_parakeet),
    "openrouter": (load_openrouter, run_openrouter),
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True, help="backend:variant, e.g. faster-whisper:large-v3")
    parser.add_argument("--source", choices=["raw", "vocals"], default="raw")
    parser.add_argument("--skip-existing", action="store_true", help="skip segments that already have a transcript")
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
        if args.skip_existing and (out_dir / f"{seg['id']}.txt").exists():
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
    if isinstance(model, dict) and "cost" in model:
        print(f"  reported cost: ${model['cost']:.4f}; last usage: {model.get('usage')}")


if __name__ == "__main__":
    main()
