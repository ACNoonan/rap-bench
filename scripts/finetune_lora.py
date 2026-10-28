#!/usr/bin/env python3
"""LoRA fine-tune whisper on train/manifest.jsonl, and transcribe every eval
clip before and after (DESIGN.md v4).

    python scripts/finetune_lora.py --out runs/turbo-lora           # full run
    python scripts/finetune_lora.py --out /tmp/smoke --max-steps 2 --eval-limit 2

Order, so a crash at any point leaves everything before it on disk:
  1. base model transcribes the eval set -> <out>/outputs/<base-slug>__raw/
  2. per epoch: train, val loss, save <out>/adapter-e<N>/, transcribe the
     eval set with the adapter merged -> <out>/outputs/<slug>-e<N>__raw/,
     rewrite <out>/metrics.json
Nothing is scored here. Transcripts land in the layout score.py and
bootstrap_ci.py read, so scoring happens locally after the pull, and fresh
scores stay hidden until the fresh lyrics are verified.

Eval set: every exhibition, core and fresh segment with audio/<id>.wav, the
held-out val chunks of the training set (in-distribution check), and the
clean read-speech clips in train/clean/ (regression check). Base and adapter
go through the same transformers ASR pipeline call as transcribe.py's hf
backend, with language fixed to English for both.

Audio is read with the stdlib wave module (16 kHz mono int16, as
build_train.py and fetch.py write it), so the box needs no audio library.
"""

import argparse
import copy
import json
import math
import os
import random
import sys
import time
import wave
from pathlib import Path

import numpy as np
import torch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from rapbench import REPO_ROOT, load_segments

SR = 16000
EVAL_POPULATIONS = ("exhibition", "core", "fresh")


def read_wav(path: Path) -> np.ndarray:
    with wave.open(str(path)) as w:
        assert w.getframerate() == SR and w.getnchannels() == 1 and w.getsampwidth() == 2, path
        return np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16)


def as_float(x: np.ndarray) -> np.ndarray:
    return x.astype(np.float32) / 32768.0


def log(msg: str) -> None:
    print(msg, flush=True)


class Chunks(torch.utils.data.Dataset):
    def __init__(self, rows, audio, processor):
        self.rows, self.audio, self.proc = rows, audio, processor

    def __len__(self):
        return len(self.rows)

    def __getitem__(self, i):
        r = self.rows[i]
        x = as_float(self.audio[r["audio"]][int(r["start"] * SR): int(r["end"] * SR)])
        feats = self.proc.feature_extractor(x, sampling_rate=SR, return_tensors="np").input_features[0]
        ids = self.proc.tokenizer(r["text"]).input_ids[:448]
        return feats, ids


def collate(batch, start_id):
    feats = torch.tensor(np.stack([f for f, _ in batch]))
    labels = [ids[1:] if ids and ids[0] == start_id else ids for _, ids in batch]
    n = max(map(len, labels))
    lab = torch.full((len(labels), n), -100, dtype=torch.long)
    for i, l in enumerate(labels):
        lab[i, : len(l)] = torch.tensor(l)
    return feats, lab


def eval_items(manifest_val, limit):
    """(output name, audio loader, seconds) for the benchmark segments, the
    clean read-speech clips and the val chunks. --eval-limit takes that many
    from each group, so a smoke run exercises all three paths."""
    segs, clean, val = [], [], []
    for s in load_segments():
        p = REPO_ROOT / "audio" / f"{s['id']}.wav"
        if s.get("population", "exhibition") in EVAL_POPULATIONS and p.exists():
            segs.append((s["id"], lambda p=p: as_float(read_wav(p)), s["end"] - s["start"]))
    clean_dir = REPO_ROOT / "train" / "clean"
    for p in sorted(clean_dir.glob("*.wav")) if clean_dir.exists() else []:
        clean.append((f"clean-{p.stem}", lambda p=p: as_float(read_wav(p)), None))
    for k, (r, x) in enumerate(manifest_val):
        val.append((f"val-{k:04d}", lambda x=x: x, r["end"] - r["start"]))
    if limit:
        segs, clean, val = segs[:limit], clean[:limit], val[:limit]
    return segs + clean + val


