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
from rapbench.scoring import SURVIVAL_WER, TIER_ORDER, max_clean_rate, score_segment


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
        f"WER after lyric normalization; survival threshold {SURVIVAL_WER:.0%}. "
        "**max clean rate** = fastest syl/sec tier survived (control excluded).",
        "",
        "| model | " + " | ".join(ordered) + " | max clean rate |",
        "|---" * (len(ordered) + 2) + "|",
    ]

    for run in runs:
        scores = []
        cells = []
        for sid in ordered:
            hyp_path = run / f"{sid}.txt"
            if not hyp_path.exists():
                cells.append("—")
                continue
            score = score_segment(segments[sid], references[sid], hyp_path.read_text())
            scores.append(score)
            mark = "" if score.survived else " 💀"
            cells.append(f"{score.wer:.0%}{mark}")
        rate = max_clean_rate(scores)
        lines.append(f"| {run.name} | " + " | ".join(cells) + f" | {rate:.1f} syl/s |")
        print(f"{run.name}: max clean rate {rate:.1f} syl/s")

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
