"""WER scoring and the tier leaderboard stat."""

from dataclasses import dataclass

import jiwer

from .normalize import normalize

TIER_ORDER = ["control", "baseline", "fast", "insane"]

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

    @property
    def survived(self) -> bool:
        return self.wer < SURVIVAL_WER


def score_segment(segment: dict, reference: str, hypothesis: str) -> SegmentScore:
    ref = normalize(reference)
    hyp = normalize(hypothesis)
    return SegmentScore(
        segment_id=segment["id"],
        tier=segment["tier"],
        syl_per_sec=segment["syl_per_sec"],
        wer=jiwer.wer(ref, hyp),
        ref_words=len(ref.split()),
    )


def max_clean_rate(scores: list[SegmentScore]) -> float:
    """The headline stat: fastest syllable rate the model survives.

    Returns the highest syl_per_sec among surviving non-control segments,
    or 0.0 if the model can't even hold the baseline tier.
    """
    survived = [s for s in scores if s.survived and s.tier != "control"]
    return max((s.syl_per_sec for s in survived), default=0.0)
