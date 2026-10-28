#!/usr/bin/env python3
"""Confidence intervals for WER, critical rate, and the memorization delta.

    python scripts/bootstrap_ci.py [--reps 2000] [--seed 0] [--rate listed|mean]
    -> results/ci.md, or results/ci-mean.md with --rate mean

--rate mean replaces each segment's listed syl_per_sec with its mean rate:
syllables in the verified lyrics over the clip's duration. The listed
exhibition rates are peaks while the core rates are means (LOG.md,
2026-10-28), so only --rate mean compares the two populations in one unit.

Why lines, not words: errors cluster. A temperature-fallback storm or a
dropped bar wipes out a whole line, so resampling words independently would
treat 8 correlated errors as 8 independent ones and make the interval too
narrow. Each lyric line is one resampling unit (a cluster bootstrap): every
reference word carries its substitution/deletion count, insertions are
charged to the word before them, and a replicate's WER is
sum(errors over drawn lines) / sum(words over drawn lines).

Per replicate, every segment of a model is redrawn independently and the
critical rate is recomputed on the isotonic envelope exactly as score.py
does, so the interval reflects word-sampling noise in every point of the
curve. What it does NOT cover: the shape of the curve between tested rates.
With two core points (4.9 and 8.4 syl/s) the straight line between them is
an assumption, and the true crossing can sit anywhere in that bracket. The
table reports the bracket next to the interval for that reason.
"""

import argparse
import random
import sys
from pathlib import Path

import jiwer

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from rapbench import OUTPUTS_DIR, RESULTS_DIR, load_segments
from rapbench.normalize import normalize
from rapbench.scoring import SURVIVAL_WER, SegmentScore, critical_rate
from score import POPULATIONS, load_reference
from synth import count_syllables


DELTAS = [("exhibition", "core"), ("exhibition", "fresh"), ("fresh", "core")]


def line_errors(reference: str, hypothesis: str) -> list[tuple[int, int]]:
    """(errors, words) per reference line, using whichever ad-lib variant
    scores best, as score_segment does."""
    hyp = normalize(hypothesis)
    best = None
    for strip in (True, False):
        lines = [normalize(l, strip_adlibs=strip) for l in reference.splitlines()]
        lines = [l for l in lines if l]
        words = " ".join(lines).split()
        if not words:
            continue
        line_of = [i for i, l in enumerate(lines) for _ in l.split()]
        out = jiwer.process_words(" ".join(words), hyp)
        errs = [0] * len(words)
        for chunk in out.alignments[0]:
            if chunk.type in ("substitute", "delete"):
                for k in range(chunk.ref_start_idx, chunk.ref_end_idx):
                    errs[k] += 1
            elif chunk.type == "insert":
                errs[max(chunk.ref_start_idx - 1, 0)] += chunk.hyp_end_idx - chunk.hyp_start_idx
        per_line = [[0, 0] for _ in lines]
        for k, e in enumerate(errs):
            per_line[line_of[k]][0] += e
            per_line[line_of[k]][1] += 1
        wer = sum(errs) / len(words)
        if best is None or wer < best[0]:
            best = (wer, [tuple(x) for x in per_line if x[1]])
    return best[1]


def resample(lines: list[tuple[int, int]], rng: random.Random) -> float:
    draw = [lines[rng.randrange(len(lines))] for _ in lines]
    return sum(e for e, _ in draw) / sum(w for _, w in draw)


