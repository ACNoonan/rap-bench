#!/usr/bin/env python3
"""Score every model run in outputs/ and write results/results.md.

    python scripts/score.py

A run is any outputs/<name>/ directory produced by scripts/transcribe.py.
Segments whose lyric file still contains TODO markers are skipped.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from rapbench import LYRICS_DIR, OUTPUTS_DIR, RESULTS_DIR, load_segments
from rapbench.scoring import (
    SURVIVAL_WER,
    TIER_ORDER,
    max_clean_rate,
    max_live_rate,
    score_segment,
)


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


def main() -> None:
    segments = {s["id"]: s for s in load_segments()}
    references = {sid: load_reference(sid) for sid in segments}
    scorable = [sid for sid, ref in references.items() if ref]
    skipped = sorted(set(segments) - set(scorable))
    if skipped:
        print(f"skipping (no verified lyrics yet): {', '.join(skipped)}")
    if not scorable:
        sys.exit("no scorable segments — fill in lyrics/<id>.txt first")

    runs = sorted(d for d in OUTPUTS_DIR.iterdir() if d.is_dir()) if OUTPUTS_DIR.exists() else []
    if not runs:
        sys.exit("no runs in outputs/ — run scripts/transcribe.py first")

    ordered = sorted(
        scorable, key=lambda sid: (TIER_ORDER.index(segments[sid]["tier"]), segments[sid]["syl_per_sec"])
    )

    lines = [
        "# rap-bench results",
        "",
        f"Cells are `WER · RTF` after lyric normalization; survival threshold {SURVIVAL_WER:.0%}. "
        "💀 = WER over threshold, 🐢 = accurate but slower than real time. "
        "**max clean rate** = fastest syl/sec transcribed accurately; "
        "**max live rate** = fastest syl/sec transcribed accurately AND faster "
        "than the rapper (RTF < 1) — the golden standard.",
        "",
        "| model | " + " | ".join(ordered) + " | max clean rate | max live rate |",
        "|---" * (len(ordered) + 3) + "|",
    ]

    for run in runs:
        scores = []
        cells = []
        for sid in ordered:
            hyp_path = run / f"{sid}.txt"
            if not hyp_path.exists():
                cells.append("—")
                continue
            score = score_segment(
                segments[sid], references[sid], hyp_path.read_text(), rtf=load_rtf(run, segments[sid])
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
        clean, live = max_clean_rate(scores), max_live_rate(scores)
        lines.append(
            f"| {run.name} | " + " | ".join(cells) + f" | {clean:.1f} syl/s | {live:.1f} syl/s |"
        )
        print(f"{run.name}: max clean rate {clean:.1f} syl/s, max live rate {live:.1f} syl/s")

    lines += [
        "",
        "Segments ordered easy → hard: "
        + ", ".join(f"{sid} ({segments[sid]['syl_per_sec']} syl/s)" for sid in ordered),
        "",
    ]

    RESULTS_DIR.mkdir(exist_ok=True)
    out = RESULTS_DIR / "results.md"
    out.write_text("\n".join(lines))
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
