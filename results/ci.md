# rap-bench confidence intervals

Cluster bootstrap over lyric lines, 2000 replicates, seed 0, rates: listed; 95% percentile intervals. Written by `scripts/bootstrap_ci.py`; see its docstring for the design.

## Critical rate

`bracket` is the pair of tested rates the crossing is interpolated between: the bootstrap interval assumes a straight line inside it, so the bracket is the honest bound on curve shape. `censored` is the share of replicates where the curve never crossed 25% or failed at the slowest point; those replicates sit at an end point and narrow the interval.

| model | population | critical rate | 95% CI | bracket | censored |
|---|---|---|---|---|---|
| faster-whisper-distil-large-v3__raw | exhibition | 8.0 | 7.1–9.6 | 5.5–9.0 | 0% |
| faster-whisper-distil-large-v3__raw | core | 5.6 | 4.9–6.1 | 4.9–8.4 | 5% |
| faster-whisper-distil-large-v3__raw | **delta** (exhibition − core) | +2.5 | +1.4 to +4.2 | | |
| faster-whisper-large-v3__raw | exhibition | 9.2 | 7.8–10.6 | 9.0–9.6 | 8% |
| faster-whisper-large-v3__raw | core | 6.2 | 5.7–6.9 | 4.9–8.4 | 0% |
| faster-whisper-large-v3__raw | **delta** (exhibition − core) | +3.0 | +1.5 to +4.6 | | |
| faster-whisper-large-v3__vocals | exhibition | 9.7 | 7.4–10.6 | 9.6–10.0 | 4% |
| faster-whisper-small__raw | exhibition | 7.5 | 6.5–9.2 | 5.5–9.0 | 0% |
| faster-whisper-small__raw | core | 4.9 | 4.9–5.7 | 4.9–8.4 | 47% |
| faster-whisper-small__raw | **delta** (exhibition − core) | +2.6 | +1.3 to +4.2 | | |
| faster-whisper-tiny__raw | exhibition | <5.5 | 5.5–5.5 | censored | 100% |
| faster-whisper-tiny__raw | core | <4.9 | 4.9–4.9 | censored | 100% |
| faster-whisper-tiny__vocals | exhibition | <5.5 | 5.5–5.5 | censored | 100% |
| faster-whisper-turbo__raw | exhibition | 9.0 | 8.5–9.1 | 9.0–9.6 | 0% |
| faster-whisper-turbo__raw | core | 6.1 | 5.1–7.4 | 4.9–8.4 | 2% |
| faster-whisper-turbo__raw | **delta** (exhibition − core) | +2.9 | +1.6 to +3.9 | | |
| hf-UsefulSensors-moonshine-base__raw | exhibition | <5.5 | 5.5–5.9 | censored | 78% |
| hf-UsefulSensors-moonshine-base__raw | core | <4.9 | 4.9–4.9 | censored | 99% |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | exhibition | <5.5 | 5.5–5.5 | censored | 100% |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | core | <4.9 | 4.9–4.9 | censored | 100% |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | exhibition | 9.1 | 8.2–9.6 | 9.0–9.6 | 0% |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | core | 6.2 | 5.2–7.4 | 4.9–8.4 | 1% |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | **delta** (exhibition − core) | +2.9 | +1.4 to +4.0 | | |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | exhibition | 7.6 | 6.8–9.1 | 5.5–9.0 | 0% |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | core | 6.0 | 5.5–6.4 | 4.9–8.4 | 0% |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | **delta** (exhibition − core) | +1.6 | +0.7 to +3.2 | | |

## WER per segment

