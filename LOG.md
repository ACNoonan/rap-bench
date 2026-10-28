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

## 2026-07-07 — parakeet native streaming wired up: fast enough, not accurate enough

Fixed the earlier 254% "WER" — two bugs in OUR harness, not the model:
parakeet emits SUBWORD tokens (' C','al','ib') which we were joining with
spaces (turning "Calibrated" into four words), and tokens near the live
edge get revised as right-context arrives, defeating timestamp-based
dedup. Fix: index-based commits of the stable region (older than guard),
text joined without injected spaces, words regrouped on leading-space
boundaries.

Native-stream results on suno02 (transcribe_stream, context 256/256):
- hop 0.5s: unsustainable — per-add_audio cost is ~0.45s FIXED regardless
  of chunk size (graph-eval overhead, not audio-proportional) → 27/62
  overruns, 5.5s worst lag.
- **hop 1.0s: sustained.** Zero overruns, 0.78s worst lag, ~2.3s
  end-to-end caption delay. Live WER 71%.
- depth 2 vs 8 vs 24: identical WER (71%) and latency — the streaming
  accuracy penalty is the local attention itself, not cache exactness.

**Live-crown standings on unseen-chopper audio (suno02, 8.4 syl/s):**
| pipeline | sustained? | delay | live WER |
|---|---|---|---|
| mlx-whisper turbo, temp0, 2s hop | yes | ~2.6s | **58%** |
| parakeet-native, 1s hop | yes | ~2.3s | 71% |
| mlx-whisper naive word-ts | no (55s behind) | — | 57% |

Whisper keeps the live crown; parakeet streams more cheaply but hears
worse. Both are far above the 25% survival line: live captioning of
unseen fast rap remains open. Lesson for the harness: streaming
evaluation needs its own commit protocol per architecture — subword vs
word units and tail-revision behavior are model-specific.

## 2026-07-07 — realtime on KNOWN samples: first live survival, and streaming flattens memorization

Ran both sustained live configs over the exhibition tier (batch WER →
live WER):

| segment (syl/s) | whisper-fast live | parakeet-native live |
|---|---|---|
| lose-yourself (5.5) | 7% → 34% | 11% → **22% ✓ SURVIVES** |
| speedom (9.0) | 22% → 43% | 33% → 80%* |
| rap-god (9.6) | 39% → 42% | 26% → 62% |
| godzilla (10.6) | 51% → 59% | 40% → 63% |
| suno02 unseen (8.4) | 42% → 58% | 55% → 71% |

- **First live survival on record: parakeet-native live-captions Lose
  Yourself at 22% WER, zero overruns, ~2.3s delay.** The live golden
  standard is finally claimed — at baseline tier, on famous material.
- **Reversal at baseline: parakeet beats whisper live** (22% vs 34%)
  despite losing everywhere in batch. Whisper's chunked-window hack
  bleeds accuracy on easy audio (6s windows starve its LM context;
  temp=0 removes its recovery mechanism), while parakeet's native
  streaming was designed for this. Architecture-for-streaming matters
  more than raw batch accuracy on the easy end.
- **Streaming compresses the memorization advantage but doesn't erase
  it**: whisper famous-vs-unseen delta at ~9 syl/s is ~15 pts live
  (43 vs 58) vs ~20 pts batch. Even 6-second windows carry enough
  context to surf memorized lyrics.
- **Streaming hurts most where batch was best** (whisper: +27 pts on
  Lose Yourself, +3 on Rap God) — when batch is already failing there's
  little left to lose. The live-vs-batch gap is largest exactly on the
  material vendors demo.
- *parakeet speedom 80% came with 306 commits vs ~220 ref words — some
  may be commit-protocol insertions on the dense mix rather than pure
  mishearing; commit-protocol noise is itself a streaming-eval finding.

## 2026-07-07 — critical rate finally implemented (it was design-only)

