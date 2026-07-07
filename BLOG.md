# MMLU: Marshall Mathers Lyrical Understanding

*Or: I built a joke benchmark to see if Whisper could transcribe "Rap God,"
and it turned out the models had memorized the answers.*

## The tweet

Someone on X posted that they'd gotten local dictation running at **527.9
tokens/second** with ~2.5% word error rate on a MacBook. Impressive number.
But 2.5% WER on *what*? Dictation benchmarks are people speaking clearly, at
comfortable speed, into good microphones.

I wanted to know what happens at the other end of the difficulty axis. The
fastest verified rap verses run over **10 syllables per second** — Eminem's
third verse on "Godzilla" holds the Guinness record pace — layered over a
produced mix that actively fights the vocal. So I built a benchmark:
open-source ASR models versus fast rap, tiered from "Lose Yourself" (~5.5
syl/s) up through the supersonic section of "Rap God" (9.6) to "Godzilla"
verse 3 (10.6).

One evening of setup: seven segments with hand-verified lyrics, a
lyrics-aware WER normalizer (ad-libs in parens score as optional, censoring
normalized, following the [Jam-ALT](https://audioshake.github.io/jam-alt/)
benchmark's lead), and a golden-standard metric with a bit of showmanship to
it — **max live rate**: the fastest verse a model transcribes accurately
*while generating tokens faster than the rapper spits them* (real-time
factor < 1). Could your dictation model caption the song live?

## Round one: the wall at 9.6

Eleven configurations across seven model families (whisper large-v3 / turbo
/ small / tiny / distil, mlx-whisper on Apple GPU, NVIDIA Parakeet,
moonshine, wav2vec2). Highlights:

- **Nothing survived the insane tier.** The golden standard topped out at
  9.0 syl/s — a three-way tie between large-v3, turbo, and mlx large-v3-turbo
  on Tech N9ne's "Speedom" (Eminem's verse).
- **Models die in genre-specific ways.** whisper-tiny returned a literally
  empty file for "Rap God" — its anti-hallucination checks decided the
  fastest rapping alive "wasn't speech" and silently gave up. wav2vec2 (CTC,
  no language model) decayed into honest phoneme soup: `THE OTON NOW IT OPO
  O OO NATATSOE`. moonshine stayed perfectly fluent and confidently wrong —
  the most dangerous failure of the three, because you can't detect it
  without ground truth.
- **Difficulty multiplies latency.** large-v3's real-time factor went from
  0.63 on mid-tempo verses to **3.09** on "Rap God" — dense syllables mean
  more tokens per second of audio, and when whisper's quality checks fail it
  re-decodes at escalating temperatures, up to five retries. Hard audio
  costs 5× more compute. Throughput measured on easy audio tells you nothing
  about the adversarial regime — which is the polite version of my reply to
  that tweet.
- **Clean-speech leaderboards don't transfer.** Parakeet tops the Hugging
  Face Open ASR Leaderboard and was the fastest model I tested (RTF 0.02,
  flat, because transducers have no retry loop). It folded at the fast tier
  anyway. Leaderboards measure distribution match, not robustness.

Fun results. Then I looked closer at one transcript and the project changed.

## The tell

large-v3's transcript of Godzilla verse 3 — the Guinness-pace one — was
*nearly word-perfect*. At 10.6 syllables per second, through a full mix. I
don't believe any acoustic model can do that, and it turns out it doesn't
have to: those lyrics saturate the training data. Genius, lyric sites,
karaoke captions, YouTube transcripts. The decoder isn't hearing "I'm
undebatable, I'm unavoidable" — it's *remembering* it, with the audio as a
prompt.

The smoking gun came from moonshine, the weakest whisper-style model: it
butchered everything except exactly one line, which it transcribed
verbatim — *"mom's spaghetti."* The most memed lyric in hip-hop history was
the one line it "heard" perfectly.

So the benchmark wasn't measuring transcription. It was measuring
transcription *plus recall*, inseparably. And this isn't a rap problem: any
ASR eval built on famous audio — audiobooks, TED talks, podcasts — has the
same issue. For music there's a particularly nasty bind: **the ground truth
you can get is exactly the ground truth models trained on.** If lyrics are
indexed enough for you to verify, they were indexed enough to be scraped.
Obscurity only shrinks the contamination; it can't zero it, and it costs you
your reference lyrics in the bargain.

## The fix that failed first

The clean escape is audio that has never existed before. Attempt one: write
an original chopper-style verse (dense multisyllabic internal rhyme, in the
Tech N9ne register — checked for n-gram overlap against real lyrics so the
LLM didn't smuggle in memorized bars), render it with TTS, and time-stretch
it to each target syllable rate. Perfect ground truth by construction, a
continuous difficulty dial, no copyright, fully distributable. Beautiful
design.

It failed in the most instructive way possible. Whisper stayed flat at 5–8%
WER all the way to 11 syllables per second — a rate where it scores 39% on
real Eminem. **Pitch-preserving time-stretch produces slow speech played
fast, not fast speech.** When a human actually raps at 10 syl/s,
articulation degrades: vowels reduce, consonants blur, coarticulation smears
word boundaries. That *reduction* is what makes fast rap hard — and
time-stretch preserves the TTS render's careful slow-speech articulation
perfectly. I'd built a difficulty dial that turned the pace without turning
the difficulty.

## The fix that worked

Attempt two: feed the same original verse to a music-generation model
(Suno) with a chopper-style prompt. Take two came back at a **peak of 10.6
syllables per second** — Godzilla pace — singing my lyrics nearly verbatim
over a real produced mix. Contamination-free, hard-for-the-right-reasons,
and the ground-truth labor collapses to one read-along listen.

Two delightful things happened during verification. First, both ASR models
misheard "adamant and" the same way — because Suno actually mispronounced
it. The models were right; my written lyrics were wrong. Ground truth for
generated vocals has to be *what was sung, not what was written*. Second,
another Suno take drove whisper into emitting a wall of **Chinese
characters** while Parakeet returned an empty string — on audio a human can
follow. No training data to lean on, no memorized continuation to surf:
pure acoustic failure, of a kind the famous tracks never once produced.

## The reckoning

Full model roster against the unseen chopper at a *mean* of 8.4 syl/s —
slower than the "Speedom" verse several models had survived:

| model | unseen verse (8.4 syl/s) | famous "Speedom" (9.0 syl/s) |
|---|---|---|
| mlx large-v3-turbo | **42%** | 22% |
| whisper turbo | **44%** | 21% |
| whisper large-v3 | **51%** | 23% |
| parakeet | 55% | 33% |

Every model dead, by a huge margin, on material it couldn't have memorized.
Roughly **20 points of WER on the famous tracks was recall**, not hearing.

With a second synthetic segment at 4.9 syl/s (same generated voice, same
production — so the domain is held constant and only the rate moves), the
psychometric curves resolve, and with them a metric I'd designed but not
yet earned: **critical rate**, the interpolated syllable rate where a
model's WER crosses 25%. Two numbers per model — one on famous material,
one on unseen — and their difference is the memorization, denominated in
syllables per second:

| model | unseen critical rate | famous critical rate | memorization delta |
|---|---|---|---|
| whisper large-v3 | 6.2 | 9.2 | **3.0** |
| mlx large-v3-turbo | 6.2 | 9.1 | 2.9 |
| whisper turbo | 6.1 | 9.0 | 2.9 |
| parakeet | 6.0 | 7.6 | **1.6** |

Two findings in one table. **The real ceiling for open-source ASR on fast
rap it hasn't heard before is about 6 syllables per second** — barely above
energetic conversation, nowhere near a chopper. And the memorization delta
splits by training data exactly as you'd predict: whisper, trained on
web-scraped audio soaked in music and lyric captions, carries about **twice
the famous-track inflation of Parakeet**, which trained on clean speech.
The models' training diets are legible in the gap.

(Caveats, because they matter: one synthetic voice, two-point curves, and
the unseen-vs-famous comparison still bundles any residual domain gap
between Suno vocals and studio rap. The 4.9 syl/s segment scoring 10–17%
kills the strong version of the domain-shift objection — same voice, easy
rate, no problem — but a human-recorded original verse is the full
control, and it's on the list.)

## "But could it caption a livestream?"

One more turn of the screw. Batch RTF says mlx-turbo processes audio at 20×
real time — surely it could caption the rap live? I built the simulation:
audio arrives in real time, sliding-window re-decode, words commit once
they're old enough that later windows won't revise them, and decode
overruns become caption lag, honestly accounted.

The naive configuration fell **55 seconds behind on a 31-second song.**
Whisper pads every window to 30 seconds, so overlapping re-decodes pay the
full-window tax dozens of times, and those temperature-fallback storms
recur *per window* on hard audio — one 8-second window took 8.7 seconds to
decode. Batch RTF is a throughput number. Streaming lives and dies on
worst-case per-window latency, and no spec sheet quotes it.

A sustainable configuration exists (fallback disabled, segment-level
commits, 2-second hop): zero overruns, captions ~2.6s behind the rapper,
at 58% WER — the accuracy cost of going live is another ~15 points on top
of everything above. I rendered the video. The captions keep perfect pace
and read like a ransom note: *"Metronomolish or abolish homological
illogical,"* at ten syllables per second, forever.

And the final reversal: wired up properly (Parakeet has a native streaming
API — transducers carry decode state across chunks, no window hack), the
model that *lost* everywhere in batch **beat whisper live on the easy
tier** — 22% vs 34% on "Lose Yourself," the first and only configuration in
the whole project to be simultaneously accurate and real-time on anything.
Architecture built for streaming beats superior batch accuracy, right up
until the acoustics get hard.

## What I actually learned

1. **Tokens per second is the least interesting number in ASR.** Every
   model I tested had compute headroom to burn on hard audio; not one had
   the robustness. And the throughput number itself dissolves on contact
   with streaming, where worst-case window latency rules.
2. **Contamination isn't just an LLM problem.** ASR evals on famous audio
   measure recall plus hearing, inseparably — and for music, verifiable
   ground truth and training contamination are the same variable. Generated
   audio is the clean escape, and it's cheap now.
3. **You can measure what a model memorized, in physical units.** Famous
   critical rate minus unseen critical rate: ~3 syl/s for whisper, ~1.6 for
   Parakeet. The training data shows up in the gap.
4. **Stimulus design is where benchmarks quietly go wrong.** My time-stretch
   ladder was elegant, controlled, distributable — and measured nothing,
   because sped-up slow speech lacks the articulatory reduction that makes
   fast speech hard. The pilot that kills your clever mechanism is the
   pilot working.
5. **Metrics fail like models do.** My original pass/fail-at-25% metric
   awarded survivals decided by two words of edge noise, and credited a
   model for a lucky pass above a rate it had already failed. Interpolated
   crossings on an isotonic envelope fixed both. If your metric can be
   gamed by luck, n=1 will game it.

Total cost: one laptop, one evening plus a day, a Suno account, and a
verse about a syllable centrifuge that no rapper has ever performed — which
is precisely why it was worth more than "Rap God."

*Benchmark, methodology log, and all scripts: [repo link]. The livestream
caption video is in the repo too. I still can't stop watching it.*
