# rap-bench

**MMLU: Marshall Mathers Lyrical Understanding.** How fast can a rapper go
before open-source speech recognition falls apart?

Local dictation models post 2.5% word error rates on clean speech. rap-bench
runs them on fast rap instead, from "Lose Yourself" at 5.5 syllables per
second up to the third verse of "Godzilla" at 10.6, and reports where each
model falls off the cliff.

Write-up: [Can Whisper transcribe "Rap God"?](https://adamnoonan-xyz.vercel.app/blog/rap-god/)

## What it measures

- **Critical rate.** The syllable rate where a model's word error rate (WER)
  crosses 25%, read off its WER-vs-rate curve. The curve is made monotone
  first (an isotonic envelope), and the crossing is interpolated between the
  two tested rates either side of it. `>x` means the model survived every
  segment, `<x` means it failed the slowest one.
- **Live critical rate.** The same, but a segment counts as failed if the
  model transcribed it slower than real time (RTF ≥ 1). It answers whether
  the model could caption the verse as it's being rapped.
- **Confidence intervals.** `scripts/bootstrap_ci.py` resamples whole lyric
  lines (errors come in runs, so resampling single words would make intervals
  too narrow) and reports 95% intervals on WER, critical rate, and the gap
  between populations.

## Three populations

Famous tracks are in every model's training data, so a good score on them
can be recall instead of hearing. Segments are scored in separate
populations:

| population | what it is | n | status |
|---|---|---|---|
| exhibition | famous commercial tracks (Eminem, Twista, Busta Rhymes) | 7 | scored |
| core | Suno-generated verses no model has seen | 2 | scored |
| fresh | real tracks first released after 2025-06-01, after every model in the roster | 21 | transcribed, lyrics awaiting verification |

The fresh tier is the clean test: human vocals, real production, and
contamination ruled out by release date. Scores for it are withheld until
the lyrics are hand-verified.

## Findings so far

- **Almost nothing transcribes the top tier.** Only whisper large-v3 on
  demucs-separated vocals stays at or under 25% WER on both "Rap God" (9.6
  syl/s, 22%) and "Godzilla" v3 (10.6, 25%), and it runs slower than real
  time on both.
- **Famous tracks look easier than they are, but by less than the first
  analysis said.** On published rates, whisper large-v3 survives about 3
  syl/s faster on famous tracks than on unseen ones. Two audits shrank that
  ([LOG.md](LOG.md), 2026-10-28):
  - The famous tracks' rates were peaks and the Suno verses' were means. On
    mean rates for both, the large-v3 gap is +2.0 syl/s (95% CI −0.4 to +4.3).
  - The Suno verses use rarer words (15.1% rare vs 6.5%). Adjusting for
    vocabulary takes the gap to +1.6 (−0.8 to +4.1).

  Every model's interval includes zero. The fresh tier is built to settle it.
- **Fast and accurate rarely come together.** large-v3 is the most accurate
  model on famous tracks but runs slower than real time on the hardest ones.
  Parakeet runs 17–50× faster than real time and MLX whisper turbo 7–25×.

Tables: [results/results.md](results/results.md) ·
[results/ci-mean.md](results/ci-mean.md) ·
[results/ci-mean-vocab.md](results/ci-mean-vocab.md). Design and
pre-registered predictions: [DESIGN.md](DESIGN.md). Every run and dead end:
[LOG.md](LOG.md).

## No commercial audio in this repo

The repo ships the harness, the segment manifest (timestamps plus links to
public uploads, official audio where it exists), short lyric excerpts for
scoring, and results. `scripts/fetch.py` downloads and trims your own local
copies. `audio/`, `stems/` and `outputs/` are gitignored. The only audio
committed is the synthetic material in `synthetic/`, which was generated for
this project.

## Running it

Python 3.10+ and ffmpeg on PATH.

```bash
uv venv && uv pip install -e ".[fetch,whisper,analysis,mlx]"
# mlx is Apple silicon only; other extras: separate (demucs), hf (transformers)

python scripts/fetch.py                       # download + trim to audio/<id>.wav
python scripts/separate.py                    # optional: demucs vocal stems

python scripts/transcribe.py --model faster-whisper:large-v3 --source raw
python scripts/transcribe.py --model parakeet:mlx-community/parakeet-tdt-0.6b-v2

python scripts/score.py                       # results/results.md
python scripts/bootstrap_ci.py --rate mean    # results/ci-mean.md
python scripts/bootstrap_ci.py --rate mean --adjust vocab
```

Backends: `faster-whisper:<size>`, `whisper:<size>` (openai-whisper),
`hf:<model-id>` (anything the Hugging Face ASR pipeline loads),
`mlx-whisper:<repo>` and `parakeet:<repo>`. To add another, add a load/run
pair to `BACKENDS` in [scripts/transcribe.py](scripts/transcribe.py).

## Scripts

| script | does |
|---|---|
| `fetch.py` | downloads each segment's source and trims it to 16 kHz mono |
| `separate.py` | demucs vocal stems, for the raw-vs-vocals comparison |
| `transcribe.py` | runs a backend over the segments, timing inference |
| `score.py` | WER, RTF and critical rates per population |
| `bootstrap_ci.py` | line-level bootstrap intervals; `--rate mean`, `--adjust vocab` |
| `draft_lyrics.py` | drafts reference lyrics from LRCLIB's synced lyrics |
| `verify.sh` | tmux cockpit: clip on loop at 0.5× beside the lyric file |
| `scout.py` | finds post-cutoff fast tracks (MusicBrainz + LRCLIB) |
| `select_fresh.py` | turns scouted tracks into fresh segments |
| `synth.py` | builds a speed-swept synthetic tier from a rendered verse |
| `stream_sim.py` | simulates live captioning and measures caption lag |
| `prior_probe.py`, `prior_logprob.py` | probe whisper's decoder for memorized lyrics |

## Ground truth

Official lyrics often don't match what's rapped in fast passages. Every
reference in `lyrics/` is checked by ear at 0.5× against its clip. A lyric
file containing `TODO` is a draft, and the scorer skips it. Reference and
transcript both go through the same normalizer
([rapbench/normalize.py](rapbench/normalize.py)), which ignores casing,
punctuation and censoring and treats ad-libs as optional, in the spirit of
[Jam-ALT](https://audioshake.github.io/jam-alt/).

Known issues:

- The "Look at Me Now" source is a music-video rip and sounds muddy. Treat
  its scores with suspicion.
- Clip edges cut a word or two mid-syllable. That noise hits every model
  equally, so it doesn't change rankings.
- RTF on separated-vocals runs excludes demucs time, so live rates from
  those runs are optimistic.

Verified segments are welcome, especially fast rap from after mid-2025 and
fast rap in languages other than English.

## License

Code is [MIT](LICENSE). The lyric excerpts in `lyrics/` belong to their
rights holders and are included only as short references for scoring; the
MIT license doesn't cover them.
