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

# v3: the fresh tier (draft, 2026-10-28)

## Why

v2's memorization claim compares famous human recordings against one
Suno verse at two rates. Three things are confounded with "memorized vs
not": human vs synthetic vocals at speed, ordinary vs rare vocabulary
("monological"), and, until 2026-10-28, peak vs mean rate units (LOG.md).
With rates on one scale, no model's delta excludes zero.

The blog post argued that for real recordings, verifiable lyrics and
training contamination are the same variable. That holds only while the
model keeps training. Every roster model is frozen, and the newest,
parakeet-tdt-0.6b-v2, was released 2025-05-01. A track first released
after that date cannot be in any roster model's training data, and its
lyrics can still be verified. So contamination is ruled out by date, not
by obscurity.

Release dates, from memory except parakeet (searched 2026-10-28):
wav2vec2-960h 2020, whisper large-v3 2023-11, distil-large-v3 2024-03,
whisper turbo 2024-10, moonshine 2024-10, parakeet v2 2025-05-01.

## Population `fresh`

- Real tracks, first released on or after **2025-06-01** (MusicBrainz
  first-release-date), English, commercially released.
- Target 12–20 segments of 25–45 s, spread over **4–10 syl/s mean rate**,
  at least two per 1 syl/s bin, several artists per bin so no single voice
  owns a rate.
- Candidates from `scripts/scout.py` → results/scout.md; Adam adds any he
  knows. A segment's window is chosen on its densest contiguous passage.
- Same pipeline as exhibition: yt-dlp official audio, `draft_lyrics.py`
  from LRCLIB, then Adam verifies timing by ear and lyrics at 0.5×, and
  deletes the TODO-VERIFY line. The scorer skips a segment until then.
