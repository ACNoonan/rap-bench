# rap-bench results

Cells are `WER · RTF` (batch); survival threshold 25%; 💀 = over threshold, 🐢 = accurate but slower than real time.

**Critical rate** (primary metric): interpolated syl/sec where the WER-vs-rate curve crosses the threshold, on an isotonic envelope; `>x` = survived everything tested, `<x` = failed the slowest point. **Live** variant treats RTF ≥ 1 as total failure. Populations are scored separately — exhibition tracks are training-contaminated, core is synthetic/unseen (see DESIGN.md).

## exhibition

| model | lose-yourself-v1 | the-way-i-am-v1 | speedom-em | rap-god-fast | worldwide-choppers-twista | godzilla-v3 | critical rate | live critical rate |
|---|---|---|---|---|---|---|---|---|
| faster-whisper-distil-large-v3__raw | 10% · 0.16× | 14% · 0.15× | 30% · 0.19× 💀 | 31% · 0.21× 💀 | 50% · 0.20× 💀 | 58% · 0.32× 💀 | 8.0 | 8.0 |
| faster-whisper-large-v3__raw | 6% · 0.73× | 9% · 0.63× | 23% · 0.98× | 28% · 3.09× 💀 | 22% · 1.39× 🐢 | 26% · 1.53× 💀 | 9.2 | 9.0 |
| faster-whisper-large-v3__vocals | 10% · 0.77× | 21% · 0.69× | 22% · 1.29× 🐢 | 22% · 1.09× 🐢 | 33% · 1.62× 💀 | 25% · 1.78× 🐢 | 9.7 | 5.9 |
| faster-whisper-small__raw | 11% · 0.14× | 18% · 0.14× | 33% · 0.21× 💀 | 32% · 0.28× 💀 | 61% · 0.98× 💀 | 38% · 0.42× 💀 | 7.5 | 7.5 |
| faster-whisper-tiny__raw | 21% · 0.03× | 57% · 0.18× 💀 | 44% · 0.04× 💀 | 100% · 0.27× 💀 | 78% · 0.05× 💀 | 98% · 0.20× 💀 | <5.5 | <5.5 |
| faster-whisper-tiny__vocals | 24% · 0.03× | 57% · 0.20× 💀 | 44% · 0.04× 💀 | 64% · 0.06× 💀 | 74% · 0.25× 💀 | 59% · 0.06× 💀 | <5.5 | <5.5 |
| faster-whisper-turbo__raw | 6% · 0.21× | 10% · 0.18× | 21% · 0.24× | 88% · 0.14× 💀 | 33% · 0.58× 💀 | 34% · 0.40× 💀 | 9.0 | 9.0 |
| hf-UsefulSensors-moonshine-base__raw | 30% · 0.25× 💀 | 29% · 0.10× 💀 | 75% · 0.09× 💀 | 28% · 0.12× 💀 | 68% · 0.10× 💀 | 72% · 0.10× 💀 | <5.5 | <5.5 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | 59% · 0.06× 💀 | 91% · 0.04× 💀 | 78% · 0.03× 💀 | 81% · 0.03× 💀 | 86% · 0.04× 💀 | 88% · 0.03× 💀 | <5.5 | <5.5 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | 7% · 0.04× | 8% · 0.04× | 22% · 0.05× | 39% · 0.05× 💀 | 34% · 0.14× 💀 | 51% · 0.05× 💀 | 9.1 | 9.1 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | 11% · 0.06× | 16% · 0.02× | 33% · 0.02× 💀 | 26% · 0.03× 💀 | 52% · 0.02× 💀 | 40% · 0.03× 💀 | 7.6 | 7.6 |

Segments easy → hard: lose-yourself-v1 (5.5 syl/s), the-way-i-am-v1 (5.5 syl/s), speedom-em (9.0 syl/s), rap-god-fast (9.6 syl/s), worldwide-choppers-twista (10.0 syl/s), godzilla-v3 (10.6 syl/s)

## core

| model | suno02 | critical rate | live critical rate |
|---|---|---|---|
| faster-whisper-distil-large-v3__raw | 60% · 0.24× 💀 | <8.4 | <8.4 |
| faster-whisper-large-v3__raw | 51% · 1.39× 💀 | <8.4 | <8.4 |
| faster-whisper-small__raw | 64% · 0.24× 💀 | <8.4 | <8.4 |
| faster-whisper-tiny__raw | 66% · 0.20× 💀 | <8.4 | <8.4 |
| faster-whisper-turbo__raw | 44% · 0.29× 💀 | <8.4 | <8.4 |
| hf-UsefulSensors-moonshine-base__raw | 64% · 0.16× 💀 | <8.4 | <8.4 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | 91% · 0.03× 💀 | <8.4 | <8.4 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | 42% · 0.05× 💀 | <8.4 | <8.4 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | 55% · 0.03× 💀 | <8.4 | <8.4 |

Segments easy → hard: suno02 (8.4 syl/s)
