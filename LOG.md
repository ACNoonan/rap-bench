# Methodology log

Lab-notebook of what we tried, what we found, and what we changed our minds
about. Raw material for a future writeup.

## 2026-07-06 — v1: the M&M benchmark

**Premise.** An X post bragged 527.9 tok/s local dictation at ~2.5% WER.
On what audio, though? Built rap-bench to ask: can open-source ASR
transcribe fast rap — tagline "MMLU: Marshall Mathers Lyrical
Understanding."

**Design decisions.**
- 7 real segments tiered by peak syllable rate: baseline (~5.5 syl/s,
  Lose Yourself) → fast (8–9, Busta / Speedom) → insane (9.6–10.6, Rap
  God / Worldwide Choppers / Godzilla v3).
- Copyright: no audio distributed; manifest ships timestamps + public
  URLs, users fetch locally. Lyrics as short excerpts.
- Lyric-aware WER (Jam-ALT-inspired normalization; parenthesized ad-libs
  scored as optional — best-of with/without reference).
- Golden standard: **max live rate** — fastest syl/sec transcribed under
  25% WER at RTF < 1, i.e. generating tokens faster than the rapper.
- Dropped a planned interview-clip control (never goes fast; off-thesis).

**Ground-truth shortcut that worked.** LRCLIB's time-synced lyrics,
trimmed to each excerpt's window, turned transcription-from-scratch into
a read-along fix-up pass (~2–3 min/segment). One landmine: sync stamps
are album-relative — the one music-video-sourced segment (Look at Me
Now) got Lil Wayne's verse drafted instead of Busta's.

## 2026-07-06 — v1 results (11 runs, 7 model families)

Full table: results/results.md at commit e1ddb07.

- **Golden standard: three-way tie at 9.0 syl/s** (Speedom) — large-v3
  (RTF 0.98!), CT2 turbo, mlx large-v3-turbo (RTF 0.05, 20× headroom).
  Nothing live-transcribes the insane tier. Godzilla v3 (10.6) unclaimed
  at any speed.
- **Failure taxonomy.** (1) Silent collapse: whisper's anti-hallucination
  checks bail mid-verse — tiny emitted an *empty file* on Rap God; CT2
  turbo quit after 16 words. (2) Graceful degradation: large-v3 loses on
  points with phonetic near-misses ("ricochetin' off of me" → "pick a
  shang and offer me"). (3) CTC phoneme soup vs seq2seq fluent lies:
  wav2vec2 fails as visible garbage; moonshine fails as confident,
  undetectable fabrication. The "worse-looking" failure is safer to
  build on.
- **Difficulty multiplies latency (whisper only).** large-v3 RTF 0.63 on
  baseline → 3.09 on Rap God: denser syllables = more tokens/audio-sec,
  plus temperature-fallback re-decoding (up to 5 retries). Parakeet's
  transducer has no retry loop: RTF flat 0.02–0.06 regardless.
  Consequence: throughput measured on easy audio (cf. the 527.9 tps
  post) says nothing about the adversarial regime.
- **Clean-speech leaderboards don't transfer.** Parakeet tops the HF
  Open ASR Leaderboard; here it's the fastest and folds at the fast
  tier. Whisper's robustness looks like a data story (680k hrs of webby
  audio incl. music), not architecture.
- **Same weights ≠ same result.** CT2 turbo 88% vs mlx turbo 39% on Rap
  God — identical weights, different decode-fallback behavior.
- **Demucs stems**: rescue insane-tier accuracy (Rap God 28→22%,
  Godzilla 26→25%) but worsen Choppers (22→33%, separation artifacts on
  Twista) and slow whisper down. Separation is a confound, not a clean
  control.

## 2026-07-06 — contamination realization → v2 design

large-v3's Godzilla tail is near-perfect *at 10.6 syl/s* — these lyrics
saturate training data; part of that is recall, not listening. The tell:
moonshine transcribes exactly one line perfectly — "mom's spaghetti."
Also: binary survival on n=1 clips is decided by ~2 words (Godzilla died
26% vs 25% threshold, same magnitude as our clip-boundary noise).

**V2 (DESIGN.md):** exhibition tier (real tracks, labeled contaminated) +
synthetic core (LLM-written original chopper verses, n-gram-checked,
TTS-rendered, speed-swept) + ±beat ablation. Primary metric becomes
**critical rate**: interpolated syl/sec where the WER-vs-rate curve
crosses 25%. Exhibition−core delta at matched rate = memorization,
measured.

## 2026-07-06 — pilot: time-stretch is OUT

Pilot: 1 original verse (contamination-checked clean), OpenAI TTS render
(4.69 syl/s base), pitch-preserving atempo to {5, 6.5, 8, 9.5, 11}
syl/s × {a cappella, synthesized beat}.

**Finding (the good):** harness end-to-end works; ground truth by
construction eliminated all verification labor; Parakeet produced a
clean monotone psychometric curve — 5% → 22% (acap) / 28% (beat) —
critical rate ≈ 11 syl/s, beat penalty emerging at high rates exactly
as designed.

**Finding (the fatal):** mlx-turbo stayed FLAT at 5–8% WER through 11
syl/s — versus 39% on real Rap God at 9.6. **Pitch-preserving
time-stretch produces slow speech played fast, not fast speech.** Real
fast speech has articulatory reduction — vowels reduce, consonants
blur, coarticulation smears boundaries — and that reduction, not pace
itself, is what makes fast rap hard. atempo preserves the TTS render's
careful articulation perfectly. Our difficulty dial turned pace without
turning difficulty. (Also: a −9dB kick/snare/hat loop masks nothing
like a produced mix.)

**Decision:** drop time-stretch as the difficulty mechanism. Candidate
replacements:
1. **Suno-class generated vocals** — original lyrics with real(ish) rap
   flow. Escapes the fundamental bind (see below) but reintroduces
   sung-lyrics verification, and may simply be unable to rap at 10+
   syl/s (feasibility unknown).
2. **Obscure real fast rap** — real flow, real production. But
   contamination and ground-truth availability are the *same variable*:
   if lyrics are indexed (Genius/LRCLIB), models may have trained on
   them; if they aren't, we're back to by-ear transcription of choppers.
   Obscurity reduces contamination probabilistically, never to zero.
3. Natively-fast TTS (instructed maximum speaking speed) — real
   reduction, still not rap flow. Cheap; possibly a useful mid rung.

**The bind worth writing about:** for real music, ground-truth
availability *correlates with* training-set contamination — the
tracks you can verify are the tracks models memorized. Synthetic
generation is the only clean escape, if it can reach the required
syllable rates.
