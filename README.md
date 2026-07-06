# rap-bench

**MMLU: Marshall Mathers Lyrical Understanding.**

Local dictation models keep posting insane tokens/sec numbers at ~2.5% WER —
on clean speech. This benchmark asks the question that actually matters:
*can it transcribe "Rap God"?*

rap-bench scores open-source ASR models on a difficulty ladder of fast-rap
excerpts, from conversational speech (control) up to the Guinness-pace third
verse of "Godzilla" (~10.6 syllables/sec). The headline stat per model is its
**max clean rate**: the fastest syllable rate it survives with WER under 25%.

## Results

See [results/results.md](results/results.md).

## Design

- **Difficulty ladder, not just WER.** Segments are tiered
  `control → baseline → fast → insane` by peak syllable rate
  (see [segments.yaml](segments.yaml)). Everyone aces the control; the
  leaderboard is about where each model falls off the cliff.
- **Raw mix vs. separated vocals.** Half of what kills ASR on rap is the beat,
  not the speed. Every model runs twice — on the raw track and on
  demucs-extracted vocal stems — turning that confound into a second axis.
- **Lyric-aware normalization.** Naive WER punishes casing, punctuation,
  ad-lib markers, and censoring. Both reference and hypothesis pass through
  the same normalizer ([rapbench/normalize.py](rapbench/normalize.py)),
  following the spirit of the [Jam-ALT](https://audioshake.github.io/jam-alt/)
  lyrics-transcription benchmark.
- **Contested ground truth.** Official lyrics often don't match what's
  actually rapped in fast passages. References in `lyrics/` are hand-verified
  by ear at 0.5× speed against the excerpt; segments still marked
  `verified: false` in the manifest are excluded from headline results.

## No audio in this repo

The audio is commercially released music, so the repo ships **no audio, no
stems, and no source URLs** — only the harness, the segment manifest
(timestamps), short lyric excerpts for scoring, and results. Bring your own
copies: fill in `url:` per segment in `segments.yaml` (any yt-dlp-compatible
source) or drop pre-trimmed 16 kHz mono WAVs into `audio/<id>.wav` yourself.
`audio/`, `stems/`, and `outputs/` are gitignored.

## Running it

```bash
pip install -e ".[fetch,separate,whisper,hf]"   # plus ffmpeg on PATH

python scripts/fetch.py        # download + trim segments (needs url: filled in)
python scripts/separate.py    # demucs vocal stems

python scripts/transcribe.py --model faster-whisper:large-v3 --source raw
python scripts/transcribe.py --model faster-whisper:large-v3 --source vocals
python scripts/transcribe.py --model hf:distil-whisper/distil-large-v3 --source raw

python scripts/score.py       # writes results/results.md
```

Backends: `faster-whisper:<size>`, `whisper:<size>` (openai-whisper), and
`hf:<model-id>` (anything the HF ASR pipeline loads — distil-whisper,
wav2vec2, moonshine…). NVIDIA Parakeet/Canary, Kyutai STT, Voxtral, or your
own dictation service: add a function to `BACKENDS` in
[scripts/transcribe.py](scripts/transcribe.py).

## Roster

| tier | segment | ~syl/sec |
|---|---|---|
| control | Eminem interview clip (speech baseline) | ~4 |
| baseline | Lose Yourself v1 · The Way I Am v1 | ~5.5 |
| fast | Look at Me Now (Busta) · Speedom (Em) | 8–9 |
| insane | Worldwide Choppers (Twista) · Rap God fast bit · Godzilla v3 | 9.6–10.6 |

Contributions of verified segments welcome — especially non-Eminem choppers
(Tech N9ne, Krayzie Bone, Daveed Diggs…) and non-English fast rap.
