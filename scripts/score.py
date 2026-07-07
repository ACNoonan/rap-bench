#!/usr/bin/env python3
"""Score every model run in outputs/ and write results/results.md.

    python scripts/score.py

A run is any outputs/<name>/ directory produced by scripts/transcribe.py.
Segments whose lyric file still contains TODO markers are skipped, as is
the deprecated-stretch population (see LOG.md: time-stretch is out).

Primary metric (DESIGN.md v2): critical rate — the interpolated syl/sec
where a model's WER-vs-rate curve crosses the survival threshold —
reported separately per population (exhibition = real/contaminated
tracks; core = synthetic/unseen), batch-accuracy and live variants.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from rapbench import LYRICS_DIR, OUTPUTS_DIR, RESULTS_DIR, load_segments
from rapbench.scoring import SURVIVAL_WER, TIER_ORDER, critical_rate, score_segment

POPULATIONS = ["exhibition", "core"]


def load_reference(segment_id: str) -> str | None:
    path = LYRICS_DIR / f"{segment_id}.txt"
    if not path.exists():
        return None
    text = "\n".join(
        line for line in path.read_text().splitlines() if not line.startswith("#")
    ).strip()
    if not text or "TODO" in text:
        return None
    return text


def load_rtf(run: Path, segment: dict) -> float | None:
    time_path = run / f"{segment['id']}.time"
    if not time_path.exists():
        return None
    return float(time_path.read_text()) / (segment["end"] - segment["start"])


def fmt_crit(value: float, qual: str) -> str:
    return {"=": f"{value:.1f}", "<": f"<{value:.1f}", ">": f">{value:.1f}"}[qual]


def main() -> None:
    segments = {s["id"]: s for s in load_segments()}
    references = {sid: load_reference(sid) for sid in segments}
    skipped = sorted(
        sid for sid, s in segments.items()
        if s.get("population", "exhibition") in POPULATIONS and not references[sid]
    )
    if skipped:
        print(f"skipping (no verified lyrics yet): {', '.join(skipped)}")

    runs = sorted(d for d in OUTPUTS_DIR.iterdir() if d.is_dir()) if OUTPUTS_DIR.exists() else []
    if not runs:
        sys.exit("no runs in outputs/ — run scripts/transcribe.py first")

    lines = [
        "# rap-bench results",
        "",
        f"Cells are `WER · RTF` (batch); survival threshold {SURVIVAL_WER:.0%}; "
        "💀 = over threshold, 🐢 = accurate but slower than real time.",
        "",
        "**Critical rate** (primary metric): interpolated syl/sec where the "
        "WER-vs-rate curve crosses the threshold, on an isotonic envelope; "
        "`>x` = survived everything tested, `<x` = failed the slowest point. "
        "**Live** variant treats RTF ≥ 1 as total failure. Populations are "
        "scored separately — exhibition tracks are training-contaminated, "
        "core is synthetic/unseen (see DESIGN.md).",
        "",
    ]

    for pop in POPULATIONS:
        pop_ids = [
            sid for sid, s in segments.items()
            if s.get("population", "exhibition") == pop and references[sid]
        ]
        if not pop_ids:
            continue
        ordered = sorted(
            pop_ids,
            key=lambda sid: (TIER_ORDER.index(segments[sid]["tier"]), segments[sid]["syl_per_sec"]),
        )
        lines += [
            f"## {pop}",
            "",
            "| model | " + " | ".join(ordered) + " | critical rate | live critical rate |",
            "|---" * (len(ordered) + 3) + "|",
        ]
        for run in runs:
            scores, cells = [], []
            for sid in ordered:
                hyp_path = run / f"{sid}.txt"
                if not hyp_path.exists():
                    cells.append("—")
                    continue
                score = score_segment(
                    segments[sid], references[sid], hyp_path.read_text(),
                    rtf=load_rtf(run, segments[sid]),
                )
                scores.append(score)
                cell = f"{score.wer:.0%}"
                if score.rtf is not None:
                    cell += f" · {score.rtf:.2f}×"
                if not score.survived:
                    cell += " 💀"
                elif score.rtf is not None and not score.live:
                    cell += " 🐢"
                cells.append(cell)
            if not scores:
                continue
            crit = fmt_crit(*critical_rate(scores))
            crit_live = fmt_crit(*critical_rate(scores, live=True))
            lines.append(f"| {run.name} | " + " | ".join(cells) + f" | {crit} | {crit_live} |")
            print(f"[{pop}] {run.name}: critical rate {crit}, live {crit_live} syl/s")
        lines += [
            "",
            "Segments easy → hard: "
            + ", ".join(f"{sid} ({segments[sid]['syl_per_sec']} syl/s)" for sid in ordered),
            "",
        ]

    RESULTS_DIR.mkdir(exist_ok=True)
    out = RESULTS_DIR / "results.md"
    out.write_text("\n".join(lines))
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
