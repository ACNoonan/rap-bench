# Can Whisper transcribe "Rap God"?

Someone posted that their local dictation setup hits 527.9 tokens per second
at 2.5% word error rate. This is a genuinely impressive number, and my first
thought on reading it was: transcribing *what*? Nobody dictates at 527
tokens per second. The fastest speech a human being has ever produced under
studio conditions is a rapper, and the word error rates on *that* are not
in anyone's marketing material.

So I built the benchmark. Seven segments of commercially released fast rap,
tiered by syllable rate: "Lose Yourself" at a comfortable 5.5 syllables per
second, up through Busta Rhymes and Tech N9ne, to the supersonic bit of
"Rap God" (9.6) and the third verse of "Godzilla" (10.6, the Guinness
record). Hand-verified lyrics, a WER normalizer that treats ad-libs as
optional, and one headline stat I'll call the **live rate**: the fastest
verse a model transcribes at under 25% WER *while generating tokens faster
than the rapper emits them*. I called the project MMLU — Marshall Mathers
Lyrical Understanding — and expected to get an afternoon of entertainment
out of it.

I got that. I also got a memorization scandal, a failed experiment I'm
fonder of than most successful ones, and a video of a language model
confidently captioning nonsense at ten syllables per second.

## Round one

I ran eleven configurations across seven open-source model families —
whisper in five sizes, Apple-GPU whisper via MLX, NVIDIA's Parakeet,
moonshine, wav2vec2 — on raw tracks and on demucs-separated vocal stems.

Nothing survived the top tier. The live rate maxed out at 9.0 syllables per
second, a three-way tie between whisper large-v3 and two turbo variants.
More interesting than the scores was *how* models die, because they don't
die the same way:

- whisper-tiny returned a **literally empty file** for "Rap God." Whisper
  has internal checks that suppress output when it decides audio isn't
  speech; the fastest verified rapping alive apparently isn't speech. Note
  this failure mode is silent — in a product, your captions just stop.
- wav2vec2, which has no language model to lean on, decayed into honest
  garbage: `THE OTON NOW IT OPO O OO NATATSOE`. You can *see* it failing,
  which I'll defend as a feature.
