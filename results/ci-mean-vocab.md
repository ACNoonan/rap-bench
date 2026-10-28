# rap-bench confidence intervals

Cluster bootstrap over lyric lines, 2000 replicates, seed 0, rates: mean; vocabulary adjustment: vocab; 95% percentile intervals. Written by `scripts/bootstrap_ci.py`; see its docstring for the design.

## Vocabulary of the scored references

Share of reference words per wordfreq Zipf bin (common >= 5, mid 3-5, rare < 3). Critical rates and intervals below use the standardized WER; the per-segment 95% CI is on the adjusted WER.

| population | words | mean Zipf | common | mid | rare |
|---|---|---|---|---|---|
| exhibition | 1008 | 5.66 | 70.1% | 23.3% | 6.5% |
| core | 218 | 4.86 | 44.0% | 40.8% | 15.1% |
| **pooled weights p_b** | 1226 | | 65.5% | 26.4% | 8.1% |

## Critical rate

`bracket` is the pair of tested rates the crossing is interpolated between: the bootstrap interval assumes a straight line inside it, so the bracket is the honest bound on curve shape. `censored` is the share of replicates where the curve never crossed 25% or failed at the slowest point; those replicates sit at an end point and narrow the interval.

| model | population | critical rate | 95% CI | bracket | censored |
|---|---|---|---|---|---|
| faster-whisper-distil-large-v3__raw | exhibition | 5.6 | 4.4–6.8 | 4.31–6.74 | 2% |
| faster-whisper-distil-large-v3__raw | core | 5.8 | 5.0–6.5 | 4.82–8.24 | 1% |
| faster-whisper-distil-large-v3__raw | **delta** (exhibition − core) | -0.2 | -1.5 to +1.2 | | |
| faster-whisper-large-v3__raw | exhibition | 7.9 | 5.7–10.3 | 7.6–8.72 | 6% |
| faster-whisper-large-v3__raw | core | 6.3 | 5.7–7.1 | 4.82–8.24 | 0% |
| faster-whisper-large-v3__raw | **delta** (exhibition − core) | +1.6 | -0.8 to +4.1 | | |
| faster-whisper-large-v3__vocals | exhibition | <4.2 | 4.2–9.0 | censored | 59% |
| faster-whisper-small__raw | exhibition | 4.8 | 4.2–6.8 | 4.31–6.74 | 37% |
| faster-whisper-small__raw | core | 5.0 | 4.8–5.7 | 4.82–8.24 | 38% |
| faster-whisper-small__raw | **delta** (exhibition − core) | -0.2 | -1.3 to +1.9 | | |
| faster-whisper-tiny__raw | exhibition | <4.2 | 4.2–4.2 | censored | 100% |
| faster-whisper-tiny__raw | core | <4.8 | 4.8–4.8 | censored | 100% |
| faster-whisper-tiny__vocals | exhibition | <4.2 | 4.2–4.2 | censored | 100% |
| faster-whisper-turbo__raw | exhibition | 7.0 | 6.3–7.6 | 6.74–7.6 | 0% |
| faster-whisper-turbo__raw | core | 6.4 | 5.4–8.0 | 4.82–8.24 | 2% |
| faster-whisper-turbo__raw | **delta** (exhibition − core) | +0.6 | -1.1 to +1.7 | | |
| hf-UsefulSensors-moonshine-base__raw | exhibition | <4.2 | 4.2–4.4 | censored | 90% |
| hf-UsefulSensors-moonshine-base__raw | core | <4.8 | 4.8–4.8 | censored | 98% |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | exhibition | <4.2 | 4.2–4.2 | censored | 100% |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | core | <4.8 | 4.8–4.8 | censored | 100% |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | exhibition | 7.0 | 6.1–7.7 | 6.74–7.6 | 0% |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | core | 6.7 | 5.7–8.2 | 4.82–8.24 | 4% |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | **delta** (exhibition − core) | +0.2 | -1.3 to +1.5 | | |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | exhibition | 5.1 | 4.2–6.1 | 4.31–6.74 | 14% |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | core | 6.1 | 5.5–6.7 | 4.82–8.24 | 0% |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | **delta** (exhibition − core) | -1.0 | -2.2 to +0.2 | | |

## WER per segment

