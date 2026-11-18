#!/usr/bin/env python3
"""Re-transcribe the eval set with a finished run's adapters, decoding with
whisper's standard loop guards (DESIGN.md v4, secondary analysis).

    python scripts/eval_adapters.py --run train/adapters/turbo-lora-v1 --out runs/turbo-lora-v1-guard
    python scripts/eval_adapters.py --run ... --out /tmp/smoke --eval-limit 2

finetune_lora.py decodes greedily with no fallback, so a transcript that
falls into a repetition loop is never retried. Here every checkpoint (base,
then each adapter-e<N> in --run, merged into a fresh copy of the base) goes
through the same eval items and the same pipeline call, plus:

  temperature                 0.0, then 0.2 .. 1.0 on a failed segment
  compression_ratio_threshold 1.35  (transformers' token-level zlib ratio;
                                     the docs' equivalent of openai's 2.4)
  logprob_threshold           -1.0  (openai whisper's default)

A segment is redecoded at the next temperature when its compression ratio is
above 1.35 (it repeats itself) or its mean log-probability is below -1.0.
Sampling reseeds per clip from --seed and the clip's name, so a rerun gives
the same transcripts.

Output dirs are hf-<slug>-guard-base__raw and hf-<slug>-guard-lora-e<N>__raw,
so score_finetune.py reads this run like a training run and its copies into
outputs/ never collide with the unguarded transcripts. The training run's
metrics.json is carried over, with the guard settings and eval times added.
"""

import argparse
import copy
import json
import sys
import time
from pathlib import Path

import torch

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from finetune_lora import REPO_ROOT, SR, as_float, eval_items, log, read_wav, transcribe_all

GUARD = {"temperature": (0.0, 0.2, 0.4, 0.6, 0.8, 1.0),
         "compression_ratio_threshold": 1.35,
         "logprob_threshold": -1.0}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--run", required=True, help="dir holding adapter-e<N>/ and the run's metrics.json")
    p.add_argument("--manifest", default="train/manifest.jsonl")
    p.add_argument("--base", default="openai/whisper-large-v3-turbo")
    p.add_argument("--out", required=True)
    p.add_argument("--seed", type=int, default=7)
    p.add_argument("--eval-limit", type=int, default=0, help="smoke: this many clips per eval group")
    args = p.parse_args()

    import peft
    import transformers
    from peft import PeftModel
    from transformers import WhisperForConditionalGeneration, WhisperProcessor

    run, out = Path(args.run), Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    log(f"device {device} torch {torch.__version__} transformers {transformers.__version__} peft {peft.__version__}")
    adapters = sorted(run.glob("adapter-e*"), key=lambda d: int(d.name.split("-e")[1]))
    if not adapters:
        sys.exit(f"no adapter-e<N>/ in {run}")
    log(f"adapters: {', '.join(a.name for a in adapters)}; guard {GUARD}")

    rows = [json.loads(l) for l in Path(args.manifest).read_text().splitlines()]
    val_rows = [r for r in rows if r["split"] == "val"]
    audio = {a: read_wav(REPO_ROOT / a) for a in sorted({r["audio"] for r in val_rows})}
    val_audio = [(r, as_float(audio[r["audio"]][int(r["start"] * SR): int(r["end"] * SR)])) for r in val_rows]
    items = eval_items(val_audio, args.eval_limit)
    (out / "eval_items.json").write_text(json.dumps(
        [{"name": n, "secs": s} for n, _, s in items if not n.startswith("val-")] +
        [{"name": f"val-{k:04d}", "song": r["song"], "start": r["start"], "end": r["end"], "text": r["text"]}
         for k, (r, _) in enumerate(val_audio)], indent=1))
    log(f"data: {len(items)} eval clips, {len(val_rows)} val chunks")

    metrics = json.loads((run / "metrics.json").read_text()) if (run / "metrics.json").exists() else {}
    metrics["evals"] = []
    metrics["guard"] = {"kwargs": {k: list(v) if isinstance(v, tuple) else v for k, v in GUARD.items()},
                        "seed": args.seed, "eval_limit": args.eval_limit,
                        "versions": {"torch": torch.__version__, "transformers": transformers.__version__,
                                     "peft": peft.__version__}}

    def flush():
        (out / "metrics.json").write_text(json.dumps(metrics, indent=1))

    processor = WhisperProcessor.from_pretrained(args.base)
    base = WhisperForConditionalGeneration.from_pretrained(args.base, dtype=torch.float32).to(device)
    base.eval()
    slug = args.base.split("/")[-1]

    # Same fp32, no-autocast eval path as finetune_lora.py.
    secs = transcribe_all(base, processor, items, out / "outputs" / f"hf-{slug}-guard-base__raw", device,
                          guard=GUARD, seed=args.seed)
    metrics["evals"].append({"tag": "guard-base", "clips": len(items), "secs": round(secs, 1)})
    flush()

    for a in adapters:
        tag = f"guard-lora-e{a.name.split('-e')[1]}"
        model = PeftModel.from_pretrained(copy.deepcopy(base), str(a)).merge_and_unload()
        model.eval()
        secs = transcribe_all(model, processor, items, out / "outputs" / f"hf-{slug}-{tag}__raw", device,
                              guard=GUARD, seed=args.seed)
        metrics["evals"].append({"tag": tag, "clips": len(items), "secs": round(secs, 1)})
        flush()
        del model
        torch.cuda.empty_cache() if device == "cuda" else None
    log("EVAL-DONE")


if __name__ == "__main__":
    main()
