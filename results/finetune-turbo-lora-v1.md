# Fine-tune run turbo-lora-v1

Written by `scripts/score_finetune.py`. Base `openai/whisper-large-v3-turbo`, rank 32, alpha 64, lr 0.0003, seed 7, 3283 train chunks (21.507 h), 136 val chunks. Versions {'torch': '2.13.0+rocm7.2', 'transformers': '5.14.1', 'peft': '0.19.1'}.

## Training

| epoch | steps | train loss | val loss | time |
|---|---|---|---|---|
| 1 | 205 | 1.0561 | 0.8157 | 62 min |
| 2 | 410 | 0.8781 | 0.8151 | 63 min |
| 3 | 615 | 0.7433 | 0.8266 | 63 min |

## WER by checkpoint

`clean` is LibriSpeech read speech (regression check); `val` is held-out training songs, labelled from unverified LRCLIB lyrics, so its floor is the label noise, not zero. Clip counts in parentheses.

| checkpoint | clean | val |
|---|---|---|
| hf-whisper-large-v3-turbo-base__raw | 4.5% (73) | 27.6% (136) |
| hf-whisper-large-v3-turbo-lora-e1__raw | 5.0% (73) | 33.0% (136) |
| hf-whisper-large-v3-turbo-lora-e2__raw | 4.6% (73) | 25.4% (136) |
| hf-whisper-large-v3-turbo-lora-e3__raw | 4.6% (73) | 25.4% (136) |

## Instrument check: base model vs faster-whisper turbo (July)

Same weights, different implementation and hardware. A large gap means the eval path is broken.

| segment | HF base (this run) | faster-whisper turbo | diff |
|---|---|---|---|
| lose-yourself-v1 | 5% | 6% | -1% |
| the-way-i-am-v1 | 10% | 10% | +0% |
| speedom-em | 23% | 21% | +2% |
| worldwide-choppers-twista | 89% | 35% | +55% |
| rap-god-fast | 33% | 89% | -57% |
| godzilla-v3 | 30% | 34% | -4% |
| suno02 | 47% | 44% | +3% |
| suno01 | 14% | 16% | -2% |

**median |diff| 2 points: PASS (threshold 5).**

## Coverage on clips over 30 s

Transcript words relative to the base model on the same clip. Under 0.7 suggests the adapter broke long-form seeking and the transcript stops early.

| checkpoint | clips | median ratio | min | flagged < 0.7 |
|---|---|---|---|---|
| hf-whisper-large-v3-turbo-lora-e1__raw | 11 | 1.00 | 0.19 | worldwide-choppers-twista 0.19 |
| hf-whisper-large-v3-turbo-lora-e2__raw | 11 | 0.99 | 0.23 | worldwide-choppers-twista 0.23 |
| hf-whisper-large-v3-turbo-lora-e3__raw | 11 | 1.00 | 0.95 | none |

## Loops

Clips where at least 30% of the 4-word windows repeat a 4-gram seen 4+ times. Counts per eval group; no reference used.

| checkpoint | exhibition (n=7) | core (n=2) | fresh (n=21) | clean (n=73) | val (n=136) |
|---|---|---|---|---|---|
| hf-whisper-large-v3-turbo-base__raw | 1 | 0 | 0 | 0 | 3 |
| hf-whisper-large-v3-turbo-lora-e1__raw | 0 | 0 | 1 | 0 | 8 |
| hf-whisper-large-v3-turbo-lora-e2__raw | 0 | 1 | 0 | 0 | 6 |
| hf-whisper-large-v3-turbo-lora-e3__raw | 1 | 1 | 1 | 0 | 5 |

Scored clips that loop: hf-whisper-large-v3-turbo-base__raw: worldwide-choppers-twista; hf-whisper-large-v3-turbo-lora-e2__raw: suno02; hf-whisper-large-v3-turbo-lora-e3__raw: godzilla-v3; hf-whisper-large-v3-turbo-lora-e3__raw: suno02.

Benchmark scores: transcripts are copied to `outputs/`; run `score.py` and `bootstrap_ci.py --rate mean` (fresh segments score only once verified).
