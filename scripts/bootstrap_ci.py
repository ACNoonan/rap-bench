#!/usr/bin/env python3
"""Confidence intervals for WER, critical rate, and the memorization delta.

    python scripts/bootstrap_ci.py [--reps 2000] [--seed 0] [--rate listed|mean] [--adjust vocab]
    -> results/ci.md; --rate mean adds -mean, --adjust vocab adds -vocab

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

--adjust vocab removes vocabulary mix from every WER by direct
standardization. Rare words are harder to transcribe whether or not a
model has heard the song, and famous Eminem verses carry more of them
("monological") than a Suno verse does, so a raw WER gap mixes rarity with
memorization. Each reference word goes in a frequency bin by its wordfreq
Zipf score (log10 of occurrences per billion words: common >= 5, mid 3-5,
rare < 3), and a segment's adjusted WER is

    sum over bins b of  p_b * (errors in b / words in b)

where p_b is the share of bin b across every scored reference word, all
populations pooled. Every segment is scored as if it had the same
vocabulary mix, so what's left of a population gap is not rarity. A bin a
segment has no words in falls back to that segment's raw WER. Corpus
frequency rather than a language model's log-prob: whisper's decoder has
memorized the famous verses, so its log-prob would score memorized words
as "expected" and fold memorization into the covariate. A unigram
frequency can't contain any lyric sequence.
"""

import argparse
import random
import sys
from pathlib import Path

import jiwer
from wordfreq import zipf_frequency

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from rapbench import OUTPUTS_DIR, RESULTS_DIR, load_segments
from rapbench.normalize import normalize
from rapbench.scoring import SURVIVAL_WER, SegmentScore, critical_rate
from score import POPULATIONS, load_reference
from synth import count_syllables


DELTAS = [("exhibition", "core"), ("exhibition", "fresh"), ("fresh", "core")]
BINS = ["common", "mid", "rare"]


def vocab_bin(word: str) -> int:
    z = zipf_frequency(word, "en")
    return 0 if z >= 5 else 1 if z >= 3 else 2


def line_errors(reference: str, hypothesis: str, bins: bool = False) -> list[list[list[int]]]:
    """Per reference line, [errors, words] per vocabulary bin (a single
    bin unless `bins`), using whichever ad-lib variant scores best, as
    score_segment does."""
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
        per_line = [[[0, 0] for _ in (BINS if bins else [0])] for _ in lines]
        for k, e in enumerate(errs):
            cell = per_line[line_of[k]][vocab_bin(words[k]) if bins else 0]
            cell[0] += e
            cell[1] += 1
        wer = sum(errs) / len(words)
        if best is None or wer < best[0]:
            best = (wer, [x for x in per_line if any(w for _, w in x)])
    return best[1]


def wer_of(lines: list[list[list[int]]], weights: list[float] | None) -> float:
    """Raw WER, or the standardized WER when bin weights are given."""
    tot = [[sum(l[b][i] for l in lines) for i in (0, 1)] for b in range(len(lines[0]))]
    raw = sum(e for e, _ in tot) / sum(w for _, w in tot)
    if weights is None:
        return raw
    return sum(p * (e / w if w else raw) for p, (e, w) in zip(weights, tot))


def resample(lines: list[list[list[int]]], rng: random.Random, weights: list[float] | None) -> float:
    return wer_of([lines[rng.randrange(len(lines))] for _ in lines], weights)


def pct(xs: list[float], q: float) -> float:
    xs = sorted(xs)
    return xs[min(int(q * len(xs)), len(xs) - 1)]


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--reps", type=int, default=2000)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--rate", choices=["listed", "mean"], default="listed")
    p.add_argument("--adjust", choices=["none", "vocab"], default="none")
    args = p.parse_args()
    bins = args.adjust == "vocab"

    segments = {s["id"]: s for s in load_segments()}
    refs = {sid: load_reference(sid) for sid in segments}
    if args.rate == "mean":
        for sid, s in segments.items():
            if refs[sid]:
                s["syl_per_sec"] = round(count_syllables(normalize(refs[sid])) / (s["end"] - s["start"]), 2)
    runs = sorted(d for d in OUTPUTS_DIR.iterdir() if d.is_dir())

    # Vocabulary of the scored references, per population and pooled.
    vocab_rows, weights = [], None
    if bins:
        pooled = [0, 0, 0]
        for pop in POPULATIONS:
            words = [w for sid, s in segments.items()
                     if s.get("population", "exhibition") == pop and refs[sid]
                     for w in normalize(refs[sid]).split()]
            if not words:
                continue
            counts = [0, 0, 0]
            for w in words:
                counts[vocab_bin(w)] += 1
            pooled = [a + b for a, b in zip(pooled, counts)]
            zipf = sum(zipf_frequency(w, "en") for w in words) / len(words)
            vocab_rows.append(f"| {pop} | {len(words)} | {zipf:.2f} | "
                              + " | ".join(f"{c / len(words):.1%}" for c in counts) + " |")
        weights = [c / sum(pooled) for c in pooled]
        vocab_rows.append(f"| **pooled weights p_b** | {sum(pooled)} | | "
                          + " | ".join(f"{w:.1%}" for w in weights) + " |")

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
            data = {sid: line_errors(refs[sid], (run / f"{sid}.txt").read_text(), bins) for sid in ids}
            rng = random.Random(args.seed)
            seg_reps = {sid: [] for sid in ids}
            reps = []
            for _ in range(args.reps):
                scores = []
                for sid in ids:
                    w = resample(data[sid], rng, weights)
                    seg_reps[sid].append(w)
                    scores.append(SegmentScore(sid, segments[sid]["tier"], segments[sid]["syl_per_sec"], w, 0))
                reps.append(critical_rate(scores))
            crit_reps[pop] = reps
            full = [SegmentScore(sid, segments[sid]["tier"], segments[sid]["syl_per_sec"],
                                 wer_of(data[sid], weights), 0) for sid in ids]
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
                n_words = sum(w for l in data[sid] for _, w in l)
                raw = wer_of(data[sid], None)
                adj = f" {wer_of(data[sid], weights):.0%} |" if bins else ""
                wer_rows.append(f"| {run.name} | {sid} | {raw:.0%} |{adj} {pct(seg_reps[sid], .025):.0%}–"
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
        f"rates: {args.rate}; vocabulary adjustment: {args.adjust}; "
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
        "| model | segment | WER |" + (" adjusted WER |" if bins else "") + " 95% CI | lines | words |",
        "|---|---|---|---|---|---|" + ("---|" if bins else ""),
        *wer_rows,
        "",
    ]
    if bins:
        out[4:4] = [
            "## Vocabulary of the scored references",
            "",
            "Share of reference words per wordfreq Zipf bin (common >= 5, mid 3-5, rare < 3). "
            "Critical rates and intervals below use the standardized WER; the per-segment "
            "95% CI is on the adjusted WER.",
            "",
            "| population | words | mean Zipf | common | mid | rare |",
            "|---|---|---|---|---|---|",
            *vocab_rows,
            "",
        ]
    RESULTS_DIR.mkdir(exist_ok=True)
    name = "ci" + ("-mean" if args.rate == "mean" else "") + ("-vocab" if bins else "") + ".md"
    (RESULTS_DIR / name).write_text("\n".join(out))
    print(f"wrote {RESULTS_DIR / name}")


if __name__ == "__main__":
    main()
