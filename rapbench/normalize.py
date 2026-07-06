"""Lyric-aware text normalization for WER scoring.

Naive WER punishes transcripts for things that aren't transcription errors:
punctuation style, casing, ad-lib markers, curly quotes, censored words.
Both reference and hypothesis go through the same pipeline so those wash out.

Rules (in order):
  1. Drop section headers like [Verse 2], [Chorus].
  2. Optionally drop parenthesized ad-libs / backing vocals from the reference.
  3. Standardize unicode apostrophes/quotes to ASCII.
  4. Map censored variants to the uncensored word (see CENSOR_MAP).
  5. Lowercase.
  6. Remove all punctuation except intra-word apostrophes and hyphens.
  7. Collapse whitespace.

Deliberately NOT handled: number expansion ("9 to 5" vs "nine to five") and
contraction expansion ("gonna" vs "going to"). Those are real transcription
choices; hand-verified references should use what is actually rapped.
"""

import re

SECTION_HEADER = re.compile(r"\[[^\]]*\]")
ADLIB = re.compile(r"\([^)]*\)")
APOSTROPHES = str.maketrans({"’": "'", "‘": "'", "“": '"', "”": '"'})
PUNCT = re.compile(r"[^\w\s'-]")
STRAY_MARKS = re.compile(r"(?<!\w)['-]|['-](?!\w)")

# Radio edits and some ASR models censor; map both directions to one token.
CENSOR_MAP = {
    "f***": "fuck", "f**k": "fuck", "f--k": "fuck",
    "s***": "shit", "s**t": "shit",
    "b****": "bitch", "b***h": "bitch",
    "n****": "nigga", "n***a": "nigga",
}


def normalize(text: str, strip_adlibs: bool = True) -> str:
    text = SECTION_HEADER.sub(" ", text)
    if strip_adlibs:
        text = ADLIB.sub(" ", text)
    text = text.translate(APOSTROPHES)
    text = text.lower()
    for censored, plain in CENSOR_MAP.items():
        text = text.replace(censored, plain)
    text = PUNCT.sub(" ", text)
    text = STRAY_MARKS.sub(" ", text)
    return " ".join(text.split())
