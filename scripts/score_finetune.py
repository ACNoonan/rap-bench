#!/usr/bin/env python3
"""Score a pulled finetune_lora.py run, locally.

    python scripts/score_finetune.py ~/Documents/gpu-harness/gpu/out/rb-v4-turbo-lora/turbo-lora-v1
    -> results/finetune-<run>.md, and the run's transcripts copied into outputs/

Three readouts per checkpoint (base, lora-e1, ...):
  clean  WER on the LibriSpeech read-speech clips: the regression check.
  val    WER on the held-out training songs: did training learn anything?
  bench  not scored here. The transcripts are copied to outputs/ so
         score.py and bootstrap_ci.py score them like any other run, and
         their TODO gate keeps fresh scores hidden until verification.

Instrument check (D1): the base model's WER on the scored exhibition and
core segments next to faster-whisper turbo's from July. Same weights,
different decoder implementation and hardware, so they should agree within
a few points; a large gap means the eval path is broken, not the model.
Pre-registered pass (DESIGN.md v4): median |difference| <= 5 WER points.

Coverage check: on every benchmark clip longer than 30 s, each checkpoint's
transcript word count over the base model's. Long-form decoding seeks on
timestamp tokens; an adapter that broke seeking stops near 30 s and shows up
here as a ratio well under 1 (flagged below 0.7), with no reference needed,
so it can be read for fresh clips before their lyrics are verified.
"""

import statistics

import json
import shutil
import sys
from pathlib import Path

import jiwer

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from rapbench import OUTPUTS_DIR, REPO_ROOT, RESULTS_DIR, load_segments
from rapbench.normalize import normalize
from score import load_reference

REFERENCE_RUN = "faster-whisper-turbo__raw"


def wer(refs: list[str], hyps: list[str]) -> float:
    pairs = [(normalize(r), normalize(h)) for r, h in zip(refs, hyps) if normalize(r)]
    return jiwer.wer([r for r, _ in pairs], [h or "<empty>" for _, h in pairs])


def main() -> None:
    run = Path(sys.argv[1]).expanduser()
    items = json.loads((run / "eval_items.json").read_text())
    val_text = {i["name"]: i["text"] for i in items if "text" in i}
    clean_refs = json.loads((REPO_ROOT / "train" / "clean" / "refs.json").read_text())
    metrics = json.loads((run / "metrics.json").read_text())
    tags = sorted((run / "outputs").iterdir(), key=lambda d: (d.name.count("lora"), d.name))

    rows = []
    for d in tags:
        read = lambda n: (d / f"{n}.txt").read_text() if (d / f"{n}.txt").exists() else ""
        clean = [n for n in clean_refs if (d / f"clean-{n}.txt").exists()]
        val = [n for n in val_text if (d / f"{n}.txt").exists()]
        c = wer([clean_refs[n] for n in clean], [read(f"clean-{n}") for n in clean]) if clean else None
        v = wer([val_text[n] for n in val], [read(n) for n in val]) if val else None
        rows.append(f"| {d.name} | {c:.1%} ({len(clean)}) | {v:.1%} ({len(val)}) |" if c is not None and v is not None
                    else f"| {d.name} | {c} | {v} |")

    base = next(d for d in tags if d.name.endswith("-base__raw"))
    ref_dir = OUTPUTS_DIR / REFERENCE_RUN
    d1 = []
    for s in load_segments():
        ref = load_reference(s["id"])
        if s.get("population") not in ("exhibition", "core") or not ref:
            continue
        if (base / f"{s['id']}.txt").exists() and (ref_dir / f"{s['id']}.txt").exists():
            a = wer([ref], [(base / f"{s['id']}.txt").read_text()])
            b = wer([ref], [(ref_dir / f"{s['id']}.txt").read_text()])
            d1.append(f"| {s['id']} | {a:.0%} | {b:.0%} | {a - b:+.0%} |")

    med = statistics.median(abs(float(r.split("|")[4].strip().rstrip("%"))) for r in d1) if d1 else None
    verdict = ("no segments to compare" if med is None else
               f"median |diff| {med:.0f} points: {'PASS' if med <= 5 else 'FAIL, eval path suspect'} (threshold 5)")

    long_ids = [s["id"] for s in load_segments() if s.get("population") in ("exhibition", "core", "fresh")
                and s["end"] - s["start"] > 30 and (base / f"{s['id']}.txt").exists()]
    cov = []
    for d in tags:
        if d == base:
            continue
        ratios = []
        for sid in long_ids:
            b = len((base / f"{sid}.txt").read_text().split())
            h = len((d / f"{sid}.txt").read_text().split()) if (d / f"{sid}.txt").exists() else 0
            if b:
                ratios.append((h / b, sid))
        if ratios:
            low = [f"{sid} {r:.2f}" for r, sid in ratios if r < 0.7]
            cov.append(f"| {d.name} | {len(ratios)} | {statistics.median(r for r, _ in ratios):.2f} | "
                       f"{min(r for r, _ in ratios):.2f} | {', '.join(low) or 'none'} |")

    epochs = [f"| {e['epoch']} | {e['steps']} | {e['train_loss']} | {e['val_loss']} | {e['secs'] / 60:.0f} min |"
              for e in metrics["epochs"]]
    out = [
        f"# Fine-tune run {run.name}", "",
        f"Written by `scripts/score_finetune.py`. Base `{metrics['args']['base']}`, rank {metrics['args']['rank']}, "
        f"alpha {metrics['args']['alpha']}, lr {metrics['args']['lr']}, seed {metrics['args']['seed']}, "
        f"{metrics['n_train_chunks']} train chunks ({metrics['train_hours']} h), {metrics['n_val_chunks']} val chunks. "
        f"Versions {metrics['versions']}.", "",
        "## Training", "", "| epoch | steps | train loss | val loss | time |", "|---|---|---|---|---|", *epochs, "",
        "## WER by checkpoint", "",
        "`clean` is LibriSpeech read speech (regression check); `val` is held-out training songs, labelled "
        "from unverified LRCLIB lyrics, so its floor is the label noise, not zero. Clip counts in parentheses.", "",
        "| checkpoint | clean | val |", "|---|---|---|", *rows, "",
        "## Instrument check: base model vs faster-whisper turbo (July)", "",
        "Same weights, different implementation and hardware. A large gap means the eval path is broken.", "",
        "| segment | HF base (this run) | faster-whisper turbo | diff |", "|---|---|---|---|", *d1, "",
        f"**{verdict}.**", "",
        "## Coverage on clips over 30 s", "",
        "Transcript words relative to the base model on the same clip. Under 0.7 suggests the adapter broke "
        "long-form seeking and the transcript stops early.", "",
        "| checkpoint | clips | median ratio | min | flagged < 0.7 |", "|---|---|---|---|---|", *cov, "",
        "Benchmark scores: transcripts are copied to `outputs/`; run `score.py` and "
        "`bootstrap_ci.py --rate mean` (fresh segments score only once verified).", "",
    ]
    RESULTS_DIR.mkdir(exist_ok=True)
    path = RESULTS_DIR / f"finetune-{run.name}.md"
    path.write_text("\n".join(out))
    for d in tags:
        dest = OUTPUTS_DIR / d.name
        dest.mkdir(parents=True, exist_ok=True)
        for f in d.iterdir():
            if not f.name.startswith(("clean-", "val-")):
                shutil.copy2(f, dest / f.name)
    print(f"wrote {path}; copied {len(tags)} transcript dirs to {OUTPUTS_DIR}")


if __name__ == "__main__":
    main()
