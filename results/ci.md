# rap-bench confidence intervals

Cluster bootstrap over lyric lines, 2000 replicates, seed 0, rates: listed; vocabulary adjustment: none; 95% percentile intervals. Written by `scripts/bootstrap_ci.py`; see its docstring for the design.

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
| faster-whisper-distil-large-v3__raw | exhibition | 8.0 | 7.3–9.6 | 8.0 | 7.1–9.6 | 5.5–9.0 | 0% |
| faster-whisper-distil-large-v3__raw | core | 5.6 | 4.9–6.1 | 5.6 | 4.9–6.1 | 4.9–8.4 | 5% |
| faster-whisper-distil-large-v3__raw | fresh | 6.9 | 5.9–7.0 | <4.4 | 4.4–6.2 | censored | 78% |
| faster-whisper-distil-large-v3__raw | **delta** (exhibition − core) | +2.5 | +1.5 to +4.3 | +2.5 | +1.4 to +4.2 | | |
| faster-whisper-distil-large-v3__raw | **delta** (exhibition − fresh) | +1.1 | +0.5 to +3.3 |  |  | | |
| faster-whisper-distil-large-v3__raw | **delta** (fresh − core) | +1.4 | +0.1 to +2.0 |  |  | | |
| faster-whisper-large-v3__raw | exhibition | 10.1 | 8.4–10.6 | 9.2 | 7.8–10.6 | 9.0–9.6 | 8% |
| faster-whisper-large-v3__raw | core | 6.2 | 5.7–6.9 | 6.2 | 5.7–6.9 | 4.9–8.4 | 0% |
| faster-whisper-large-v3__raw | fresh | 8.7 | 7.4–8.9 | <4.4 | 4.4–7.2 | censored | 49% |
| faster-whisper-large-v3__raw | **delta** (exhibition − core) | +3.9 | +2.0 to +4.8 | +3.0 | +1.5 to +4.6 | | |
| faster-whisper-large-v3__raw | **delta** (exhibition − fresh) | +1.4 | -0.3 to +2.8 |  |  | | |
| faster-whisper-large-v3__raw | **delta** (fresh − core) | +2.5 | +1.1 to +3.0 |  |  | | |
| faster-whisper-large-v3__vocals | exhibition | 9.8 | 8.3–10.6 | 9.7 | 7.4–10.6 | 9.6–10.0 | 4% |
| faster-whisper-small__raw | exhibition | 7.5 | 6.7–9.4 | 7.5 | 6.5–9.2 | 5.5–9.0 | 0% |
| faster-whisper-small__raw | core | 4.9 | 4.9–5.7 | 4.9 | 4.9–5.7 | 4.9–8.4 | 47% |
| faster-whisper-small__raw | fresh | 5.7 | 5.7–7.1 | <4.4 | 4.4–5.7 | censored | 60% |
| faster-whisper-small__raw | **delta** (exhibition − core) | +2.6 | +1.4 to +4.3 | +2.6 | +1.3 to +4.2 | | |
| faster-whisper-small__raw | **delta** (exhibition − fresh) | +1.8 | +0.3 to +3.6 |  |  | | |
| faster-whisper-small__raw | **delta** (fresh − core) | +0.8 | +0.1 to +2.1 |  |  | | |
| faster-whisper-tiny__raw | exhibition | <5.5 | 5.5–5.5 | <5.5 | 5.5–5.5 | censored | 100% |
| faster-whisper-tiny__raw | core | <4.9 | 4.9–4.9 | <4.9 | 4.9–4.9 | censored | 100% |
| faster-whisper-tiny__raw | fresh | <4.4 | 4.4–4.4 | <4.4 | 4.4–4.4 | censored | 100% |
| faster-whisper-tiny__vocals | exhibition | <5.5 | 5.5–5.5 | <5.5 | 5.5–5.5 | censored | 100% |
| faster-whisper-turbo__raw | exhibition | 9.1 | 8.5–9.2 | 9.0 | 8.5–9.1 | 9.0–9.6 | 0% |
| faster-whisper-turbo__raw | core | 6.1 | 5.1–7.4 | 6.1 | 5.1–7.4 | 4.9–8.4 | 2% |
| faster-whisper-turbo__raw | fresh | 8.5 | 4.4–8.7 | <4.4 | 4.4–6.1 | censored | 76% |
| faster-whisper-turbo__raw | **delta** (exhibition − core) | +3.0 | +1.6 to +4.0 | +2.9 | +1.6 to +3.9 | | |
| faster-whisper-turbo__raw | **delta** (exhibition − fresh) | +0.6 | +0.1 to +4.7 |  |  | | |
| faster-whisper-turbo__raw | **delta** (fresh − core) | +2.3 | -2.2 to +3.2 |  |  | | |
| hf-UsefulSensors-moonshine-base__raw | exhibition | <5.5 | 5.5–6.2 | <5.5 | 5.5–5.9 | censored | 78% |
| hf-UsefulSensors-moonshine-base__raw | core | <4.9 | 4.9–4.9 | <4.9 | 4.9–4.9 | censored | 99% |
| hf-UsefulSensors-moonshine-base__raw | fresh | <4.4 | 4.4–5.8 | <4.4 | 4.4–4.6 | censored | 93% |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | exhibition | <5.5 | 5.5–5.5 | <5.5 | 5.5–5.5 | censored | 100% |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | core | <4.9 | 4.9–4.9 | <4.9 | 4.9–4.9 | censored | 100% |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh | <4.4 | 4.4–4.4 | <4.4 | 4.4–4.4 | censored | 100% |
| hf-whisper-large-v3-turbo-base__raw | exhibition | 9.1 | 8.2–9.6 | 9.1 | 8.1–9.6 | 9.0–9.6 | 0% |
| hf-whisper-large-v3-turbo-base__raw | core | 6.2 | 5.5–7.1 | 6.2 | 5.5–7.1 | 4.9–8.4 | 0% |
| hf-whisper-large-v3-turbo-base__raw | fresh | 8.3 | 7.2–8.7 | <4.4 | 4.4–6.4 | censored | 76% |
| hf-whisper-large-v3-turbo-base__raw | **delta** (exhibition − core) | +2.9 | +1.8 to +3.8 | +2.9 | +1.7 to +3.8 | | |
| hf-whisper-large-v3-turbo-base__raw | **delta** (exhibition − fresh) | +0.9 | -0.1 to +2.1 |  |  | | |
| hf-whisper-large-v3-turbo-base__raw | **delta** (fresh − core) | +2.1 | +0.7 to +2.9 |  |  | | |
| hf-whisper-large-v3-turbo-guard-base__raw | exhibition | 9.1 | 8.2–9.7 | 9.1 | 8.1–9.7 | 9.0–9.6 | 0% |
| hf-whisper-large-v3-turbo-guard-base__raw | core | 6.2 | 5.5–7.1 | 6.2 | 5.5–7.1 | 4.9–8.4 | 0% |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh | 8.3 | 7.2–8.7 | <4.4 | 4.4–6.4 | censored | 76% |
| hf-whisper-large-v3-turbo-guard-base__raw | **delta** (exhibition − core) | +2.9 | +1.8 to +3.9 | +2.9 | +1.7 to +3.8 | | |
| hf-whisper-large-v3-turbo-guard-base__raw | **delta** (exhibition − fresh) | +0.9 | -0.1 to +2.1 |  |  | | |
| hf-whisper-large-v3-turbo-guard-base__raw | **delta** (fresh − core) | +2.1 | +0.7 to +2.9 |  |  | | |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | exhibition | 9.2 | 8.4–9.7 | 9.2 | 8.3–9.7 | 9.0–9.6 | 0% |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | core | 5.9 | 5.0–6.8 | 5.9 | 5.0–6.8 | 4.9–8.4 | 2% |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh | 8.5 | 6.9–8.9 | <4.4 | 4.4–6.3 | censored | 77% |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | **delta** (exhibition − core) | +3.2 | +2.1 to +4.3 | +3.2 | +2.0 to +4.3 | | |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | **delta** (exhibition − fresh) | +0.7 | -0.1 to +2.4 |  |  | | |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | **delta** (fresh − core) | +2.6 | +0.8 to +3.5 |  |  | | |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | exhibition | 9.1 | 8.3–9.6 | 9.1 | 8.3–9.6 | 9.0–9.6 | 0% |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | core | 5.9 | 5.0–6.5 | 5.9 | 5.0–6.5 | 4.9–8.4 | 2% |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh | 8.2 | 6.9–8.7 | <4.4 | 4.4–6.0 | censored | 91% |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | **delta** (exhibition − core) | +3.3 | +2.3 to +4.2 | +3.3 | +2.3 to +4.2 | | |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | **delta** (exhibition − fresh) | +0.9 | +0.2 to +2.4 |  |  | | |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | **delta** (fresh − core) | +2.3 | +0.7 to +3.3 |  |  | | |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | exhibition | 9.2 | 8.6–9.8 | 9.2 | 8.6–9.7 | 9.0–9.6 | 0% |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | core | 6.0 | 5.5–6.5 | 6.0 | 5.5–6.5 | 4.9–8.4 | 0% |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh | 7.4 | 6.9–8.7 | <4.4 | 4.4–6.0 | censored | 88% |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | **delta** (exhibition − core) | +3.2 | +2.5 to +4.0 | +3.2 | +2.4 to +4.0 | | |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | **delta** (exhibition − fresh) | +1.8 | +0.5 to +2.5 |  |  | | |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | **delta** (fresh − core) | +1.4 | +0.7 to +2.9 |  |  | | |
| hf-whisper-large-v3-turbo-lora-e1__raw | exhibition | 9.2 | 8.4–9.7 | 9.2 | 8.3–9.6 | 9.0–9.6 | 0% |
| hf-whisper-large-v3-turbo-lora-e1__raw | core | 5.3 | 4.9–6.7 | 5.3 | 4.9–6.7 | 4.9–8.4 | 2% |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh | 6.3 | 5.8–8.8 | <4.4 | 4.4–6.3 | censored | 77% |
| hf-whisper-large-v3-turbo-lora-e1__raw | **delta** (exhibition − core) | +3.8 | +2.3 to +4.6 | +3.8 | +2.2 to +4.5 | | |
| hf-whisper-large-v3-turbo-lora-e1__raw | **delta** (exhibition − fresh) | +2.9 | +0.1 to +3.6 |  |  | | |
| hf-whisper-large-v3-turbo-lora-e1__raw | **delta** (fresh − core) | +1.0 | -0.4 to +3.6 |  |  | | |
| hf-whisper-large-v3-turbo-lora-e2__raw | exhibition | 9.1 | 8.2–9.6 | 9.1 | 8.2–9.6 | 9.0–9.6 | 0% |
| hf-whisper-large-v3-turbo-lora-e2__raw | core | 5.1 | 4.9–6.4 | 5.1 | 4.9–6.4 | 4.9–8.4 | 2% |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh | 8.2 | 6.9–8.7 | <4.4 | 4.4–6.0 | censored | 91% |
| hf-whisper-large-v3-turbo-lora-e2__raw | **delta** (exhibition − core) | +4.1 | +2.4 to +4.5 | +4.1 | +2.4 to +4.5 | | |
| hf-whisper-large-v3-turbo-lora-e2__raw | **delta** (exhibition − fresh) | +0.9 | +0.0 to +2.4 |  |  | | |
| hf-whisper-large-v3-turbo-lora-e2__raw | **delta** (fresh − core) | +3.1 | +0.9 to +3.6 |  |  | | |
| hf-whisper-large-v3-turbo-lora-e3__raw | exhibition | 9.2 | 8.6–9.7 | 9.2 | 8.6–9.7 | 9.0–9.6 | 0% |
| hf-whisper-large-v3-turbo-lora-e3__raw | core | 5.1 | 5.0–6.4 | 5.1 | 5.0–6.4 | 4.9–8.4 | 0% |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh | 6.3 | 5.8–8.6 | <4.4 | 4.4–6.0 | censored | 88% |
| hf-whisper-large-v3-turbo-lora-e3__raw | **delta** (exhibition − core) | +4.1 | +2.7 to +4.7 | +4.1 | +2.7 to +4.7 | | |
| hf-whisper-large-v3-turbo-lora-e3__raw | **delta** (exhibition − fresh) | +2.9 | +0.6 to +3.7 |  |  | | |
| hf-whisper-large-v3-turbo-lora-e3__raw | **delta** (fresh − core) | +1.2 | -0.3 to +3.5 |  |  | | |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | exhibition | 9.1 | 8.2–9.6 | 9.1 | 8.2–9.6 | 9.0–9.6 | 0% |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | core | 6.2 | 5.2–7.4 | 6.2 | 5.2–7.4 | 4.9–8.4 | 1% |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh | 8.5 | 7.0–8.7 | <4.4 | 4.4–6.3 | censored | 81% |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | **delta** (exhibition − core) | +2.9 | +1.4 to +4.1 | +2.9 | +1.4 to +4.0 | | |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | **delta** (exhibition − fresh) | +0.6 | -0.2 to +2.3 |  |  | | |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | **delta** (fresh − core) | +2.3 | +0.2 to +3.3 |  |  | | |
| openrouter-assemblyai-universal-3-6-pro__raw | exhibition | 8.6 | 7.6–9.7 | 8.6 | 7.5–9.6 | 5.5–9.0 | 0% |
| openrouter-assemblyai-universal-3-6-pro__raw | core | 6.1 | 5.0–7.0 | 6.1 | 5.0–7.0 | 4.9–8.4 | 2% |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh | 8.2 | 7.2–8.6 | 6.3 | 4.4–6.4 | 6.28–6.49 | 30% |
| openrouter-assemblyai-universal-3-6-pro__raw | **delta** (exhibition − core) | +2.5 | +1.1 to +3.9 | +2.5 | +1.0 to +3.9 | | |
| openrouter-assemblyai-universal-3-6-pro__raw | **delta** (exhibition − fresh) | +0.4 | -0.7 to +2.0 | +2.3 | +1.2 to +4.8 | | |
| openrouter-assemblyai-universal-3-6-pro__raw | **delta** (fresh − core) | +2.1 | +0.5 to +3.2 | +0.2 | -2.3 to +1.1 | | |
| openrouter-deepgram-nova-3__raw | exhibition | 5.9 | 5.5–6.3 | 5.9 | 5.5–6.3 | 5.5–9.0 | 2% |
| openrouter-deepgram-nova-3__raw | core | <4.9 | 4.9–4.9 | <4.9 | 4.9–4.9 | censored | 100% |
| openrouter-deepgram-nova-3__raw | fresh | <4.4 | 4.4–4.4 | <4.4 | 4.4–4.4 | censored | 100% |
| openrouter-elevenlabs-scribe-v2__raw | exhibition | >10.6 | 10.6–10.6 | >10.6 | 8.1–10.6 | censored | 49% |
| openrouter-elevenlabs-scribe-v2__raw | core | 6.9 | 5.9–8.4 | 6.9 | 5.9–8.4 | 4.9–8.4 | 8% |
| openrouter-elevenlabs-scribe-v2__raw | fresh | 8.9 | 8.3–9.2 | 6.4 | 4.4–7.4 | 6.28–6.49 | 29% |
| openrouter-elevenlabs-scribe-v2__raw | **delta** (fresh − core) | +2.0 | +0.3 to +3.0 | -0.5 | -3.7 to +0.8 | | |
| openrouter-google-chirp-3__raw | exhibition | 8.0 | 7.3–9.2 | 8.0 | 7.2–9.1 | 5.5–9.0 | 0% |
| openrouter-google-chirp-3__raw | core | <4.9 | 4.9–5.5 | <4.9 | 4.9–5.5 | censored | 51% |
| openrouter-google-chirp-3__raw | fresh | 5.8 | 5.8–6.6 | <4.4 | 4.4–5.8 | censored | 68% |
| openrouter-google-chirp-3__raw | **delta** (exhibition − fresh) | +2.2 | +1.2 to +3.4 |  |  | | |
| openrouter-google-gemini-3.5-transcribe__raw | exhibition | 8.6 | 7.5–9.1 | 8.6 | 7.5–9.1 | 5.5–9.0 | 0% |
| openrouter-google-gemini-3.5-transcribe__raw | core | <4.9 | 4.9–4.9 | <4.9 | 4.9–4.9 | censored | 100% |
| openrouter-google-gemini-3.5-transcribe__raw | fresh | 6.3 | 4.4–6.4 | <4.4 | 4.4–4.4 | censored | 100% |
| openrouter-google-gemini-3.5-transcribe__raw | **delta** (exhibition − fresh) | +2.3 | +1.2 to +4.6 |  |  | | |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | exhibition | 8.7 | 7.5–9.1 | 8.7 | 7.5–9.1 | 5.5–9.0 | 0% |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | core | 5.7 | 4.9–6.4 | 5.7 | 4.9–6.4 | 4.9–8.4 | 6% |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh | 7.2 | 7.0–7.4 | <4.4 | 4.4–6.9 | censored | 53% |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | **delta** (exhibition − core) | +3.0 | +1.7 to +4.1 | +3.0 | +1.7 to +4.1 | | |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | **delta** (exhibition − fresh) | +1.5 | +0.3 to +2.0 |  |  | | |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | **delta** (fresh − core) | +1.5 | +0.8 to +2.4 |  |  | | |
| openrouter-openai-gpt-4o-transcribe__raw | exhibition | 8.7 | 7.8–9.1 | 8.7 | 7.8–9.0 | 5.5–9.0 | 0% |
| openrouter-openai-gpt-4o-transcribe__raw | core | 6.3 | 5.5–7.0 | 6.3 | 5.5–7.0 | 4.9–8.4 | 0% |
| openrouter-openai-gpt-4o-transcribe__raw | fresh | 6.4 | 6.1–6.5 | <4.4 | 4.4–4.4 | censored | 100% |
| openrouter-openai-gpt-4o-transcribe__raw | **delta** (exhibition − core) | +2.4 | +1.2 to +3.4 | +2.4 | +1.2 to +3.3 | | |
| openrouter-openai-gpt-4o-transcribe__raw | **delta** (exhibition − fresh) | +2.2 | +1.4 to +2.8 |  |  | | |
| openrouter-openai-gpt-4o-transcribe__raw | **delta** (fresh − core) | +0.2 | -0.7 to +0.9 |  |  | | |
| openrouter-openai-gpt-transcribe__raw | exhibition | >10.6 | 8.6–10.6 | 8.2 | 7.5–9.6 | 5.5–9.0 | 0% |
| openrouter-openai-gpt-transcribe__raw | core | 5.8 | 4.9–6.7 | 5.8 | 4.9–6.7 | 4.9–8.4 | 8% |
| openrouter-openai-gpt-transcribe__raw | fresh | 7.4 | 6.9–8.6 | <4.4 | 4.4–6.3 | censored | 71% |
| openrouter-openai-gpt-transcribe__raw | **delta** (exhibition − core) |  |  | +2.4 | +1.3 to +3.9 | | |
| openrouter-openai-gpt-transcribe__raw | **delta** (fresh − core) | +1.6 | +0.6 to +3.4 |  |  | | |
| openrouter-x-ai-grok-stt-2.0__raw | exhibition | 8.4 | 7.4–9.1 | 8.4 | 7.4–9.0 | 5.5–9.0 | 0% |
| openrouter-x-ai-grok-stt-2.0__raw | core | 5.8 | 4.9–6.5 | 5.8 | 4.9–6.5 | 4.9–8.4 | 6% |
| openrouter-x-ai-grok-stt-2.0__raw | fresh | 7.3 | 6.9–8.5 | <4.4 | 4.4–6.4 | censored | 75% |
| openrouter-x-ai-grok-stt-2.0__raw | **delta** (exhibition − core) | +2.6 | +1.3 to +3.9 | +2.6 | +1.3 to +3.9 | | |
| openrouter-x-ai-grok-stt-2.0__raw | **delta** (exhibition − fresh) | +1.1 | -0.7 to +2.1 |  |  | | |
| openrouter-x-ai-grok-stt-2.0__raw | **delta** (fresh − core) | +1.5 | +0.6 to +3.3 |  |  | | |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | exhibition | 8.0 | 7.1–9.7 | 7.6 | 6.8–9.1 | 5.5–9.0 | 0% |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | core | 6.0 | 5.5–6.4 | 6.0 | 5.5–6.4 | 4.9–8.4 | 0% |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh | 7.0 | 5.9–7.1 | <4.4 | 4.4–6.0 | censored | 74% |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | **delta** (exhibition − core) | +2.1 | +1.0 to +3.9 | +1.6 | +0.7 to +3.2 | | |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | **delta** (exhibition − fresh) | +1.1 | +0.1 to +2.8 |  |  | | |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | **delta** (fresh − core) | +1.0 | -0.2 to +1.5 |  |  | | |

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
| faster-whisper-distil-large-v3__raw | fresh-titanic-gawne | 68% | 58%–78% | 30 | 187 |
| faster-whisper-distil-large-v3__raw | fresh-nightmares-gawne | 21% | 12%–30% | 16 | 102 |
| faster-whisper-distil-large-v3__raw | fresh-animals-pt-i-jid | 37% | 26%–49% | 21 | 188 |
| faster-whisper-distil-large-v3__raw | fresh-sk8-jid | 42% | 32%–53% | 15 | 129 |
| faster-whisper-distil-large-v3__raw | fresh-behold-jid | 37% | 27%–47% | 20 | 182 |
| faster-whisper-distil-large-v3__raw | fresh-never-me-token | 21% | 14%–29% | 19 | 167 |
| faster-whisper-distil-large-v3__raw | fresh-the-ropes-token | 45% | 35%–56% | 32 | 188 |
| faster-whisper-distil-large-v3__raw | fresh-kumquat-token | 23% | 13%–33% | 17 | 154 |
| faster-whisper-distil-large-v3__raw | fresh-gta-6-joyner-lucas | 34% | 25%–48% | 13 | 148 |
| faster-whisper-distil-large-v3__raw | fresh-one-of-them-joyner-lucas | 43% | 34%–53% | 20 | 161 |
| faster-whisper-distil-large-v3__raw | fresh-monsters-joyner-lucas | 16% | 10%–22% | 15 | 138 |
| faster-whisper-distil-large-v3__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 25% | 18%–31% | 18 | 153 |
| faster-whisper-distil-large-v3__raw | fresh-call-them-less-logic | 15% | 9%–22% | 15 | 136 |
| faster-whisper-distil-large-v3__raw | fresh-give-me-a-reason-nf | 17% | 6%–31% | 8 | 138 |
| faster-whisper-distil-large-v3__raw | fresh-bad-news-merkules | 22% | 12%–32% | 11 | 140 |
| faster-whisper-distil-large-v3__raw | fresh-richards-tale-set-the-scene-ren | 21% | 14%–28% | 12 | 112 |
| faster-whisper-distil-large-v3__raw | fresh-caught-you-in-the-bed-dax | 9% | 5%–13% | 11 | 126 |
| faster-whisper-distil-large-v3__raw | fresh-crash-out-king-iso | 16% | 7%–26% | 12 | 121 |
| faster-whisper-distil-large-v3__raw | fresh-raw-thoughts-vii-chris-webby | 4% | 0%–9% | 11 | 108 |
| faster-whisper-distil-large-v3__raw | fresh-jealous-type-doja-cat | 32% | 16%–50% | 10 | 96 |
| faster-whisper-large-v3__raw | lose-yourself-v1 | 6% | 2%–11% | 16 | 143 |
| faster-whisper-large-v3__raw | the-way-i-am-v1 | 9% | 3%–15% | 15 | 138 |
| faster-whisper-large-v3__raw | speedom-em | 23% | 14%–34% | 22 | 220 |
| faster-whisper-large-v3__raw | worldwide-choppers-twista | 22% | 15%–30% | 19 | 183 |
| faster-whisper-large-v3__raw | rap-god-fast | 28% | 13%–43% | 11 | 108 |
| faster-whisper-large-v3__raw | godzilla-v3 | 26% | 18%–34% | 24 | 227 |
| faster-whisper-large-v3__raw | suno02 | 51% | 38%–63% | 16 | 118 |
| faster-whisper-large-v3__raw | suno01 | 10% | 4%–17% | 14 | 102 |
| faster-whisper-large-v3__raw | fresh-titanic-gawne | 49% | 38%–61% | 30 | 187 |
| faster-whisper-large-v3__raw | fresh-nightmares-gawne | 14% | 8%–22% | 15 | 100 |
| faster-whisper-large-v3__raw | fresh-animals-pt-i-jid | 21% | 13%–30% | 21 | 188 |
| faster-whisper-large-v3__raw | fresh-sk8-jid | 18% | 9%–29% | 15 | 129 |
| faster-whisper-large-v3__raw | fresh-behold-jid | 32% | 22%–44% | 20 | 182 |
| faster-whisper-large-v3__raw | fresh-never-me-token | 13% | 7%–18% | 19 | 167 |
| faster-whisper-large-v3__raw | fresh-the-ropes-token | 23% | 16%–31% | 32 | 188 |
| faster-whisper-large-v3__raw | fresh-kumquat-token | 11% | 5%–19% | 17 | 154 |
| faster-whisper-large-v3__raw | fresh-gta-6-joyner-lucas | 23% | 14%–35% | 13 | 148 |
| faster-whisper-large-v3__raw | fresh-one-of-them-joyner-lucas | 28% | 18%–40% | 20 | 161 |
| faster-whisper-large-v3__raw | fresh-monsters-joyner-lucas | 13% | 8%–18% | 15 | 138 |
| faster-whisper-large-v3__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 22% | 16%–27% | 18 | 153 |
| faster-whisper-large-v3__raw | fresh-call-them-less-logic | 10% | 4%–18% | 15 | 136 |
| faster-whisper-large-v3__raw | fresh-give-me-a-reason-nf | 7% | 1%–13% | 8 | 138 |
| faster-whisper-large-v3__raw | fresh-bad-news-merkules | 19% | 11%–28% | 11 | 140 |
| faster-whisper-large-v3__raw | fresh-richards-tale-set-the-scene-ren | 15% | 8%–23% | 12 | 112 |
| faster-whisper-large-v3__raw | fresh-caught-you-in-the-bed-dax | 2% | 1%–5% | 11 | 126 |
| faster-whisper-large-v3__raw | fresh-crash-out-king-iso | 8% | 3%–14% | 12 | 121 |
| faster-whisper-large-v3__raw | fresh-raw-thoughts-vii-chris-webby | 3% | 0%–9% | 11 | 108 |
| faster-whisper-large-v3__raw | fresh-jealous-type-doja-cat | 25% | 12%–43% | 10 | 96 |
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
| faster-whisper-small__raw | fresh-titanic-gawne | 61% | 50%–74% | 30 | 187 |
| faster-whisper-small__raw | fresh-nightmares-gawne | 24% | 11%–38% | 16 | 102 |
| faster-whisper-small__raw | fresh-animals-pt-i-jid | 36% | 25%–48% | 21 | 188 |
| faster-whisper-small__raw | fresh-sk8-jid | 40% | 30%–52% | 15 | 129 |
| faster-whisper-small__raw | fresh-behold-jid | 43% | 30%–56% | 20 | 182 |
| faster-whisper-small__raw | fresh-never-me-token | 14% | 9%–20% | 19 | 167 |
| faster-whisper-small__raw | fresh-the-ropes-token | 37% | 27%–49% | 32 | 188 |
| faster-whisper-small__raw | fresh-kumquat-token | 20% | 10%–31% | 17 | 154 |
| faster-whisper-small__raw | fresh-gta-6-joyner-lucas | 30% | 17%–45% | 13 | 148 |
| faster-whisper-small__raw | fresh-one-of-them-joyner-lucas | 32% | 23%–42% | 20 | 161 |
| faster-whisper-small__raw | fresh-monsters-joyner-lucas | 24% | 16%–32% | 15 | 138 |
| faster-whisper-small__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 20% | 14%–27% | 18 | 153 |
| faster-whisper-small__raw | fresh-call-them-less-logic | 18% | 9%–27% | 15 | 136 |
| faster-whisper-small__raw | fresh-give-me-a-reason-nf | 11% | 2%–19% | 8 | 138 |
| faster-whisper-small__raw | fresh-bad-news-merkules | 26% | 18%–34% | 11 | 140 |
| faster-whisper-small__raw | fresh-richards-tale-set-the-scene-ren | 112% | 27%–276% | 12 | 112 |
| faster-whisper-small__raw | fresh-caught-you-in-the-bed-dax | 5% | 2%–8% | 11 | 126 |
| faster-whisper-small__raw | fresh-crash-out-king-iso | 17% | 9%–26% | 12 | 121 |
| faster-whisper-small__raw | fresh-raw-thoughts-vii-chris-webby | 4% | 0%–8% | 11 | 108 |
| faster-whisper-small__raw | fresh-jealous-type-doja-cat | 28% | 12%–48% | 10 | 96 |
| faster-whisper-tiny__raw | lose-yourself-v1 | 21% | 13%–30% | 16 | 143 |
| faster-whisper-tiny__raw | the-way-i-am-v1 | 57% | 42%–72% | 15 | 138 |
| faster-whisper-tiny__raw | speedom-em | 44% | 36%–51% | 22 | 220 |
| faster-whisper-tiny__raw | worldwide-choppers-twista | 78% | 63%–92% | 19 | 183 |
| faster-whisper-tiny__raw | rap-god-fast | 100% | 100%–100% | 11 | 104 |
| faster-whisper-tiny__raw | godzilla-v3 | 98% | 95%–100% | 24 | 227 |
| faster-whisper-tiny__raw | suno02 | 66% | 50%–80% | 16 | 118 |
| faster-whisper-tiny__raw | suno01 | 47% | 33%–61% | 14 | 102 |
| faster-whisper-tiny__raw | fresh-titanic-gawne | 92% | 86%–97% | 30 | 187 |
| faster-whisper-tiny__raw | fresh-nightmares-gawne | 45% | 31%–59% | 16 | 102 |
| faster-whisper-tiny__raw | fresh-animals-pt-i-jid | 60% | 50%–72% | 21 | 192 |
| faster-whisper-tiny__raw | fresh-sk8-jid | 64% | 51%–77% | 15 | 129 |
| faster-whisper-tiny__raw | fresh-behold-jid | 78% | 70%–87% | 20 | 183 |
| faster-whisper-tiny__raw | fresh-never-me-token | 41% | 34%–48% | 19 | 167 |
| faster-whisper-tiny__raw | fresh-the-ropes-token | 71% | 57%–85% | 32 | 188 |
| faster-whisper-tiny__raw | fresh-kumquat-token | 46% | 33%–59% | 17 | 154 |
| faster-whisper-tiny__raw | fresh-gta-6-joyner-lucas | 66% | 50%–82% | 13 | 148 |
| faster-whisper-tiny__raw | fresh-one-of-them-joyner-lucas | 65% | 52%–80% | 20 | 161 |
| faster-whisper-tiny__raw | fresh-monsters-joyner-lucas | 38% | 29%–48% | 15 | 138 |
| faster-whisper-tiny__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 46% | 36%–55% | 18 | 153 |
| faster-whisper-tiny__raw | fresh-call-them-less-logic | 34% | 24%–45% | 15 | 136 |
| faster-whisper-tiny__raw | fresh-give-me-a-reason-nf | 39% | 21%–58% | 8 | 138 |
| faster-whisper-tiny__raw | fresh-bad-news-merkules | 39% | 25%–52% | 11 | 140 |
| faster-whisper-tiny__raw | fresh-richards-tale-set-the-scene-ren | 62% | 50%–72% | 12 | 112 |
| faster-whisper-tiny__raw | fresh-caught-you-in-the-bed-dax | 20% | 10%–31% | 11 | 126 |
| faster-whisper-tiny__raw | fresh-crash-out-king-iso | 34% | 21%–47% | 12 | 121 |
| faster-whisper-tiny__raw | fresh-raw-thoughts-vii-chris-webby | 34% | 22%–49% | 11 | 108 |
| faster-whisper-tiny__raw | fresh-jealous-type-doja-cat | 51% | 36%–67% | 10 | 96 |
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
| faster-whisper-turbo__raw | fresh-titanic-gawne | 60% | 47%–74% | 30 | 187 |
| faster-whisper-turbo__raw | fresh-nightmares-gawne | 9% | 3%–15% | 15 | 100 |
| faster-whisper-turbo__raw | fresh-animals-pt-i-jid | 21% | 12%–31% | 21 | 188 |
| faster-whisper-turbo__raw | fresh-sk8-jid | 20% | 10%–35% | 15 | 129 |
| faster-whisper-turbo__raw | fresh-behold-jid | 25% | 17%–36% | 20 | 182 |
| faster-whisper-turbo__raw | fresh-never-me-token | 15% | 10%–20% | 19 | 167 |
| faster-whisper-turbo__raw | fresh-the-ropes-token | 27% | 18%–35% | 32 | 188 |
| faster-whisper-turbo__raw | fresh-kumquat-token | 16% | 8%–25% | 17 | 154 |
| faster-whisper-turbo__raw | fresh-gta-6-joyner-lucas | 19% | 10%–30% | 13 | 148 |
| faster-whisper-turbo__raw | fresh-one-of-them-joyner-lucas | 30% | 22%–41% | 20 | 161 |
| faster-whisper-turbo__raw | fresh-monsters-joyner-lucas | 16% | 9%–23% | 15 | 138 |
| faster-whisper-turbo__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 20% | 14%–27% | 18 | 153 |
| faster-whisper-turbo__raw | fresh-call-them-less-logic | 10% | 4%–16% | 15 | 136 |
| faster-whisper-turbo__raw | fresh-give-me-a-reason-nf | 14% | 5%–27% | 8 | 138 |
| faster-whisper-turbo__raw | fresh-bad-news-merkules | 25% | 17%–33% | 11 | 140 |
| faster-whisper-turbo__raw | fresh-richards-tale-set-the-scene-ren | 23% | 12%–34% | 12 | 112 |
| faster-whisper-turbo__raw | fresh-caught-you-in-the-bed-dax | 104% | 7%–286% | 11 | 137 |
| faster-whisper-turbo__raw | fresh-crash-out-king-iso | 10% | 6%–14% | 12 | 121 |
| faster-whisper-turbo__raw | fresh-raw-thoughts-vii-chris-webby | 4% | 0%–10% | 11 | 108 |
| faster-whisper-turbo__raw | fresh-jealous-type-doja-cat | 32% | 15%–53% | 10 | 96 |
| hf-UsefulSensors-moonshine-base__raw | lose-yourself-v1 | 30% | 13%–49% | 16 | 143 |
| hf-UsefulSensors-moonshine-base__raw | the-way-i-am-v1 | 29% | 18%–42% | 15 | 138 |
| hf-UsefulSensors-moonshine-base__raw | speedom-em | 75% | 59%–90% | 22 | 220 |
| hf-UsefulSensors-moonshine-base__raw | worldwide-choppers-twista | 68% | 55%–80% | 18 | 176 |
| hf-UsefulSensors-moonshine-base__raw | rap-god-fast | 28% | 14%–42% | 11 | 104 |
| hf-UsefulSensors-moonshine-base__raw | godzilla-v3 | 72% | 60%–83% | 24 | 227 |
| hf-UsefulSensors-moonshine-base__raw | suno02 | 64% | 47%–79% | 16 | 118 |
| hf-UsefulSensors-moonshine-base__raw | suno01 | 42% | 28%–57% | 14 | 100 |
| hf-UsefulSensors-moonshine-base__raw | fresh-titanic-gawne | 72% | 60%–84% | 30 | 187 |
| hf-UsefulSensors-moonshine-base__raw | fresh-nightmares-gawne | 35% | 23%–51% | 16 | 102 |
| hf-UsefulSensors-moonshine-base__raw | fresh-animals-pt-i-jid | 53% | 38%–68% | 21 | 188 |
| hf-UsefulSensors-moonshine-base__raw | fresh-sk8-jid | 53% | 43%–65% | 15 | 129 |
| hf-UsefulSensors-moonshine-base__raw | fresh-behold-jid | 92% | 81%–99% | 20 | 182 |
| hf-UsefulSensors-moonshine-base__raw | fresh-never-me-token | 37% | 26%–50% | 19 | 167 |
| hf-UsefulSensors-moonshine-base__raw | fresh-the-ropes-token | 68% | 55%–81% | 32 | 188 |
| hf-UsefulSensors-moonshine-base__raw | fresh-kumquat-token | 34% | 19%–52% | 17 | 154 |
| hf-UsefulSensors-moonshine-base__raw | fresh-gta-6-joyner-lucas | 35% | 19%–55% | 13 | 148 |
| hf-UsefulSensors-moonshine-base__raw | fresh-one-of-them-joyner-lucas | 40% | 30%–52% | 20 | 161 |
| hf-UsefulSensors-moonshine-base__raw | fresh-monsters-joyner-lucas | 22% | 17%–28% | 15 | 138 |
| hf-UsefulSensors-moonshine-base__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 37% | 22%–54% | 18 | 153 |
| hf-UsefulSensors-moonshine-base__raw | fresh-call-them-less-logic | 20% | 14%–26% | 15 | 136 |
| hf-UsefulSensors-moonshine-base__raw | fresh-give-me-a-reason-nf | 16% | 7%–25% | 8 | 138 |
| hf-UsefulSensors-moonshine-base__raw | fresh-bad-news-merkules | 26% | 17%–35% | 11 | 140 |
| hf-UsefulSensors-moonshine-base__raw | fresh-richards-tale-set-the-scene-ren | 40% | 26%–52% | 12 | 112 |
| hf-UsefulSensors-moonshine-base__raw | fresh-caught-you-in-the-bed-dax | 10% | 3%–18% | 11 | 126 |
| hf-UsefulSensors-moonshine-base__raw | fresh-crash-out-king-iso | 21% | 11%–31% | 12 | 121 |
| hf-UsefulSensors-moonshine-base__raw | fresh-raw-thoughts-vii-chris-webby | 7% | 2%–16% | 11 | 108 |
| hf-UsefulSensors-moonshine-base__raw | fresh-jealous-type-doja-cat | 114% | 21%–278% | 10 | 96 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | lose-yourself-v1 | 59% | 42%–78% | 16 | 143 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | the-way-i-am-v1 | 91% | 85%–95% | 15 | 138 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | speedom-em | 78% | 69%–86% | 22 | 220 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | worldwide-choppers-twista | 86% | 77%–93% | 18 | 176 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | rap-god-fast | 81% | 70%–92% | 11 | 108 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | godzilla-v3 | 88% | 79%–95% | 24 | 227 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | suno02 | 91% | 77%–102% | 16 | 118 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | suno01 | 95% | 86%–101% | 14 | 102 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-titanic-gawne | 98% | 95%–100% | 30 | 187 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-nightmares-gawne | 72% | 62%–81% | 15 | 100 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-animals-pt-i-jid | 82% | 76%–88% | 21 | 188 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-sk8-jid | 75% | 62%–86% | 15 | 129 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-behold-jid | 88% | 82%–93% | 20 | 183 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-never-me-token | 76% | 65%–88% | 19 | 167 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-the-ropes-token | 94% | 91%–97% | 32 | 188 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-kumquat-token | 72% | 62%–81% | 17 | 154 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-gta-6-joyner-lucas | 84% | 77%–90% | 13 | 148 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-one-of-them-joyner-lucas | 89% | 83%–94% | 20 | 161 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-monsters-joyner-lucas | 77% | 71%–84% | 15 | 144 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 70% | 60%–80% | 18 | 156 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-call-them-less-logic | 71% | 59%–81% | 15 | 136 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-give-me-a-reason-nf | 57% | 47%–67% | 8 | 138 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-bad-news-merkules | 65% | 56%–74% | 11 | 140 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-richards-tale-set-the-scene-ren | 60% | 43%–76% | 12 | 112 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-caught-you-in-the-bed-dax | 48% | 31%–67% | 11 | 126 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-crash-out-king-iso | 68% | 57%–79% | 12 | 121 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-raw-thoughts-vii-chris-webby | 65% | 46%–83% | 11 | 108 |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | fresh-jealous-type-doja-cat | 96% | 93%–99% | 10 | 96 |
| hf-whisper-large-v3-turbo-base__raw | lose-yourself-v1 | 5% | 2%–8% | 16 | 143 |
| hf-whisper-large-v3-turbo-base__raw | the-way-i-am-v1 | 10% | 6%–15% | 15 | 138 |
| hf-whisper-large-v3-turbo-base__raw | speedom-em | 23% | 15%–31% | 22 | 220 |
| hf-whisper-large-v3-turbo-base__raw | worldwide-choppers-twista | 86% | 69%–99% | 19 | 183 |
| hf-whisper-large-v3-turbo-base__raw | rap-god-fast | 32% | 19%–49% | 11 | 108 |
| hf-whisper-large-v3-turbo-base__raw | godzilla-v3 | 30% | 21%–39% | 24 | 227 |
| hf-whisper-large-v3-turbo-base__raw | suno02 | 47% | 34%–61% | 16 | 118 |
| hf-whisper-large-v3-turbo-base__raw | suno01 | 12% | 5%–20% | 14 | 102 |
| hf-whisper-large-v3-turbo-base__raw | fresh-titanic-gawne | 49% | 38%–62% | 30 | 187 |
| hf-whisper-large-v3-turbo-base__raw | fresh-nightmares-gawne | 9% | 3%–15% | 15 | 100 |
| hf-whisper-large-v3-turbo-base__raw | fresh-animals-pt-i-jid | 30% | 16%–46% | 21 | 188 |
| hf-whisper-large-v3-turbo-base__raw | fresh-sk8-jid | 19% | 9%–33% | 15 | 129 |
| hf-whisper-large-v3-turbo-base__raw | fresh-behold-jid | 32% | 23%–45% | 20 | 182 |
| hf-whisper-large-v3-turbo-base__raw | fresh-never-me-token | 14% | 9%–19% | 19 | 167 |
| hf-whisper-large-v3-turbo-base__raw | fresh-the-ropes-token | 28% | 19%–38% | 32 | 188 |
| hf-whisper-large-v3-turbo-base__raw | fresh-kumquat-token | 16% | 8%–25% | 17 | 154 |
| hf-whisper-large-v3-turbo-base__raw | fresh-gta-6-joyner-lucas | 20% | 11%–33% | 13 | 148 |
| hf-whisper-large-v3-turbo-base__raw | fresh-one-of-them-joyner-lucas | 27% | 19%–37% | 20 | 161 |
| hf-whisper-large-v3-turbo-base__raw | fresh-monsters-joyner-lucas | 18% | 11%–25% | 15 | 138 |
| hf-whisper-large-v3-turbo-base__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 20% | 14%–27% | 18 | 153 |
| hf-whisper-large-v3-turbo-base__raw | fresh-call-them-less-logic | 11% | 4%–18% | 15 | 136 |
| hf-whisper-large-v3-turbo-base__raw | fresh-give-me-a-reason-nf | 12% | 4%–23% | 8 | 138 |
| hf-whisper-large-v3-turbo-base__raw | fresh-bad-news-merkules | 24% | 16%–32% | 11 | 140 |
| hf-whisper-large-v3-turbo-base__raw | fresh-richards-tale-set-the-scene-ren | 15% | 7%–24% | 12 | 112 |
| hf-whisper-large-v3-turbo-base__raw | fresh-caught-you-in-the-bed-dax | 5% | 2%–9% | 11 | 126 |
| hf-whisper-large-v3-turbo-base__raw | fresh-crash-out-king-iso | 9% | 5%–14% | 12 | 121 |
| hf-whisper-large-v3-turbo-base__raw | fresh-raw-thoughts-vii-chris-webby | 4% | 0%–10% | 11 | 108 |
| hf-whisper-large-v3-turbo-base__raw | fresh-jealous-type-doja-cat | 32% | 15%–53% | 10 | 96 |
| hf-whisper-large-v3-turbo-guard-base__raw | lose-yourself-v1 | 5% | 2%–8% | 16 | 143 |
| hf-whisper-large-v3-turbo-guard-base__raw | the-way-i-am-v1 | 10% | 6%–15% | 15 | 138 |
| hf-whisper-large-v3-turbo-guard-base__raw | speedom-em | 23% | 15%–31% | 22 | 220 |
| hf-whisper-large-v3-turbo-guard-base__raw | worldwide-choppers-twista | 40% | 32%–51% | 19 | 183 |
| hf-whisper-large-v3-turbo-guard-base__raw | rap-god-fast | 32% | 19%–49% | 11 | 108 |
| hf-whisper-large-v3-turbo-guard-base__raw | godzilla-v3 | 30% | 21%–39% | 24 | 227 |
| hf-whisper-large-v3-turbo-guard-base__raw | suno02 | 47% | 34%–61% | 16 | 118 |
| hf-whisper-large-v3-turbo-guard-base__raw | suno01 | 12% | 5%–20% | 14 | 102 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-titanic-gawne | 49% | 38%–62% | 30 | 187 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-nightmares-gawne | 9% | 3%–15% | 15 | 100 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-animals-pt-i-jid | 30% | 16%–46% | 21 | 188 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-sk8-jid | 19% | 9%–33% | 15 | 129 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-behold-jid | 32% | 23%–45% | 20 | 182 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-never-me-token | 14% | 9%–19% | 19 | 167 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-the-ropes-token | 28% | 19%–38% | 32 | 188 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-kumquat-token | 16% | 8%–25% | 17 | 154 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-gta-6-joyner-lucas | 20% | 11%–33% | 13 | 148 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-one-of-them-joyner-lucas | 27% | 19%–37% | 20 | 161 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-monsters-joyner-lucas | 18% | 11%–25% | 15 | 138 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 20% | 14%–27% | 18 | 153 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-call-them-less-logic | 11% | 4%–18% | 15 | 136 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-give-me-a-reason-nf | 12% | 4%–23% | 8 | 138 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-bad-news-merkules | 24% | 16%–32% | 11 | 140 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-richards-tale-set-the-scene-ren | 15% | 7%–24% | 12 | 112 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-caught-you-in-the-bed-dax | 5% | 2%–9% | 11 | 126 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-crash-out-king-iso | 9% | 5%–14% | 12 | 121 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-raw-thoughts-vii-chris-webby | 4% | 0%–10% | 11 | 108 |
| hf-whisper-large-v3-turbo-guard-base__raw | fresh-jealous-type-doja-cat | 32% | 15%–53% | 10 | 96 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | lose-yourself-v1 | 7% | 3%–12% | 16 | 143 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | the-way-i-am-v1 | 12% | 6%–17% | 15 | 138 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | speedom-em | 23% | 17%–29% | 22 | 220 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | worldwide-choppers-twista | 45% | 34%–59% | 19 | 183 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | rap-god-fast | 31% | 17%–46% | 11 | 108 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | godzilla-v3 | 30% | 21%–39% | 24 | 227 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | suno02 | 47% | 34%–60% | 16 | 118 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | suno01 | 16% | 9%–24% | 14 | 102 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-titanic-gawne | 42% | 33%–52% | 30 | 187 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-nightmares-gawne | 17% | 6%–29% | 15 | 100 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-animals-pt-i-jid | 24% | 15%–35% | 21 | 188 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-sk8-jid | 25% | 16%–36% | 15 | 129 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-behold-jid | 35% | 26%–45% | 20 | 182 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-never-me-token | 14% | 8%–19% | 19 | 167 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-the-ropes-token | 32% | 23%–42% | 32 | 188 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-kumquat-token | 19% | 10%–29% | 17 | 154 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-gta-6-joyner-lucas | 22% | 12%–35% | 13 | 148 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-one-of-them-joyner-lucas | 26% | 17%–37% | 20 | 161 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-monsters-joyner-lucas | 13% | 6%–20% | 15 | 138 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 15% | 9%–21% | 18 | 153 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-call-them-less-logic | 12% | 6%–19% | 15 | 136 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-give-me-a-reason-nf | 9% | 2%–18% | 8 | 138 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-bad-news-merkules | 23% | 14%–32% | 11 | 140 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-richards-tale-set-the-scene-ren | 26% | 13%–39% | 12 | 112 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-caught-you-in-the-bed-dax | 6% | 2%–11% | 11 | 126 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-crash-out-king-iso | 12% | 6%–19% | 12 | 121 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-raw-thoughts-vii-chris-webby | 3% | 0%–9% | 11 | 108 |
| hf-whisper-large-v3-turbo-guard-lora-e1__raw | fresh-jealous-type-doja-cat | 33% | 15%–59% | 10 | 96 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | lose-yourself-v1 | 10% | 5%–18% | 16 | 143 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | the-way-i-am-v1 | 14% | 7%–20% | 15 | 138 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | speedom-em | 21% | 15%–28% | 22 | 220 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | worldwide-choppers-twista | 46% | 34%–60% | 19 | 183 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | rap-god-fast | 37% | 24%–52% | 11 | 108 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | godzilla-v3 | 30% | 20%–40% | 24 | 227 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | suno02 | 54% | 42%–68% | 16 | 118 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | suno01 | 14% | 6%–24% | 14 | 102 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-titanic-gawne | 45% | 37%–54% | 30 | 187 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-nightmares-gawne | 18% | 6%–30% | 15 | 100 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-animals-pt-i-jid | 27% | 17%–38% | 21 | 188 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-sk8-jid | 22% | 13%–35% | 15 | 129 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-behold-jid | 32% | 23%–43% | 20 | 182 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-never-me-token | 16% | 10%–21% | 19 | 167 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-the-ropes-token | 34% | 25%–44% | 32 | 188 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-kumquat-token | 19% | 9%–31% | 17 | 154 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-gta-6-joyner-lucas | 22% | 12%–34% | 13 | 148 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-one-of-them-joyner-lucas | 27% | 19%–37% | 20 | 161 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-monsters-joyner-lucas | 11% | 6%–17% | 15 | 138 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 16% | 10%–24% | 18 | 153 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-call-them-less-logic | 12% | 5%–19% | 15 | 136 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-give-me-a-reason-nf | 13% | 6%–22% | 8 | 138 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-bad-news-merkules | 27% | 16%–37% | 11 | 140 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-richards-tale-set-the-scene-ren | 22% | 11%–33% | 12 | 112 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-caught-you-in-the-bed-dax | 2% | 0%–5% | 11 | 126 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-crash-out-king-iso | 8% | 5%–12% | 12 | 121 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-raw-thoughts-vii-chris-webby | 5% | 0%–11% | 11 | 108 |
| hf-whisper-large-v3-turbo-guard-lora-e2__raw | fresh-jealous-type-doja-cat | 40% | 19%–62% | 10 | 96 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | lose-yourself-v1 | 13% | 7%–21% | 16 | 143 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | the-way-i-am-v1 | 13% | 7%–20% | 15 | 138 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | speedom-em | 20% | 14%–27% | 22 | 220 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | worldwide-choppers-twista | 36% | 26%–49% | 19 | 183 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | rap-god-fast | 35% | 19%–52% | 11 | 108 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | godzilla-v3 | 37% | 27%–47% | 24 | 227 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | suno02 | 54% | 44%–67% | 16 | 118 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | suno01 | 12% | 6%–19% | 14 | 102 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-titanic-gawne | 46% | 36%–55% | 30 | 187 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-nightmares-gawne | 19% | 6%–31% | 15 | 100 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-animals-pt-i-jid | 27% | 17%–38% | 21 | 188 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-sk8-jid | 24% | 15%–36% | 15 | 129 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-behold-jid | 34% | 23%–48% | 20 | 182 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-never-me-token | 15% | 9%–20% | 19 | 167 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-the-ropes-token | 39% | 28%–52% | 32 | 188 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-kumquat-token | 17% | 7%–28% | 17 | 154 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-gta-6-joyner-lucas | 21% | 12%–32% | 13 | 148 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-one-of-them-joyner-lucas | 25% | 18%–34% | 20 | 161 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-monsters-joyner-lucas | 11% | 6%–16% | 15 | 138 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 18% | 11%–25% | 18 | 153 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-call-them-less-logic | 15% | 7%–22% | 15 | 136 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-give-me-a-reason-nf | 14% | 6%–23% | 8 | 138 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-bad-news-merkules | 29% | 19%–38% | 11 | 140 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-richards-tale-set-the-scene-ren | 23% | 10%–38% | 12 | 112 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-caught-you-in-the-bed-dax | 9% | 4%–15% | 11 | 126 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-crash-out-king-iso | 13% | 7%–21% | 12 | 121 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-raw-thoughts-vii-chris-webby | 3% | 0%–7% | 11 | 108 |
| hf-whisper-large-v3-turbo-guard-lora-e3__raw | fresh-jealous-type-doja-cat | 36% | 19%–58% | 10 | 96 |
| hf-whisper-large-v3-turbo-lora-e1__raw | lose-yourself-v1 | 7% | 3%–12% | 16 | 143 |
| hf-whisper-large-v3-turbo-lora-e1__raw | the-way-i-am-v1 | 12% | 7%–16% | 15 | 138 |
| hf-whisper-large-v3-turbo-lora-e1__raw | speedom-em | 23% | 17%–29% | 22 | 220 |
| hf-whisper-large-v3-turbo-lora-e1__raw | worldwide-choppers-twista | 84% | 67%–96% | 18 | 176 |
| hf-whisper-large-v3-turbo-lora-e1__raw | rap-god-fast | 31% | 17%–45% | 11 | 108 |
| hf-whisper-large-v3-turbo-lora-e1__raw | godzilla-v3 | 30% | 21%–39% | 24 | 227 |
| hf-whisper-large-v3-turbo-lora-e1__raw | suno02 | 90% | 35%–188% | 16 | 118 |
| hf-whisper-large-v3-turbo-lora-e1__raw | suno01 | 16% | 9%–24% | 14 | 102 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-titanic-gawne | 42% | 33%–52% | 30 | 187 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-nightmares-gawne | 17% | 6%–29% | 15 | 100 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-animals-pt-i-jid | 24% | 15%–35% | 21 | 188 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-sk8-jid | 25% | 16%–36% | 15 | 129 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-behold-jid | 203% | 26%–625% | 20 | 183 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-never-me-token | 14% | 8%–19% | 19 | 167 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-the-ropes-token | 32% | 23%–42% | 32 | 188 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-kumquat-token | 19% | 10%–29% | 17 | 154 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-gta-6-joyner-lucas | 22% | 12%–35% | 13 | 148 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-one-of-them-joyner-lucas | 26% | 17%–37% | 20 | 161 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-monsters-joyner-lucas | 13% | 6%–20% | 15 | 138 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 15% | 9%–21% | 18 | 153 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-call-them-less-logic | 12% | 6%–19% | 15 | 136 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-give-me-a-reason-nf | 9% | 2%–18% | 8 | 138 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-bad-news-merkules | 23% | 14%–32% | 11 | 140 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-richards-tale-set-the-scene-ren | 26% | 13%–39% | 12 | 112 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-caught-you-in-the-bed-dax | 6% | 2%–11% | 11 | 126 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-crash-out-king-iso | 12% | 6%–19% | 12 | 121 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-raw-thoughts-vii-chris-webby | 3% | 0%–9% | 11 | 108 |
| hf-whisper-large-v3-turbo-lora-e1__raw | fresh-jealous-type-doja-cat | 33% | 15%–59% | 10 | 96 |
| hf-whisper-large-v3-turbo-lora-e2__raw | lose-yourself-v1 | 10% | 5%–18% | 16 | 143 |
| hf-whisper-large-v3-turbo-lora-e2__raw | the-way-i-am-v1 | 14% | 8%–20% | 15 | 138 |
| hf-whisper-large-v3-turbo-lora-e2__raw | speedom-em | 21% | 15%–29% | 22 | 220 |
| hf-whisper-large-v3-turbo-lora-e2__raw | worldwide-choppers-twista | 82% | 66%–95% | 18 | 176 |
| hf-whisper-large-v3-turbo-lora-e2__raw | rap-god-fast | 37% | 24%–52% | 11 | 108 |
| hf-whisper-large-v3-turbo-lora-e2__raw | godzilla-v3 | 30% | 20%–40% | 24 | 227 |
| hf-whisper-large-v3-turbo-lora-e2__raw | suno02 | 242% | 43%–652% | 16 | 118 |
| hf-whisper-large-v3-turbo-lora-e2__raw | suno01 | 14% | 6%–24% | 14 | 102 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-titanic-gawne | 45% | 37%–54% | 30 | 187 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-nightmares-gawne | 18% | 6%–30% | 15 | 100 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-animals-pt-i-jid | 27% | 17%–38% | 21 | 188 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-sk8-jid | 22% | 13%–35% | 15 | 129 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-behold-jid | 32% | 23%–43% | 20 | 182 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-never-me-token | 16% | 10%–21% | 19 | 167 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-the-ropes-token | 34% | 25%–44% | 32 | 188 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-kumquat-token | 19% | 9%–31% | 17 | 154 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-gta-6-joyner-lucas | 22% | 12%–34% | 13 | 148 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-one-of-them-joyner-lucas | 27% | 19%–37% | 20 | 161 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-monsters-joyner-lucas | 11% | 6%–17% | 15 | 138 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 16% | 10%–24% | 18 | 153 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-call-them-less-logic | 12% | 5%–19% | 15 | 136 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-give-me-a-reason-nf | 13% | 6%–22% | 8 | 138 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-bad-news-merkules | 27% | 16%–37% | 11 | 140 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-richards-tale-set-the-scene-ren | 22% | 11%–33% | 12 | 112 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-caught-you-in-the-bed-dax | 2% | 0%–5% | 11 | 126 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-crash-out-king-iso | 8% | 5%–12% | 12 | 121 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-raw-thoughts-vii-chris-webby | 5% | 0%–11% | 11 | 108 |
| hf-whisper-large-v3-turbo-lora-e2__raw | fresh-jealous-type-doja-cat | 40% | 19%–62% | 10 | 96 |
| hf-whisper-large-v3-turbo-lora-e3__raw | lose-yourself-v1 | 13% | 7%–21% | 16 | 143 |
| hf-whisper-large-v3-turbo-lora-e3__raw | the-way-i-am-v1 | 13% | 7%–20% | 15 | 138 |
| hf-whisper-large-v3-turbo-lora-e3__raw | speedom-em | 20% | 14%–27% | 22 | 220 |
| hf-whisper-large-v3-turbo-lora-e3__raw | worldwide-choppers-twista | 36% | 26%–49% | 19 | 183 |
| hf-whisper-large-v3-turbo-lora-e3__raw | rap-god-fast | 35% | 19%–52% | 11 | 108 |
| hf-whisper-large-v3-turbo-lora-e3__raw | godzilla-v3 | 100% | 34%–232% | 24 | 227 |
| hf-whisper-large-v3-turbo-lora-e3__raw | suno02 | 243% | 45%–651% | 16 | 118 |
| hf-whisper-large-v3-turbo-lora-e3__raw | suno01 | 12% | 6%–19% | 14 | 102 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-titanic-gawne | 46% | 36%–55% | 30 | 187 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-nightmares-gawne | 19% | 6%–31% | 15 | 100 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-animals-pt-i-jid | 27% | 17%–38% | 21 | 188 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-sk8-jid | 24% | 15%–36% | 15 | 129 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-behold-jid | 98% | 22%–274% | 20 | 182 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-never-me-token | 15% | 9%–20% | 19 | 167 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-the-ropes-token | 39% | 28%–52% | 32 | 188 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-kumquat-token | 17% | 7%–28% | 17 | 154 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-gta-6-joyner-lucas | 21% | 12%–32% | 13 | 148 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-one-of-them-joyner-lucas | 25% | 18%–34% | 20 | 161 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-monsters-joyner-lucas | 11% | 6%–16% | 15 | 138 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 18% | 11%–25% | 18 | 153 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-call-them-less-logic | 15% | 7%–22% | 15 | 136 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-give-me-a-reason-nf | 14% | 6%–23% | 8 | 138 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-bad-news-merkules | 29% | 19%–38% | 11 | 140 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-richards-tale-set-the-scene-ren | 23% | 10%–38% | 12 | 112 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-caught-you-in-the-bed-dax | 9% | 4%–15% | 11 | 126 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-crash-out-king-iso | 13% | 7%–21% | 12 | 121 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-raw-thoughts-vii-chris-webby | 3% | 0%–7% | 11 | 108 |
| hf-whisper-large-v3-turbo-lora-e3__raw | fresh-jealous-type-doja-cat | 36% | 19%–58% | 10 | 96 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | lose-yourself-v1 | 7% | 3%–11% | 16 | 143 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | the-way-i-am-v1 | 8% | 4%–13% | 15 | 138 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | speedom-em | 22% | 14%–30% | 22 | 220 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | worldwide-choppers-twista | 34% | 23%–47% | 19 | 183 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | rap-god-fast | 39% | 23%–54% | 11 | 108 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | godzilla-v3 | 51% | 37%–65% | 24 | 227 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | suno02 | 42% | 29%–55% | 16 | 118 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | suno01 | 15% | 7%–24% | 14 | 102 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-titanic-gawne | 52% | 42%–63% | 30 | 187 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-nightmares-gawne | 11% | 4%–18% | 15 | 100 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-animals-pt-i-jid | 21% | 13%–31% | 21 | 188 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-sk8-jid | 19% | 8%–33% | 15 | 129 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-behold-jid | 33% | 23%–45% | 20 | 183 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-never-me-token | 15% | 10%–20% | 19 | 167 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-the-ropes-token | 27% | 19%–35% | 32 | 188 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-kumquat-token | 16% | 8%–26% | 17 | 154 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-gta-6-joyner-lucas | 24% | 13%–37% | 13 | 148 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-one-of-them-joyner-lucas | 30% | 22%–38% | 20 | 161 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-monsters-joyner-lucas | 17% | 9%–23% | 15 | 138 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 20% | 14%–26% | 18 | 153 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-call-them-less-logic | 18% | 6%–33% | 15 | 136 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-give-me-a-reason-nf | 13% | 4%–26% | 8 | 138 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-bad-news-merkules | 23% | 15%–31% | 11 | 140 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-richards-tale-set-the-scene-ren | 26% | 12%–42% | 12 | 112 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-caught-you-in-the-bed-dax | 16% | 3%–35% | 11 | 126 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-crash-out-king-iso | 12% | 6%–19% | 12 | 121 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-raw-thoughts-vii-chris-webby | 4% | 0%–10% | 11 | 108 |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | fresh-jealous-type-doja-cat | 36% | 15%–65% | 10 | 96 |
| openrouter-assemblyai-universal-3-6-pro__raw | lose-yourself-v1 | 7% | 2%–12% | 16 | 143 |
| openrouter-assemblyai-universal-3-6-pro__raw | the-way-i-am-v1 | 9% | 3%–18% | 15 | 138 |
| openrouter-assemblyai-universal-3-6-pro__raw | speedom-em | 27% | 19%–37% | 22 | 220 |
| openrouter-assemblyai-universal-3-6-pro__raw | worldwide-choppers-twista | 43% | 33%–56% | 19 | 183 |
| openrouter-assemblyai-universal-3-6-pro__raw | rap-god-fast | 39% | 20%–62% | 11 | 108 |
| openrouter-assemblyai-universal-3-6-pro__raw | godzilla-v3 | 31% | 23%–40% | 24 | 227 |
| openrouter-assemblyai-universal-3-6-pro__raw | suno02 | 44% | 32%–55% | 16 | 118 |
| openrouter-assemblyai-universal-3-6-pro__raw | suno01 | 15% | 7%–25% | 14 | 102 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-titanic-gawne | 59% | 47%–72% | 30 | 187 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-nightmares-gawne | 7% | 2%–13% | 15 | 100 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-animals-pt-i-jid | 26% | 18%–34% | 21 | 188 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-sk8-jid | 30% | 17%–46% | 15 | 129 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-behold-jid | 36% | 26%–47% | 20 | 183 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-never-me-token | 18% | 12%–25% | 19 | 167 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-the-ropes-token | 28% | 20%–38% | 32 | 188 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-kumquat-token | 14% | 6%–23% | 17 | 154 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-gta-6-joyner-lucas | 24% | 13%–37% | 13 | 148 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-one-of-them-joyner-lucas | 30% | 23%–37% | 20 | 161 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-monsters-joyner-lucas | 13% | 6%–20% | 15 | 138 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 21% | 15%–27% | 18 | 153 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-call-them-less-logic | 8% | 3%–14% | 15 | 136 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-give-me-a-reason-nf | 3% | 0%–7% | 8 | 138 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-bad-news-merkules | 17% | 9%–25% | 11 | 140 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-richards-tale-set-the-scene-ren | 21% | 10%–32% | 12 | 112 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-caught-you-in-the-bed-dax | 6% | 2%–11% | 11 | 126 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-crash-out-king-iso | 10% | 3%–19% | 12 | 121 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-raw-thoughts-vii-chris-webby | 2% | 0%–6% | 11 | 108 |
| openrouter-assemblyai-universal-3-6-pro__raw | fresh-jealous-type-doja-cat | 21% | 8%–39% | 10 | 96 |
| openrouter-deepgram-nova-3__raw | lose-yourself-v1 | 9% | 4%–15% | 16 | 143 |
| openrouter-deepgram-nova-3__raw | the-way-i-am-v1 | 25% | 14%–39% | 15 | 138 |
| openrouter-deepgram-nova-3__raw | speedom-em | 78% | 64%–90% | 22 | 220 |
| openrouter-deepgram-nova-3__raw | worldwide-choppers-twista | 100% | 100%–100% | 18 | 176 |
| openrouter-deepgram-nova-3__raw | rap-god-fast | 90% | 75%–100% | 11 | 104 |
| openrouter-deepgram-nova-3__raw | godzilla-v3 | 98% | 94%–100% | 24 | 227 |
| openrouter-deepgram-nova-3__raw | suno02 | 82% | 65%–96% | 16 | 118 |
| openrouter-deepgram-nova-3__raw | suno01 | 72% | 53%–92% | 14 | 100 |
| openrouter-deepgram-nova-3__raw | fresh-titanic-gawne | 100% | 100%–100% | 30 | 187 |
| openrouter-deepgram-nova-3__raw | fresh-nightmares-gawne | 100% | 100%–100% | 15 | 100 |
| openrouter-deepgram-nova-3__raw | fresh-animals-pt-i-jid | 100% | 100%–100% | 21 | 188 |
| openrouter-deepgram-nova-3__raw | fresh-sk8-jid | 100% | 100%–100% | 15 | 129 |
| openrouter-deepgram-nova-3__raw | fresh-behold-jid | 82% | 68%–94% | 20 | 182 |
| openrouter-deepgram-nova-3__raw | fresh-never-me-token | 100% | 100%–100% | 19 | 167 |
| openrouter-deepgram-nova-3__raw | fresh-the-ropes-token | 100% | 100%–100% | 32 | 188 |
| openrouter-deepgram-nova-3__raw | fresh-kumquat-token | 99% | 98%–100% | 17 | 154 |
| openrouter-deepgram-nova-3__raw | fresh-gta-6-joyner-lucas | 100% | 100%–100% | 13 | 148 |
| openrouter-deepgram-nova-3__raw | fresh-one-of-them-joyner-lucas | 100% | 100%–100% | 20 | 161 |
| openrouter-deepgram-nova-3__raw | fresh-monsters-joyner-lucas | 14% | 7%–23% | 15 | 138 |
| openrouter-deepgram-nova-3__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 63% | 42%–82% | 18 | 153 |
| openrouter-deepgram-nova-3__raw | fresh-call-them-less-logic | 48% | 28%–71% | 15 | 136 |
| openrouter-deepgram-nova-3__raw | fresh-give-me-a-reason-nf | 14% | 4%–23% | 8 | 138 |
| openrouter-deepgram-nova-3__raw | fresh-bad-news-merkules | 26% | 18%–34% | 11 | 140 |
| openrouter-deepgram-nova-3__raw | fresh-richards-tale-set-the-scene-ren | 85% | 63%–100% | 12 | 112 |
| openrouter-deepgram-nova-3__raw | fresh-caught-you-in-the-bed-dax | 36% | 11%–64% | 11 | 126 |
| openrouter-deepgram-nova-3__raw | fresh-crash-out-king-iso | 15% | 6%–25% | 12 | 121 |
| openrouter-deepgram-nova-3__raw | fresh-raw-thoughts-vii-chris-webby | 7% | 2%–13% | 11 | 108 |
| openrouter-deepgram-nova-3__raw | fresh-jealous-type-doja-cat | 100% | 100%–100% | 10 | 96 |
| openrouter-elevenlabs-scribe-v2__raw | lose-yourself-v1 | 1% | 0%–2% | 16 | 143 |
| openrouter-elevenlabs-scribe-v2__raw | the-way-i-am-v1 | 2% | 0%–5% | 15 | 138 |
| openrouter-elevenlabs-scribe-v2__raw | speedom-em | 24% | 15%–33% | 22 | 220 |
| openrouter-elevenlabs-scribe-v2__raw | worldwide-choppers-twista | 21% | 12%–32% | 19 | 183 |
| openrouter-elevenlabs-scribe-v2__raw | rap-god-fast | 10% | 3%–19% | 11 | 104 |
| openrouter-elevenlabs-scribe-v2__raw | godzilla-v3 | 9% | 4%–15% | 24 | 227 |
| openrouter-elevenlabs-scribe-v2__raw | suno02 | 36% | 22%–51% | 16 | 118 |
| openrouter-elevenlabs-scribe-v2__raw | suno01 | 11% | 4%–19% | 14 | 102 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-titanic-gawne | 47% | 38%–56% | 30 | 187 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-nightmares-gawne | 11% | 5%–19% | 16 | 102 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-animals-pt-i-jid | 17% | 8%–29% | 21 | 188 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-sk8-jid | 21% | 12%–31% | 15 | 129 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-behold-jid | 30% | 21%–38% | 20 | 183 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-never-me-token | 13% | 7%–19% | 19 | 167 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-the-ropes-token | 26% | 18%–34% | 32 | 188 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-kumquat-token | 10% | 3%–19% | 17 | 154 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-gta-6-joyner-lucas | 22% | 12%–37% | 13 | 148 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-one-of-them-joyner-lucas | 14% | 8%–21% | 20 | 161 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-monsters-joyner-lucas | 10% | 4%–16% | 15 | 138 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 23% | 16%–31% | 18 | 153 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-call-them-less-logic | 3% | 0%–6% | 16 | 137 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-give-me-a-reason-nf | 4% | 0%–11% | 8 | 138 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-bad-news-merkules | 18% | 10%–26% | 11 | 140 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-richards-tale-set-the-scene-ren | 12% | 5%–19% | 12 | 112 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-caught-you-in-the-bed-dax | 2% | 0%–4% | 11 | 126 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-crash-out-king-iso | 12% | 3%–22% | 12 | 121 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-raw-thoughts-vii-chris-webby | 3% | 0%–9% | 11 | 108 |
| openrouter-elevenlabs-scribe-v2__raw | fresh-jealous-type-doja-cat | 20% | 4%–44% | 10 | 96 |
| openrouter-google-chirp-3__raw | lose-yourself-v1 | 4% | 1%–9% | 16 | 143 |
| openrouter-google-chirp-3__raw | the-way-i-am-v1 | 12% | 6%–20% | 15 | 138 |
| openrouter-google-chirp-3__raw | speedom-em | 31% | 22%–41% | 22 | 220 |
| openrouter-google-chirp-3__raw | worldwide-choppers-twista | 41% | 32%–52% | 18 | 176 |
| openrouter-google-chirp-3__raw | rap-god-fast | 41% | 22%–62% | 11 | 108 |
| openrouter-google-chirp-3__raw | godzilla-v3 | 99% | 95%–100% | 24 | 227 |
| openrouter-google-chirp-3__raw | suno02 | 81% | 65%–95% | 16 | 118 |
| openrouter-google-chirp-3__raw | suno01 | 25% | 13%–41% | 14 | 102 |
| openrouter-google-chirp-3__raw | fresh-titanic-gawne | 100% | 100%–100% | 30 | 187 |
| openrouter-google-chirp-3__raw | fresh-nightmares-gawne | 10% | 5%–15% | 15 | 100 |
| openrouter-google-chirp-3__raw | fresh-animals-pt-i-jid | 35% | 24%–46% | 21 | 188 |
| openrouter-google-chirp-3__raw | fresh-sk8-jid | 33% | 22%–45% | 15 | 129 |
| openrouter-google-chirp-3__raw | fresh-behold-jid | 40% | 31%–50% | 20 | 182 |
| openrouter-google-chirp-3__raw | fresh-never-me-token | 19% | 12%–27% | 19 | 167 |
| openrouter-google-chirp-3__raw | fresh-the-ropes-token | 100% | 100%–100% | 32 | 188 |
| openrouter-google-chirp-3__raw | fresh-kumquat-token | 21% | 11%–34% | 17 | 154 |
| openrouter-google-chirp-3__raw | fresh-gta-6-joyner-lucas | 39% | 23%–60% | 13 | 148 |
| openrouter-google-chirp-3__raw | fresh-one-of-them-joyner-lucas | 100% | 100%–100% | 20 | 161 |
| openrouter-google-chirp-3__raw | fresh-monsters-joyner-lucas | 23% | 14%–33% | 15 | 138 |
| openrouter-google-chirp-3__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 44% | 30%–59% | 18 | 153 |
| openrouter-google-chirp-3__raw | fresh-call-them-less-logic | 11% | 6%–17% | 15 | 136 |
| openrouter-google-chirp-3__raw | fresh-give-me-a-reason-nf | 25% | 10%–46% | 8 | 138 |
| openrouter-google-chirp-3__raw | fresh-bad-news-merkules | 19% | 11%–27% | 11 | 140 |
| openrouter-google-chirp-3__raw | fresh-richards-tale-set-the-scene-ren | 40% | 22%–61% | 12 | 112 |
| openrouter-google-chirp-3__raw | fresh-caught-you-in-the-bed-dax | 7% | 2%–12% | 11 | 126 |
| openrouter-google-chirp-3__raw | fresh-crash-out-king-iso | 11% | 3%–22% | 12 | 121 |
| openrouter-google-chirp-3__raw | fresh-raw-thoughts-vii-chris-webby | 3% | 0%–7% | 11 | 108 |
| openrouter-google-chirp-3__raw | fresh-jealous-type-doja-cat | 31% | 11%–56% | 10 | 96 |
| openrouter-google-gemini-3.5-transcribe__raw | lose-yourself-v1 | 5% | 2%–9% | 16 | 143 |
| openrouter-google-gemini-3.5-transcribe__raw | the-way-i-am-v1 | 8% | 2%–16% | 15 | 138 |
| openrouter-google-gemini-3.5-transcribe__raw | speedom-em | 27% | 18%–38% | 22 | 220 |
| openrouter-google-gemini-3.5-transcribe__raw | worldwide-choppers-twista | 100% | 100%–100% | 18 | 176 |
| openrouter-google-gemini-3.5-transcribe__raw | rap-god-fast | 91% | 77%–100% | 11 | 104 |
| openrouter-google-gemini-3.5-transcribe__raw | godzilla-v3 | 98% | 94%–100% | 24 | 227 |
| openrouter-google-gemini-3.5-transcribe__raw | suno02 | 85% | 68%–98% | 16 | 118 |
| openrouter-google-gemini-3.5-transcribe__raw | suno01 | 100% | 100%–100% | 14 | 100 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-titanic-gawne | 100% | 100%–100% | 30 | 187 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-nightmares-gawne | 10% | 2%–22% | 15 | 100 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-animals-pt-i-jid | 100% | 100%–100% | 21 | 188 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-sk8-jid | 26% | 15%–39% | 15 | 129 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-behold-jid | 100% | 100%–100% | 20 | 182 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-never-me-token | 100% | 100%–100% | 19 | 167 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-the-ropes-token | 100% | 100%–100% | 32 | 188 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-kumquat-token | 13% | 6%–20% | 17 | 154 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-gta-6-joyner-lucas | 100% | 100%–100% | 13 | 148 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-one-of-them-joyner-lucas | 100% | 100%–100% | 20 | 161 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-monsters-joyner-lucas | 16% | 9%–23% | 15 | 138 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 27% | 19%–35% | 18 | 153 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-call-them-less-logic | 12% | 6%–18% | 15 | 136 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-give-me-a-reason-nf | 9% | 3%–17% | 8 | 138 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-bad-news-merkules | 19% | 11%–29% | 11 | 140 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-richards-tale-set-the-scene-ren | 18% | 10%–27% | 12 | 112 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-caught-you-in-the-bed-dax | 7% | 2%–12% | 11 | 126 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-crash-out-king-iso | 12% | 3%–25% | 12 | 121 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-raw-thoughts-vii-chris-webby | 4% | 0%–10% | 11 | 108 |
| openrouter-google-gemini-3.5-transcribe__raw | fresh-jealous-type-doja-cat | 100% | 100%–100% | 10 | 96 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | lose-yourself-v1 | 8% | 3%–14% | 16 | 143 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | the-way-i-am-v1 | 11% | 4%–20% | 15 | 138 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | speedom-em | 26% | 19%–36% | 22 | 220 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | worldwide-choppers-twista | 36% | 29%–46% | 18 | 176 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | rap-god-fast | 88% | 70%–100% | 11 | 104 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | godzilla-v3 | 30% | 23%–40% | 24 | 227 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | suno02 | 58% | 44%–72% | 16 | 118 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | suno01 | 16% | 7%–27% | 14 | 102 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-titanic-gawne | 95% | 90%–99% | 30 | 187 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-nightmares-gawne | 9% | 2%–17% | 15 | 100 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-animals-pt-i-jid | 23% | 15%–32% | 21 | 188 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-sk8-jid | 22% | 13%–32% | 15 | 129 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-behold-jid | 28% | 18%–40% | 20 | 182 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-never-me-token | 17% | 11%–24% | 19 | 167 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-the-ropes-token | 51% | 37%–65% | 32 | 188 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-kumquat-token | 14% | 7%–23% | 17 | 154 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-gta-6-joyner-lucas | 24% | 14%–36% | 13 | 148 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-one-of-them-joyner-lucas | 33% | 25%–42% | 20 | 161 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-monsters-joyner-lucas | 12% | 6%–19% | 15 | 138 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 21% | 14%–28% | 18 | 153 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-call-them-less-logic | 10% | 3%–17% | 15 | 136 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-give-me-a-reason-nf | 7% | 1%–14% | 8 | 138 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-bad-news-merkules | 19% | 11%–27% | 11 | 140 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-richards-tale-set-the-scene-ren | 12% | 6%–20% | 12 | 112 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-caught-you-in-the-bed-dax | 6% | 2%–10% | 11 | 126 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-crash-out-king-iso | 8% | 3%–14% | 12 | 121 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-raw-thoughts-vii-chris-webby | 1% | 0%–3% | 11 | 108 |
| openrouter-mistralai-voxtral-small-transcribe-3-0__raw | fresh-jealous-type-doja-cat | 26% | 9%–47% | 10 | 96 |
| openrouter-openai-gpt-4o-transcribe__raw | lose-yourself-v1 | 3% | 1%–7% | 16 | 143 |
| openrouter-openai-gpt-4o-transcribe__raw | the-way-i-am-v1 | 3% | 0%–6% | 15 | 138 |
| openrouter-openai-gpt-4o-transcribe__raw | speedom-em | 27% | 19%–37% | 22 | 220 |
| openrouter-openai-gpt-4o-transcribe__raw | worldwide-choppers-twista | 25% | 14%–38% | 19 | 183 |
| openrouter-openai-gpt-4o-transcribe__raw | rap-god-fast | 94% | 80%–100% | 11 | 104 |
| openrouter-openai-gpt-4o-transcribe__raw | godzilla-v3 | 19% | 15%–24% | 24 | 227 |
| openrouter-openai-gpt-4o-transcribe__raw | suno02 | 47% | 36%–59% | 16 | 118 |
| openrouter-openai-gpt-4o-transcribe__raw | suno01 | 11% | 4%–20% | 14 | 102 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-titanic-gawne | 97% | 93%–100% | 30 | 187 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-nightmares-gawne | 14% | 3%–25% | 15 | 100 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-animals-pt-i-jid | 32% | 21%–44% | 21 | 188 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-sk8-jid | 31% | 20%–44% | 15 | 129 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-behold-jid | 26% | 18%–37% | 20 | 183 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-never-me-token | 14% | 8%–22% | 19 | 167 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-the-ropes-token | 29% | 19%–41% | 32 | 188 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-kumquat-token | 15% | 8%–23% | 17 | 154 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-gta-6-joyner-lucas | 91% | 73%–100% | 13 | 148 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-one-of-them-joyner-lucas | 94% | 84%–100% | 20 | 161 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-monsters-joyner-lucas | 14% | 8%–20% | 15 | 138 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 93% | 81%–100% | 18 | 153 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-call-them-less-logic | 13% | 7%–20% | 15 | 136 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-give-me-a-reason-nf | 4% | 1%–10% | 8 | 138 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-bad-news-merkules | 21% | 11%–30% | 11 | 140 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-richards-tale-set-the-scene-ren | 17% | 7%–27% | 12 | 112 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-caught-you-in-the-bed-dax | 6% | 1%–11% | 11 | 126 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-crash-out-king-iso | 9% | 3%–16% | 12 | 121 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-raw-thoughts-vii-chris-webby | 3% | 0%–9% | 11 | 108 |
| openrouter-openai-gpt-4o-transcribe__raw | fresh-jealous-type-doja-cat | 85% | 64%–100% | 10 | 96 |
| openrouter-openai-gpt-transcribe__raw | lose-yourself-v1 | 3% | 0%–6% | 16 | 143 |
| openrouter-openai-gpt-transcribe__raw | the-way-i-am-v1 | 7% | 2%–13% | 15 | 138 |
| openrouter-openai-gpt-transcribe__raw | speedom-em | 31% | 24%–40% | 22 | 220 |
| openrouter-openai-gpt-transcribe__raw | worldwide-choppers-twista | 34% | 24%–45% | 18 | 176 |
| openrouter-openai-gpt-transcribe__raw | rap-god-fast | 14% | 6%–25% | 11 | 104 |
| openrouter-openai-gpt-transcribe__raw | godzilla-v3 | 15% | 9%–21% | 24 | 227 |
| openrouter-openai-gpt-transcribe__raw | suno02 | 49% | 36%–62% | 16 | 118 |
| openrouter-openai-gpt-transcribe__raw | suno01 | 17% | 7%–28% | 14 | 102 |
| openrouter-openai-gpt-transcribe__raw | fresh-titanic-gawne | 60% | 51%–69% | 30 | 187 |
| openrouter-openai-gpt-transcribe__raw | fresh-nightmares-gawne | 13% | 5%–22% | 15 | 100 |
| openrouter-openai-gpt-transcribe__raw | fresh-animals-pt-i-jid | 27% | 16%–39% | 21 | 188 |
| openrouter-openai-gpt-transcribe__raw | fresh-sk8-jid | 29% | 17%–43% | 15 | 129 |
| openrouter-openai-gpt-transcribe__raw | fresh-behold-jid | 32% | 21%–45% | 20 | 182 |
| openrouter-openai-gpt-transcribe__raw | fresh-never-me-token | 17% | 10%–24% | 19 | 167 |
| openrouter-openai-gpt-transcribe__raw | fresh-the-ropes-token | 31% | 22%–40% | 32 | 188 |
| openrouter-openai-gpt-transcribe__raw | fresh-kumquat-token | 18% | 8%–30% | 17 | 154 |
| openrouter-openai-gpt-transcribe__raw | fresh-gta-6-joyner-lucas | 32% | 18%–49% | 13 | 148 |
| openrouter-openai-gpt-transcribe__raw | fresh-one-of-them-joyner-lucas | 22% | 13%–33% | 20 | 161 |
| openrouter-openai-gpt-transcribe__raw | fresh-monsters-joyner-lucas | 9% | 4%–15% | 15 | 138 |
| openrouter-openai-gpt-transcribe__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 25% | 19%–32% | 18 | 153 |
| openrouter-openai-gpt-transcribe__raw | fresh-call-them-less-logic | 10% | 3%–18% | 15 | 136 |
| openrouter-openai-gpt-transcribe__raw | fresh-give-me-a-reason-nf | 7% | 1%–12% | 8 | 138 |
| openrouter-openai-gpt-transcribe__raw | fresh-bad-news-merkules | 21% | 12%–29% | 11 | 140 |
| openrouter-openai-gpt-transcribe__raw | fresh-richards-tale-set-the-scene-ren | 27% | 16%–37% | 12 | 112 |
| openrouter-openai-gpt-transcribe__raw | fresh-caught-you-in-the-bed-dax | 4% | 1%–7% | 11 | 126 |
| openrouter-openai-gpt-transcribe__raw | fresh-crash-out-king-iso | 10% | 3%–18% | 12 | 121 |
| openrouter-openai-gpt-transcribe__raw | fresh-raw-thoughts-vii-chris-webby | 3% | 0%–7% | 11 | 108 |
| openrouter-openai-gpt-transcribe__raw | fresh-jealous-type-doja-cat | 32% | 12%–57% | 10 | 96 |
| openrouter-x-ai-grok-stt-2.0__raw | lose-yourself-v1 | 13% | 7%–19% | 16 | 143 |
| openrouter-x-ai-grok-stt-2.0__raw | the-way-i-am-v1 | 11% | 5%–17% | 15 | 138 |
| openrouter-x-ai-grok-stt-2.0__raw | speedom-em | 28% | 20%–36% | 22 | 220 |
| openrouter-x-ai-grok-stt-2.0__raw | worldwide-choppers-twista | 23% | 15%–34% | 18 | 176 |
| openrouter-x-ai-grok-stt-2.0__raw | rap-god-fast | 89% | 72%–100% | 11 | 104 |
| openrouter-x-ai-grok-stt-2.0__raw | godzilla-v3 | 36% | 26%–47% | 24 | 227 |
| openrouter-x-ai-grok-stt-2.0__raw | suno02 | 52% | 41%–64% | 16 | 118 |
| openrouter-x-ai-grok-stt-2.0__raw | suno01 | 16% | 7%–27% | 14 | 102 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-titanic-gawne | 55% | 44%–66% | 30 | 187 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-nightmares-gawne | 9% | 3%–16% | 15 | 100 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-animals-pt-i-jid | 29% | 18%–41% | 21 | 188 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-sk8-jid | 31% | 21%–43% | 15 | 129 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-behold-jid | 36% | 25%–48% | 20 | 182 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-never-me-token | 13% | 8%–17% | 19 | 167 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-the-ropes-token | 38% | 29%–49% | 32 | 188 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-kumquat-token | 17% | 7%–29% | 17 | 154 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-gta-6-joyner-lucas | 26% | 15%–39% | 13 | 148 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-one-of-them-joyner-lucas | 29% | 20%–38% | 20 | 161 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-monsters-joyner-lucas | 14% | 8%–21% | 15 | 138 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 26% | 18%–34% | 18 | 153 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-call-them-less-logic | 10% | 4%–15% | 15 | 136 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-give-me-a-reason-nf | 6% | 1%–12% | 8 | 138 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-bad-news-merkules | 20% | 12%–28% | 11 | 140 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-richards-tale-set-the-scene-ren | 23% | 13%–34% | 12 | 112 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-caught-you-in-the-bed-dax | 9% | 3%–15% | 11 | 126 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-crash-out-king-iso | 12% | 6%–20% | 12 | 121 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-raw-thoughts-vii-chris-webby | 3% | 0%–8% | 11 | 108 |
| openrouter-x-ai-grok-stt-2.0__raw | fresh-jealous-type-doja-cat | 33% | 14%–58% | 10 | 96 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | lose-yourself-v1 | 11% | 5%–18% | 16 | 143 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | the-way-i-am-v1 | 16% | 9%–24% | 15 | 138 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | speedom-em | 33% | 25%–41% | 22 | 220 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | worldwide-choppers-twista | 52% | 35%–77% | 18 | 176 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | rap-god-fast | 26% | 13%–40% | 11 | 104 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | godzilla-v3 | 40% | 30%–51% | 24 | 227 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | suno02 | 55% | 45%–65% | 16 | 118 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | suno01 | 12% | 6%–18% | 14 | 100 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-titanic-gawne | 70% | 61%–78% | 30 | 187 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-nightmares-gawne | 12% | 7%–18% | 15 | 100 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-animals-pt-i-jid | 31% | 22%–41% | 21 | 188 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-sk8-jid | 35% | 23%–49% | 15 | 129 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-behold-jid | 35% | 26%–45% | 20 | 182 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-never-me-token | 25% | 16%–33% | 19 | 167 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-the-ropes-token | 55% | 44%–65% | 32 | 188 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-kumquat-token | 23% | 11%–36% | 17 | 154 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-gta-6-joyner-lucas | 28% | 18%–40% | 13 | 148 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-one-of-them-joyner-lucas | 30% | 21%–40% | 20 | 161 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-monsters-joyner-lucas | 16% | 9%–23% | 15 | 138 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-black-walt-street-the-new-breed-tech-n9ne | 24% | 18%–30% | 18 | 153 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-call-them-less-logic | 12% | 5%–21% | 15 | 136 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-give-me-a-reason-nf | 9% | 1%–21% | 8 | 138 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-bad-news-merkules | 21% | 13%–28% | 11 | 140 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-richards-tale-set-the-scene-ren | 31% | 22%–41% | 12 | 112 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-caught-you-in-the-bed-dax | 6% | 2%–11% | 11 | 126 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-crash-out-king-iso | 12% | 6%–21% | 12 | 121 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-raw-thoughts-vii-chris-webby | 5% | 0%–13% | 11 | 108 |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | fresh-jealous-type-doja-cat | 31% | 14%–52% | 10 | 96 |
