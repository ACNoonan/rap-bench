#!/usr/bin/env python3
"""Paired bootstrap on the WER difference between two transcript dirs.

    python scripts/paired_ci.py <eval_items.json> <base dir> <other dir> [...]

For DESIGN.md v4's noise rule: is checkpoint B's pooled WER different from
A's on the same clips? Both are scored on the same units, and every resample
draws the same units for both, so clip difficulty cancels out of the
difference.

Units:
  exhibition, core  reference lines (errors are attributed to lines as in
                    bootstrap_ci.line_errors). bootstrap_ci picks the ad-lib
                    variant per model, which would give the two models
                    different line sets, so here each segment's variant is
                    fixed at the one that scores best for the FIRST dir and
                    used for every dir. That can differ slightly from the
                    score.py point estimate, and both are printed.
  val, clean        whole clips (val texts from eval_items.json, clean refs
                    from train/clean/refs.json).

Pooled WER = sum(errors) / sum(reference words) over the resampled units.
10,000 resamples, seed 0, percentile 95% interval on B − A in WER points.
"""

import json
import random
import sys
from pathlib import Path

import jiwer

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from rapbench import REPO_ROOT, load_segments
from rapbench.normalize import normalize
from score import load_reference

N_BOOT = 10_000


def line_errors(reference: str, hypothesis: str, strip: bool) -> list[tuple[int, int]]:
    """[(errors, words)] per non-empty reference line, for one ad-lib variant."""
    lines = [l for l in (normalize(x, strip_adlibs=strip) for x in reference.splitlines()) if l]
    words = " ".join(lines).split()
    line_of = [i for i, l in enumerate(lines) for _ in l.split()]
    errs = [0] * len(words)
    for c in jiwer.process_words(" ".join(words), normalize(hypothesis) or "<empty>").alignments[0]:
        if c.type in ("substitute", "delete"):
            for k in range(c.ref_start_idx, c.ref_end_idx):
                errs[k] += 1
        elif c.type == "insert":
            errs[max(c.ref_start_idx - 1, 0)] += c.hyp_end_idx - c.hyp_start_idx
    out = [[0, 0] for _ in lines]
    for k, e in enumerate(errs):
        out[line_of[k]][0] += e
        out[line_of[k]][1] += 1
    return [tuple(x) for x in out]


def clip_errors(ref: str, hyp: str) -> tuple[int, int]:
    r = normalize(ref)
    o = jiwer.process_words(r, normalize(hyp) or "<empty>")
    return o.substitutions + o.deletions + o.insertions, o.hits + o.substitutions + o.deletions


def read(d: Path, name: str) -> str:
    p = d / f"{name}.txt"
    return p.read_text() if p.exists() else ""


def units(group: str, items: list[dict], dirs: list[Path]) -> list[list[tuple[int, int]]]:
    """Per dir, the same list of (errors, words) units."""
    per = [[] for _ in dirs]
    if group in ("exhibition", "core"):
        for s in load_segments():
            ref = load_reference(s["id"])
            if s.get("population") != group or not ref:
                continue
            first = read(dirs[0], s["id"])
            strip = min((True, False), key=lambda v: (lambda le: sum(e for e, _ in le) / max(sum(w for _, w in le), 1))(
                line_errors(ref, first, v)))
            for k, d in enumerate(dirs):
                per[k] += line_errors(ref, read(d, s["id"]), strip)
    elif group == "val":
        for i in items:
            if i["name"].startswith("val-") and "text" in i and normalize(i["text"]):
                for k, d in enumerate(dirs):
                    per[k].append(clip_errors(i["text"], read(d, i["name"])))
    elif group == "clean":
        refs = json.loads((REPO_ROOT / "train" / "clean" / "refs.json").read_text())
        for n, ref in refs.items():
            for k, d in enumerate(dirs):
                per[k].append(clip_errors(ref, read(d, f"clean-{n}")))
    return per


def pooled(u: list[tuple[int, int]], idx: list[int]) -> float:
    return sum(u[i][0] for i in idx) / sum(u[i][1] for i in idx)


def main() -> None:
    items = json.loads(Path(sys.argv[1]).read_text())
    seen, uniq = set(), []
    for i in items:
        if i["name"] not in seen:
            seen.add(i["name"]); uniq.append(i)
    dirs = [Path(d) for d in sys.argv[2:]]
    print(f"| group | units | {dirs[0].name} | other | WER | B − A | 95% CI |")
    print("|---|---|---|---|---|---|---|")
    for group in ("exhibition", "core", "val", "clean"):
        per = units(group, uniq, dirs)
        n = len(per[0])
        if not n:
            continue
        a = pooled(per[0], range(n))
        for k, d in enumerate(dirs[1:], 1):
            b = pooled(per[k], range(n))
            rng = random.Random(0)
            diffs = []
            for _ in range(N_BOOT):
                idx = [rng.randrange(n) for _ in range(n)]
                diffs.append(pooled(per[k], idx) - pooled(per[0], idx))
            diffs.sort()
            lo, hi = diffs[int(0.025 * N_BOOT)], diffs[int(0.975 * N_BOOT) - 1]
            print(f"| {group} | {n} | {a:.1%} | {d.name} | {b:.1%} | {100 * (b - a):+.1f} | "
                  f"{100 * lo:+.1f} to {100 * hi:+.1f} |")


if __name__ == "__main__":
    main()
