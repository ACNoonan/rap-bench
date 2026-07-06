# rap-bench

**MMLU: Marshall Mathers Lyrical Understanding.**

Local dictation models keep posting insane tokens/sec numbers at ~2.5% WER —
on clean speech. This benchmark asks the question that actually matters:
*can it transcribe "Rap God"?*

rap-bench scores open-source ASR models on a difficulty ladder of fast-rap
excerpts, up to the Guinness-pace third verse of "Godzilla"
(~10.6 syllables/sec). Two stats per model:

- **max clean rate** — the fastest syllable rate it transcribes with WER
  under 25%.
- **max live rate** — the fastest syllable rate it transcribes accurately
  *and* faster than real time (RTF < 1). This is the golden standard:
  generating tokens at least as fast as the rapper spits them, i.e. the
  model could live-transcribe the verse.

## Results

See [results/results.md](results/results.md).

## Design

- **Difficulty ladder, not just WER.** Segments are tiered
  `baseline → fast → insane` by peak syllable rate
  (see [segments.yaml](segments.yaml)). The leaderboard is about where each
  model falls off the cliff.
- **Speed counts.** `transcribe.py` times inference (model load excluded)
  and `score.py` reports real-time factor per segment. Accuracy alone gets
  you *max clean rate*; accuracy at RTF < 1 gets you *max live rate*.
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
  by ear at 0.5× speed against the excerpt; the manifest tracks
  `timing_verified` and `lyrics_verified` per segment, and the scorer skips
  segments whose lyrics are still TODO.

## No audio in this repo

The audio is commercially released music, so the repo ships **no audio and no
stems** — only the harness, the segment manifest (timestamps plus links to
public YouTube uploads, official where available), short lyric excerpts for
scoring, and results. You fetch your own copies locally with
`scripts/fetch.py`, or drop pre-trimmed 16 kHz mono WAVs into
`audio/<id>.wav`. `audio/`, `stems/`, and `outputs/` are gitignored.

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
| baseline | Lose Yourself v1 · The Way I Am v1 | ~5.5 |
| fast | Look at Me Now (Busta) · Speedom (Em) | 8–9 |
| insane | Worldwide Choppers (Twista) · Rap God fast bit · Godzilla v3 | 9.6–10.6 |

All timestamps verified by ear against the linked sources. Known issues:

- The Look at Me Now rip (music video, no official audio exists) sounds
  quiet and muddled — treat that segment's scores with suspicion until a
  better source is found. Its sync stamps also don't match the album, so
  LRCLIB drafts for it need manual re-windowing.
- Clip boundaries don't land exactly on lyric-line boundaries; references
  were hand-trimmed to match the audio, but expect a word or two of edge
  noise (partial words at cut points) in absolute WER. It affects every
  model identically, so rankings are unaffected.

Contributions of verified segments welcome — especially non-Eminem choppers
(Tech N9ne, Krayzie Bone, Daveed Diggs…) and non-English fast rap.
