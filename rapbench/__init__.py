"""rap-bench — MMLU: Marshall Mathers Lyrical Understanding."""

from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
AUDIO_DIR = REPO_ROOT / "audio"
STEMS_DIR = REPO_ROOT / "stems"
OUTPUTS_DIR = REPO_ROOT / "outputs"
LYRICS_DIR = REPO_ROOT / "lyrics"
RESULTS_DIR = REPO_ROOT / "results"


def load_segments() -> list[dict]:
    with open(REPO_ROOT / "segments.yaml") as f:
        return yaml.safe_load(f)["segments"]


def audio_path(segment_id: str, source: str) -> Path:
    """source: 'raw' (full mix) or 'vocals' (demucs-separated)."""
    if source == "raw":
        return AUDIO_DIR / f"{segment_id}.wav"
    if source == "vocals":
        return STEMS_DIR / f"{segment_id}_vocals.wav"
    raise ValueError(f"unknown source: {source}")