def pct(xs: list[float], q: float) -> float:
    xs = sorted(xs)
    return xs[min(int(q * len(xs)), len(xs) - 1)]


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--reps", type=int, default=2000)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--rate", choices=["listed", "mean"], default="listed")
    args = p.parse_args()

    segments = {s["id"]: s for s in load_segments()}
    refs = {sid: load_reference(sid) for sid in segments}
    if args.rate == "mean":
        for sid, s in segments.items():
            if refs[sid]:
                s["syl_per_sec"] = round(count_syllables(normalize(refs[sid])) / (s["end"] - s["start"]), 2)
    runs = sorted(d for d in OUTPUTS_DIR.iterdir() if d.is_dir())

    wer_rows, crit_rows = [], []
    for run in runs:
        crit_reps: dict[str, list[tuple[float, str]]] = {}
        point: dict[str, tuple[float, str]] = {}
        bracket: dict[str, str] = {}
        for pop in POPULATIONS:
            ids = [sid for sid, s in segments.items()
                   if s.get("population", "exhibition") == pop and refs[sid]
                   and (run / f"{sid}.txt").exists()]
            if not ids:
                continue
            data = {sid: line_errors(refs[sid], (run / f"{sid}.txt").read_text()) for sid in ids}
            rng = random.Random(args.seed)
            seg_reps = {sid: [] for sid in ids}
            reps = []
            for _ in range(args.reps):
                scores = []
                for sid in ids:
                    w = resample(data[sid], rng)
                    seg_reps[sid].append(w)
                    scores.append(SegmentScore(sid, segments[sid]["tier"], segments[sid]["syl_per_sec"], w, 0))
                reps.append(critical_rate(scores))
            crit_reps[pop] = reps
            full = [SegmentScore(sid, segments[sid]["tier"], segments[sid]["syl_per_sec"],
                                 sum(e for e, _ in data[sid]) / sum(w for _, w in data[sid]), 0) for sid in ids]
            point[pop] = critical_rate(full)
            # the pair of tested rates the point estimate's crossing sits between
            rates = sorted({s.syl_per_sec for s in full})
            r, q = point[pop]
            if q == "=":
                lo = max(x for x in rates if x <= r)
                hi = min(x for x in rates if x >= r)
                bracket[pop] = f"{lo}–{hi}"
            else:
                bracket[pop] = "censored"
            for sid in ids:
                n_lines = len(data[sid])
                n_words = sum(w for _, w in data[sid])
                wer = sum(e for e, _ in data[sid]) / n_words
                wer_rows.append(f"| {run.name} | {sid} | {wer:.0%} | {pct(seg_reps[sid], .025):.0%}–"
                                f"{pct(seg_reps[sid], .975):.0%} | {n_lines} | {n_words} |")
        for pop, reps in crit_reps.items():
            vals = [r for r, _ in reps]
            cens = sum(q != "=" for _, q in reps) / len(reps)
            r, q = point[pop]
            crit_rows.append(f"| {run.name} | {pop} | {q if q != '=' else ''}{r:.1f} | "
                             f"{pct(vals, .025):.1f}–{pct(vals, .975):.1f} | {bracket[pop]} | {cens:.0%} |")
        # exhibition − fresh is the memorization delta on human vocals (DESIGN.md
        # v3); fresh − core is human vs synthetic vocals. A delta between end
        # points is meaningless, so it is only reported when both curves cross.
        for a, b in DELTAS:
            if {a, b} <= crit_reps.keys() and point[a][1] == point[b][1] == "=":
                d = [x[0] - y[0] for x, y in zip(crit_reps[a], crit_reps[b])]
                pd = point[a][0] - point[b][0]
                crit_rows.append(f"| {run.name} | **delta** ({a} − {b}) | {pd:+.1f} | "
                                 f"{pct(d, .025):+.1f} to {pct(d, .975):+.1f} | | |")

    out = [
        "# rap-bench confidence intervals",
        "",
        f"Cluster bootstrap over lyric lines, {args.reps} replicates, seed {args.seed}, "
        f"rates: {args.rate}; "
        "95% percentile intervals. Written by `scripts/bootstrap_ci.py`; see its docstring for the design.",
        "",
        "## Critical rate",
        "",
        "`bracket` is the pair of tested rates the crossing is interpolated between: the bootstrap "
        "interval assumes a straight line inside it, so the bracket is the honest bound on curve shape. "
        f"`censored` is the share of replicates where the curve never crossed {SURVIVAL_WER:.0%} "
        "or failed at the slowest point; those replicates sit at an end point and narrow the interval.",
        "",
        "| model | population | critical rate | 95% CI | bracket | censored |",
        "|---|---|---|---|---|---|",
        *crit_rows,
        "",
        "## WER per segment",
        "",
        "| model | segment | WER | 95% CI | lines | words |",
        "|---|---|---|---|---|---|",
        *wer_rows,
        "",
    ]
    RESULTS_DIR.mkdir(exist_ok=True)
    name = "ci.md" if args.rate == "listed" else "ci-mean.md"
    (RESULTS_DIR / name).write_text("\n".join(out))
    print(f"wrote {RESULTS_DIR / name}")


if __name__ == "__main__":
    main()