| model | segment | WER | adjusted WER | 95% CI | lines | words |
|---|---|---|---|---|---|---|
| faster-whisper-distil-large-v3__raw | lose-yourself-v1 | 10% | 15% | 6%–21% | 16 | 143 |
| faster-whisper-distil-large-v3__raw | the-way-i-am-v1 | 14% | 18% | 12%–25% | 15 | 138 |
| faster-whisper-distil-large-v3__raw | speedom-em | 30% | 31% | 23%–40% | 22 | 220 |
| faster-whisper-distil-large-v3__raw | worldwide-choppers-twista | 50% | 48% | 39%–58% | 19 | 183 |
| faster-whisper-distil-large-v3__raw | rap-god-fast | 31% | 32% | 19%–45% | 11 | 108 |
| faster-whisper-distil-large-v3__raw | godzilla-v3 | 58% | 58% | 47%–71% | 24 | 227 |
| faster-whisper-distil-large-v3__raw | suno02 | 60% | 51% | 39%–62% | 16 | 118 |
| faster-whisper-distil-large-v3__raw | suno01 | 17% | 15% | 7%–24% | 14 | 102 |
| faster-whisper-large-v3__raw | lose-yourself-v1 | 6% | 8% | 2%–13% | 16 | 143 |
| faster-whisper-large-v3__raw | the-way-i-am-v1 | 9% | 12% | 7%–17% | 15 | 138 |
| faster-whisper-large-v3__raw | speedom-em | 23% | 23% | 14%–34% | 22 | 220 |
| faster-whisper-large-v3__raw | worldwide-choppers-twista | 22% | 21% | 16%–29% | 19 | 183 |
| faster-whisper-large-v3__raw | rap-god-fast | 28% | 30% | 15%–44% | 11 | 108 |
| faster-whisper-large-v3__raw | godzilla-v3 | 26% | 27% | 19%–35% | 24 | 227 |
| faster-whisper-large-v3__raw | suno02 | 51% | 47% | 34%–58% | 16 | 118 |
| faster-whisper-large-v3__raw | suno01 | 10% | 9% | 3%–17% | 14 | 102 |
| faster-whisper-large-v3__vocals | lose-yourself-v1 | 10% | 14% | 7%–21% | 16 | 143 |
| faster-whisper-large-v3__vocals | the-way-i-am-v1 | 21% | 27% | 14%–40% | 15 | 138 |
| faster-whisper-large-v3__vocals | speedom-em | 22% | 22% | 14%–31% | 22 | 220 |
| faster-whisper-large-v3__vocals | worldwide-choppers-twista | 33% | 32% | 20%–46% | 19 | 183 |
| faster-whisper-large-v3__vocals | rap-god-fast | 22% | 24% | 14%–33% | 11 | 104 |
| faster-whisper-large-v3__vocals | godzilla-v3 | 25% | 25% | 17%–34% | 24 | 227 |
| faster-whisper-small__raw | lose-yourself-v1 | 11% | 15% | 6%–21% | 16 | 143 |
| faster-whisper-small__raw | the-way-i-am-v1 | 18% | 23% | 13%–33% | 15 | 138 |
| faster-whisper-small__raw | speedom-em | 33% | 33% | 22%–44% | 22 | 220 |
| faster-whisper-small__raw | worldwide-choppers-twista | 61% | 60% | 49%–72% | 19 | 183 |
| faster-whisper-small__raw | rap-god-fast | 32% | 34% | 23%–44% | 11 | 108 |
| faster-whisper-small__raw | godzilla-v3 | 38% | 39% | 26%–54% | 24 | 227 |
| faster-whisper-small__raw | suno02 | 64% | 60% | 51%–69% | 16 | 118 |
| faster-whisper-small__raw | suno01 | 25% | 23% | 13%–37% | 14 | 102 |
| faster-whisper-tiny__raw | lose-yourself-v1 | 21% | 24% | 15%–34% | 16 | 143 |
| faster-whisper-tiny__raw | the-way-i-am-v1 | 57% | 60% | 48%–74% | 15 | 138 |
| faster-whisper-tiny__raw | speedom-em | 44% | 44% | 36%–51% | 22 | 220 |
| faster-whisper-tiny__raw | worldwide-choppers-twista | 78% | 78% | 62%–92% | 19 | 183 |
| faster-whisper-tiny__raw | rap-god-fast | 100% | 100% | 100%–100% | 11 | 104 |
| faster-whisper-tiny__raw | godzilla-v3 | 98% | 98% | 95%–100% | 24 | 227 |
| faster-whisper-tiny__raw | suno02 | 66% | 63% | 46%–77% | 16 | 118 |
| faster-whisper-tiny__raw | suno01 | 47% | 42% | 30%–54% | 14 | 102 |
| faster-whisper-tiny__vocals | lose-yourself-v1 | 24% | 27% | 17%–39% | 16 | 143 |
| faster-whisper-tiny__vocals | the-way-i-am-v1 | 57% | 61% | 46%–74% | 15 | 138 |
| faster-whisper-tiny__vocals | speedom-em | 44% | 45% | 38%–54% | 22 | 220 |
| faster-whisper-tiny__vocals | worldwide-choppers-twista | 74% | 73% | 61%–87% | 18 | 176 |
| faster-whisper-tiny__vocals | rap-god-fast | 64% | 64% | 42%–90% | 11 | 108 |
| faster-whisper-tiny__vocals | godzilla-v3 | 59% | 60% | 51%–69% | 24 | 227 |
| faster-whisper-turbo__raw | lose-yourself-v1 | 6% | 11% | 3%–14% | 16 | 143 |
| faster-whisper-turbo__raw | the-way-i-am-v1 | 10% | 13% | 9%–19% | 15 | 138 |
| faster-whisper-turbo__raw | speedom-em | 21% | 22% | 17%–27% | 22 | 220 |
| faster-whisper-turbo__raw | worldwide-choppers-twista | 33% | 32% | 24%–43% | 19 | 183 |
| faster-whisper-turbo__raw | rap-god-fast | 88% | 88% | 70%–100% | 11 | 108 |
| faster-whisper-turbo__raw | godzilla-v3 | 34% | 35% | 27%–42% | 24 | 227 |
| faster-whisper-turbo__raw | suno02 | 44% | 38% | 26%–52% | 16 | 118 |
| faster-whisper-turbo__raw | suno01 | 15% | 13% | 7%–22% | 14 | 102 |
| hf-UsefulSensors-moonshine-base__raw | lose-yourself-v1 | 30% | 30% | 13%–48% | 16 | 143 |
| hf-UsefulSensors-moonshine-base__raw | the-way-i-am-v1 | 29% | 32% | 21%–45% | 15 | 138 |
| hf-UsefulSensors-moonshine-base__raw | speedom-em | 75% | 76% | 60%–90% | 22 | 220 |
| hf-UsefulSensors-moonshine-base__raw | worldwide-choppers-twista | 68% | 67% | 55%–78% | 18 | 176 |
| hf-UsefulSensors-moonshine-base__raw | rap-god-fast | 28% | 30% | 17%–43% | 11 | 104 |
| hf-UsefulSensors-moonshine-base__raw | godzilla-v3 | 72% | 73% | 61%–83% | 24 | 227 |
| hf-UsefulSensors-moonshine-base__raw | suno02 | 64% | 63% | 45%–77% | 16 | 118 |
| hf-UsefulSensors-moonshine-base__raw | suno01 | 42% | 39% | 26%–54% | 14 | 100 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | lose-yourself-v1 | 59% | 62% | 45%–79% | 16 | 143 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | the-way-i-am-v1 | 91% | 92% | 87%–96% | 15 | 138 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | speedom-em | 78% | 78% | 70%–86% | 22 | 220 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | worldwide-choppers-twista | 86% | 85% | 77%–93% | 18 | 176 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | rap-god-fast | 81% | 83% | 72%–92% | 11 | 108 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | godzilla-v3 | 88% | 88% | 79%–95% | 24 | 227 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | suno02 | 91% | 91% | 77%–105% | 16 | 118 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | suno01 | 95% | 94% | 84%–102% | 14 | 102 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | lose-yourself-v1 | 7% | 11% | 3%–14% | 16 | 143 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | the-way-i-am-v1 | 8% | 12% | 8%–16% | 15 | 138 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | speedom-em | 22% | 22% | 15%–30% | 22 | 220 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | worldwide-choppers-twista | 34% | 34% | 23%–46% | 19 | 183 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | rap-god-fast | 39% | 40% | 25%–54% | 11 | 108 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | godzilla-v3 | 51% | 52% | 37%–65% | 24 | 227 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | suno02 | 42% | 35% | 24%–47% | 16 | 118 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | suno01 | 15% | 12% | 6%–20% | 14 | 102 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | lose-yourself-v1 | 11% | 17% | 7%–22% | 16 | 143 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | the-way-i-am-v1 | 16% | 21% | 13%–29% | 15 | 138 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | speedom-em | 33% | 33% | 27%–41% | 22 | 220 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | worldwide-choppers-twista | 52% | 51% | 34%–77% | 18 | 176 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | rap-god-fast | 26% | 28% | 14%–41% | 11 | 104 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | godzilla-v3 | 40% | 41% | 31%–51% | 24 | 227 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | suno02 | 55% | 48% | 38%–57% | 16 | 118 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | suno01 | 12% | 11% | 5%–19% | 14 | 100 |
