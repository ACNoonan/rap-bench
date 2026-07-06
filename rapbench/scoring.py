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