| model | segment | WER | 95% CI | lines | words |
|---|---|---|---|---|---|
| faster-whisper-distil-large-v3__raw | lose-yourself-v1 | 10% | 4%–16% | 16 | 143 |
| faster-whisper-distil-large-v3__raw | the-way-i-am-v1 | 14% | 6%–23% | 15 | 138 |
| faster-whisper-distil-large-v3__raw | speedom-em | 30% | 21%–39% | 22 | 220 |
| faster-whisper-distil-large-v3__raw | worldwide-choppers-twista | 50% | 40%–60% | 19 | 183 |
| faster-whisper-distil-large-v3__raw | rap-god-fast | 31% | 17%–43% | 11 | 108 |
| faster-whisper-distil-large-v3__raw | godzilla-v3 | 58% | 46%–70% | 24 | 227 |
| faster-whisper-distil-large-v3__raw | suno02 | 60% | 48%–72% | 16 | 118 |
| faster-whisper-distil-large-v3__raw | suno01 | 17% | 8%–26% | 14 | 102 |
| faster-whisper-large-v3__raw | lose-yourself-v1 | 6% | 2%–11% | 16 | 143 |
| faster-whisper-large-v3__raw | the-way-i-am-v1 | 9% | 3%–15% | 15 | 138 |
| faster-whisper-large-v3__raw | speedom-em | 23% | 14%–34% | 22 | 220 |
| faster-whisper-large-v3__raw | worldwide-choppers-twista | 22% | 15%–30% | 19 | 183 |
| faster-whisper-large-v3__raw | rap-god-fast | 28% | 13%–43% | 11 | 108 |
| faster-whisper-large-v3__raw | godzilla-v3 | 26% | 18%–34% | 24 | 227 |
| faster-whisper-large-v3__raw | suno02 | 51% | 38%–63% | 16 | 118 |
| faster-whisper-large-v3__raw | suno01 | 10% | 4%–17% | 14 | 102 |
| faster-whisper-large-v3__vocals | lose-yourself-v1 | 10% | 5%–16% | 16 | 143 |
| faster-whisper-large-v3__vocals | the-way-i-am-v1 | 21% | 10%–34% | 15 | 138 |
| faster-whisper-large-v3__vocals | speedom-em | 22% | 13%–31% | 22 | 220 |
| faster-whisper-large-v3__vocals | worldwide-choppers-twista | 33% | 21%–47% | 19 | 183 |
| faster-whisper-large-v3__vocals | rap-god-fast | 22% | 13%–32% | 11 | 104 |
| faster-whisper-large-v3__vocals | godzilla-v3 | 25% | 16%–34% | 24 | 227 |
| faster-whisper-small__raw | lose-yourself-v1 | 11% | 6%–17% | 16 | 143 |
| faster-whisper-small__raw | the-way-i-am-v1 | 18% | 10%–27% | 15 | 138 |
| faster-whisper-small__raw | speedom-em | 33% | 22%–44% | 22 | 220 |
| faster-whisper-small__raw | worldwide-choppers-twista | 61% | 51%–72% | 19 | 183 |
| faster-whisper-small__raw | rap-god-fast | 32% | 22%–43% | 11 | 108 |
| faster-whisper-small__raw | godzilla-v3 | 38% | 25%–54% | 24 | 227 |
| faster-whisper-small__raw | suno02 | 64% | 52%–75% | 16 | 118 |
| faster-whisper-small__raw | suno01 | 25% | 14%–36% | 14 | 102 |
| faster-whisper-tiny__raw | lose-yourself-v1 | 21% | 13%–30% | 16 | 143 |
| faster-whisper-tiny__raw | the-way-i-am-v1 | 57% | 42%–72% | 15 | 138 |
| faster-whisper-tiny__raw | speedom-em | 44% | 36%–51% | 22 | 220 |
| faster-whisper-tiny__raw | worldwide-choppers-twista | 78% | 63%–92% | 19 | 183 |
| faster-whisper-tiny__raw | rap-god-fast | 100% | 100%–100% | 11 | 104 |
| faster-whisper-tiny__raw | godzilla-v3 | 98% | 95%–100% | 24 | 227 |
| faster-whisper-tiny__raw | suno02 | 66% | 50%–80% | 16 | 118 |
| faster-whisper-tiny__raw | suno01 | 47% | 33%–61% | 14 | 102 |
| faster-whisper-tiny__vocals | lose-yourself-v1 | 24% | 15%–36% | 16 | 143 |
| faster-whisper-tiny__vocals | the-way-i-am-v1 | 57% | 43%–71% | 15 | 138 |
| faster-whisper-tiny__vocals | speedom-em | 44% | 36%–52% | 22 | 220 |
| faster-whisper-tiny__vocals | worldwide-choppers-twista | 74% | 61%–87% | 18 | 176 |
| faster-whisper-tiny__vocals | rap-god-fast | 64% | 39%–90% | 11 | 108 |
| faster-whisper-tiny__vocals | godzilla-v3 | 59% | 49%–69% | 24 | 227 |
| faster-whisper-turbo__raw | lose-yourself-v1 | 6% | 2%–9% | 16 | 143 |
| faster-whisper-turbo__raw | the-way-i-am-v1 | 10% | 5%–16% | 15 | 138 |
| faster-whisper-turbo__raw | speedom-em | 21% | 15%–28% | 22 | 220 |
| faster-whisper-turbo__raw | worldwide-choppers-twista | 33% | 24%–43% | 19 | 183 |
| faster-whisper-turbo__raw | rap-god-fast | 88% | 69%–100% | 11 | 108 |
| faster-whisper-turbo__raw | godzilla-v3 | 34% | 27%–42% | 24 | 227 |
| faster-whisper-turbo__raw | suno02 | 44% | 29%–60% | 16 | 118 |
| faster-whisper-turbo__raw | suno01 | 15% | 7%–24% | 14 | 102 |
| hf-UsefulSensors-moonshine-base__raw | lose-yourself-v1 | 30% | 13%–49% | 16 | 143 |
| hf-UsefulSensors-moonshine-base__raw | the-way-i-am-v1 | 29% | 18%–42% | 15 | 138 |
| hf-UsefulSensors-moonshine-base__raw | speedom-em | 75% | 59%–90% | 22 | 220 |
| hf-UsefulSensors-moonshine-base__raw | worldwide-choppers-twista | 68% | 55%–80% | 18 | 176 |
| hf-UsefulSensors-moonshine-base__raw | rap-god-fast | 28% | 14%–42% | 11 | 104 |
| hf-UsefulSensors-moonshine-base__raw | godzilla-v3 | 72% | 60%–83% | 24 | 227 |
| hf-UsefulSensors-moonshine-base__raw | suno02 | 64% | 47%–79% | 16 | 118 |
| hf-UsefulSensors-moonshine-base__raw | suno01 | 42% | 28%–57% | 14 | 100 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | lose-yourself-v1 | 59% | 42%–78% | 16 | 143 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | the-way-i-am-v1 | 91% | 85%–95% | 15 | 138 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | speedom-em | 78% | 69%–86% | 22 | 220 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | worldwide-choppers-twista | 86% | 77%–93% | 18 | 176 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | rap-god-fast | 81% | 70%–92% | 11 | 108 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | godzilla-v3 | 88% | 79%–95% | 24 | 227 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | suno02 | 91% | 77%–102% | 16 | 118 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | suno01 | 95% | 86%–101% | 14 | 102 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | lose-yourself-v1 | 7% | 3%–11% | 16 | 143 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | the-way-i-am-v1 | 8% | 4%–13% | 15 | 138 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | speedom-em | 22% | 14%–30% | 22 | 220 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | worldwide-choppers-twista | 34% | 23%–47% | 19 | 183 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | rap-god-fast | 39% | 23%–54% | 11 | 108 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | godzilla-v3 | 51% | 37%–65% | 24 | 227 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | suno02 | 42% | 29%–55% | 16 | 118 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | suno01 | 15% | 7%–24% | 14 | 102 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | lose-yourself-v1 | 11% | 5%–18% | 16 | 143 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | the-way-i-am-v1 | 16% | 9%–24% | 15 | 138 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | speedom-em | 33% | 25%–41% | 22 | 220 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | worldwide-choppers-twista | 52% | 35%–77% | 18 | 176 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | rap-god-fast | 26% | 13%–40% | 11 | 104 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | godzilla-v3 | 40% | 30%–51% | 24 | 227 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | suno02 | 55% | 45%–65% | 16 | 118 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | suno01 | 12% | 6%–18% | 14 | 100 |
