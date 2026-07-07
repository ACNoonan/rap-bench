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

## 2026-07-06 — Suno feasibility probe (take 1)

Generated "Syllable Centrifuge" from verse-01 lyrics via Suno web UI
(style: "midwest chopper hip hop, rapid-fire double-time flow, 150 BPM").
77.7s track. Measured via mlx-turbo word timestamps:

- **Adherence: strong.** The sung verse tracks our lyrics nearly
  verbatim — verification burden is a light read-along, not a rewrite.
  (Apparent errors like "abolisher of bicycles" are plausibly ASR
  mistakes, not Suno's; needs one listen to attribute. First two lines
  possibly absorbed into the intro.)
- **Speed: insufficient (this take).** Verse mean 4.9 syl/s, peak 5s
  window 6.2 — baseline tier, despite the double-time style prompt.
  Chopper territory (8-11) not reached.
- **Bonus finding:** whisper loop-hallucinated "Ja" ~230 times over the
  non-verse intro — music-conditioned repetition collapse on a clip
  whose lyrics it definitely never saw in training.

Open: can prompt engineering push Suno to 8+? If its ceiling is ~6.5
native, options are (a) hybrid: small stretch (≤1.3×) on natively-rapped
audio — partially reintroduces the stretch confound but on real flow;
(b) Suno covers baseline/fast, obscure real choppers cover insane.

## 2026-07-06 — Suno feasibility probe (takes 2-3): FEASIBLE

Two more generations with speed-focused prompts:

- **suno-02 (30s): the breakthrough.** Mean 8.4 syl/s, peak-5s 10.6 —
  Godzilla-v3 pace — with verbatim adherence at the open ("Calibrated,
  agitated, animated when I'm activated"). Both mlx-turbo and parakeet
  degrade visibly mid-verse on it ("clickin' with the cataclysm scatter
  pattern mapper data splatter") — real ASR-adversarial chopper audio
  with zero training contamination. Suno CAN reach the insane tier;
  speed is promptable.
- **suno-03 (64s): total ASR whiteout.** whisper emits "currently" ×8
  then a wall of Chinese characters; parakeet returns the empty string.
  Needs one listen to adjudicate: mostly-instrumental dud take, or an
  intelligible-to-humans take that zeroes every model (which would be
  the most adversarial sample in the corpus). Do not use before human
  adjudication.
- Both models mishear the same word the same way ("adamant and" →
  "Adam in and" / "Atom in and") — could be Suno's pronunciation, not
  an ASR error. Ground truth for generated vocals must be what was
  SUNG, not what was written: the read-along verification step stays.
- Licensing note: free-tier Suno outputs are non-commercial-licensed;
  distributing clips in the repo needs a ToS check (or a paid plan).

**Decision: Suno is the core-tier engine.** Next: verify suno-02 by ear
→ first core segment; generate more verses/takes at varied rates for
the psychometric ladder; obscure real choppers remain an option for a
memorization-probe tier rather than the core.

## 2026-07-06 — suno-03 adjudicated; suno-02 formalized as core segment #1

Adam's listen: **suno-03 is intelligible-ish rapping that follows our
lyrics** (with hooks and pauses between rap segments) — so the double
ASR whiteout (whisper → Chinese characters; parakeet → empty string) is
a REAL adversarial result on contamination-free audio, not a dud take.
Most adversarial clip in the corpus; ground truth deferred (needs full
by-ear transcription including Suno's invented hooks).

Also confirmed by ear: Suno mispronounced "adamant and" (sounds like
"Adam and / Adam in an") — both ASR models heard the same thing, i.e.
they were RIGHT and the written lyrics were wrong. Locks in the
sung-not-written ground-truth principle. suno02 formalized as core
segment #1 (31.4s, mean 8.4 syl/s, peak 10.6) with sung-truth lyrics.

## 2026-07-06 — core segment #1 results: the fast-tier leaderboard was memorization

Full roster on suno02 (contamination-free chopper, mean 8.4 syl/s, peak
10.6, sung-truth reference):

**Every model dead. Best: mlx-turbo 42%.** Ranking: mlx-turbo 42%, CT2
turbo 44%, large-v3 51%, parakeet 55%, distil 60%, small/moonshine 64%,
tiny 66%, wav2vec2 91%.

The comparison that matters — same models on famous Speedom (9.0 syl/s,
HIGHER rate than suno02's mean): large-v3 23%, turbo 21%, mlx-turbo 22%.
On unseen lyrics at a comparable-or-lower rate, the same models score
42-51%. **~20-25 WER points of v1's fast-tier "survival" was training-set
familiarity, not transcription.** (Upper bound: the delta also includes
Suno-vs-studio domain shift — voice, mix, AI pronunciation quirks. Needs
more verses and a human-recorded control to decompose.)

Consequences:
- v1's golden standard (9.0 syl/s live) was set on memorized material.
  On unseen lyrics, nothing survives even 8.4 mean. The honest current
  answer to "can anything live-transcribe a chopper it hasn't heard
  before?" is NO at any rate we've tested above baseline.
- Model ranking survives (mlx-turbo still best, wav2vec2 still worst) —
  contamination inflated everyone roughly together — but absolute
  numbers from famous tracks should not be quoted as transcription
  ability.
- Next: formalize suno-01 (~5-6 syl/s) as the low-rung core segment to
  find where unseen-lyrics survival actually begins; more verses/takes
  to fill the ladder.

## 2026-07-07 — streaming simulation: batch RTF wildly overstates liveability

Built scripts/stream_sim.py: audio arrives in real time, sliding-window
re-decode every hop, words/segments commit once GUARD behind the live
edge, decodes run serially so overruns become caption lag. Three configs
on suno02:

| config | latency mean/max | worst lag | live WER |
|---|---|---|---|
| mlx-turbo, word-ts, full fallback, hop 0.5s | 1.38s / 8.67s | **55s** | 57% |
| mlx-turbo, temp=0, segment commits, hop 2s | 0.49s / 0.63s | **0.63s** | 58% |
| parakeet, hop 0.5s | 0.21s / 0.28s | 0.28s | (254%*) |

- **Batch RTF 0.05 predicted 20× headroom; the naive streaming config
  fell 55 SECONDS behind on a 31s clip.** Two causes: whisper pads every
  window to 30s (62 overlapping decodes pay the full-window tax), and
  temperature-fallback storms recur per window on hard audio (max 8.7s
  for one 8s-window decode). Batch RTF is a throughput number; streaming
  needs worst-case per-window latency.
- Sustainable config exists: temp=0 + segment commits + 2s hop → zero
  overruns, ~2.6s end-to-end caption delay (guard 1.5 + decode 0.6),
  at 58% WER. Live rap captions are FEASIBLE; correct ones are not.
- Streaming degrades accuracy as predicted: 42% batch → 57-58% live
  (lost right-context + boundary flicker).
- *parakeet: fastest by far (max 0.28s/window) but our window-stitch
  dedup produced 254% WER from duplicate commits — token timestamps
  drift across overlapping windows. Needs its native streaming API
  (transducers keep decode state), not window hacks. Marked future work.
- Artifact: synthetic/suno02-livecaption.mp4 — the sustained config's
  captions burned over the audio, i.e. exactly what a livestream would
  have shown.
