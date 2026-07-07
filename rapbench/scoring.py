"""WER scoring, real-time factor, and the leaderboard stats."""

from dataclasses import dataclass

import jiwer

from .normalize import normalize

TIER_ORDER = ["baseline", "fast", "insane"]

# A segment "survives" if WER stays under this. 25% is generous on purpose:
# the interesting signal at the top tiers is total collapse, not polish.
SURVIVAL_WER = 0.25


@dataclass
class SegmentScore:
    segment_id: str
    tier: str
    syl_per_sec: float
    wer: float
    ref_words: int
    rtf: float | None = None  # transcription seconds per audio second

    @property
    def survived(self) -> bool:
        return self.wer < SURVIVAL_WER

    @property
    def live(self) -> bool:
        """The golden standard: accurate AND generating tokens at least as
        fast as the rapper spits them (RTF < 1 → could live-transcribe)."""
        return self.survived and self.rtf is not None and self.rtf < 1.0


def score_segment(
    segment: dict, reference: str, hypothesis: str, rtf: float | None = None
) -> SegmentScore:
    """Parenthesized (ad-libs) in the reference are optional: the hypothesis
    is scored against the reference both with and without them, best taken —
    a model shouldn't lose points for hearing more of the track."""
    hyp = normalize(hypothesis)
    variants = {normalize(reference, strip_adlibs=s) for s in (True, False)}
    return SegmentScore(
        segment_id=segment["id"],
        tier=segment["tier"],
        syl_per_sec=segment["syl_per_sec"],
        wer=min(jiwer.wer(ref, hyp) for ref in variants),
        ref_words=len(normalize(reference).split()),
        rtf=rtf,
    )


def max_clean_rate(scores: list[SegmentScore]) -> float:
    """Fastest syllable rate the model transcribes accurately (WER < 25%)."""
    return max((s.syl_per_sec for s in scores if s.survived), default=0.0)


def max_live_rate(scores: list[SegmentScore]) -> float:
    """Fastest syllable rate the model could transcribe accurately AND in
    real time. The crown: a nonzero value on the insane tier means this
    model can live-transcribe Eminem."""
    return max((s.syl_per_sec for s in scores if s.live), default=0.0)


def critical_rate(
    scores: list[SegmentScore], threshold: float = SURVIVAL_WER, live: bool = False
) -> tuple[float, str]:
    """Primary v2 metric (DESIGN.md): the interpolated syl/sec at which the
    WER-vs-rate curve crosses `threshold`.

    Robustness choices, made deliberately:
    - Segments at the same rate are averaged into one point.
    - The curve is made monotone with a running max (isotonic envelope):
      once WER has exceeded the threshold at some rate, a lucky lower WER
      at a higher rate doesn't restore credit. Conservative by design.
    - With live=True, a segment slower than real time (RTF >= 1, or no
      timing recorded) counts as a total live failure (WER treated as 1.0).

    Returns (rate, qualifier): qualifier is "=" for an interpolated
    crossing, "<" if even the slowest point fails (rate is that slowest
    point), ">" if nothing fails (rate is the fastest point tested).
    """
    by_rate: dict[float, list[float]] = {}
    for s in scores:
        wer = s.wer
        if live and not (s.rtf is not None and s.rtf < 1.0):
            wer = 1.0
        by_rate.setdefault(s.syl_per_sec, []).append(wer)
    if not by_rate:
        return 0.0, "<"
    pts = sorted((r, sum(ws) / len(ws)) for r, ws in by_rate.items())
    env, running = [], 0.0
    for r, w in pts:
        running = max(running, w)
        env.append((r, running))
    if env[0][1] >= threshold:
        return env[0][0], "<"
    for (r1, w1), (r2, w2) in zip(env, env[1:]):
        if w1 < threshold <= w2:
            return r1 + (threshold - w1) / (w2 - w1) * (r2 - r1), "="
    return env[-1][0], ">"