- `syl_per_sec` for every population is the **mean** rate: syllables of
  the verified lyrics (synth.py's counter) over clip duration.

## What gets measured

1. **Fresh critical rate** per model: the honest ceiling on unseen human
   rap, from a real curve rather than two points.
2. **Memorization delta** = exhibition − fresh critical rate, mean rates
   on both sides, with a bootstrap interval. Human vs human, so the
   synthetic-vocals confound is gone.
3. **Vocabulary covariate**: WER standardized to a pooled word-frequency
   mix (`bootstrap_ci.py --adjust vocab`, wordfreq Zipf bins). Amended
   2026-10-28 from decoder log-prob, which memorization contaminates; see
   LOG.md. On v2 data rarity runs the other way (Suno verses are rarer),
   so adjusting shrinks the delta.
4. Core (Suno) stays as a secondary population; fresh vs core at matched
   rate tests whether synthetic vocals at speed are harder than human.

## Predictions, recorded before any fresh segment is scored

- Claude (2026-10-28): whisper large-v3 fresh critical rate **7.0 syl/s**
  (between core 6.1 and exhibition 8.0); large-v3 exhibition − fresh
  delta **+1.0**, with an interval that still includes zero unless n ≥ 15;
  parakeet delta **≈ 0**.
- Adam: _(fill in before verifying lyrics, since verification is what
  unlocks the scores)_

## Pre-requisites still open from v2

- suno01's human read-along (lyrics/suno01.txt says "full line-by-line
  read-along still worth doing before publishing numbers").

## Status 2026-10-28 and the weekend checklist

Done by Claude: 21 fresh segments in segments.yaml (12 artists, draft mean
rates 4.5–10.6 syl/s, nothing between 9 and 10), audio fetched, lyric
drafts from the same LRCLIB entry the window was chosen on, all nine raw
configurations transcribed. Fresh scores stay hidden until verification:
score.py and bootstrap_ci.py skip any lyric file containing TODO.

Adam, in this order:

1. **Bet first.** Write your fresh-tier predictions above (large-v3 fresh
   critical rate, large-v3 and parakeet exhibition − fresh delta, mean
   rates) before step 2 — verification is what reveals the scores.
2. **Verify each fresh clip** (`lyrics/fresh-*.txt` against
   `audio/fresh-*.wav` at 0.5×): fix words to what is actually rapped,
   delete any opening line that starts before the clip (draft_lyrics.py
   pads 3 s before the window), mark ad-libs in parentheses, delete the
   TODO-VERIFY line, then set `timing_verified` and `lyrics_verified` in
   segments.yaml. About 21 × 30 s of audio; budget 1.5–2 h.
3. **suno01 read-along**, the open v2 item.
4. Then: `python scripts/score.py`, `python scripts/bootstrap_ci.py --rate mean`.
   The mean-rate run re-measures every rate from the verified lyrics.
5. ~~Decide the repo link~~: public since 2026-10-28, MIT for the code.

Run the vocabulary-adjusted table too: `bootstrap_ci.py --rate mean
--adjust vocab` → results/ci-mean-vocab.md (built 2026-10-28, LOG.md).

The 9–10 syl/s gap stays open: 54 artists scouted, no post-cutoff track
holds 9+ for 25 s besides TITANIC (LOG.md, 2026-10-28).


# v4: fine-tuning for fast rap (draft, 2026-10-28)

Not started. Blocked on v3: the verified fresh tier is the baseline every
fine-tune is measured against.

## Question

Can a cheap adapter teach a fast model to hear fast rap? The v2/v3 picture
is that whisper large-v3 is the most accurate model but runs slower than
real time at the top tier, while turbo (809M) and parakeet-tdt-0.6b-v2 run
7–50× faster than real time and fall off around 6 syl/s on unseen material.
A fast model that stays accurate at 8+ syl/s would be the first one that
could caption fast rap live. So the targets are turbo and parakeet, not
large-v3.

## Methods, in order

1. **LoRA SFT.** Audio paired with verified lyrics, ordinary cross-entropy
   on the transcript tokens. Standard for whisper (PEFT, or MLX on the Mac);
   parakeet goes through NeMo. This is the method that teaches hearing,
   which is the v2 failure: syllables dropped and mangled at speed.
2. **DPO, only if SFT leaves a specific failure.** Pairs of (verified
   transcript, the model's own bad transcript on the same clip). Aimed at
   whisper's temperature-fallback loops and invented lines, which are a
   preference problem more than a hearing one.
3. **Minimum-WER training (the ASR form of RL), only if SFT plateaus.**
   Sample N transcripts per clip, reward −WER. Published gains over SFT are
   usually small; I did not check them for singing or rap specifically.

## Training data

All of it must be disjoint from every eval population (below).

- **Real rap, LRCLIB-synced.** `scout.py` + `select_fresh.py` already find
  tracks, pick windows and fetch audio. Training wants whole songs, or many
  windows per song, not one 30 s window. Pre-cutoff catalogs are fine for
  training (contamination only matters for eval). LRCLIB lyrics are
  unverified, so training labels are noisy; budget a verified subset for
  validation only. Audio stays local and gitignored like the rest. Training
  on commercial audio is a legal gray zone even kept private.
- **DALI** (about 5,000 songs with aligned lyrics, mostly not rap). I did
  not check its license or its rap share.
- **Suno.** Unlimited fast verses with exact lyrics. Worth generating only
  if v3's fresh − core comparison at matched rate shows synthetic vocals
  behave like human ones; otherwise the adapter learns Suno.
- **Time-stretch augmentation** with `synth.py`'s pitch-preserving stretch,
  capped near 1.3× because it sounds unnatural beyond that.
- Train on full mixes, not demucs stems: live captioning gets the mix.

Target size for the first run: about 20 hours.

## Eval and the leak rules

- **Primary: fresh tier, artist-held-out.** No track by any artist credited
  on a fresh segment goes in training: GAWNE, JID, Token, Joyner Lucas,
  Tech N9ne, Logic, NF, Merkules, Ren, Dax, King Iso, Chris Webby, Doja Cat
  (13). That tests unseen voices, not only unseen songs, so an adapter that
  learns particular voices doesn't pass.
- **Exhibition** stays a secondary readout and its artists are excluded
  from training too: Eminem, Twista, Busta Rhymes, Chris Brown, and every
  feature on "Worldwide Choppers" and "Speedom" (Tech N9ne is already out).
- **Core** (Suno) stays as is. If Suno data goes into training, core is no
  longer unseen in style and gets reported as such.
- **Clean-speech regression check.** A few minutes of ordinary read speech
  (a LibriSpeech test-clean slice) before and after, so a rap gain that
  wrecks normal dictation is visible.

## Measures

- Fresh critical rate, base vs fine-tuned, per target model, on mean rates.
- **Paired** bootstrap interval on the difference: both models scored on
  the same resampled lines in each replicate. bootstrap_ci.py is close but
  not there. It reseeds identically per run, but `line_errors` picks the
  ad-lib variant that scores best per model, and a line made only of
  ad-libs disappears when they're stripped, so two models can resample
  different line sets. It needs one fixed variant per segment for paired
  runs, plus a cross-model delta next to the cross-population ones.
- Live critical rate, because the point is a fast model: an adapter that
  slows decoding past real time fails the question even if WER drops.
- With 21 fresh segments, a gain under about 1 syl/s will likely sit inside
  the interval (my estimate from v3-era interval widths, before the fresh
  tier is scored; recheck once it is).

## Predictions, recorded before any training

- Claude (2026-10-28): LoRA SFT on about 20 h of real rap lifts turbo's
  fresh critical rate from about 6.5 to about **8.0 syl/s** (unsure; the 6.5
  base is itself a guess until v3 is scored). DPO on top adds **under 0.5**.
  Clean-speech WER moves less than 1 point. The main risk is voice
  memorization, which the artist hold-out is there to catch.
- Adam: _(blank)_

## Decisions fixed before the first run (2026-10-28, after hostile review)

- **Headline checkpoint: the final epoch (e3).** Not the best-looking one.
  Picking an epoch after seeing fresh scores would be selection on the test
  set. e1 and e2 transcripts are kept as a learning curve only.
- **One seed (7).** The bootstrap covers sampling over clips, not training
  noise, so the result is reported as a single training run.
- **Instrument pass (D1):** the base model through the HF pipeline must land
  within a median 5 WER points of July's faster-whisper turbo on the scored
  exhibition and core segments. If it doesn't, the eval path is broken and
  the run answers nothing.
- **Coverage gate:** on clips over 30 s, an adapter transcript under 0.7× the
  base model's word count flags broken long-form seeking. Half the training
  labels carry timestamp tokens to prevent that.
- **Leak check is independent of the name filter:** `build_train.py check`
  fails on 3+ 8-grams shared between one training song and any lyric
  reference, and on any chunk over 30 s. Lil Wayne (on "Look at Me Now") is
  held out with the other exhibition guests. I did not check guest credits
  on the fresh tracks beyond the primary artist; the 8-gram check covers the
  songs, not the voices.

## Cost

A LoRA on turbo with about 20 h of audio is a few GPU-hours on a 24 GB card,
under $10 on RunPod (my estimate, unsure). It may fit on the Mac through MLX,
more slowly. Paid runs go through /gpu-run with its smoke gate and cost
confirmation.

## Pre-requisites

1. v3 verified and scored (the baseline).
2. The fresh − core matched-rate result, which decides whether Suno data is
   worth generating.
3. A training-set builder that enforces the artist exclusion list above
   from segments.yaml, so the leak rule is code, not memory.
4. Cross-model paired delta in bootstrap_ci.py, with the ad-lib variant
   fixed per segment.
