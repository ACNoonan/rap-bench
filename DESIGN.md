# rap-bench v2 methodology (draft)

Status: proposal, 2026-07-06. V1 results (results/results.md) exposed three
methodology problems this redesign addresses.

## What v1 taught us

1. **Contamination.** Famous lyrics saturate ASR training data; large-v3's
   near-perfect Godzilla tail at 10.6 syl/s is partly recall, not listening
   (see moonshine nailing exactly the meme line "mom's spaghetti" while
   butchering the rest). Absolute WER on famous tracks measures
   transcription + memorization, inseparably.
2. **Binary survival on n=1 clips is fragile.** Godzilla died at 26% vs a
   25% threshold on a 227-word reference — a ~2-word margin, the same
   magnitude as our clip-boundary noise. The ladder also has holes
   (nothing between 5.5 and 9.0 syl/s).
3. **Difficulty multiplies latency for encoder-decoder models** (large-v3
   RTF 0.63 → 3.09 as syllable rate rises, via temperature-fallback
   re-decoding), so RTF must be reported as a function of rate, not a
   scalar — and squeaker results like RTF 0.98 need repeated timing runs.

## V2 tier structure

### Tier A — Exhibition (real tracks, the current 7 segments)
Kept as the headline ("can it transcribe Rap God?") with an explicit
label: contaminated, memorization-aided, absolute WER not comparable
across models trained on different data. The exhibition-vs-core delta at
matched syl/sec is itself a metric: it estimates memorization advantage.

### Tier B — Core (synthetic verses, speed-swept)
- Original chopper-style verses (dense multisyllabic internal rhyme, in
  the Tech N9ne register) written by an LLM.
- **Contamination hygiene:** every verse is n-gram-checked against a real
  lyrics corpus before use; style-prompted LLMs can regurgitate real bars.
- Each verse rendered once by TTS, then pitch-preserving time-stretched to
  a rate ladder (target ~5, 6.5, 8, 9.5, 11 syl/s). Syllable counts are
  computed from the known text (CMUdict/pyphen), rates from measured audio
  duration — difficulty becomes a continuous, exactly-known variable.
- Ground truth is exact by construction: no verification pass, no lyric
  sourcing, and the audio is distributable (no copyright), making the
  benchmark reproducible end-to-end.

### Tier C — Ablation (same verses ± beat)
Each Tier B verse also rendered mixed over an instrumental at matched
loudness. Isolates speed from music masking without demucs artifacts
(v1's stems both rescued Godzilla and *worsened* Choppers — separation is
a confound, not a clean control).

## V2 success definitions

- **Critical rate** (primary): per model, the interpolated syl/sec where
  the WER-vs-rate curve crosses 25%. Replaces binary survival.
- **RTF curve**: RTF vs syl/sec, median of ≥3 timing runs on an otherwise
  idle machine. Whisper-family retry blowup is a finding, not noise.
- **Golden standard (live)**: critical rate restricted to points with
  RTF < 1. Pipeline entries (e.g. demucs+ASR) must count all stages in
  RTF or be labeled as pipelines.
- **Memorization delta**: exhibition WER minus core WER at matched rate.

## Known limits, accepted deliberately

- TTS + time-stretch is *fast dense speech*, not rap flow (no beat-riding
  prosody, cleaner phonation). Tier A stays precisely so the benchmark
  keeps one foot in reality. A music-gen (Suno-class) tier could later
  bridge the gap, at the cost of re-introducing sung-lyrics verification.
- Synthetic audio is likely systematically easier per syl/sec than real
  rap. Cross-tier absolute comparisons are invalid by design; each tier
  answers its own question.

## Pilot before scaling

1 verse × 5 rates × {a cappella, beat-mixed}, run on mlx large-v3-turbo
and parakeet. Ship only if the psychometric curves are monotone-ish and
the critical rate is stable across the two renders; then scale to ~5
verses and the full model roster.
