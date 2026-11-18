# rap-bench confidence intervals

Cluster bootstrap over lyric lines, 2000 replicates, seed 0, rates: mean; vocabulary adjustment: vocab; 95% percentile intervals. Written by `scripts/bootstrap_ci.py`; see its docstring for the design.

## Vocabulary of the scored references

Share of reference words per wordfreq Zipf bin (common >= 5, mid 3-5, rare < 3). Critical rates and intervals below use the standardized WER; the per-segment 95% CI is on the adjusted WER.

| population | words | mean Zipf | common | mid | rare |
|---|---|---|---|---|---|
| exhibition | 1008 | 5.66 | 70.1% | 23.3% | 6.5% |
| core | 218 | 4.86 | 44.0% | 40.8% | 15.1% |
| fresh | 2872 | 5.81 | 74.5% | 21.3% | 4.2% |
| **pooled weights p_b** | 4098 | | 71.8% | 22.8% | 5.4% |

## Pooled WER

Errors over reference words across a population's clips, raw (no vocabulary adjustment). Two-stage bootstrap: clips are drawn with replacement, then lines within each drawn clip. With 2 core clips and 6 or 7 exhibition clips the interval is wide because the clip draw dominates.

| model | population | pooled WER | 95% CI | clips | words |
|---|---|---|---|---|---|
| faster-whisper-distil-large-v3__raw | exhibition | 34.7% | 18.4%–48.8% | 6 | 1019 |
| faster-whisper-distil-large-v3__raw | core | 40.0% | 13.1%–66.4% | 2 | 220 |
| faster-whisper-distil-large-v3__raw | fresh | 29.1% | 22.1%–36.6% | 20 | 2874 |
| faster-whisper-large-v3__raw | exhibition | 19.7% | 11.6%–26.2% | 6 | 1019 |
| faster-whisper-large-v3__raw | core | 31.8% | 6.9%–56.9% | 2 | 220 |
| faster-whisper-large-v3__raw | fresh | 19.0% | 13.8%–24.7% | 20 | 2872 |
| faster-whisper-large-v3__vocals | exhibition | 22.8% | 16.1%–29.2% | 6 | 1015 |
| faster-whisper-small__raw | exhibition | 34.1% | 20.1%–47.0% | 6 | 1019 |
| faster-whisper-small__raw | core | 45.5% | 19.8%–69.5% | 2 | 220 |
| faster-whisper-small__raw | fresh | 30.5% | 21.8%–43.2% | 20 | 2874 |
| faster-whisper-tiny__raw | exhibition | 66.4% | 42.9%–89.5% | 6 | 1015 |
| faster-whisper-tiny__raw | core | 57.3% | 41.2%–72.8% | 2 | 220 |
| faster-whisper-tiny__raw | fresh | 53.2% | 44.6%–62.5% | 20 | 2879 |
| faster-whisper-tiny__vocals | exhibition | 53.7% | 40.1%–66.9% | 6 | 1012 |
| faster-whisper-turbo__raw | exhibition | 29.4% | 15.1%–48.7% | 6 | 1019 |
| faster-whisper-turbo__raw | core | 30.5% | 11.3%–51.5% | 2 | 220 |
| faster-whisper-turbo__raw | fresh | 25.8% | 17.1%–40.8% | 20 | 2883 |
| hf-UsefulSensors-moonshine-base__raw | exhibition | 55.7% | 36.3%–70.2% | 6 | 1008 |
| hf-UsefulSensors-moonshine-base__raw | core | 54.1% | 35.3%–72.6% | 2 | 218 |
| hf-UsefulSensors-moonshine-base__raw | fresh | 43.1% | 31.4%–57.5% | 20 | 2874 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | exhibition | 80.9% | 70.6%–88.3% | 6 | 1012 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | core | 92.7% | 83.9%–100.0% | 2 | 220 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh | 76.5% | 70.3%–82.4% | 20 | 2882 |
| hf-whisper-large-v3-turbo-base__raw | exhibition | 32.4% | 13.5%–55.9% | 6 | 1019 |
| hf-whisper-large-v3-turbo-base__raw | core | 30.9% | 8.5%–53.8% | 2 | 220 |
| hf-whisper-large-v3-turbo-base__raw | fresh | 21.1% | 15.7%–26.9% | 20 | 2872 |
| hf-whisper-large-v3-turbo-guard-base__raw | exhibition | 24.2% | 13.5%–33.5% | 6 | 1019 |
| hf-whisper-large-v3-turbo-guard-base__raw | core | 30.9% | 8.5%–53.8% | 2 | 220 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh | 21.1% | 15.7%–26.9% | 20 | 2872 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | exhibition | 25.5% | 14.5%–35.9% | 6 | 1019 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | core | 32.7% | 12.4%–53.0% | 2 | 220 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh | 21.3% | 16.4%–26.4% | 20 | 2872 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | exhibition | 26.7% | 16.3%–37.3% | 6 | 1019 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | core | 35.5% | 10.0%–60.4% | 2 | 220 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh | 21.9% | 16.7%–27.2% | 20 | 2872 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | exhibition | 26.2% | 16.5%–35.2% | 6 | 1019 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | core | 34.5% | 9.0%–60.1% | 2 | 220 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh | 22.8% | 17.5%–28.4% | 20 | 2872 |
| hf-whisper-large-v3-turbo-lora-e1__raw | exhibition | 32.0% | 14.6%–56.9% | 6 | 1012 |
| hf-whisper-large-v3-turbo-lora-e1__raw | core | 55.5% | 12.4%–133.1% | 2 | 220 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh | 32.0% | 16.5%–72.4% | 20 | 2873 |
| hf-whisper-large-v3-turbo-lora-e2__raw | exhibition | 32.9% | 16.6%–57.3% | 6 | 1012 |
| hf-whisper-large-v3-turbo-lora-e2__raw | core | 136.4% | 10.0%–434.7% | 2 | 220 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh | 21.9% | 16.7%–27.2% | 20 | 2872 |
| hf-whisper-large-v3-turbo-lora-e3__raw | exhibition | 40.3% | 16.5%–85.5% | 6 | 1019 |
| hf-whisper-large-v3-turbo-lora-e3__raw | core | 135.9% | 9.0%–433.9% | 2 | 220 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh | 26.9% | 17.7%–43.3% | 20 | 2872 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | exhibition | 28.4% | 13.8%–42.7% | 6 | 1019 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | core | 29.1% | 11.3%–48.0% | 2 | 220 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh | 22.5% | 17.4%–28.1% | 20 | 2873 |
| openrouter-assemblyai-universal-3-6-pro__raw | exhibition | 26.9% | 14.9%–36.8% | 6 | 1019 |
| openrouter-assemblyai-universal-3-6-pro__raw | core | 30.5% | 10.5%–50.0% | 2 | 220 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh | 21.3% | 15.0%–28.5% | 20 | 2873 |
| openrouter-deepgram-nova-3__raw | exhibition | 70.6% | 37.7%–94.4% | 6 | 1008 |
| openrouter-deepgram-nova-3__raw | core | 77.5% | 61.8%–90.4% | 2 | 218 |
| openrouter-deepgram-nova-3__raw | fresh | 72.0% | 55.8%–86.2% | 20 | 2872 |
| openrouter-elevenlabs-scribe-v2__raw | exhibition | 12.3% | 4.4%–19.8% | 6 | 1015 |
| openrouter-elevenlabs-scribe-v2__raw | core | 24.1% | 7.4%–42.7% | 2 | 220 |
| openrouter-elevenlabs-scribe-v2__raw | fresh | 17.0% | 11.6%–22.3% | 20 | 2876 |
| openrouter-google-chirp-3__raw | exhibition | 42.8% | 16.7%–70.4% | 6 | 1012 |
| openrouter-google-chirp-3__raw | core | 55.5% | 19.7%–89.1% | 2 | 220 |
| openrouter-google-chirp-3__raw | fresh | 39.2% | 24.9%–54.7% | 20 | 2872 |
| openrouter-google-gemini-3.5-transcribe__raw | exhibition | 56.6% | 21.2%–87.1% | 6 | 1008 |
| openrouter-google-gemini-3.5-transcribe__raw | core | 91.7% | 77.1%–100.0% | 2 | 218 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh | 53.9% | 34.5%–72.2% | 20 | 2872 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | exhibition | 30.7% | 17.1%–49.9% | 6 | 1008 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | core | 38.2% | 11.1%–64.6% | 2 | 220 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh | 24.4% | 15.1%–35.9% | 20 | 2872 |
| openrouter-openai-gpt-4o-transcribe__raw | exhibition | 25.2% | 10.4%–46.4% | 6 | 1015 |
| openrouter-openai-gpt-4o-transcribe__raw | core | 30.5% | 7.1%–53.3% | 2 | 220 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh | 37.1% | 23.1%–53.6% | 20 | 2873 |
| openrouter-openai-gpt-transcribe__raw | exhibition | 18.9% | 8.4%–28.7% | 6 | 1008 |
| openrouter-openai-gpt-transcribe__raw | core | 34.1% | 12.1%–55.9% | 2 | 220 |
| openrouter-openai-gpt-transcribe__raw | fresh | 22.7% | 16.4%–29.9% | 20 | 2872 |
| openrouter-x-ai-grok-stt-2.0__raw | exhibition | 30.7% | 17.6%–49.0% | 6 | 1008 |
| openrouter-x-ai-grok-stt-2.0__raw | core | 35.0% | 11.3%–57.1% | 2 | 220 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh | 23.3% | 16.8%–30.1% | 20 | 2872 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | exhibition | 31.7% | 18.9%–43.3% | 6 | 1008 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | core | 35.3% | 9.2%–60.4% | 2 | 218 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh | 27.5% | 19.9%–35.9% | 20 | 2872 |

## Paired difference in pooled WER against the best model

Populations with at least 10 clips. Clip-level paired bootstrap: each replicate draws the same clips for both models. Difference in WER points, model − best.

| population | model | pooled WER | best | pooled WER | difference | 95% CI | clips |
|---|---|---|---|---|---|---|---|
| fresh | faster-whisper-large-v3__raw | 19.0% | openrouter-elevenlabs-scribe-v2__raw | 17.0% | +2.0 | +0.4 to +4.1 | 20 |
| fresh | hf-whisper-large-v3-turbo-base__raw | 21.1% | openrouter-elevenlabs-scribe-v2__raw | 17.0% | +4.1 | +2.0 to +6.3 | 20 |
| fresh | hf-whisper-large-v3-turbo-guard-base__raw | 21.1% | openrouter-elevenlabs-scribe-v2__raw | 17.0% | +4.1 | +2.0 to +6.3 | 20 |
| fresh | hf-whisper-large-v3-turbo-guard-lora-e1__raw | 21.3% | openrouter-elevenlabs-scribe-v2__raw | 17.0% | +4.3 | +1.9 to +6.6 | 20 |
| fresh | openrouter-assemblyai-universal-3-6-pro__raw | 21.3% | openrouter-elevenlabs-scribe-v2__raw | 17.0% | +4.3 | +2.1 to +6.8 | 20 |
| fresh | hf-whisper-large-v3-turbo-guard-lora-e2__raw | 21.9% | openrouter-elevenlabs-scribe-v2__raw | 17.0% | +5.0 | +2.5 to +7.5 | 20 |
| fresh | hf-whisper-large-v3-turbo-lora-e2__raw | 21.9% | openrouter-elevenlabs-scribe-v2__raw | 17.0% | +5.0 | +2.5 to +7.5 | 20 |
| fresh | mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | 22.5% | openrouter-elevenlabs-scribe-v2__raw | 17.0% | +5.5 | +3.3 to +8.1 | 20 |
| fresh | openrouter-openai-gpt-transcribe__raw | 22.7% | openrouter-elevenlabs-scribe-v2__raw | 17.0% | +5.7 | +3.8 to +7.8 | 20 |
| fresh | hf-whisper-large-v3-turbo-guard-lora-e3__raw | 22.8% | openrouter-elevenlabs-scribe-v2__raw | 17.0% | +5.8 | +3.5 to +8.2 | 20 |
| fresh | openrouter-x-ai-grok-stt-2.0__raw | 23.3% | openrouter-elevenlabs-scribe-v2__raw | 17.0% | +6.4 | +4.2 to +8.5 | 20 |
| fresh | openrouter-mistralai-voxtral-small-transcribe-3-0__raw | 24.4% | openrouter-elevenlabs-scribe-v2__raw | 17.0% | +7.4 | +1.8 to +14.5 | 20 |
| fresh | faster-whisper-turbo__raw | 25.8% | openrouter-elevenlabs-scribe-v2__raw | 17.0% | +8.9 | +2.3 to +19.3 | 20 |
| fresh | hf-whisper-large-v3-turbo-lora-e3__raw | 26.9% | openrouter-elevenlabs-scribe-v2__raw | 17.0% | +9.9 | +4.0 to +18.9 | 20 |
| fresh | parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | 27.5% | openrouter-elevenlabs-scribe-v2__raw | 17.0% | +10.5 | +7.0 to +14.3 | 20 |
| fresh | faster-whisper-distil-large-v3__raw | 29.1% | openrouter-elevenlabs-scribe-v2__raw | 17.0% | +12.2 | +8.9 to +15.5 | 20 |
| fresh | faster-whisper-small__raw | 30.5% | openrouter-elevenlabs-scribe-v2__raw | 17.0% | +13.6 | +8.2 to +22.4 | 20 |
| fresh | hf-whisper-large-v3-turbo-lora-e1__raw | 32.0% | openrouter-elevenlabs-scribe-v2__raw | 17.0% | +15.0 | +2.5 to +37.7 | 20 |
| fresh | openrouter-openai-gpt-4o-transcribe__raw | 37.1% | openrouter-elevenlabs-scribe-v2__raw | 17.0% | +20.2 | +8.7 to +33.8 | 20 |
| fresh | openrouter-google-chirp-3__raw | 39.2% | openrouter-elevenlabs-scribe-v2__raw | 17.0% | +22.2 | +11.2 to +34.9 | 20 |
| fresh | hf-UsefulSensors-moonshine-base__raw | 43.1% | openrouter-elevenlabs-scribe-v2__raw | 17.0% | +26.1 | +18.8 to +34.7 | 20 |
| fresh | faster-whisper-tiny__raw | 53.2% | openrouter-elevenlabs-scribe-v2__raw | 17.0% | +36.2 | +31.6 to +40.5 | 20 |
| fresh | openrouter-google-gemini-3.5-transcribe__raw | 53.9% | openrouter-elevenlabs-scribe-v2__raw | 17.0% | +36.9 | +20.0 to +52.0 | 20 |
| fresh | openrouter-deepgram-nova-3__raw | 72.0% | openrouter-elevenlabs-scribe-v2__raw | 17.0% | +55.1 | +41.3 to +67.5 | 20 |
| fresh | hf-facebook-wav2vec2-large-960h-lv60-self__raw | 76.5% | openrouter-elevenlabs-scribe-v2__raw | 17.0% | +59.6 | +55.7 to +63.5 | 20 |