def transcribe_all(model, processor, items, out_dir: Path, device) -> float:
    from transformers import pipeline

    pipe = pipeline("automatic-speech-recognition", model=model, tokenizer=processor.tokenizer,
                    feature_extractor=processor.feature_extractor, device=device)
    out_dir.mkdir(parents=True, exist_ok=True)
    t_all = time.perf_counter()
    for name, load, _ in items:
        x = load()
        t0 = time.perf_counter()
        text = pipe({"raw": x, "sampling_rate": SR}, return_timestamps=True,
                    generate_kwargs={"language": "en", "task": "transcribe"})["text"].strip()
        elapsed = time.perf_counter() - t0
        (out_dir / f"{name}.txt").write_text(text + "\n")
        (out_dir / f"{name}.time").write_text(f"{elapsed:.3f}\n")
    secs = time.perf_counter() - t_all
    log(f"EVAL {out_dir.name}: {len(items)} clips in {secs:.0f}s")
    return secs


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--manifest", default="train/manifest.jsonl")
    p.add_argument("--base", default="openai/whisper-large-v3-turbo")
    p.add_argument("--out", required=True)
    p.add_argument("--epochs", type=int, default=3)
    p.add_argument("--lr", type=float, default=3e-4)
    p.add_argument("--rank", type=int, default=32)
    p.add_argument("--alpha", type=int, default=64)
    p.add_argument("--batch", type=int, default=8)
    p.add_argument("--accum", type=int, default=2)
    p.add_argument("--warmup", type=int, default=100)
    p.add_argument("--seed", type=int, default=7)
    p.add_argument("--max-steps", type=int, default=0, help="smoke: stop after this many optimizer steps")
    p.add_argument("--eval-limit", type=int, default=0, help="smoke: transcribe only this many eval clips")
    p.add_argument("--workers", type=int, default=4)
    args = p.parse_args()

    import peft
    import transformers
    from peft import LoraConfig, get_peft_model
    from transformers import WhisperForConditionalGeneration, WhisperProcessor

    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    log(f"device {device} torch {torch.__version__} transformers {transformers.__version__} peft {peft.__version__}")

    rows = [json.loads(l) for l in Path(args.manifest).read_text().splitlines()]
    audio = {a: read_wav(REPO_ROOT / a) for a in sorted({r["audio"] for r in rows})}
    train_rows = [r for r in rows if r["split"] == "train"]
    val_rows = [r for r in rows if r["split"] == "val"]
    hours = sum(r["end"] - r["start"] for r in train_rows) / 3600
    log(f"data: {len(train_rows)} train chunks ({hours:.2f} h, {len({r['song'] for r in train_rows})} songs), "
        f"{len(val_rows)} val chunks, {len(audio)} songs loaded")

    processor = WhisperProcessor.from_pretrained(args.base)
    processor.tokenizer.set_prefix_tokens(language="en", task="transcribe", predict_timestamps=False)
    model = WhisperForConditionalGeneration.from_pretrained(args.base, dtype=torch.float32).to(device)
    start_id = model.config.decoder_start_token_id
    slug = args.base.split("/")[-1]

    val_audio = [(r, as_float(audio[r["audio"]][int(r["start"] * SR): int(r["end"] * SR)])) for r in val_rows]
    items = eval_items(val_audio, args.eval_limit)
    (out / "eval_items.json").write_text(json.dumps(
        [{"name": n, "secs": s} for n, _, s in items] +
        [{"name": f"val-{k:04d}", "song": r["song"], "start": r["start"], "end": r["end"], "text": r["text"]}
         for k, (r, _) in enumerate(val_audio)], indent=1))

    metrics = {"args": vars(args), "versions": {"torch": torch.__version__, "transformers": transformers.__version__,
               "peft": peft.__version__}, "device": device, "n_train_chunks": len(train_rows),
               "n_val_chunks": len(val_rows), "train_hours": round(hours, 3), "epochs": [], "evals": []}

    def flush():
        (out / "metrics.json").write_text(json.dumps(metrics, indent=1))

    # Eval decodes in fp32 without autocast: autocast reaches the pipeline's
    # feature extractor and bf16 log-mels break it. Same for base and adapter.
    model.eval()
    secs = transcribe_all(model, processor, items, out / "outputs" / f"hf-{slug}-base__raw", device)
    metrics["evals"].append({"tag": "base", "clips": len(items), "secs": round(secs, 1)})
    flush()

    model = get_peft_model(model, LoraConfig(
        r=args.rank, lora_alpha=args.alpha, lora_dropout=0.05, bias="none",
        target_modules=["q_proj", "k_proj", "v_proj", "out_proj"]))
    n_tr = sum(p.numel() for p in model.parameters() if p.requires_grad)
    log(f"lora: {n_tr / 1e6:.1f}M trainable params")
    metrics["trainable_params"] = n_tr

    g = torch.Generator().manual_seed(args.seed)
    col = lambda b: collate(b, start_id)
    train_dl = torch.utils.data.DataLoader(Chunks(train_rows, audio, processor), batch_size=args.batch,
                                           shuffle=True, generator=g, collate_fn=col, num_workers=args.workers)
    val_dl = torch.utils.data.DataLoader(Chunks(val_rows, audio, processor), batch_size=args.batch,
                                         collate_fn=col, num_workers=args.workers)
    steps_per_epoch = math.ceil(len(train_dl) / args.accum)
    total = args.max_steps or steps_per_epoch * args.epochs
    opt = torch.optim.AdamW([p for p in model.parameters() if p.requires_grad], lr=args.lr, weight_decay=0.01)
    sched = torch.optim.lr_scheduler.LambdaLR(
        opt, lambda s: min(1.0, (s + 1) / args.warmup) * max(0.0, (total - s) / max(1, total - args.warmup)))
    log(f"steps: {steps_per_epoch}/epoch, {total} total")

    step = 0
    for epoch in range(1, args.epochs + 1):
        model.train()
        t0, run_loss, n_loss = time.perf_counter(), 0.0, 0
        for i, (feats, lab) in enumerate(train_dl):
            with torch.autocast(device, dtype=torch.bfloat16):
                loss = model(input_features=feats.to(device), labels=lab.to(device)).loss / args.accum
            loss.backward()
            run_loss += loss.item() * args.accum
            n_loss += 1
            if (i + 1) % args.accum == 0:
                torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
                opt.step(); sched.step(); opt.zero_grad()
                step += 1
                if step % 10 == 0 or step == total:
                    log(f"epoch {epoch} step {step}/{total} loss {run_loss / n_loss:.4f} lr {sched.get_last_lr()[0]:.2e}")
                if step >= total:
                    break
        train_loss = run_loss / max(n_loss, 1)

        model.eval()
        vl, vn = 0.0, 0
        with torch.no_grad():
            for k, (feats, lab) in enumerate(val_dl):
                with torch.autocast(device, dtype=torch.bfloat16):
                    vl += model(input_features=feats.to(device), labels=lab.to(device)).loss.item()
                vn += 1
                if args.max_steps and k >= 1:
                    break
        val_loss = vl / max(vn, 1)
        log(f"epoch {epoch} done: train_loss {train_loss:.4f} val_loss {val_loss:.4f} "
            f"({time.perf_counter() - t0:.0f}s)")
        model.save_pretrained(out / f"adapter-e{epoch}")

        merged = copy.deepcopy(model).merge_and_unload()
        merged.eval()
        secs = transcribe_all(merged, processor, items, out / "outputs" / f"hf-{slug}-lora-e{epoch}__raw", device)
        del merged
        torch.cuda.empty_cache() if device == "cuda" else None
        metrics["epochs"].append({"epoch": epoch, "steps": step, "train_loss": round(train_loss, 4),
                                  "val_loss": round(val_loss, 4), "secs": round(time.perf_counter() - t0, 1)})
        metrics["evals"].append({"tag": f"lora-e{epoch}", "clips": len(items), "secs": round(secs, 1)})
        flush()
        if step >= total:
            break
    log("TRAIN-DONE")


if __name__ == "__main__":
    main()