- moonshine failed fluent: grammatical, confident, wrong ("Time's up, over
  plow"). Undetectable without ground truth, which makes it the worst
  failure of the three, and it looks the best.

Also worth knowing: whisper large-v3's real-time factor went from 0.63 on
mid-tempo verses to **3.09 on "Rap God."** Hard audio makes it *slower* —
more tokens per second of audio, plus a fallback mechanism that re-decodes
failing windows at up to five escalating temperatures. Dense syllables are
a compute multiplier. Keep this in mind whenever someone quotes you a
tokens-per-second figure measured on podcast audio.

## It works too well

Here's the thing that stopped me. large-v3's transcript of Godzilla verse 3
— 10.6 syllables per second, through a full mix — was nearly word-perfect:

> "...every bit of me is the epitome of a spitter when I'm in the vicinity...
> I'm unfadable, you wanna battle, I'm available, I'm blowin' up like an
> inflatable..."

I don't believe any acoustic system can do that, and it doesn't have to.
These lyrics are all over the training data — lyric sites, karaoke videos,
YouTube captions. The decoder isn't hearing "I'm undebatable, I'm
unavoidable." It's *remembering* it, with the audio as a retrieval cue.

The tell came from moonshine, the weakest model in the roster. It butchered
"Lose Yourself" — except for one line, which it transcribed verbatim:
*mom's spaghetti*. The single most memed lyric in hip-hop was the one thing
it "heard" perfectly.

## You might reasonably object

*Maybe rap over a beat is just hard, and famous verses are where the models
happen to do well for boring acoustic reasons.* Fair. To answer that you
need fast rap the models have never heard, with ground truth you trust —
and for real music those two requirements fight each other. If a song's
lyrics are indexed well enough for you to verify, they were indexed well
enough to be scraped. **For real recordings, verifiable ground truth and
training contamination are the same variable.** Obscurity shrinks the
problem; it can't zero it.

So: manufacture the audio. I wrote an original chopper verse — dense
multisyllabic internal rhyme in the Tech N9ne register, checked for n-gram
overlap against real lyrics so the LLM that helped write it couldn't
smuggle in memorized bars — and had Suno sing it.

(My first attempt was cleverer and it failed completely: render the verse
with TTS, then time-stretch it to each target syllable rate. Perfect
experimental control, and it measured nothing — whisper cruised at 5–8%
WER up to 11 syllables per second, a rate where real Eminem puts it at
39%. Pitch-preserving time-stretch gives you *slow speech played fast*.
Actual fast speech degrades articulation — vowels reduce, consonants blur
into each other — and that degradation, not the pace, is the difficulty.
I'd built a difficulty dial that didn't dial difficulty.)

Suno, on a speed-focused prompt, came back rapping my verse at a peak of
**10.6 syllables per second** — Godzilla pace — nearly verbatim. During
verification both ASR models "misheard" one word the same way, which
turned out to be because Suno mispronounced it: the models transcribed
what was sung more faithfully than my own reference did. Ground truth for
generated vocals is what was *sung*, not what was written.

## The reckoning

Full roster against the unseen verse, mean 8.4 syllables per second —
*slower* than a famous verse several models had already survived:

| model | unseen verse (8.4 syl/s) | famous "Speedom" (9.0 syl/s) |
|---|---|---|
| mlx large-v3-turbo | 42% | 22% |
| whisper turbo | 44% | 21% |
| whisper large-v3 | 51% | 23% |
| parakeet | 55% | 33% |

Everything died, by roughly twenty points of WER against material it
couldn't have memorized.

*Second reasonable objection: maybe AI-generated vocals are just weird for
ASR.* Also testable: a second segment from the same generation session —
same voice, same production, at an easy 4.9 syllables per second — scored
10–17% for the strong models. Unseen synthetic vocals are fine. Within an
identical domain, moving 4.9 → 8.4 syl/s takes large-v3 from 10% to 51%.
It's the rate.

With two rate points per model I could compute the statistic this whole
project had been circling: the syllable rate at which each model's WER
curve crosses 25%, on famous material versus unseen material. The
difference between those two numbers is the memorization, in physical
units:

| model | unseen | famous | memorization |
|---|---|---|---|
| whisper large-v3 | 6.2 | 9.2 | **3.0 syl/s** |
| whisper turbo | 6.1 | 9.0 | 2.9 |
| parakeet | 6.0 | 7.6 | **1.6** |

Two things fall out. **The honest ceiling for open-source ASR on fast rap
it hasn't heard before is about six syllables per second** — energetic
conversation pace, nowhere near a chopper. And the memorization splits by
training data exactly as it should: whisper, trained on web scrape soaked
in lyric captions, carries roughly *twice* the famous-track inflation of
Parakeet, which trained mostly on clean speech corpora. You can read the
training diet in the gap. (wav2vec2, whose LibriSpeech training set is
public and verifiably Eminem-free, fails everything everywhere — a clean
control: that's what zero recall actually looks like.)

## The livestream test

Back to the original tweet, because "tokens per second" has one more lie
in it. mlx-turbo transcribes these clips at 20× real time in batch, so
surely it can caption the rap live? I simulated it properly: audio
arriving in real time, sliding-window re-decode, words committed once old
enough that later windows won't revise them, and decode overruns become
caption lag, honestly accounted.

The naive configuration fell **55 seconds behind on a 31-second song.**
Whisper pads every window to 30 seconds — so overlapping re-decodes pay
the full-window cost dozens of times — and those temperature-fallback
storms recur per window on hard audio. One 8-second window took 8.7
seconds to decode. Batch throughput is simply not a liveness number;
worst-case window latency is, and nobody publishes it.

A sustainable configuration exists (fallback off, coarser commits, 2-second
hop): zero overruns, captions ~2.6 seconds behind the rapper, 58% WER. I
rendered the video. The captions keep perfect pace and read like a ransom
note — *"Metronomolish or abolish homological illogical"* — at ten
syllables per second, indefinitely.

The final twist came from wiring up Parakeet's native streaming API
(transducers carry decode state across chunks; no window hack). Parakeet
lost to whisper everywhere in batch — and **beat it live on the easy
tier**, 22% vs 34% on "Lose Yourself," becoming the only configuration in
the entire project that is simultaneously accurate and real-time on
anything. Architecture built for streaming beats batch accuracy, right up
until the acoustics get hard.

## Looking for the memorization in the weights

If whisper memorized the lyrics, can you see it without any audio? I tried
three probes on the decoder, ablating the audio to silence. Free-run
completion from a verse's opening words: it emits filler — "the the
the..." — never lyrics. Forced-scoring the true continuation under its
real preceding words versus a wrong prompt: the lift is tiny and nearly
identical for famous and unseen verses. Raw likelihoods: famous lyrics
score far higher than my synthetic verse — but a reference LM shows
almost the same gap, because Eminem's English is simply more typical than
a verse built around the word "monological." After fixing a normalization
bug (per-token comparisons across different tokenizers are invalid;
per-word is the comparable unit) whisper keeps a small excess preference
for famous lyrics, too noisy at this sample size to call.

So I can't find the memorization in the naked decoder, and it turns out
that's the expected answer: a recent [membership-inference study of audio
language models](https://arxiv.org/abs/2603.28378) found that membership
signals collapse to chance when you disrupt the audio-text pairing with
silence or noise — memorization in these models is *cross-modal binding*,
not a text prior. ([Naive membership inference on LLMs mostly measures
distribution shift anyway](https://arxiv.org/abs/2402.07841), which is
exactly the trap the reference-model control caught here.) The lyric
knowledge only activates with audio in the loop: a prior that biases
*perception*, pulling acoustically ambiguous frames toward remembered
word sequences. The behavioral test — matched-domain WER on verses that
have never existed before — wasn't the fallback method. It was the only
instrument that could see the effect.

## What this cost

One laptop, a weekend, a Suno account, and a verse about a syllable
centrifuge that no human has ever performed — which is exactly why it was
worth more to me than "Rap God."

Whether anything can transcribe "Rap God": no. Not the real question
anymore, though. The models that look like they can are reciting; the
honest ceiling on unseen fast rap is about six syllables per second; and
the one model that can caption *anything* accurately in real time is the
one that loses every batch benchmark. All the scripts, the methodology log
(including the dead ends), and the ransom-note video are in the repo:
[link].