## Critical rate

`isotonic fit` is the crossing on the best non-decreasing curve through the points. `running max` is the metric as registered: it stops at the first failing point (LOG.md, 2026-11-18). The bracket and censored columns describe the running max.

`bracket` is the pair of tested rates the crossing is interpolated between: the bootstrap interval assumes a straight line inside it, so the bracket is the honest bound on curve shape. `censored` is the share of replicates where the curve never crossed 25% or failed at the slowest point; those replicates sit at an end point and narrow the interval.

| model | population | isotonic fit | 95% CI | running max | 95% CI | bracket | censored |
|---|---|---|---|---|---|---|---|
| faster-whisper-distil-large-v3__raw | exhibition | 6.1 | 5.4–7.0 | 6.1 | 5.1–6.9 | 4.31–6.74 | 0% |
| faster-whisper-distil-large-v3__raw | core | 5.9 | 5.1–6.7 | 5.9 | 5.1–6.7 | 4.82–8.24 | 1% |
| faster-whisper-distil-large-v3__raw | fresh | 6.9 | 5.9–7.0 | <4.4 | 4.4–6.2 | censored | 94% |
| faster-whisper-distil-large-v3__raw | **delta** (exhibition − core) | +0.2 | -0.8 to +1.5 | +0.1 | -1.1 to +1.4 | | |
| faster-whisper-distil-large-v3__raw | **delta** (exhibition − fresh) | -0.8 | -1.5 to +0.7 |  |  | | |
| faster-whisper-distil-large-v3__raw | **delta** (fresh − core) | +1.0 | -0.3 to +1.7 |  |  | | |
| faster-whisper-large-v3__raw | exhibition | 8.4 | 6.6–10.3 | 8.2 | 5.9–10.3 | 7.6–8.72 | 12% |
| faster-whisper-large-v3__raw | core | 6.4 | 5.8–7.2 | 6.4 | 5.8–7.2 | 4.82–8.24 | 0% |
| faster-whisper-large-v3__raw | fresh | 8.6 | 7.3–8.8 | <4.4 | 4.4–6.4 | censored | 81% |
| faster-whisper-large-v3__raw | **delta** (exhibition − core) | +2.1 | +0.1 to +4.3 | +1.8 | -0.7 to +4.2 | | |
| faster-whisper-large-v3__raw | **delta** (exhibition − fresh) | -0.1 | -1.9 to +2.9 |  |  | | |
| faster-whisper-large-v3__raw | **delta** (fresh − core) | +2.2 | +0.6 to +2.8 |  |  | | |
| faster-whisper-large-v3__vocals | exhibition | 7.5 | 6.1–10.3 | 6.9 | 4.2–10.3 | 6.74–7.6 | 44% |
| faster-whisper-small__raw | exhibition | 5.7 | 5.0–6.9 | 5.3 | 4.2–6.8 | 4.31–6.74 | 14% |
| faster-whisper-small__raw | core | 5.0 | 4.8–5.7 | 5.0 | 4.8–5.7 | 4.82–8.24 | 36% |
| faster-whisper-small__raw | fresh | 5.7 | 5.6–7.0 | <4.4 | 4.4–5.6 | censored | 79% |
| faster-whisper-small__raw | **delta** (exhibition − core) | +0.7 | -0.4 to +2.0 | +0.3 | -1.3 to +1.9 | | |
| faster-whisper-small__raw | **delta** (exhibition − fresh) | -0.0 | -1.3 to +1.2 |  |  | | |
| faster-whisper-small__raw | **delta** (fresh − core) | +0.7 | -0.0 to +2.0 |  |  | | |
| faster-whisper-tiny__raw | exhibition | <4.2 | 4.2–4.2 | <4.2 | 4.2–4.2 | censored | 100% |
| faster-whisper-tiny__raw | core | <4.8 | 4.8–4.8 | <4.8 | 4.8–4.8 | censored | 99% |
| faster-whisper-tiny__raw | fresh | <4.4 | 4.4–4.4 | <4.4 | 4.4–4.4 | censored | 100% |
| faster-whisper-tiny__vocals | exhibition | <4.2 | 4.2–4.2 | <4.2 | 4.2–4.2 | censored | 100% |
| faster-whisper-turbo__raw | exhibition | 7.2 | 6.8–7.7 | 7.2 | 6.8–7.6 | 6.74–7.6 | 0% |
| faster-whisper-turbo__raw | core | 6.6 | 5.5–8.2 | 6.6 | 5.5–8.2 | 4.82–8.24 | 4% |
| faster-whisper-turbo__raw | fresh | 4.9 | 4.4–8.6 | <4.4 | 4.4–4.8 | censored | 94% |
| faster-whisper-turbo__raw | **delta** (exhibition − core) | +0.6 | -1.1 to +1.8 | +0.6 | -1.1 to +1.8 | | |
| faster-whisper-turbo__raw | **delta** (exhibition − fresh) | +2.3 | -1.5 to +3.2 |  |  | | |
| faster-whisper-turbo__raw | **delta** (fresh − core) | -1.8 | -3.3 to +2.5 |  |  | | |
| hf-UsefulSensors-moonshine-base__raw | exhibition | <4.2 | 4.2–4.7 | <4.2 | 4.2–4.4 | censored | 83% |
| hf-UsefulSensors-moonshine-base__raw | core | <4.8 | 4.8–4.8 | <4.8 | 4.8–4.8 | censored | 97% |
| hf-UsefulSensors-moonshine-base__raw | fresh | <4.4 | 4.4–5.7 | <4.4 | 4.4–4.4 | censored | 99% |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | exhibition | <4.2 | 4.2–4.2 | <4.2 | 4.2–4.2 | censored | 100% |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | core | <4.8 | 4.8–4.8 | <4.8 | 4.8–4.8 | censored | 100% |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh | <4.4 | 4.4–4.4 | <4.4 | 4.4–4.4 | censored | 100% |
| hf-whisper-large-v3-turbo-base__raw | exhibition | 6.9 | 6.2–7.0 | 6.8 | 6.2–6.9 | 6.74–7.6 | 0% |
| hf-whisper-large-v3-turbo-base__raw | core | 6.7 | 6.1–7.8 | 6.7 | 6.1–7.8 | 4.82–8.24 | 1% |
| hf-whisper-large-v3-turbo-base__raw | fresh | 8.2 | 7.1–8.6 | <4.4 | 4.4–6.3 | censored | 94% |
| hf-whisper-large-v3-turbo-base__raw | **delta** (exhibition − core) | +0.1 | -1.0 to +0.8 | +0.1 | -1.1 to +0.7 | | |
| hf-whisper-large-v3-turbo-base__raw | **delta** (exhibition − fresh) | -1.4 | -2.0 to -0.3 |  |  | | |
| hf-whisper-large-v3-turbo-base__raw | **delta** (fresh − core) | +1.5 | -0.1 to +2.2 |  |  | | |
| hf-whisper-large-v3-turbo-guard-base__raw | exhibition | 7.0 | 6.3–7.6 | 7.0 | 6.2–7.4 | 6.74–7.6 | 0% |
| hf-whisper-large-v3-turbo-guard-base__raw | core | 6.7 | 6.1–7.8 | 6.7 | 6.1–7.8 | 4.82–8.24 | 1% |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh | 8.2 | 7.1–8.6 | <4.4 | 4.4–6.3 | censored | 94% |
| hf-whisper-large-v3-turbo-guard-base__raw | **delta** (exhibition − core) | +0.3 | -0.9 to +1.3 | +0.3 | -1.0 to +1.0 | | |
| hf-whisper-large-v3-turbo-guard-base__raw | **delta** (exhibition − fresh) | -1.2 | -1.9 to +0.3 |  |  | | |
| hf-whisper-large-v3-turbo-guard-base__raw | **delta** (fresh − core) | +1.5 | -0.1 to +2.2 |  |  | | |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | exhibition | 7.0 | 6.6–7.4 | 6.9 | 6.5–7.2 | 6.74–7.6 | 0% |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | core | 6.3 | 5.6–7.3 | 6.3 | 5.6–7.3 | 4.82–8.24 | 0% |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh | 7.4 | 6.9–8.8 | <4.4 | 4.4–6.0 | censored | 92% |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | **delta** (exhibition − core) | +0.7 | -0.3 to +1.6 | +0.6 | -0.4 to +1.3 | | |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | **delta** (exhibition − fresh) | -0.4 | -1.9 to +0.3 |  |  | | |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | **delta** (fresh − core) | +1.1 | +0.1 to +2.8 |  |  | | |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | exhibition | 7.0 | 6.4–7.3 | 6.9 | 6.2–7.2 | 6.74–7.6 | 0% |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | core | 6.3 | 5.6–7.0 | 6.3 | 5.6–7.0 | 4.82–8.24 | 0% |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh | 7.3 | 6.9–8.5 | <4.4 | 4.4–4.4 | censored | 98% |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | **delta** (exhibition − core) | +0.7 | -0.2 to +1.5 | +0.6 | -0.4 to +1.4 | | |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | **delta** (exhibition − fresh) | -0.3 | -1.6 to +0.3 |  |  | | |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | **delta** (fresh − core) | +1.0 | +0.1 to +2.5 |  |  | | |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | exhibition | 7.1 | 6.9–8.1 | 7.1 | 6.8–7.7 | 6.74–7.6 | 0% |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | core | 6.3 | 5.7–6.8 | 6.3 | 5.7–6.8 | 4.82–8.24 | 0% |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh | 7.3 | 6.9–8.5 | <4.4 | 4.4–4.4 | censored | 98% |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | **delta** (exhibition − core) | +0.8 | +0.2 to +2.0 | +0.8 | +0.1 to +1.6 | | |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | **delta** (exhibition − fresh) | -0.1 | -1.5 to +1.0 |  |  | | |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | **delta** (fresh − core) | +0.9 | +0.3 to +2.4 |  |  | | |
| hf-whisper-large-v3-turbo-lora-e1__raw | exhibition | 6.9 | 6.5–7.0 | 6.8 | 6.5–6.9 | 6.74–7.6 | 0% |
| hf-whisper-large-v3-turbo-lora-e1__raw | core | 5.8 | 5.2–7.2 | 5.8 | 5.2–7.2 | 4.82–8.24 | 0% |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh | 6.3 | 5.8–8.7 | <4.4 | 4.4–6.0 | censored | 92% |
| hf-whisper-large-v3-turbo-lora-e1__raw | **delta** (exhibition − core) | +1.1 | -0.3 to +1.7 | +1.0 | -0.4 to +1.6 | | |
| hf-whisper-large-v3-turbo-lora-e1__raw | **delta** (exhibition − fresh) | +0.6 | -1.8 to +1.1 |  |  | | |
| hf-whisper-large-v3-turbo-lora-e1__raw | **delta** (fresh − core) | +0.5 | -0.8 to +3.1 |  |  | | |
| hf-whisper-large-v3-turbo-lora-e2__raw | exhibition | 6.9 | 6.3–7.0 | 6.8 | 6.2–6.9 | 6.74–7.6 | 0% |
| hf-whisper-large-v3-turbo-lora-e2__raw | core | 5.3 | 4.9–7.0 | 5.3 | 4.9–7.0 | 4.82–8.24 | 0% |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh | 7.3 | 6.9–8.5 | <4.4 | 4.4–4.4 | censored | 98% |
| hf-whisper-large-v3-turbo-lora-e2__raw | **delta** (exhibition − core) | +1.6 | -0.2 to +2.0 | +1.5 | -0.3 to +1.9 | | |
| hf-whisper-large-v3-turbo-lora-e2__raw | **delta** (exhibition − fresh) | -0.4 | -1.8 to +0.1 |  |  | | |
| hf-whisper-large-v3-turbo-lora-e2__raw | **delta** (fresh − core) | +2.0 | +0.2 to +3.3 |  |  | | |
| hf-whisper-large-v3-turbo-lora-e3__raw | exhibition | 7.1 | 6.9–8.1 | 7.1 | 6.8–7.7 | 6.74–7.6 | 0% |
| hf-whisper-large-v3-turbo-lora-e3__raw | core | 5.3 | 5.0–6.7 | 5.3 | 5.0–6.7 | 4.82–8.24 | 0% |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh | 6.3 | 5.8–8.5 | <4.4 | 4.4–4.4 | censored | 98% |
| hf-whisper-large-v3-turbo-lora-e3__raw | **delta** (exhibition − core) | +1.8 | +0.3 to +2.7 | +1.8 | +0.2 to +2.5 | | |
| hf-whisper-large-v3-turbo-lora-e3__raw | **delta** (exhibition − fresh) | +0.8 | -1.3 to +1.8 |  |  | | |
| hf-whisper-large-v3-turbo-lora-e3__raw | **delta** (fresh − core) | +1.0 | -0.7 to +3.2 |  |  | | |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | exhibition | 7.1 | 6.3–7.9 | 7.1 | 6.3–7.8 | 6.74–7.6 | 0% |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | core | 7.0 | 5.9–8.2 | 7.0 | 5.9–8.2 | 4.82–8.24 | 8% |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh | 7.4 | 6.9–8.6 | <4.4 | 4.4–5.8 | censored | 95% |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | **delta** (exhibition − core) | +0.1 | -1.4 to +1.6 | +0.1 | -1.4 to +1.5 | | |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | **delta** (exhibition − fresh) | -0.3 | -1.9 to +0.7 |  |  | | |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | **delta** (fresh − core) | +0.4 | -1.0 to +2.4 |  |  | | |
| openrouter-assemblyai-universal-3-6-pro__raw | exhibition | 6.7 | 5.8–7.3 | 6.7 | 5.6–7.2 | 4.31–6.74 | 0% |
| openrouter-assemblyai-universal-3-6-pro__raw | core | 6.4 | 5.6–7.4 | 6.4 | 5.6–7.4 | 4.82–8.24 | 0% |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh | 7.3 | 7.1–8.5 | <4.4 | 4.4–6.4 | censored | 51% |
| openrouter-assemblyai-universal-3-6-pro__raw | **delta** (exhibition − core) | +0.2 | -1.0 to +1.3 | +0.2 | -1.2 to +1.2 | | |
| openrouter-assemblyai-universal-3-6-pro__raw | **delta** (exhibition − fresh) | -0.7 | -2.1 to -0.0 |  |  | | |
| openrouter-assemblyai-universal-3-6-pro__raw | **delta** (fresh − core) | +0.9 | -0.0 to +2.4 |  |  | | |
| openrouter-deepgram-nova-3__raw | exhibition | 4.6 | 4.2–4.8 | <4.2 | 4.2–4.7 | censored | 61% |
| openrouter-deepgram-nova-3__raw | core | <4.8 | 4.8–4.8 | <4.8 | 4.8–4.8 | censored | 100% |
| openrouter-deepgram-nova-3__raw | fresh | <4.4 | 4.4–4.4 | <4.4 | 4.4–4.4 | censored | 100% |
| openrouter-elevenlabs-scribe-v2__raw | exhibition | >10.3 | 10.3–10.3 | >10.3 | 6.2–10.3 | censored | 55% |
| openrouter-elevenlabs-scribe-v2__raw | core | 7.5 | 6.4–8.2 | 7.5 | 6.4–8.2 | 4.82–8.24 | 23% |
| openrouter-elevenlabs-scribe-v2__raw | fresh | 8.8 | 8.3–9.1 | 6.3 | 4.4–7.4 | 6.28–6.49 | 40% |
| openrouter-elevenlabs-scribe-v2__raw | **delta** (fresh − core) | +1.3 | +0.1 to +2.4 | -1.2 | -3.8 to +0.3 | | |
| openrouter-google-chirp-3__raw | exhibition | 6.1 | 5.6–7.0 | 5.9 | 5.1–7.0 | 4.31–6.74 | 0% |
| openrouter-google-chirp-3__raw | core | 5.0 | 4.8–5.6 | 5.0 | 4.8–5.6 | 4.82–8.24 | 32% |
| openrouter-google-chirp-3__raw | fresh | 5.8 | 5.8–6.9 | <4.4 | 4.4–5.8 | censored | 74% |
| openrouter-google-chirp-3__raw | **delta** (exhibition − core) | +1.1 | +0.3 to +2.1 | +0.9 | -0.1 to +2.1 | | |
| openrouter-google-chirp-3__raw | **delta** (exhibition − fresh) | +0.3 | -0.7 to +1.2 |  |  | | |
| openrouter-google-chirp-3__raw | **delta** (fresh − core) | +0.8 | +0.2 to +1.6 |  |  | | |
| openrouter-google-gemini-3.5-transcribe__raw | exhibition | 6.6 | 5.8–6.8 | 6.6 | 5.6–6.8 | 4.31–6.74 | 0% |
| openrouter-google-gemini-3.5-transcribe__raw | core | <4.8 | 4.8–4.8 | <4.8 | 4.8–4.8 | censored | 100% |
| openrouter-google-gemini-3.5-transcribe__raw | fresh | 6.3 | 4.4–6.3 | <4.4 | 4.4–4.4 | censored | 100% |
| openrouter-google-gemini-3.5-transcribe__raw | **delta** (exhibition − fresh) | +0.3 | -0.5 to +2.4 |  |  | | |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | exhibition | 6.8 | 6.0–7.6 | 6.8 | 5.6–7.6 | 6.74–7.6 | 0% |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | core | 5.9 | 5.0–6.7 | 5.9 | 5.0–6.7 | 4.82–8.24 | 1% |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh | 7.2 | 7.0–7.3 | <4.4 | 4.4–6.9 | censored | 75% |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | **delta** (exhibition − core) | +0.9 | -0.2 to +2.0 | +0.9 | -0.4 to +2.0 | | |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | **delta** (exhibition − fresh) | -0.4 | -1.2 to +0.5 |  |  | | |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | **delta** (fresh − core) | +1.3 | +0.5 to +2.2 |  |  | | |
| openrouter-openai-gpt-4o-transcribe__raw | exhibition | 6.7 | 6.2–7.8 | 6.6 | 5.9–7.7 | 4.31–6.74 | 0% |
| openrouter-openai-gpt-4o-transcribe__raw | core | 6.7 | 6.1–7.6 | 6.7 | 6.1–7.6 | 4.82–8.24 | 0% |
| openrouter-openai-gpt-4o-transcribe__raw | fresh | 6.5 | 4.4–6.5 | <4.4 | 4.4–4.4 | censored | 100% |
| openrouter-openai-gpt-4o-transcribe__raw | **delta** (exhibition − core) | +0.0 | -1.0 to +1.5 | -0.1 | -1.2 to +1.4 | | |
| openrouter-openai-gpt-4o-transcribe__raw | **delta** (exhibition − fresh) | +0.2 | -0.3 to +1.8 |  |  | | |
| openrouter-openai-gpt-4o-transcribe__raw | **delta** (fresh − core) | -0.2 | -1.8 to +0.4 |  |  | | |
| openrouter-openai-gpt-transcribe__raw | exhibition | >10.3 | 6.6–10.3 | 6.2 | 5.6–7.1 | 4.31–6.74 | 1% |
| openrouter-openai-gpt-transcribe__raw | core | 5.9 | 4.8–7.0 | 5.9 | 4.8–7.0 | 4.82–8.24 | 7% |
| openrouter-openai-gpt-transcribe__raw | fresh | 7.3 | 6.9–8.5 | <4.4 | 4.4–6.3 | censored | 85% |
| openrouter-openai-gpt-transcribe__raw | **delta** (exhibition − core) |  |  | +0.3 | -0.9 to +1.8 | | |
| openrouter-openai-gpt-transcribe__raw | **delta** (fresh − core) | +1.4 | +0.2 to +3.3 |  |  | | |
| openrouter-x-ai-grok-stt-2.0__raw | exhibition | 7.6 | 5.9–7.8 | 6.5 | 5.4–7.7 | 4.31–6.74 | 0% |
| openrouter-x-ai-grok-stt-2.0__raw | core | 6.2 | 5.1–7.1 | 6.2 | 5.1–7.1 | 4.82–8.24 | 1% |
| openrouter-x-ai-grok-stt-2.0__raw | fresh | 7.2 | 6.9–8.3 | <4.4 | 4.4–6.3 | censored | 88% |
| openrouter-x-ai-grok-stt-2.0__raw | **delta** (exhibition − core) | +1.4 | -0.6 to +2.4 | +0.3 | -1.1 to +2.1 | | |
| openrouter-x-ai-grok-stt-2.0__raw | **delta** (exhibition − fresh) | +0.4 | -1.6 to +0.8 |  |  | | |
| openrouter-x-ai-grok-stt-2.0__raw | **delta** (fresh − core) | +1.0 | +0.1 to +2.4 |  |  | | |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | exhibition | 5.8 | 5.2–6.8 | 5.6 | 4.2–6.8 | 4.31–6.74 | 5% |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | core | 6.2 | 5.5–6.8 | 6.2 | 5.5–6.8 | 4.82–8.24 | 0% |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh | 6.9 | 5.9–7.0 | <4.4 | 4.4–5.7 | censored | 89% |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | **delta** (exhibition − core) | -0.5 | -1.3 to +0.8 | -0.6 | -2.1 to +0.7 | | |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | **delta** (exhibition − fresh) | -1.2 | -1.7 to +0.4 |  |  | | |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | **delta** (fresh − core) | +0.7 | -0.6 to +1.5 |  |  | | |