DESIGN.md defined the v2 metrics; the scoring code still did flat binary
survival. Now implemented: `critical_rate()` — interpolated syl/sec where
WER crosses the threshold, on an isotonic envelope (running-max WER, so a
lucky low WER above an earlier failure doesn't restore credit), segments
at equal rates averaged, live variant treats RTF ≥ 1 as total failure.
Populations scored separately (exhibition vs core; deprecated-stretch
excluded); manifest entries now carry a `population:` field.

Effects vs the old max-clean-rate metric:
- large-v3 raw: was "10.0" (Choppers happened to survive), now 9.2 — the
  envelope holds its Rap God failure (28% at 9.6) against it. The old
  metric rewarded exactly the n=1 luck the redesign was about.
- Exhibition leaderboard: large-v3-vocals 9.7 > large-v3 9.2 > mlx-turbo
  9.1 > turbo 9.0 >> parakeet 7.6 >> tiny/moonshine/wav2vec2 <5.5.
- Core: every model "<8.4" — the core population has one rate point
  (suno02), so critical rates are unresolved-below. The metric surfaces
  the data gap directly: we need core segments at lower rates
  (formalize suno-01 at ~5, suno-03 pending transcription) to see where
  unseen-lyrics survival begins.

Still design-only from DESIGN.md: RTF as median of ≥3 timing runs;
bootstrap CIs; memorization delta as a computed stat (needs matched-rate
exhibition/core pairs — currently hand-read).

## 2026-07-07 — core curve resolves: unseen ceiling ~6 syl/s; whisper memorized ~2x more than parakeet

suno01 (4.9 syl/s, same Suno voice/production as suno02) formalized as
the core low rung. With two rate points the core critical rates resolve:

| model | core crit. rate | exhibition crit. rate | delta (memorization + domain) |
|---|---|---|---|
| mlx-turbo | 6.2 | 9.1 | 2.9 |
| large-v3 | 6.2 | 9.2 | 3.0 |
| turbo | 6.1 | 9.0 | 2.9 |
| parakeet | 6.0 | 7.6 | **1.6** |
| distil | 5.6 | 8.0 | 2.4 |
| small | 4.9 | 7.5 | 2.6 |

- **Unseen fast rap: every surviving model's critical rate sits at
  ~5-6 syl/s** — barely above conversational speech. The insane tier
  (9.6-10.6) is 4+ syl/s beyond anything's real ability.
- **suno01 exonerates the domain-shift alternative**: at 4.9 syl/s the
  same synthetic voice/production scores 10-17% for the strong models —
  unseen synthetic vocals are NOT inherently hard. Within identical
  domain, 4.9 → 8.4 syl/s takes large-v3 from 10% to 51%. It's the
  rate.
- **The exhibition−core critical-rate delta differs by training data:
  ~2.9-3.0 syl/s for whisper-family vs 1.6 for parakeet.** Whisper's
  web-scraped corpus memorized roughly twice as much famous-rap
  advantage as parakeet's clean-speech corpus. The delta metric works.
- Caveats: two-point curves make the interpolated crossings coarse
  (long linear span 4.9→8.4); suno01 ground truth is ASR-consensus,
  human read-along pending; cross-population delta still bundles any
  residual domain gap — matched human-recorded material would isolate
  it fully.

## 2026-07-07 — membership-inference probe: the memorization is NOT in the naked decoder

Appendix experiment (Adam's proposal): probe whisper's decoder prior
directly, no dataset access needed. Three escalating probes on turbo:

1. **Free-run completion** (silence/noise + initial_prompt = verse
   opening): NULL. The decoder never continues lyrics without acoustic
   evidence — it emits filler ("the the the...", "you") for famous and
   synthetic prompts alike.
2. **Forced-scoring prompt-swap lift** (teacher-force the true
   continuation over silence, matched vs mismatched prompt): NULL.
   Famous lift +0.161 nats/token ≈ control lift +0.124 — the small
   matched-prompt advantage is topical coherence, present equally for
   the unseen verse.
3. **Absolute likelihood gap**: famous continuations −5.0 nats/token vs
   synthetic −6.8 (4-9× per token) — looks like memorization, BUT the
   GPT-2 typicality control shows a LARGER gap (+2.00 vs whisper's
   +1.76) on the same texts. Fully explained by text typicality; no
   whisper-specific excess.

**Conclusion: whisper's lyric memorization does not manifest as a
free-standing text prior probeable over silence. It only shows up with
audio in the loop** — the prior biases perception (pulling acoustically
ambiguous frames toward memorized word sequences) rather than acting as
a standalone LM. The behavioral evidence (matched-domain WER deltas,
famous vs synthetic) remains the strongest — and now the only —
demonstration. A probe-resistant memorization is itself a finding.

Caveats/future: GPT-2 is itself lyric-contaminated (WebText), so the
typicality control is conservative but impure — no clean reference LM
exists for famous lyrics. A stronger elicitation: use the matched
instrumental (demucs accompaniment stem) instead of silence, giving the
decoder rhythmic anchoring without vocal evidence. Untested.

Dataset-lineage context (per model, for the appendix): whisper's data
is unpublished (behavioral evidence is the ONLY option); parakeet's
Granary mix is partially public incl. the YouTube-derived leak paths
(consistent with its smaller 1.6 syl/s delta); wav2vec2 is verifiably
Eminem-free (LibriSpeech/Libri-Light) making its universal failure a
pure-acoustics control; distil-whisper's published distillation data
doesn't clean its lineage (teacher knowledge passes through).

## 2026-07-07 — methodology audit of the membership-inference probes

Literature check + self-audit before standing behind the appendix.

**Literature says we did the right things, and anticipated our result:**
- MIA on Large Audio Language Models (arXiv 2603.28378): membership
  signals collapse to ~chance when audio-text pairing is disrupted via
  silence/noise/resynthesis — "memorization is instance-specific and
  cross-modal." Independently corroborates our conclusion that whisper's
  lyric memorization needs audio in the loop. Also validates hygiene: on
  contaminated eval sets, blind acoustic features alone hit 99.8 AUC —
  naive famous-vs-unseen MIA is a domain classifier.
- Duan et al. 2024 (Do MIAs Work on LLMs?): LLM MIAs ≈ random once
  member/non-member distribution shift is controlled — our GPT-2
  reference calibration (à la Carlini et al. 2021) was the correct
  instinct.
- Careless Whisper (Koenecke et al. 2024): silence/pauses trigger
  generic hallucinations, matching our free-run filler exactly.

**Self-audit found one real flaw — and fixing it changed a number:**
The probe-3 comparison of whisper vs GPT-2 gaps used nats/TOKEN across
two different tokenizers; rare words (our synthetic verse is full of
them) tokenize differently per vocab, making per-token averages
incomparable across models. Recomputed per WORD (same 40 words all
conditions): whisper gap +3.89 nats/word vs GPT-2 +3.33 — an excess of
+0.56 nats/word, REVERSING the "fully explained by typicality" claim.
However: per-verse excesses overlap between famous (-0.41..-1.21) and
control (-1.14..-1.57) ranges, n=4 vs 2, rough Welch t≈2.0 → not
significant; and cross-capability reference calibration is itself a
known weak point. Corrected verdict for probe 3: "no reliable
weights-level signal either way; weakly suggestive excess" — NOT
"explained away."

**What survives unchanged:** probes 1-2 (free-run, prompt-swap lift) are
within-model, single-tokenizer designs — their nulls stand. The overall
appendix conclusion softens from "the memorization is not in the naked
decoder" to "we cannot demonstrate it in the naked decoder" — which the
audio-MIA literature independently supports as the expected locus
(cross-modal binding). Behavioral matched-domain WER deltas remain the
demonstration.

## 2026-10-28 — rate units audit: the memorization delta was mostly a peak-vs-mean mismatch

Coming back to the blog post, three weaknesses: the unseen curve has two
points, the unseen verse's rare vocabulary is an untested alternative
explanation, and no WER had an interval. Added `scripts/bootstrap_ci.py`
(cluster bootstrap over lyric lines; results/ci.md) and found a fourth,
larger problem while checking the rate axis.

**The two populations were on different rate scales.** segments.yaml says
exhibition `syl_per_sec` is "approximate peak"; the core rates came from
syllables / duration (a mean). Recomputed every segment's mean rate as
count_syllables(verified lyrics) / clip duration, the same heuristic synth.py
uses:

| segment | listed | mean |
|---|---|---|
| lose-yourself-v1 | 5.5 | 4.31 |
| the-way-i-am-v1 | 5.5 | 4.22 |
| speedom-em | 9.0 | 6.74 |
| worldwide-choppers-twista | 10.0 | 7.60 |
| rap-god-fast | 9.6 | 8.72 |
| godzilla-v3 | 10.6 | 10.30 |
| suno01 (core) | 4.9 | 4.82 |
| suno02 (core) | 8.4 | 8.24 (peak 10.6) |

WER is scored over the whole clip, so the mean is the matching unit.
Exhibition − core critical-rate delta, mean rates on both sides
(`bootstrap_ci.py --rate mean`, results/ci-mean.md, 2000 reps):

| model | delta as published | delta, mean vs mean | 95% CI |
|---|---|---|---|
| whisper large-v3 | +3.0 | +2.0 | −0.4 to +4.3 |
| whisper turbo | +2.9 | +1.0 | −0.4 to +2.1 |
| mlx large-v3-turbo | +2.9 | +0.8 | −0.6 to +2.0 |
| distil-large-v3 | +2.4 | +0.5 | −0.7 to +1.8 |
| whisper small | +2.6 | +0.6 | −0.9 to +2.0 |
| parakeet tdt 0.6b v2 | +1.6 | −0.2 | −1.4 to +0.9 |

Every interval includes zero. The ordering (whisper above parakeet)
survives; "+3 syl/s of memorization" and "whisper memorized twice as much"
do not. Even on listed rates the large-v3 vs parakeet deltas overlap
(+1.5 to +4.6 vs +0.7 to +3.2, results/ci.md). The qualitative evidence
(near-verbatim Godzilla, moonshine's "mom's spaghetti") is untouched, but
the quantitative claim now rests on n = 2 core points and needs the fresh
tier below. The bootstrap intervals cover word-sampling noise only; the
core crossing is a straight line across 4.82–8.24 and could sit anywhere
in that bracket.

Next: DESIGN.md v3 (fresh tier: real tracks released after every roster
model). `scripts/scout.py` screens candidates by release date (MusicBrainz)
and peak rate from LRCLIB sync stamps → results/scout.md.

## 2026-10-28 — fresh tier built: 21 post-cutoff segments, transcribed, waiting on verification

`scripts/scout.py` screened 30 artists (scripts/scout_artists.txt) for tracks
first released ≥ 2025-06-01. Release-group dates alone let old songs through
on reissues (STANS soundtrack 2025 carries "Rap God" and "Stan"; Music To Be
Murdered By [Epilogue] 2026 carries the 2020 Side B tracks as *new recording
entities*), so a track is dropped if any MusicBrainz recording with the same
artist and title is older: 33 dropped, 81 kept (results/scout.md). "Lock It
Up" (Eminem, 2020) survived the filter under a variant title; not picked.

`scripts/select_fresh.py` took 21 picks (12 artists, ≤ 3 each), chose each
one's densest 25–40 s window from LRCLIB stamps, and kept a YouTube upload
only if its duration matched LRCLIB's within 3 s. Draft mean rates 4.48–10.56
syl/s; bins 4–5: 1, 5–6: 6, 6–7: 8, 7–8: 2, 8–9: 4, 9–10: 0, 10+: 1.
`draft_lyrics.py` now tries LRCLIB's exact-match `get` before `search`, so the
draft comes from the entry the window was chosen on, and retries 429/503.

All nine raw configurations transcribed all 21 (outputs/, gitignored).
faster-whisper 1.2.1 crashes on av 19 (`metadata_errors` kwarg); pinned
`av<16` in the whisper extra. The fresh runs used faster-whisper 1.2.1 /
av 15.1, and I don't know what versions the July runs used, so RTF and
decoding may not be perfectly comparable across the two dates. Fresh scores are
deliberately not computed: every fresh lyric file carries TODO-VERIFY and
the scorer skips it, so Adam can bet before seeing numbers. Checklist at the
end of DESIGN.md.

## 2026-10-28 — vocabulary covariate: rarity ran the other way

`bootstrap_ci.py --adjust vocab` (results/ci-mean-vocab.md). Each reference
word goes in a wordfreq Zipf bin (common ≥ 5, mid 3–5, rare < 3), and each
segment's WER is standardized to the pooled bin mix: Σ_b p_b · (errors_b /
words_b). Corpus frequency instead of the DESIGN.md plan's decoder log-prob,
because whisper's decoder has memorized the famous verses and would score
their words as expected.

The v2 worry was that famous verses carry rarer words ("monological"). They
carry fewer. Rare-word share is 6.5% in exhibition (1008 words) and 15.1% in
core (218 words, the two Suno verses); mean Zipf 5.66 vs 4.86. So rarity
made core harder, and adjusting for it shrinks the exhibition − core delta
(mean rates, 2000 reps, seed 0):

| model | delta, mean rates | adjusted for vocabulary | 95% CI, adjusted |
|---|---|---|---|
| whisper large-v3 | +2.0 | +1.6 | −0.8 to +4.1 |
| whisper turbo | +1.0 | +0.6 | −1.1 to +1.7 |
| mlx whisper turbo | +0.8 | +0.2 | −1.3 to +1.5 |
| distil-large-v3 | +0.5 | −0.2 | −1.5 to +1.2 |
| whisper small | +0.6 | −0.2 | −1.3 to +1.9 |
| parakeet | −0.2 | −1.0 | −2.2 to +0.2 |

Worked check, large-v3 on suno02: 21/52 common, 27/49 mid, 12/17 rare wrong;
0.655·0.404 + 0.264·0.551 + 0.081·0.706 = 0.467 against raw 0.508.

Only large-v3 keeps a positive point estimate worth talking about, and its
interval still spans zero. The core side is two Suno verses, so its
vocabulary share rests on 218 words and the pooled weights move once the
fresh tier is verified (they're recomputed from every scored reference).
Zipf scores slang unevenly ("tryna" 2.8, "finna" 2.3), so some "rare" words
are common in rap and uncommon in wordfreq's corpus; I did not check how
many. After verification, run `bootstrap_ci.py --rate mean --adjust vocab`
alongside the plain run; the exhibition − fresh delta is the one that
matters.
