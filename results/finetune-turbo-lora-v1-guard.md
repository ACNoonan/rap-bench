# Fine-tune run turbo-lora-v1-guard

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
| hf-whisper-large-v3-turbo-guard-base__raw | 4.5% (73) | 24.1% (136) |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | 5.0% (73) | 22.4% (136) |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | 4.6% (73) | 23.9% (136) |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | 4.6% (73) | 24.8% (136) |

## Instrument check: base model vs faster-whisper turbo (July)

Same weights, different implementation and hardware. A large gap means the eval path is broken.

| segment | HF base (this run) | faster-whisper turbo | diff |
|---|---|---|---|
| lose-yourself-v1 | 5% | 6% | -1% |
| the-way-i-am-v1 | 10% | 10% | +0% |
| speedom-em | 23% | 21% | +2% |
| worldwide-choppers-twista | 43% | 35% | +8% |
| rap-god-fast | 33% | 89% | -57% |
| godzilla-v3 | 30% | 34% | -4% |
| suno02 | 47% | 44% | +3% |
| suno01 | 14% | 16% | -2% |

**median |diff| 2 points: PASS (threshold 5).**

## Coverage on clips over 30 s

Transcript words relative to the base model on the same clip. Under 0.7 suggests the adapter broke long-form seeking and the transcript stops early.

| checkpoint | clips | median ratio | min | flagged < 0.7 |
|---|---|---|---|---|
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | 11 | 0.99 | 0.92 | none |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | 11 | 0.99 | 0.96 | none |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | 11 | 0.98 | 0.95 | none |

## Loops

Clips where at least 30% of the 4-word windows repeat a 4-gram seen 4+ times. Counts per eval group; no reference used.

| checkpoint | exhibition (n=7) | core (n=2) | fresh (n=21) | clean (n=73) | val (n=136) |
|---|---|---|---|---|---|
| hf-whisper-large-v3-turbo-guard-base__raw | 0 | 0 | 0 | 0 | 2 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | 0 | 0 | 0 | 0 | 4 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | 0 | 0 | 0 | 0 | 4 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | 0 | 0 | 0 | 0 | 2 |

Scored clips that loop: none.

Benchmark scores: transcripts are copied to `outputs/`; run `score.py` and `bootstrap_ci.py --rate mean` (fresh segments score only once verified).

## Paired bootstrap, guarded e1-e3 against guarded base

Written by `scripts/paired_ci.py` (10,000 resamples, seed 0). Exhibition and core
resample reference lines, with each segment's ad-lib variant fixed at the one
best for the base. Val and clean resample clips. B − A is in WER points.

| group | units | guarded base | checkpoint | WER | B − A | 95% CI |
|---|---|---|---|---|---|---|
| exhibition | 107 | 24.2% | e1 | 25.5% | +1.3 | −1.1 to +3.6 |
| exhibition | 107 | 24.2% | e2 | 26.7% | +2.5 | −0.3 to +5.2 |
| exhibition | 107 | 24.2% | e3 | 26.2% | +2.0 | −1.4 to +5.4 |
| core | 30 | 30.9% | e1 | 32.7% | +1.8 | −4.0 to +7.5 |
| core | 30 | 30.9% | e2 | 35.5% | +4.5 | −2.1 to +12.5 |
| core | 30 | 30.9% | e3 | 34.5% | +3.6 | −3.1 to +11.6 |
| val | 136 | 24.1% | e1 | 22.4% | −1.7 | −4.5 to +0.5 |
| val | 136 | 24.1% | e2 | 23.9% | −0.2 | −3.2 to +2.6 |
| val | 136 | 24.1% | e3 | 24.8% | +0.7 | −1.3 to +3.4 |
| clean | 73 | 4.5% | e1 | 5.0% | +0.4 | −0.3 to +1.1 |
| clean | 73 | 4.5% | e2 | 4.6% | +0.1 | −0.6 to +0.7 |
| clean | 73 | 4.5% | e3 | 4.6% | +0.1 | −0.6 to +0.7 |