## WER per segment

| model | segment | WER | adjusted WER | 95% CI | lines | words |
|---|---|---|---|---|---|---|
| faster-whisper-distil-large-v3__raw | lose-yourself-v1 | 10% | 13% | 5%–18% | 16 | 143 |
| faster-whisper-distil-large-v3__raw | the-way-i-am-v1 | 14% | 15% | 10%–23% | 15 | 138 |
| faster-whisper-distil-large-v3__raw | speedom-em | 30% | 29% | 21%–37% | 22 | 220 |
| faster-whisper-distil-large-v3__raw | worldwide-choppers-twista | 50% | 45% | 35%–55% | 19 | 183 |
| faster-whisper-distil-large-v3__raw | rap-god-fast | 31% | 30% | 17%–43% | 11 | 108 |
| faster-whisper-distil-large-v3__raw | godzilla-v3 | 58% | 57% | 46%–70% | 24 | 227 |
| faster-whisper-distil-large-v3__raw | suno02 | 60% | 48% | 36%–60% | 16 | 118 |
| faster-whisper-distil-large-v3__raw | suno01 | 17% | 14% | 7%–23% | 14 | 102 |
| faster-whisper-distil-large-v3__raw | fresh-titanic-gawne | 68% | 68% | 58%–77% | 30 | 187 |
| faster-whisper-distil-large-v3__raw | fresh-nightmares-gawne | 21% | 20% | 12%–30% | 16 | 102 |
| faster-whisper-distil-large-v3__raw | fresh-animals-pt-i-jid | 37% | 39% | 29%–51% | 21 | 188 |
| faster-whisper-distil-large-v3__raw | fresh-sk8-jid | 42% | 39% | 29%–49% | 15 | 129 |
| faster-whisper-distil-large-v3__raw | fresh-behold-jid | 37% | 36% | 27%–46% | 20 | 182 |
| faster-whisper-distil-large-v3__raw | fresh-never-me-token | 21% | 26% | 18%–33% | 19 | 167 |
| faster-whisper-distil-large-v3__raw | fresh-the-ropes-token | 45% | 46% | 37%–57% | 32 | 188 |
| faster-whisper-distil-large-v3__raw | fresh-kumquat-token | 23% | 24% | 15%–33% | 17 | 154 |
| faster-whisper-distil-large-v3__raw | fresh-gta-6-joyner-lucas | 34% | 34% | 25%–46% | 13 | 148 |
| faster-whisper-distil-large-v3__raw | fresh-one-of-them-joyner-lucas | 43% | 42% | 33%–52% | 20 | 161 |
| faster-whisper-distil-large-v3__raw | fresh-monsters-joyner-lucas | 16% | 17% | 10%–24% | 15 | 138 |
| faster-whisper-distil-large-v3__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 25% | 24% | 17%–31% | 18 | 153 |
| faster-whisper-distil-large-v3__raw | fresh-call-them-less-logic | 15% | 16% | 10%–21% | 15 | 136 |
| faster-whisper-distil-large-v3__raw | fresh-give-me-a-reason-nf | 17% | 17% | 7%–30% | 8 | 138 |
| faster-whisper-distil-large-v3__raw | fresh-bad-news-merkules | 22% | 23% | 14%–30% | 11 | 140 |
| faster-whisper-distil-large-v3__raw | fresh-richards-tale-set-the-scene-ren | 21% | 23% | 16%–28% | 12 | 112 |
| faster-whisper-distil-large-v3__raw | fresh-caught-you-in-the-bed-dax | 9% | 15% | 7%–18% | 11 | 126 |
| faster-whisper-distil-large-v3__raw | fresh-crash-out-king-iso | 16% | 17% | 7%–28% | 12 | 121 |
| faster-whisper-distil-large-v3__raw | fresh-raw-thoughts-vii-chris-webby | 4% | 4% | 0%–10% | 11 | 108 |
| faster-whisper-distil-large-v3__raw | fresh-jealous-type-doja-cat | 32% | 39% | 22%–54% | 10 | 96 |
| faster-whisper-large-v3__raw | lose-yourself-v1 | 6% | 7% | 2%–12% | 16 | 143 |
| faster-whisper-large-v3__raw | the-way-i-am-v1 | 9% | 10% | 5%–15% | 15 | 138 |
| faster-whisper-large-v3__raw | speedom-em | 23% | 22% | 13%–33% | 22 | 220 |
| faster-whisper-large-v3__raw | worldwide-choppers-twista | 22% | 19% | 14%–27% | 19 | 183 |
| faster-whisper-large-v3__raw | rap-god-fast | 28% | 28% | 13%–42% | 11 | 108 |
| faster-whisper-large-v3__raw | godzilla-v3 | 26% | 25% | 18%–33% | 24 | 227 |
| faster-whisper-large-v3__raw | suno02 | 51% | 45% | 32%–57% | 16 | 118 |
| faster-whisper-large-v3__raw | suno01 | 10% | 8% | 3%–17% | 14 | 102 |
| faster-whisper-large-v3__raw | fresh-titanic-gawne | 49% | 48% | 38%–61% | 30 | 187 |
| faster-whisper-large-v3__raw | fresh-nightmares-gawne | 14% | 13% | 7%–21% | 15 | 100 |
| faster-whisper-large-v3__raw | fresh-animals-pt-i-jid | 21% | 22% | 13%–31% | 21 | 188 |
| faster-whisper-large-v3__raw | fresh-sk8-jid | 18% | 16% | 8%–27% | 15 | 129 |
| faster-whisper-large-v3__raw | fresh-behold-jid | 32% | 31% | 21%–43% | 20 | 182 |
| faster-whisper-large-v3__raw | fresh-never-me-token | 13% | 18% | 12%–23% | 19 | 167 |
| faster-whisper-large-v3__raw | fresh-the-ropes-token | 23% | 24% | 18%–32% | 32 | 188 |
| faster-whisper-large-v3__raw | fresh-kumquat-token | 11% | 11% | 5%–20% | 17 | 154 |
| faster-whisper-large-v3__raw | fresh-gta-6-joyner-lucas | 23% | 23% | 14%–35% | 13 | 148 |
| faster-whisper-large-v3__raw | fresh-one-of-them-joyner-lucas | 28% | 28% | 18%–41% | 20 | 161 |
| faster-whisper-large-v3__raw | fresh-monsters-joyner-lucas | 13% | 13% | 7%–20% | 15 | 138 |
| faster-whisper-large-v3__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 22% | 20% | 15%–26% | 18 | 153 |
| faster-whisper-large-v3__raw | fresh-call-them-less-logic | 10% | 11% | 5%–16% | 15 | 136 |
| faster-whisper-large-v3__raw | fresh-give-me-a-reason-nf | 7% | 7% | 1%–13% | 8 | 138 |
| faster-whisper-large-v3__raw | fresh-bad-news-merkules | 19% | 21% | 13%–28% | 11 | 140 |
| faster-whisper-large-v3__raw | fresh-richards-tale-set-the-scene-ren | 15% | 16% | 9%–23% | 12 | 112 |
| faster-whisper-large-v3__raw | fresh-caught-you-in-the-bed-dax | 2% | 7% | 1%–9% | 11 | 126 |
| faster-whisper-large-v3__raw | fresh-crash-out-king-iso | 8% | 9% | 4%–15% | 12 | 121 |
| faster-whisper-large-v3__raw | fresh-raw-thoughts-vii-chris-webby | 3% | 3% | 0%–8% | 11 | 108 |
| faster-whisper-large-v3__raw | fresh-jealous-type-doja-cat | 25% | 32% | 18%–47% | 10 | 96 |
| faster-whisper-large-v3__vocals | lose-yourself-v1 | 10% | 12% | 6%–18% | 16 | 143 |
| faster-whisper-large-v3__vocals | the-way-i-am-v1 | 21% | 23% | 11%–36% | 15 | 138 |
| faster-whisper-large-v3__vocals | speedom-em | 22% | 21% | 13%–30% | 22 | 220 |
| faster-whisper-large-v3__vocals | worldwide-choppers-twista | 33% | 31% | 19%–46% | 19 | 183 |
| faster-whisper-large-v3__vocals | rap-god-fast | 22% | 22% | 13%–30% | 11 | 104 |
| faster-whisper-large-v3__vocals | godzilla-v3 | 25% | 24% | 16%–33% | 24 | 227 |
| faster-whisper-small__raw | lose-yourself-v1 | 11% | 13% | 6%–18% | 16 | 143 |
| faster-whisper-small__raw | the-way-i-am-v1 | 18% | 20% | 11%–29% | 15 | 138 |
| faster-whisper-small__raw | speedom-em | 33% | 32% | 22%–43% | 22 | 220 |
| faster-whisper-small__raw | worldwide-choppers-twista | 61% | 58% | 47%–70% | 19 | 183 |
| faster-whisper-small__raw | rap-god-fast | 32% | 32% | 22%–42% | 11 | 108 |
| faster-whisper-small__raw | godzilla-v3 | 38% | 38% | 25%–53% | 24 | 227 |
| faster-whisper-small__raw | suno02 | 64% | 58% | 50%–67% | 16 | 118 |
| faster-whisper-small__raw | suno01 | 25% | 23% | 13%–37% | 14 | 102 |
| faster-whisper-small__raw | fresh-titanic-gawne | 61% | 61% | 50%–73% | 30 | 187 |
| faster-whisper-small__raw | fresh-nightmares-gawne | 24% | 22% | 11%–37% | 16 | 102 |
| faster-whisper-small__raw | fresh-animals-pt-i-jid | 36% | 37% | 26%–49% | 21 | 188 |
| faster-whisper-small__raw | fresh-sk8-jid | 40% | 38% | 28%–51% | 15 | 129 |
| faster-whisper-small__raw | fresh-behold-jid | 43% | 41% | 29%–54% | 20 | 182 |
| faster-whisper-small__raw | fresh-never-me-token | 14% | 17% | 10%–24% | 19 | 167 |
| faster-whisper-small__raw | fresh-the-ropes-token | 37% | 38% | 28%–50% | 32 | 188 |
| faster-whisper-small__raw | fresh-kumquat-token | 20% | 21% | 11%–32% | 17 | 154 |
| faster-whisper-small__raw | fresh-gta-6-joyner-lucas | 30% | 30% | 18%–45% | 13 | 148 |
| faster-whisper-small__raw | fresh-one-of-them-joyner-lucas | 32% | 32% | 23%–42% | 20 | 161 |
| faster-whisper-small__raw | fresh-monsters-joyner-lucas | 24% | 25% | 16%–33% | 15 | 138 |
| faster-whisper-small__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 20% | 20% | 14%–26% | 18 | 153 |
| faster-whisper-small__raw | fresh-call-them-less-logic | 18% | 19% | 11%–27% | 15 | 136 |
| faster-whisper-small__raw | fresh-give-me-a-reason-nf | 11% | 11% | 2%–19% | 8 | 138 |
| faster-whisper-small__raw | fresh-bad-news-merkules | 26% | 28% | 19%–34% | 11 | 140 |
| faster-whisper-small__raw | fresh-richards-tale-set-the-scene-ren | 112% | 107% | 28%–260% | 12 | 112 |
| faster-whisper-small__raw | fresh-caught-you-in-the-bed-dax | 5% | 11% | 4%–14% | 11 | 126 |
| faster-whisper-small__raw | fresh-crash-out-king-iso | 17% | 19% | 10%–28% | 12 | 121 |
| faster-whisper-small__raw | fresh-raw-thoughts-vii-chris-webby | 4% | 4% | 0%–10% | 11 | 108 |
| faster-whisper-small__raw | fresh-jealous-type-doja-cat | 28% | 34% | 16%–51% | 10 | 96 |
| faster-whisper-tiny__raw | lose-yourself-v1 | 21% | 22% | 14%–32% | 16 | 143 |
| faster-whisper-tiny__raw | the-way-i-am-v1 | 57% | 58% | 45%–72% | 15 | 138 |
| faster-whisper-tiny__raw | speedom-em | 44% | 42% | 35%–49% | 22 | 220 |
| faster-whisper-tiny__raw | worldwide-choppers-twista | 78% | 77% | 61%–93% | 19 | 183 |
| faster-whisper-tiny__raw | rap-god-fast | 100% | 100% | 100%–100% | 11 | 104 |
| faster-whisper-tiny__raw | godzilla-v3 | 98% | 98% | 94%–100% | 24 | 227 |
| faster-whisper-tiny__raw | suno02 | 66% | 62% | 44%–76% | 16 | 118 |
| faster-whisper-tiny__raw | suno01 | 47% | 40% | 28%–52% | 14 | 102 |
| faster-whisper-tiny__raw | fresh-titanic-gawne | 92% | 92% | 85%–97% | 30 | 187 |
| faster-whisper-tiny__raw | fresh-nightmares-gawne | 45% | 46% | 32%–60% | 16 | 102 |
| faster-whisper-tiny__raw | fresh-animals-pt-i-jid | 60% | 60% | 50%–71% | 21 | 192 |
| faster-whisper-tiny__raw | fresh-sk8-jid | 64% | 62% | 48%–74% | 15 | 129 |
| faster-whisper-tiny__raw | fresh-behold-jid | 78% | 77% | 67%–86% | 20 | 183 |
| faster-whisper-tiny__raw | fresh-never-me-token | 41% | 45% | 39%–52% | 19 | 167 |
| faster-whisper-tiny__raw | fresh-the-ropes-token | 71% | 72% | 59%–85% | 32 | 188 |
| faster-whisper-tiny__raw | fresh-kumquat-token | 46% | 47% | 35%–59% | 17 | 154 |
| faster-whisper-tiny__raw | fresh-gta-6-joyner-lucas | 66% | 65% | 50%–81% | 13 | 148 |
| faster-whisper-tiny__raw | fresh-one-of-them-joyner-lucas | 65% | 65% | 51%–79% | 20 | 161 |
| faster-whisper-tiny__raw | fresh-monsters-joyner-lucas | 38% | 38% | 30%–46% | 15 | 138 |
| faster-whisper-tiny__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 46% | 45% | 36%–54% | 18 | 153 |
| faster-whisper-tiny__raw | fresh-call-them-less-logic | 34% | 35% | 26%–46% | 15 | 136 |
| faster-whisper-tiny__raw | fresh-give-me-a-reason-nf | 39% | 41% | 23%–60% | 8 | 138 |
| faster-whisper-tiny__raw | fresh-bad-news-merkules | 39% | 42% | 27%–54% | 11 | 140 |
| faster-whisper-tiny__raw | fresh-richards-tale-set-the-scene-ren | 62% | 60% | 48%–70% | 12 | 112 |
| faster-whisper-tiny__raw | fresh-caught-you-in-the-bed-dax | 20% | 26% | 13%–36% | 11 | 126 |
| faster-whisper-tiny__raw | fresh-crash-out-king-iso | 34% | 35% | 22%–49% | 12 | 121 |
| faster-whisper-tiny__raw | fresh-raw-thoughts-vii-chris-webby | 34% | 34% | 22%–49% | 11 | 108 |
| faster-whisper-tiny__raw | fresh-jealous-type-doja-cat | 51% | 58% | 45%–70% | 10 | 96 |
| faster-whisper-tiny__vocals | lose-yourself-v1 | 24% | 26% | 16%–38% | 16 | 143 |
| faster-whisper-tiny__vocals | the-way-i-am-v1 | 57% | 59% | 44%–73% | 15 | 138 |
| faster-whisper-tiny__vocals | speedom-em | 44% | 43% | 35%–51% | 22 | 220 |
| faster-whisper-tiny__vocals | worldwide-choppers-twista | 74% | 72% | 59%–87% | 18 | 176 |
| faster-whisper-tiny__vocals | rap-god-fast | 64% | 64% | 40%–90% | 11 | 108 |
| faster-whisper-tiny__vocals | godzilla-v3 | 59% | 58% | 48%–67% | 24 | 227 |
| faster-whisper-turbo__raw | lose-yourself-v1 | 6% | 9% | 2%–11% | 16 | 143 |
| faster-whisper-turbo__raw | the-way-i-am-v1 | 10% | 11% | 7%–17% | 15 | 138 |
| faster-whisper-turbo__raw | speedom-em | 21% | 19% | 14%–25% | 22 | 220 |
| faster-whisper-turbo__raw | worldwide-choppers-twista | 33% | 31% | 22%–41% | 19 | 183 |
| faster-whisper-turbo__raw | rap-god-fast | 88% | 88% | 69%–100% | 11 | 108 |
| faster-whisper-turbo__raw | godzilla-v3 | 34% | 33% | 26%–41% | 24 | 227 |
| faster-whisper-turbo__raw | suno02 | 44% | 36% | 24%–50% | 16 | 118 |
| faster-whisper-turbo__raw | suno01 | 15% | 13% | 6%–22% | 14 | 102 |
| faster-whisper-turbo__raw | fresh-titanic-gawne | 60% | 60% | 47%–74% | 30 | 187 |
| faster-whisper-turbo__raw | fresh-nightmares-gawne | 9% | 8% | 3%–14% | 15 | 100 |
| faster-whisper-turbo__raw | fresh-animals-pt-i-jid | 21% | 23% | 14%–32% | 21 | 188 |
| faster-whisper-turbo__raw | fresh-sk8-jid | 20% | 20% | 9%–35% | 15 | 129 |
| faster-whisper-turbo__raw | fresh-behold-jid | 25% | 25% | 16%–35% | 20 | 182 |
| faster-whisper-turbo__raw | fresh-never-me-token | 15% | 20% | 15%–25% | 19 | 167 |
| faster-whisper-turbo__raw | fresh-the-ropes-token | 27% | 29% | 21%–37% | 32 | 188 |
| faster-whisper-turbo__raw | fresh-kumquat-token | 16% | 17% | 9%–25% | 17 | 154 |
| faster-whisper-turbo__raw | fresh-gta-6-joyner-lucas | 19% | 19% | 10%–30% | 13 | 148 |
| faster-whisper-turbo__raw | fresh-one-of-them-joyner-lucas | 30% | 30% | 22%–40% | 20 | 161 |
| faster-whisper-turbo__raw | fresh-monsters-joyner-lucas | 16% | 16% | 9%–23% | 15 | 138 |
| faster-whisper-turbo__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 20% | 20% | 13%–27% | 18 | 153 |
| faster-whisper-turbo__raw | fresh-call-them-less-logic | 10% | 10% | 5%–16% | 15 | 136 |
| faster-whisper-turbo__raw | fresh-give-me-a-reason-nf | 14% | 15% | 6%–28% | 8 | 138 |
| faster-whisper-turbo__raw | fresh-bad-news-merkules | 25% | 27% | 18%–34% | 11 | 140 |
| faster-whisper-turbo__raw | fresh-richards-tale-set-the-scene-ren | 23% | 24% | 13%–33% | 12 | 112 |
| faster-whisper-turbo__raw | fresh-caught-you-in-the-bed-dax | 104% | 154% | 11%–411% | 11 | 137 |
| faster-whisper-turbo__raw | fresh-crash-out-king-iso | 10% | 11% | 7%–16% | 12 | 121 |
| faster-whisper-turbo__raw | fresh-raw-thoughts-vii-chris-webby | 4% | 4% | 0%–10% | 11 | 108 |
| faster-whisper-turbo__raw | fresh-jealous-type-doja-cat | 32% | 39% | 22%–56% | 10 | 96 |
| hf-UsefulSensors-moonshine-base__raw | lose-yourself-v1 | 30% | 30% | 12%–48% | 16 | 143 |
| hf-UsefulSensors-moonshine-base__raw | the-way-i-am-v1 | 29% | 30% | 20%–42% | 15 | 138 |
| hf-UsefulSensors-moonshine-base__raw | speedom-em | 75% | 75% | 59%–90% | 22 | 220 |
| hf-UsefulSensors-moonshine-base__raw | worldwide-choppers-twista | 68% | 65% | 52%–77% | 18 | 176 |
| hf-UsefulSensors-moonshine-base__raw | rap-god-fast | 28% | 28% | 15%–40% | 11 | 104 |
| hf-UsefulSensors-moonshine-base__raw | godzilla-v3 | 72% | 72% | 59%–83% | 24 | 227 |
| hf-UsefulSensors-moonshine-base__raw | suno02 | 64% | 62% | 44%–77% | 16 | 118 |
| hf-UsefulSensors-moonshine-base__raw | suno01 | 42% | 38% | 25%–53% | 14 | 100 |
| hf-UsefulSensors-moonshine-base__raw | fresh-titanic-gawne | 72% | 71% | 60%–84% | 30 | 187 |
| hf-UsefulSensors-moonshine-base__raw | fresh-nightmares-gawne | 35% | 37% | 24%–51% | 16 | 102 |
| hf-UsefulSensors-moonshine-base__raw | fresh-animals-pt-i-jid | 53% | 54% | 38%–69% | 21 | 188 |
| hf-UsefulSensors-moonshine-base__raw | fresh-sk8-jid | 53% | 53% | 41%–64% | 15 | 129 |
| hf-UsefulSensors-moonshine-base__raw | fresh-behold-jid | 92% | 91% | 81%–99% | 20 | 182 |
| hf-UsefulSensors-moonshine-base__raw | fresh-never-me-token | 37% | 41% | 30%–54% | 19 | 167 |
| hf-UsefulSensors-moonshine-base__raw | fresh-the-ropes-token | 68% | 69% | 57%–81% | 32 | 188 |
| hf-UsefulSensors-moonshine-base__raw | fresh-kumquat-token | 34% | 36% | 20%–53% | 17 | 154 |
| hf-UsefulSensors-moonshine-base__raw | fresh-gta-6-joyner-lucas | 35% | 35% | 19%–53% | 13 | 148 |
| hf-UsefulSensors-moonshine-base__raw | fresh-one-of-them-joyner-lucas | 40% | 39% | 30%–52% | 20 | 161 |
| hf-UsefulSensors-moonshine-base__raw | fresh-monsters-joyner-lucas | 22% | 22% | 15%–29% | 15 | 138 |
| hf-UsefulSensors-moonshine-base__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 37% | 37% | 22%–54% | 18 | 153 |
| hf-UsefulSensors-moonshine-base__raw | fresh-call-them-less-logic | 20% | 21% | 15%–26% | 15 | 136 |
| hf-UsefulSensors-moonshine-base__raw | fresh-give-me-a-reason-nf | 16% | 17% | 7%–27% | 8 | 138 |
| hf-UsefulSensors-moonshine-base__raw | fresh-bad-news-merkules | 26% | 28% | 18%–36% | 11 | 140 |
| hf-UsefulSensors-moonshine-base__raw | fresh-richards-tale-set-the-scene-ren | 40% | 41% | 27%–53% | 12 | 112 |
| hf-UsefulSensors-moonshine-base__raw | fresh-caught-you-in-the-bed-dax | 10% | 16% | 5%–25% | 11 | 126 |
| hf-UsefulSensors-moonshine-base__raw | fresh-crash-out-king-iso | 21% | 22% | 12%–32% | 12 | 121 |
| hf-UsefulSensors-moonshine-base__raw | fresh-raw-thoughts-vii-chris-webby | 7% | 8% | 2%–18% | 11 | 108 |
| hf-UsefulSensors-moonshine-base__raw | fresh-jealous-type-doja-cat | 114% | 109% | 27%–259% | 10 | 96 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | lose-yourself-v1 | 59% | 61% | 44%–79% | 16 | 143 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | the-way-i-am-v1 | 91% | 91% | 86%–96% | 15 | 138 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | speedom-em | 78% | 77% | 69%–85% | 22 | 220 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | worldwide-choppers-twista | 86% | 84% | 76%–92% | 18 | 176 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | rap-god-fast | 81% | 82% | 71%–92% | 11 | 108 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | godzilla-v3 | 88% | 87% | 79%–95% | 24 | 227 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | suno02 | 91% | 91% | 77%–106% | 16 | 118 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | suno01 | 95% | 94% | 83%–102% | 14 | 102 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-titanic-gawne | 98% | 98% | 95%–100% | 30 | 187 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-nightmares-gawne | 72% | 73% | 63%–82% | 15 | 100 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-animals-pt-i-jid | 82% | 82% | 75%–88% | 21 | 188 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-sk8-jid | 75% | 73% | 60%–86% | 15 | 129 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-behold-jid | 88% | 87% | 81%–92% | 20 | 183 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-never-me-token | 76% | 78% | 68%–89% | 19 | 167 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-the-ropes-token | 94% | 94% | 92%–97% | 32 | 188 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-kumquat-token | 72% | 73% | 63%–82% | 17 | 154 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-gta-6-joyner-lucas | 84% | 84% | 77%–90% | 13 | 148 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-one-of-them-joyner-lucas | 89% | 88% | 82%–94% | 20 | 161 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-monsters-joyner-lucas | 77% | 77% | 70%–84% | 15 | 144 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 70% | 69% | 59%–79% | 18 | 156 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-call-them-less-logic | 71% | 72% | 61%–82% | 15 | 136 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-give-me-a-reason-nf | 57% | 58% | 48%–68% | 8 | 138 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-bad-news-merkules | 65% | 67% | 57%–76% | 11 | 140 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-richards-tale-set-the-scene-ren | 60% | 60% | 41%–76% | 12 | 112 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-caught-you-in-the-bed-dax | 48% | 55% | 39%–71% | 11 | 126 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-crash-out-king-iso | 68% | 69% | 58%–80% | 12 | 121 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-raw-thoughts-vii-chris-webby | 65% | 64% | 45%–83% | 11 | 108 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-jealous-type-doja-cat | 96% | 96% | 94%–99% | 10 | 96 |
| hf-whisper-large-v3-turbo-base__raw | lose-yourself-v1 | 5% | 8% | 2%–10% | 16 | 143 |
| hf-whisper-large-v3-turbo-base__raw | the-way-i-am-v1 | 10% | 12% | 8%–16% | 15 | 138 |
| hf-whisper-large-v3-turbo-base__raw | speedom-em | 23% | 21% | 15%–29% | 22 | 220 |
| hf-whisper-large-v3-turbo-base__raw | worldwide-choppers-twista | 86% | 85% | 69%–99% | 19 | 183 |
| hf-whisper-large-v3-turbo-base__raw | rap-god-fast | 32% | 32% | 19%–48% | 11 | 108 |
| hf-whisper-large-v3-turbo-base__raw | godzilla-v3 | 30% | 29% | 21%–38% | 24 | 227 |
| hf-whisper-large-v3-turbo-base__raw | suno02 | 47% | 39% | 28%–50% | 16 | 118 |
| hf-whisper-large-v3-turbo-base__raw | suno01 | 12% | 8% | 3%–14% | 14 | 102 |
| hf-whisper-large-v3-turbo-base__raw | fresh-titanic-gawne | 49% | 49% | 38%–61% | 30 | 187 |
| hf-whisper-large-v3-turbo-base__raw | fresh-nightmares-gawne | 9% | 8% | 3%–14% | 15 | 100 |
| hf-whisper-large-v3-turbo-base__raw | fresh-animals-pt-i-jid | 30% | 31% | 18%–47% | 21 | 188 |
| hf-whisper-large-v3-turbo-base__raw | fresh-sk8-jid | 19% | 17% | 8%–32% | 15 | 129 |
| hf-whisper-large-v3-turbo-base__raw | fresh-behold-jid | 32% | 31% | 22%–41% | 20 | 182 |
| hf-whisper-large-v3-turbo-base__raw | fresh-never-me-token | 14% | 20% | 14%–24% | 19 | 167 |
| hf-whisper-large-v3-turbo-base__raw | fresh-the-ropes-token | 28% | 30% | 22%–39% | 32 | 188 |
| hf-whisper-large-v3-turbo-base__raw | fresh-kumquat-token | 16% | 17% | 9%–25% | 17 | 154 |
| hf-whisper-large-v3-turbo-base__raw | fresh-gta-6-joyner-lucas | 20% | 20% | 11%–33% | 13 | 148 |
| hf-whisper-large-v3-turbo-base__raw | fresh-one-of-them-joyner-lucas | 27% | 26% | 19%–36% | 20 | 161 |
| hf-whisper-large-v3-turbo-base__raw | fresh-monsters-joyner-lucas | 18% | 18% | 11%–26% | 15 | 138 |
| hf-whisper-large-v3-turbo-base__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 20% | 20% | 13%–27% | 18 | 153 |
| hf-whisper-large-v3-turbo-base__raw | fresh-call-them-less-logic | 11% | 12% | 5%–19% | 15 | 136 |
| hf-whisper-large-v3-turbo-base__raw | fresh-give-me-a-reason-nf | 12% | 13% | 4%–23% | 8 | 138 |
| hf-whisper-large-v3-turbo-base__raw | fresh-bad-news-merkules | 24% | 26% | 17%–33% | 11 | 140 |
| hf-whisper-large-v3-turbo-base__raw | fresh-richards-tale-set-the-scene-ren | 15% | 16% | 7%–24% | 12 | 112 |
| hf-whisper-large-v3-turbo-base__raw | fresh-caught-you-in-the-bed-dax | 5% | 6% | 2%–10% | 11 | 126 |
| hf-whisper-large-v3-turbo-base__raw | fresh-crash-out-king-iso | 9% | 10% | 5%–15% | 12 | 121 |
| hf-whisper-large-v3-turbo-base__raw | fresh-raw-thoughts-vii-chris-webby | 4% | 4% | 0%–10% | 11 | 108 |
| hf-whisper-large-v3-turbo-base__raw | fresh-jealous-type-doja-cat | 32% | 39% | 22%–56% | 10 | 96 |
| hf-whisper-large-v3-turbo-guard-base__raw | lose-yourself-v1 | 5% | 8% | 2%–10% | 16 | 143 |
| hf-whisper-large-v3-turbo-guard-base__raw | the-way-i-am-v1 | 10% | 12% | 8%–16% | 15 | 138 |
| hf-whisper-large-v3-turbo-guard-base__raw | speedom-em | 23% | 21% | 15%–29% | 22 | 220 |
| hf-whisper-large-v3-turbo-guard-base__raw | worldwide-choppers-twista | 40% | 35% | 27%–46% | 19 | 183 |
| hf-whisper-large-v3-turbo-guard-base__raw | rap-god-fast | 32% | 32% | 19%–48% | 11 | 108 |
| hf-whisper-large-v3-turbo-guard-base__raw | godzilla-v3 | 30% | 29% | 21%–38% | 24 | 227 |
| hf-whisper-large-v3-turbo-guard-base__raw | suno02 | 47% | 39% | 28%–50% | 16 | 118 |
| hf-whisper-large-v3-turbo-guard-base__raw | suno01 | 12% | 8% | 3%–14% | 14 | 102 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-titanic-gawne | 49% | 49% | 38%–61% | 30 | 187 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-nightmares-gawne | 9% | 8% | 3%–14% | 15 | 100 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-animals-pt-i-jid | 30% | 31% | 18%–47% | 21 | 188 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-sk8-jid | 19% | 17% | 8%–32% | 15 | 129 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-behold-jid | 32% | 31% | 22%–41% | 20 | 182 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-never-me-token | 14% | 20% | 14%–24% | 19 | 167 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-the-ropes-token | 28% | 30% | 22%–39% | 32 | 188 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-kumquat-token | 16% | 17% | 9%–25% | 17 | 154 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-gta-6-joyner-lucas | 20% | 20% | 11%–33% | 13 | 148 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-one-of-them-joyner-lucas | 27% | 26% | 19%–36% | 20 | 161 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-monsters-joyner-lucas | 18% | 18% | 11%–26% | 15 | 138 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 20% | 20% | 13%–27% | 18 | 153 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-call-them-less-logic | 11% | 12% | 5%–19% | 15 | 136 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-give-me-a-reason-nf | 12% | 13% | 4%–23% | 8 | 138 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-bad-news-merkules | 24% | 26% | 17%–33% | 11 | 140 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-richards-tale-set-the-scene-ren | 15% | 16% | 7%–24% | 12 | 112 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-caught-you-in-the-bed-dax | 5% | 6% | 2%–10% | 11 | 126 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-crash-out-king-iso | 9% | 10% | 5%–15% | 12 | 121 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-raw-thoughts-vii-chris-webby | 4% | 4% | 0%–10% | 11 | 108 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-jealous-type-doja-cat | 32% | 39% | 22%–56% | 10 | 96 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | lose-yourself-v1 | 7% | 9% | 4%–15% | 16 | 143 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | the-way-i-am-v1 | 12% | 13% | 7%–18% | 15 | 138 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | speedom-em | 23% | 21% | 17%–26% | 22 | 220 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | worldwide-choppers-twista | 45% | 41% | 29%–55% | 19 | 183 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | rap-god-fast | 31% | 30% | 17%–45% | 11 | 108 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | godzilla-v3 | 30% | 30% | 21%–38% | 24 | 227 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | suno02 | 47% | 42% | 31%–52% | 16 | 118 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | suno01 | 16% | 12% | 6%–19% | 14 | 102 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-titanic-gawne | 42% | 42% | 33%–51% | 30 | 187 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-nightmares-gawne | 17% | 16% | 6%–27% | 15 | 100 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-animals-pt-i-jid | 24% | 25% | 15%–35% | 21 | 188 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-sk8-jid | 25% | 21% | 13%–31% | 15 | 129 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-behold-jid | 35% | 33% | 25%–44% | 20 | 182 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-never-me-token | 14% | 19% | 13%–24% | 19 | 167 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-the-ropes-token | 32% | 34% | 25%–43% | 32 | 188 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-kumquat-token | 19% | 20% | 12%–29% | 17 | 154 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-gta-6-joyner-lucas | 22% | 22% | 11%–35% | 13 | 148 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-one-of-them-joyner-lucas | 26% | 26% | 17%–36% | 20 | 161 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-monsters-joyner-lucas | 13% | 13% | 6%–21% | 15 | 138 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 15% | 15% | 10%–21% | 18 | 153 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-call-them-less-logic | 12% | 13% | 7%–20% | 15 | 136 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-give-me-a-reason-nf | 9% | 10% | 2%–18% | 8 | 138 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-bad-news-merkules | 23% | 25% | 16%–33% | 11 | 140 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-richards-tale-set-the-scene-ren | 26% | 27% | 15%–38% | 12 | 112 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-caught-you-in-the-bed-dax | 6% | 11% | 3%–14% | 11 | 126 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-crash-out-king-iso | 12% | 14% | 8%–20% | 12 | 121 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-raw-thoughts-vii-chris-webby | 3% | 3% | 0%–10% | 11 | 108 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-jealous-type-doja-cat | 33% | 40% | 21%–61% | 10 | 96 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | lose-yourself-v1 | 10% | 12% | 6%–20% | 16 | 143 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | the-way-i-am-v1 | 14% | 15% | 8%–22% | 15 | 138 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | speedom-em | 21% | 21% | 15%–27% | 22 | 220 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | worldwide-choppers-twista | 46% | 41% | 29%–57% | 19 | 183 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | rap-god-fast | 37% | 37% | 24%–52% | 11 | 108 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | godzilla-v3 | 30% | 29% | 19%–39% | 24 | 227 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | suno02 | 54% | 44% | 34%–54% | 16 | 118 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | suno01 | 14% | 10% | 4%–19% | 14 | 102 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-titanic-gawne | 45% | 45% | 37%–54% | 30 | 187 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-nightmares-gawne | 18% | 17% | 6%–28% | 15 | 100 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-animals-pt-i-jid | 27% | 28% | 18%–39% | 21 | 188 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-sk8-jid | 22% | 21% | 12%–34% | 15 | 129 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-behold-jid | 32% | 31% | 22%–41% | 20 | 182 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-never-me-token | 16% | 21% | 15%–26% | 19 | 167 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-the-ropes-token | 34% | 35% | 27%–45% | 32 | 188 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-kumquat-token | 19% | 20% | 10%–32% | 17 | 154 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-gta-6-joyner-lucas | 22% | 22% | 13%–33% | 13 | 148 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-one-of-them-joyner-lucas | 27% | 27% | 19%–37% | 20 | 161 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-monsters-joyner-lucas | 11% | 11% | 5%–18% | 15 | 138 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 16% | 16% | 10%–24% | 18 | 153 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-call-them-less-logic | 12% | 12% | 5%–21% | 15 | 136 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-give-me-a-reason-nf | 13% | 14% | 6%–23% | 8 | 138 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-bad-news-merkules | 27% | 30% | 19%–40% | 11 | 140 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-richards-tale-set-the-scene-ren | 22% | 23% | 13%–32% | 12 | 112 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-caught-you-in-the-bed-dax | 2% | 3% | 0%–5% | 11 | 126 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-crash-out-king-iso | 8% | 9% | 5%–14% | 12 | 121 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-raw-thoughts-vii-chris-webby | 5% | 5% | 0%–12% | 11 | 108 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-jealous-type-doja-cat | 40% | 46% | 26%–65% | 10 | 96 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | lose-yourself-v1 | 13% | 15% | 7%–22% | 16 | 143 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | the-way-i-am-v1 | 13% | 14% | 7%–21% | 15 | 138 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | speedom-em | 20% | 18% | 13%–24% | 22 | 220 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | worldwide-choppers-twista | 36% | 35% | 24%–48% | 19 | 183 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | rap-god-fast | 35% | 35% | 19%–51% | 11 | 108 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | godzilla-v3 | 37% | 36% | 27%–46% | 24 | 227 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | suno02 | 54% | 46% | 38%–55% | 16 | 118 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | suno01 | 12% | 9% | 4%–17% | 14 | 102 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-titanic-gawne | 46% | 46% | 36%–55% | 30 | 187 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-nightmares-gawne | 19% | 20% | 7%–32% | 15 | 100 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-animals-pt-i-jid | 27% | 28% | 18%–39% | 21 | 188 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-sk8-jid | 24% | 20% | 12%–30% | 15 | 129 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-behold-jid | 34% | 33% | 22%–48% | 20 | 182 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-never-me-token | 15% | 20% | 14%–25% | 19 | 167 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-the-ropes-token | 39% | 41% | 30%–54% | 32 | 188 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-kumquat-token | 17% | 18% | 8%–29% | 17 | 154 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-gta-6-joyner-lucas | 21% | 21% | 13%–32% | 13 | 148 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-one-of-them-joyner-lucas | 25% | 25% | 18%–33% | 20 | 161 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-monsters-joyner-lucas | 11% | 11% | 6%–16% | 15 | 138 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 18% | 18% | 12%–25% | 18 | 153 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-call-them-less-logic | 15% | 16% | 8%–23% | 15 | 136 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-give-me-a-reason-nf | 14% | 14% | 6%–24% | 8 | 138 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-bad-news-merkules | 29% | 31% | 21%–40% | 11 | 140 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-richards-tale-set-the-scene-ren | 23% | 24% | 11%–37% | 12 | 112 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-caught-you-in-the-bed-dax | 9% | 15% | 6%–20% | 11 | 126 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-crash-out-king-iso | 13% | 14% | 7%–22% | 12 | 121 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-raw-thoughts-vii-chris-webby | 3% | 3% | 0%–7% | 11 | 108 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-jealous-type-doja-cat | 36% | 43% | 25%–61% | 10 | 96 |
| hf-whisper-large-v3-turbo-lora-e1__raw | lose-yourself-v1 | 7% | 9% | 4%–15% | 16 | 143 |
| hf-whisper-large-v3-turbo-lora-e1__raw | the-way-i-am-v1 | 12% | 13% | 7%–18% | 15 | 138 |
| hf-whisper-large-v3-turbo-lora-e1__raw | speedom-em | 23% | 21% | 17%–26% | 22 | 220 |
| hf-whisper-large-v3-turbo-lora-e1__raw | worldwide-choppers-twista | 84% | 83% | 65%–96% | 18 | 176 |
| hf-whisper-large-v3-turbo-lora-e1__raw | rap-god-fast | 31% | 30% | 17%–45% | 11 | 108 |
| hf-whisper-large-v3-turbo-lora-e1__raw | godzilla-v3 | 30% | 30% | 21%–38% | 24 | 227 |
| hf-whisper-large-v3-turbo-lora-e1__raw | suno02 | 90% | 58% | 31%–104% | 16 | 118 |
| hf-whisper-large-v3-turbo-lora-e1__raw | suno01 | 16% | 12% | 6%–19% | 14 | 102 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-titanic-gawne | 42% | 42% | 33%–51% | 30 | 187 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-nightmares-gawne | 17% | 16% | 6%–27% | 15 | 100 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-animals-pt-i-jid | 24% | 25% | 15%–35% | 21 | 188 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-sk8-jid | 25% | 21% | 13%–31% | 15 | 129 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-behold-jid | 203% | 220% | 24%–726% | 20 | 183 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-never-me-token | 14% | 19% | 13%–24% | 19 | 167 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-the-ropes-token | 32% | 34% | 25%–43% | 32 | 188 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-kumquat-token | 19% | 20% | 12%–29% | 17 | 154 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-gta-6-joyner-lucas | 22% | 22% | 11%–35% | 13 | 148 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-one-of-them-joyner-lucas | 26% | 26% | 17%–36% | 20 | 161 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-monsters-joyner-lucas | 13% | 13% | 6%–21% | 15 | 138 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 15% | 15% | 10%–21% | 18 | 153 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-call-them-less-logic | 12% | 13% | 7%–20% | 15 | 136 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-give-me-a-reason-nf | 9% | 10% | 2%–18% | 8 | 138 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-bad-news-merkules | 23% | 25% | 16%–33% | 11 | 140 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-richards-tale-set-the-scene-ren | 26% | 27% | 15%–38% | 12 | 112 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-caught-you-in-the-bed-dax | 6% | 11% | 3%–14% | 11 | 126 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-crash-out-king-iso | 12% | 14% | 8%–20% | 12 | 121 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-raw-thoughts-vii-chris-webby | 3% | 3% | 0%–10% | 11 | 108 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-jealous-type-doja-cat | 33% | 40% | 21%–61% | 10 | 96 |
| hf-whisper-large-v3-turbo-lora-e2__raw | lose-yourself-v1 | 10% | 12% | 5%–20% | 16 | 143 |
| hf-whisper-large-v3-turbo-lora-e2__raw | the-way-i-am-v1 | 14% | 15% | 8%–22% | 15 | 138 |
| hf-whisper-large-v3-turbo-lora-e2__raw | speedom-em | 21% | 21% | 15%–27% | 22 | 220 |
| hf-whisper-large-v3-turbo-lora-e2__raw | worldwide-choppers-twista | 82% | 82% | 65%–95% | 18 | 176 |
| hf-whisper-large-v3-turbo-lora-e2__raw | rap-god-fast | 37% | 37% | 24%–52% | 11 | 108 |
| hf-whisper-large-v3-turbo-lora-e2__raw | godzilla-v3 | 30% | 29% | 19%–39% | 24 | 227 |
| hf-whisper-large-v3-turbo-lora-e2__raw | suno02 | 242% | 114% | 34%–300% | 16 | 118 |
| hf-whisper-large-v3-turbo-lora-e2__raw | suno01 | 14% | 10% | 4%–19% | 14 | 102 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-titanic-gawne | 45% | 45% | 37%–54% | 30 | 187 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-nightmares-gawne | 18% | 17% | 6%–28% | 15 | 100 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-animals-pt-i-jid | 27% | 28% | 18%–39% | 21 | 188 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-sk8-jid | 22% | 21% | 12%–34% | 15 | 129 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-behold-jid | 32% | 31% | 22%–41% | 20 | 182 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-never-me-token | 16% | 21% | 15%–26% | 19 | 167 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-the-ropes-token | 34% | 35% | 27%–45% | 32 | 188 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-kumquat-token | 19% | 20% | 10%–32% | 17 | 154 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-gta-6-joyner-lucas | 22% | 22% | 13%–33% | 13 | 148 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-one-of-them-joyner-lucas | 27% | 27% | 19%–37% | 20 | 161 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-monsters-joyner-lucas | 11% | 11% | 5%–18% | 15 | 138 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 16% | 16% | 10%–24% | 18 | 153 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-call-them-less-logic | 12% | 12% | 5%–21% | 15 | 136 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-give-me-a-reason-nf | 13% | 14% | 6%–23% | 8 | 138 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-bad-news-merkules | 27% | 30% | 19%–40% | 11 | 140 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-richards-tale-set-the-scene-ren | 22% | 23% | 13%–32% | 12 | 112 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-caught-you-in-the-bed-dax | 2% | 3% | 0%–5% | 11 | 126 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-crash-out-king-iso | 8% | 9% | 5%–14% | 12 | 121 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-raw-thoughts-vii-chris-webby | 5% | 5% | 0%–12% | 11 | 108 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-jealous-type-doja-cat | 40% | 46% | 26%–65% | 10 | 96 |
| hf-whisper-large-v3-turbo-lora-e3__raw | lose-yourself-v1 | 13% | 15% | 7%–22% | 16 | 143 |
| hf-whisper-large-v3-turbo-lora-e3__raw | the-way-i-am-v1 | 13% | 14% | 7%–21% | 15 | 138 |
| hf-whisper-large-v3-turbo-lora-e3__raw | speedom-em | 20% | 18% | 13%–24% | 22 | 220 |
| hf-whisper-large-v3-turbo-lora-e3__raw | worldwide-choppers-twista | 36% | 35% | 24%–48% | 19 | 183 |
| hf-whisper-large-v3-turbo-lora-e3__raw | rap-god-fast | 35% | 35% | 19%–51% | 11 | 108 |
| hf-whisper-large-v3-turbo-lora-e3__raw | godzilla-v3 | 100% | 104% | 33%–247% | 24 | 227 |
| hf-whisper-large-v3-turbo-lora-e3__raw | suno02 | 243% | 116% | 38%–302% | 16 | 118 |
| hf-whisper-large-v3-turbo-lora-e3__raw | suno01 | 12% | 9% | 4%–17% | 14 | 102 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-titanic-gawne | 46% | 46% | 36%–55% | 30 | 187 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-nightmares-gawne | 19% | 20% | 7%–32% | 15 | 100 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-animals-pt-i-jid | 27% | 28% | 18%–39% | 21 | 188 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-sk8-jid | 24% | 20% | 12%–30% | 15 | 129 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-behold-jid | 98% | 105% | 21%–309% | 20 | 182 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-never-me-token | 15% | 20% | 14%–25% | 19 | 167 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-the-ropes-token | 39% | 41% | 30%–54% | 32 | 188 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-kumquat-token | 17% | 18% | 8%–29% | 17 | 154 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-gta-6-joyner-lucas | 21% | 21% | 13%–32% | 13 | 148 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-one-of-them-joyner-lucas | 25% | 25% | 18%–33% | 20 | 161 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-monsters-joyner-lucas | 11% | 11% | 6%–16% | 15 | 138 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 18% | 18% | 12%–25% | 18 | 153 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-call-them-less-logic | 15% | 16% | 8%–23% | 15 | 136 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-give-me-a-reason-nf | 14% | 14% | 6%–24% | 8 | 138 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-bad-news-merkules | 29% | 31% | 21%–40% | 11 | 140 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-richards-tale-set-the-scene-ren | 23% | 24% | 11%–37% | 12 | 112 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-caught-you-in-the-bed-dax | 9% | 15% | 6%–20% | 11 | 126 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-crash-out-king-iso | 13% | 14% | 7%–22% | 12 | 121 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-raw-thoughts-vii-chris-webby | 3% | 3% | 0%–7% | 11 | 108 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-jealous-type-doja-cat | 36% | 43% | 25%–61% | 10 | 96 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | lose-yourself-v1 | 7% | 9% | 3%–12% | 16 | 143 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | the-way-i-am-v1 | 8% | 9% | 6%–14% | 15 | 138 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | speedom-em | 22% | 21% | 14%–28% | 22 | 220 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | worldwide-choppers-twista | 34% | 32% | 21%–44% | 19 | 183 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | rap-god-fast | 39% | 38% | 23%–53% | 11 | 108 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | godzilla-v3 | 51% | 51% | 36%–64% | 24 | 227 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | suno02 | 42% | 33% | 23%–45% | 16 | 118 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | suno01 | 15% | 12% | 5%–20% | 14 | 102 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-titanic-gawne | 52% | 51% | 41%–63% | 30 | 187 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-nightmares-gawne | 11% | 10% | 3%–16% | 15 | 100 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-animals-pt-i-jid | 21% | 23% | 15%–32% | 21 | 188 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-sk8-jid | 19% | 18% | 8%–33% | 15 | 129 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-behold-jid | 33% | 31% | 22%–42% | 20 | 183 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-never-me-token | 15% | 20% | 15%–25% | 19 | 167 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-the-ropes-token | 27% | 29% | 21%–37% | 32 | 188 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-kumquat-token | 16% | 17% | 9%–27% | 17 | 154 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-gta-6-joyner-lucas | 24% | 24% | 13%–37% | 13 | 148 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-one-of-them-joyner-lucas | 30% | 30% | 23%–38% | 20 | 161 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-monsters-joyner-lucas | 17% | 16% | 9%–23% | 15 | 138 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 20% | 19% | 13%–25% | 18 | 153 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-call-them-less-logic | 18% | 18% | 6%–33% | 15 | 136 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-give-me-a-reason-nf | 13% | 14% | 5%–26% | 8 | 138 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-bad-news-merkules | 23% | 24% | 16%–29% | 11 | 140 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-richards-tale-set-the-scene-ren | 26% | 27% | 14%–42% | 12 | 112 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-caught-you-in-the-bed-dax | 16% | 20% | 6%–36% | 11 | 126 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-crash-out-king-iso | 12% | 14% | 8%–20% | 12 | 121 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-raw-thoughts-vii-chris-webby | 4% | 4% | 0%–10% | 11 | 108 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-jealous-type-doja-cat | 36% | 43% | 22%–67% | 10 | 96 |
| openrouter-assemblyai-universal-3-6-pro__raw | lose-yourself-v1 | 7% | 9% | 3%–15% | 16 | 143 |
| openrouter-assemblyai-universal-3-6-pro__raw | the-way-i-am-v1 | 9% | 10% | 3%–19% | 15 | 138 |
| openrouter-assemblyai-universal-3-6-pro__raw | speedom-em | 27% | 26% | 19%–34% | 22 | 220 |
| openrouter-assemblyai-universal-3-6-pro__raw | worldwide-choppers-twista | 43% | 38% | 28%–52% | 19 | 183 |
| openrouter-assemblyai-universal-3-6-pro__raw | rap-god-fast | 39% | 38% | 20%–63% | 11 | 108 |
| openrouter-assemblyai-universal-3-6-pro__raw | godzilla-v3 | 31% | 30% | 23%–38% | 24 | 227 |
| openrouter-assemblyai-universal-3-6-pro__raw | suno02 | 44% | 40% | 30%–49% | 16 | 118 |
| openrouter-assemblyai-universal-3-6-pro__raw | suno01 | 15% | 12% | 5%–20% | 14 | 102 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-titanic-gawne | 59% | 59% | 47%–71% | 30 | 187 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-nightmares-gawne | 7% | 7% | 2%–13% | 15 | 100 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-animals-pt-i-jid | 26% | 27% | 19%–35% | 21 | 188 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-sk8-jid | 30% | 27% | 15%–42% | 15 | 129 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-behold-jid | 36% | 35% | 25%–46% | 20 | 183 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-never-me-token | 18% | 23% | 17%–29% | 19 | 167 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-the-ropes-token | 28% | 29% | 21%–38% | 32 | 188 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-kumquat-token | 14% | 15% | 8%–23% | 17 | 154 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-gta-6-joyner-lucas | 24% | 24% | 13%–37% | 13 | 148 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-one-of-them-joyner-lucas | 30% | 30% | 24%–36% | 20 | 161 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-monsters-joyner-lucas | 13% | 13% | 6%–19% | 15 | 138 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 21% | 20% | 15%–26% | 18 | 153 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-call-them-less-logic | 8% | 9% | 5%–12% | 15 | 136 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-give-me-a-reason-nf | 3% | 3% | 0%–7% | 8 | 138 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-bad-news-merkules | 17% | 19% | 11%–25% | 11 | 140 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-richards-tale-set-the-scene-ren | 21% | 23% | 12%–32% | 12 | 112 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-caught-you-in-the-bed-dax | 6% | 12% | 3%–16% | 11 | 126 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-crash-out-king-iso | 10% | 10% | 3%–19% | 12 | 121 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-raw-thoughts-vii-chris-webby | 2% | 2% | 0%–7% | 11 | 108 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-jealous-type-doja-cat | 21% | 27% | 11%–43% | 10 | 96 |
| openrouter-deepgram-nova-3__raw | lose-yourself-v1 | 9% | 11% | 5%–17% | 16 | 143 |
| openrouter-deepgram-nova-3__raw | the-way-i-am-v1 | 25% | 27% | 16%–41% | 15 | 138 |
| openrouter-deepgram-nova-3__raw | speedom-em | 78% | 77% | 63%–90% | 22 | 220 |
| openrouter-deepgram-nova-3__raw | worldwide-choppers-twista | 100% | 100% | 100%–100% | 18 | 176 |
| openrouter-deepgram-nova-3__raw | rap-god-fast | 90% | 90% | 75%–100% | 11 | 104 |
| openrouter-deepgram-nova-3__raw | godzilla-v3 | 98% | 98% | 93%–100% | 24 | 227 |
| openrouter-deepgram-nova-3__raw | suno02 | 82% | 80% | 62%–96% | 16 | 118 |
| openrouter-deepgram-nova-3__raw | suno01 | 72% | 72% | 51%–92% | 14 | 100 |
| openrouter-deepgram-nova-3__raw | fresh-titanic-gawne | 100% | 100% | 100%–100% | 30 | 187 |
| openrouter-deepgram-nova-3__raw | fresh-nightmares-gawne | 100% | 100% | 100%–100% | 15 | 100 |
| openrouter-deepgram-nova-3__raw | fresh-animals-pt-i-jid | 100% | 100% | 100%–100% | 21 | 188 |
| openrouter-deepgram-nova-3__raw | fresh-sk8-jid | 100% | 100% | 100%–100% | 15 | 129 |
| openrouter-deepgram-nova-3__raw | fresh-behold-jid | 82% | 82% | 68%–94% | 20 | 182 |
| openrouter-deepgram-nova-3__raw | fresh-never-me-token | 100% | 100% | 100%–100% | 19 | 167 |
| openrouter-deepgram-nova-3__raw | fresh-the-ropes-token | 100% | 100% | 100%–100% | 32 | 188 |
| openrouter-deepgram-nova-3__raw | fresh-kumquat-token | 99% | 99% | 98%–100% | 17 | 154 |
| openrouter-deepgram-nova-3__raw | fresh-gta-6-joyner-lucas | 100% | 100% | 100%–100% | 13 | 148 |
| openrouter-deepgram-nova-3__raw | fresh-one-of-them-joyner-lucas | 100% | 100% | 100%–100% | 20 | 161 |
| openrouter-deepgram-nova-3__raw | fresh-monsters-joyner-lucas | 14% | 14% | 8%–20% | 15 | 138 |
| openrouter-deepgram-nova-3__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 63% | 62% | 42%–81% | 18 | 153 |
| openrouter-deepgram-nova-3__raw | fresh-call-them-less-logic | 48% | 49% | 29%–72% | 15 | 136 |
| openrouter-deepgram-nova-3__raw | fresh-give-me-a-reason-nf | 14% | 14% | 5%–23% | 8 | 138 |
| openrouter-deepgram-nova-3__raw | fresh-bad-news-merkules | 26% | 28% | 20%–35% | 11 | 140 |
| openrouter-deepgram-nova-3__raw | fresh-richards-tale-set-the-scene-ren | 85% | 85% | 64%–100% | 12 | 112 |
| openrouter-deepgram-nova-3__raw | fresh-caught-you-in-the-bed-dax | 36% | 39% | 14%–65% | 11 | 126 |
| openrouter-deepgram-nova-3__raw | fresh-crash-out-king-iso | 15% | 16% | 7%–25% | 12 | 121 |
| openrouter-deepgram-nova-3__raw | fresh-raw-thoughts-vii-chris-webby | 7% | 9% | 2%–16% | 11 | 108 |
| openrouter-deepgram-nova-3__raw | fresh-jealous-type-doja-cat | 100% | 100% | 100%–100% | 10 | 96 |
| openrouter-elevenlabs-scribe-v2__raw | lose-yourself-v1 | 1% | 1% | 0%–2% | 16 | 143 |
| openrouter-elevenlabs-scribe-v2__raw | the-way-i-am-v1 | 2% | 3% | 0%–6% | 15 | 138 |
| openrouter-elevenlabs-scribe-v2__raw | speedom-em | 24% | 23% | 14%–32% | 22 | 220 |
| openrouter-elevenlabs-scribe-v2__raw | worldwide-choppers-twista | 21% | 21% | 12%–32% | 19 | 183 |
| openrouter-elevenlabs-scribe-v2__raw | rap-god-fast | 10% | 9% | 3%–19% | 11 | 104 |
| openrouter-elevenlabs-scribe-v2__raw | godzilla-v3 | 9% | 10% | 4%–16% | 24 | 227 |
| openrouter-elevenlabs-scribe-v2__raw | suno02 | 36% | 30% | 17%–44% | 16 | 118 |
| openrouter-elevenlabs-scribe-v2__raw | suno01 | 11% | 8% | 3%–14% | 14 | 102 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-titanic-gawne | 47% | 46% | 37%–56% | 30 | 187 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-nightmares-gawne | 11% | 10% | 4%–18% | 16 | 102 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-animals-pt-i-jid | 17% | 18% | 8%–30% | 21 | 188 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-sk8-jid | 21% | 17% | 9%–26% | 15 | 129 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-behold-jid | 30% | 29% | 21%–38% | 20 | 183 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-never-me-token | 13% | 17% | 12%–23% | 19 | 167 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-the-ropes-token | 26% | 27% | 20%–35% | 32 | 188 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-kumquat-token | 10% | 11% | 4%–19% | 17 | 154 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-gta-6-joyner-lucas | 22% | 22% | 13%–34% | 13 | 148 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-one-of-them-joyner-lucas | 14% | 13% | 7%–20% | 20 | 161 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-monsters-joyner-lucas | 10% | 11% | 4%–17% | 15 | 138 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 23% | 22% | 15%–30% | 18 | 153 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-call-them-less-logic | 3% | 3% | 0%–6% | 16 | 137 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-give-me-a-reason-nf | 4% | 4% | 0%–11% | 8 | 138 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-bad-news-merkules | 18% | 19% | 12%–26% | 11 | 140 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-richards-tale-set-the-scene-ren | 12% | 14% | 7%–20% | 12 | 112 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-caught-you-in-the-bed-dax | 2% | 7% | 0%–8% | 11 | 126 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-crash-out-king-iso | 12% | 12% | 3%–23% | 12 | 121 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-raw-thoughts-vii-chris-webby | 3% | 3% | 0%–10% | 11 | 108 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-jealous-type-doja-cat | 20% | 24% | 7%–46% | 10 | 96 |
| openrouter-google-chirp-3__raw | lose-yourself-v1 | 4% | 5% | 1%–10% | 16 | 143 |
| openrouter-google-chirp-3__raw | the-way-i-am-v1 | 12% | 14% | 8%–21% | 15 | 138 |
| openrouter-google-chirp-3__raw | speedom-em | 31% | 31% | 22%–40% | 22 | 220 |
| openrouter-google-chirp-3__raw | worldwide-choppers-twista | 41% | 35% | 27%–46% | 18 | 176 |
| openrouter-google-chirp-3__raw | rap-god-fast | 41% | 41% | 23%–60% | 11 | 108 |
| openrouter-google-chirp-3__raw | godzilla-v3 | 99% | 99% | 95%–100% | 24 | 227 |
| openrouter-google-chirp-3__raw | suno02 | 81% | 79% | 60%–94% | 16 | 118 |
| openrouter-google-chirp-3__raw | suno01 | 25% | 22% | 11%–39% | 14 | 102 |
| openrouter-google-chirp-3__raw | fresh-titanic-gawne | 100% | 100% | 100%–100% | 30 | 187 |
| openrouter-google-chirp-3__raw | fresh-nightmares-gawne | 10% | 11% | 5%–17% | 15 | 100 |
| openrouter-google-chirp-3__raw | fresh-animals-pt-i-jid | 35% | 36% | 26%–47% | 21 | 188 |
| openrouter-google-chirp-3__raw | fresh-sk8-jid | 33% | 29% | 18%–42% | 15 | 129 |
| openrouter-google-chirp-3__raw | fresh-behold-jid | 40% | 38% | 29%–48% | 20 | 182 |
| openrouter-google-chirp-3__raw | fresh-never-me-token | 19% | 24% | 16%–31% | 19 | 167 |
| openrouter-google-chirp-3__raw | fresh-the-ropes-token | 100% | 100% | 100%–100% | 32 | 188 |
| openrouter-google-chirp-3__raw | fresh-kumquat-token | 21% | 22% | 12%–34% | 17 | 154 |
| openrouter-google-chirp-3__raw | fresh-gta-6-joyner-lucas | 39% | 39% | 24%–57% | 13 | 148 |
| openrouter-google-chirp-3__raw | fresh-one-of-them-joyner-lucas | 100% | 100% | 100%–100% | 20 | 161 |
| openrouter-google-chirp-3__raw | fresh-monsters-joyner-lucas | 23% | 23% | 13%–35% | 15 | 138 |
| openrouter-google-chirp-3__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 44% | 43% | 30%–58% | 18 | 153 |
| openrouter-google-chirp-3__raw | fresh-call-them-less-logic | 11% | 11% | 8%–15% | 15 | 136 |
| openrouter-google-chirp-3__raw | fresh-give-me-a-reason-nf | 25% | 27% | 11%–48% | 8 | 138 |
| openrouter-google-chirp-3__raw | fresh-bad-news-merkules | 19% | 20% | 13%–26% | 11 | 140 |
| openrouter-google-chirp-3__raw | fresh-richards-tale-set-the-scene-ren | 40% | 39% | 23%–55% | 12 | 112 |
| openrouter-google-chirp-3__raw | fresh-caught-you-in-the-bed-dax | 7% | 13% | 4%–17% | 11 | 126 |
| openrouter-google-chirp-3__raw | fresh-crash-out-king-iso | 11% | 12% | 3%–22% | 12 | 121 |
| openrouter-google-chirp-3__raw | fresh-raw-thoughts-vii-chris-webby | 3% | 2% | 0%–5% | 11 | 108 |
| openrouter-google-chirp-3__raw | fresh-jealous-type-doja-cat | 31% | 33% | 13%–58% | 10 | 96 |
| openrouter-google-gemini-3.5-transcribe__raw | lose-yourself-v1 | 5% | 7% | 2%–11% | 16 | 143 |
| openrouter-google-gemini-3.5-transcribe__raw | the-way-i-am-v1 | 8% | 9% | 3%–17% | 15 | 138 |
| openrouter-google-gemini-3.5-transcribe__raw | speedom-em | 27% | 26% | 17%–36% | 22 | 220 |
| openrouter-google-gemini-3.5-transcribe__raw | worldwide-choppers-twista | 100% | 100% | 100%–100% | 18 | 176 |
| openrouter-google-gemini-3.5-transcribe__raw | rap-god-fast | 91% | 91% | 77%–100% | 11 | 104 |
| openrouter-google-gemini-3.5-transcribe__raw | godzilla-v3 | 98% | 98% | 93%–100% | 24 | 227 |
| openrouter-google-gemini-3.5-transcribe__raw | suno02 | 85% | 85% | 67%–99% | 16 | 118 |
| openrouter-google-gemini-3.5-transcribe__raw | suno01 | 100% | 100% | 100%–100% | 14 | 100 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-titanic-gawne | 100% | 100% | 100%–100% | 30 | 187 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-nightmares-gawne | 10% | 12% | 3%–22% | 15 | 100 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-animals-pt-i-jid | 100% | 100% | 100%–100% | 21 | 188 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-sk8-jid | 26% | 22% | 12%–35% | 15 | 129 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-behold-jid | 100% | 100% | 100%–100% | 20 | 182 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-never-me-token | 100% | 100% | 100%–100% | 19 | 167 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-the-ropes-token | 100% | 100% | 100%–100% | 32 | 188 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-kumquat-token | 13% | 14% | 8%–20% | 17 | 154 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-gta-6-joyner-lucas | 100% | 100% | 100%–100% | 13 | 148 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-one-of-them-joyner-lucas | 100% | 100% | 100%–100% | 20 | 161 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-monsters-joyner-lucas | 16% | 16% | 9%–24% | 15 | 138 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 27% | 26% | 18%–34% | 18 | 153 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-call-them-less-logic | 12% | 12% | 8%–17% | 15 | 136 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-give-me-a-reason-nf | 9% | 9% | 3%–16% | 8 | 138 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-bad-news-merkules | 19% | 21% | 13%–27% | 11 | 140 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-richards-tale-set-the-scene-ren | 18% | 19% | 11%–29% | 12 | 112 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-caught-you-in-the-bed-dax | 7% | 13% | 4%–17% | 11 | 126 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-crash-out-king-iso | 12% | 13% | 3%–25% | 12 | 121 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-raw-thoughts-vii-chris-webby | 4% | 3% | 0%–8% | 11 | 108 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-jealous-type-doja-cat | 100% | 100% | 100%–100% | 10 | 96 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | lose-yourself-v1 | 8% | 9% | 3%–14% | 16 | 143 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | the-way-i-am-v1 | 11% | 12% | 5%–21% | 15 | 138 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | speedom-em | 26% | 25% | 19%–32% | 22 | 220 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | worldwide-choppers-twista | 36% | 30% | 24%–39% | 18 | 176 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | rap-god-fast | 88% | 88% | 70%–100% | 11 | 104 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | godzilla-v3 | 30% | 30% | 22%–39% | 24 | 227 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | suno02 | 58% | 50% | 37%–66% | 16 | 118 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | suno01 | 16% | 13% | 6%–23% | 14 | 102 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-titanic-gawne | 95% | 95% | 90%–99% | 30 | 187 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-nightmares-gawne | 9% | 8% | 2%–16% | 15 | 100 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-animals-pt-i-jid | 23% | 25% | 17%–33% | 21 | 188 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-sk8-jid | 22% | 20% | 12%–31% | 15 | 129 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-behold-jid | 28% | 27% | 17%–39% | 20 | 182 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-never-me-token | 17% | 22% | 16%–28% | 19 | 167 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-the-ropes-token | 51% | 52% | 38%–66% | 32 | 188 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-kumquat-token | 14% | 15% | 8%–24% | 17 | 154 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-gta-6-joyner-lucas | 24% | 24% | 14%–35% | 13 | 148 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-one-of-them-joyner-lucas | 33% | 33% | 25%–41% | 20 | 161 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-monsters-joyner-lucas | 12% | 13% | 6%–19% | 15 | 138 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 21% | 20% | 14%–27% | 18 | 153 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-call-them-less-logic | 10% | 10% | 5%–16% | 15 | 136 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-give-me-a-reason-nf | 7% | 7% | 2%–13% | 8 | 138 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-bad-news-merkules | 19% | 21% | 13%–27% | 11 | 140 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-richards-tale-set-the-scene-ren | 12% | 14% | 7%–21% | 12 | 112 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-caught-you-in-the-bed-dax | 6% | 12% | 3%–15% | 11 | 126 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-crash-out-king-iso | 8% | 9% | 3%–15% | 12 | 121 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-raw-thoughts-vii-chris-webby | 1% | 1% | 0%–4% | 11 | 108 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-jealous-type-doja-cat | 26% | 33% | 14%–51% | 10 | 96 |
| openrouter-openai-gpt-4o-transcribe__raw | lose-yourself-v1 | 3% | 5% | 1%–8% | 16 | 143 |
| openrouter-openai-gpt-4o-transcribe__raw | the-way-i-am-v1 | 3% | 4% | 0%–7% | 15 | 138 |
| openrouter-openai-gpt-4o-transcribe__raw | speedom-em | 27% | 26% | 19%–35% | 22 | 220 |
| openrouter-openai-gpt-4o-transcribe__raw | worldwide-choppers-twista | 25% | 25% | 14%–38% | 19 | 183 |
| openrouter-openai-gpt-4o-transcribe__raw | rap-god-fast | 94% | 94% | 80%–100% | 11 | 104 |
| openrouter-openai-gpt-4o-transcribe__raw | godzilla-v3 | 19% | 19% | 15%–24% | 24 | 227 |
| openrouter-openai-gpt-4o-transcribe__raw | suno02 | 47% | 41% | 29%–53% | 16 | 118 |
| openrouter-openai-gpt-4o-transcribe__raw | suno01 | 11% | 7% | 2%–13% | 14 | 102 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-titanic-gawne | 97% | 97% | 93%–100% | 30 | 187 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-nightmares-gawne | 14% | 13% | 3%–23% | 15 | 100 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-animals-pt-i-jid | 32% | 34% | 22%–46% | 21 | 188 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-sk8-jid | 31% | 28% | 18%–41% | 15 | 129 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-behold-jid | 26% | 25% | 17%–35% | 20 | 183 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-never-me-token | 14% | 20% | 12%–27% | 19 | 167 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-the-ropes-token | 29% | 31% | 21%–43% | 32 | 188 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-kumquat-token | 15% | 16% | 9%–23% | 17 | 154 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-gta-6-joyner-lucas | 91% | 90% | 74%–100% | 13 | 148 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-one-of-them-joyner-lucas | 94% | 94% | 84%–100% | 20 | 161 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-monsters-joyner-lucas | 14% | 14% | 7%–21% | 15 | 138 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 93% | 93% | 81%–100% | 18 | 153 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-call-them-less-logic | 13% | 14% | 9%–21% | 15 | 136 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-give-me-a-reason-nf | 4% | 4% | 1%–9% | 8 | 138 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-bad-news-merkules | 21% | 22% | 14%–29% | 11 | 140 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-richards-tale-set-the-scene-ren | 17% | 18% | 9%–26% | 12 | 112 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-caught-you-in-the-bed-dax | 6% | 11% | 2%–16% | 11 | 126 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-crash-out-king-iso | 9% | 9% | 3%–18% | 12 | 121 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-raw-thoughts-vii-chris-webby | 3% | 3% | 0%–10% | 11 | 108 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-jealous-type-doja-cat | 85% | 88% | 70%–100% | 10 | 96 |
| openrouter-openai-gpt-transcribe__raw | lose-yourself-v1 | 3% | 3% | 0%–6% | 16 | 143 |
| openrouter-openai-gpt-transcribe__raw | the-way-i-am-v1 | 7% | 8% | 3%–13% | 15 | 138 |
| openrouter-openai-gpt-transcribe__raw | speedom-em | 31% | 30% | 23%–39% | 22 | 220 |
| openrouter-openai-gpt-transcribe__raw | worldwide-choppers-twista | 34% | 30% | 21%–41% | 18 | 176 |
| openrouter-openai-gpt-transcribe__raw | rap-god-fast | 14% | 14% | 7%–23% | 11 | 104 |
| openrouter-openai-gpt-transcribe__raw | godzilla-v3 | 15% | 15% | 9%–21% | 24 | 227 |
| openrouter-openai-gpt-transcribe__raw | suno02 | 49% | 46% | 32%–59% | 16 | 118 |
| openrouter-openai-gpt-transcribe__raw | suno01 | 17% | 16% | 7%–28% | 14 | 102 |
| openrouter-openai-gpt-transcribe__raw | fresh-titanic-gawne | 60% | 59% | 50%–69% | 30 | 187 |
| openrouter-openai-gpt-transcribe__raw | fresh-nightmares-gawne | 13% | 13% | 6%–22% | 15 | 100 |
| openrouter-openai-gpt-transcribe__raw | fresh-animals-pt-i-jid | 27% | 29% | 18%–40% | 21 | 188 |
| openrouter-openai-gpt-transcribe__raw | fresh-sk8-jid | 29% | 26% | 14%–39% | 15 | 129 |
| openrouter-openai-gpt-transcribe__raw | fresh-behold-jid | 32% | 30% | 20%–42% | 20 | 182 |
| openrouter-openai-gpt-transcribe__raw | fresh-never-me-token | 17% | 21% | 15%–28% | 19 | 167 |
| openrouter-openai-gpt-transcribe__raw | fresh-the-ropes-token | 31% | 32% | 23%–41% | 32 | 188 |
| openrouter-openai-gpt-transcribe__raw | fresh-kumquat-token | 18% | 19% | 9%–29% | 17 | 154 |
| openrouter-openai-gpt-transcribe__raw | fresh-gta-6-joyner-lucas | 32% | 32% | 19%–48% | 13 | 148 |
| openrouter-openai-gpt-transcribe__raw | fresh-one-of-them-joyner-lucas | 22% | 22% | 13%–33% | 20 | 161 |
| openrouter-openai-gpt-transcribe__raw | fresh-monsters-joyner-lucas | 9% | 7% | 3%–13% | 15 | 138 |
| openrouter-openai-gpt-transcribe__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 25% | 25% | 17%–32% | 18 | 153 |
| openrouter-openai-gpt-transcribe__raw | fresh-call-them-less-logic | 10% | 10% | 4%–17% | 15 | 136 |
| openrouter-openai-gpt-transcribe__raw | fresh-give-me-a-reason-nf | 7% | 7% | 1%–12% | 8 | 138 |
| openrouter-openai-gpt-transcribe__raw | fresh-bad-news-merkules | 21% | 22% | 14%–28% | 11 | 140 |
| openrouter-openai-gpt-transcribe__raw | fresh-richards-tale-set-the-scene-ren | 27% | 28% | 18%–38% | 12 | 112 |
| openrouter-openai-gpt-transcribe__raw | fresh-caught-you-in-the-bed-dax | 4% | 10% | 2%–13% | 11 | 126 |
| openrouter-openai-gpt-transcribe__raw | fresh-crash-out-king-iso | 10% | 10% | 3%–20% | 12 | 121 |
| openrouter-openai-gpt-transcribe__raw | fresh-raw-thoughts-vii-chris-webby | 3% | 3% | 0%–8% | 11 | 108 |
| openrouter-openai-gpt-transcribe__raw | fresh-jealous-type-doja-cat | 32% | 38% | 17%–60% | 10 | 96 |
| openrouter-x-ai-grok-stt-2.0__raw | lose-yourself-v1 | 13% | 14% | 6%–21% | 16 | 143 |
| openrouter-x-ai-grok-stt-2.0__raw | the-way-i-am-v1 | 11% | 13% | 8%–19% | 15 | 138 |
| openrouter-x-ai-grok-stt-2.0__raw | speedom-em | 28% | 26% | 20%–33% | 22 | 220 |
| openrouter-x-ai-grok-stt-2.0__raw | worldwide-choppers-twista | 23% | 22% | 14%–33% | 18 | 176 |
| openrouter-x-ai-grok-stt-2.0__raw | rap-god-fast | 89% | 89% | 72%–100% | 11 | 104 |
| openrouter-x-ai-grok-stt-2.0__raw | godzilla-v3 | 36% | 36% | 26%–47% | 24 | 227 |
| openrouter-x-ai-grok-stt-2.0__raw | suno02 | 52% | 44% | 33%–57% | 16 | 118 |
| openrouter-x-ai-grok-stt-2.0__raw | suno01 | 16% | 12% | 4%–23% | 14 | 102 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-titanic-gawne | 55% | 55% | 44%–66% | 30 | 187 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-nightmares-gawne | 9% | 8% | 3%–15% | 15 | 100 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-animals-pt-i-jid | 29% | 31% | 21%–43% | 21 | 188 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-sk8-jid | 31% | 27% | 19%–39% | 15 | 129 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-behold-jid | 36% | 35% | 23%–47% | 20 | 182 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-never-me-token | 13% | 17% | 13%–22% | 19 | 167 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-the-ropes-token | 38% | 40% | 31%–50% | 32 | 188 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-kumquat-token | 17% | 18% | 8%–29% | 17 | 154 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-gta-6-joyner-lucas | 26% | 26% | 15%–38% | 13 | 148 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-one-of-them-joyner-lucas | 29% | 29% | 20%–37% | 20 | 161 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-monsters-joyner-lucas | 14% | 14% | 8%–21% | 15 | 138 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 26% | 25% | 18%–32% | 18 | 153 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-call-them-less-logic | 10% | 10% | 7%–13% | 15 | 136 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-give-me-a-reason-nf | 6% | 6% | 1%–12% | 8 | 138 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-bad-news-merkules | 20% | 21% | 14%–27% | 11 | 140 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-richards-tale-set-the-scene-ren | 23% | 25% | 14%–36% | 12 | 112 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-caught-you-in-the-bed-dax | 9% | 15% | 4%–22% | 11 | 126 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-crash-out-king-iso | 12% | 13% | 6%–21% | 12 | 121 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-raw-thoughts-vii-chris-webby | 3% | 3% | 0%–6% | 11 | 108 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-jealous-type-doja-cat | 33% | 39% | 19%–61% | 10 | 96 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | lose-yourself-v1 | 11% | 14% | 7%–19% | 16 | 143 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | the-way-i-am-v1 | 16% | 18% | 11%–26% | 15 | 138 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | speedom-em | 33% | 31% | 24%–39% | 22 | 220 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | worldwide-choppers-twista | 52% | 48% | 30%–77% | 18 | 176 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | rap-god-fast | 26% | 25% | 13%–38% | 11 | 104 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | godzilla-v3 | 40% | 40% | 30%–50% | 24 | 227 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | suno02 | 55% | 45% | 36%–55% | 16 | 118 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | suno01 | 12% | 11% | 4%–20% | 14 | 100 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-titanic-gawne | 70% | 70% | 60%–78% | 30 | 187 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-nightmares-gawne | 12% | 14% | 8%–20% | 15 | 100 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-animals-pt-i-jid | 31% | 33% | 25%–43% | 21 | 188 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-sk8-jid | 35% | 32% | 20%–45% | 15 | 129 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-behold-jid | 35% | 34% | 25%–44% | 20 | 182 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-never-me-token | 25% | 30% | 22%–37% | 19 | 167 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-the-ropes-token | 55% | 56% | 46%–66% | 32 | 188 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-kumquat-token | 23% | 24% | 14%–37% | 17 | 154 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-gta-6-joyner-lucas | 28% | 28% | 19%–39% | 13 | 148 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-one-of-them-joyner-lucas | 30% | 30% | 21%–40% | 20 | 161 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-monsters-joyner-lucas | 16% | 17% | 9%–26% | 15 | 138 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 24% | 23% | 17%–29% | 18 | 153 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-call-them-less-logic | 12% | 13% | 6%–21% | 15 | 136 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-give-me-a-reason-nf | 9% | 10% | 1%–21% | 8 | 138 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-bad-news-merkules | 21% | 23% | 15%–31% | 11 | 140 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-richards-tale-set-the-scene-ren | 31% | 33% | 23%–41% | 12 | 112 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-caught-you-in-the-bed-dax | 6% | 12% | 3%–16% | 11 | 126 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-crash-out-king-iso | 12% | 13% | 6%–21% | 12 | 121 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-raw-thoughts-vii-chris-webby | 5% | 4% | 0%–13% | 11 | 108 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-jealous-type-doja-cat | 31% | 38% | 19%–56% | 10 | 96 |
