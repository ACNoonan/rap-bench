# rap-bench results

Cells are `WER · RTF` after lyric normalization; survival threshold 25%. 💀 = WER over threshold, 🐢 = accurate but slower than real time. **max clean rate** = fastest syl/sec transcribed accurately; **max live rate** = fastest syl/sec transcribed accurately AND faster than the rapper (RTF < 1) — the golden standard.

| model | synth01-acap-r5.0 | synth01-beat-r5.0 | lose-yourself-v1 | the-way-i-am-v1 | synth01-acap-r6.5 | synth01-beat-r6.5 | synth01-acap-r8.0 | synth01-beat-r8.0 | speedom-em | synth01-acap-r9.5 | synth01-beat-r9.5 | rap-god-fast | worldwide-choppers-twista | godzilla-v3 | synth01-acap-r11.0 | synth01-beat-r11.0 | max clean rate | max live rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| faster-whisper-distil-large-v3__raw | — | — | 10% · 0.16× | 14% · 0.15× | — | — | — | — | 30% · 0.19× 💀 | — | — | 31% · 0.21× 💀 | 50% · 0.20× 💀 | 58% · 0.32× 💀 | — | — | 5.5 syl/s | 5.5 syl/s |
| faster-whisper-large-v3__raw | — | — | 6% · 0.73× | 9% · 0.63× | — | — | — | — | 23% · 0.98× | — | — | 28% · 3.09× 💀 | 22% · 1.39× 🐢 | 26% · 1.53× 💀 | — | — | 10.0 syl/s | 9.0 syl/s |
| faster-whisper-large-v3__vocals | — | — | 10% · 0.77× | 21% · 0.69× | — | — | — | — | 22% · 1.29× 🐢 | — | — | 22% · 1.09× 🐢 | 33% · 1.62× 💀 | 25% · 1.78× 🐢 | — | — | 10.6 syl/s | 5.5 syl/s |
| faster-whisper-small__raw | — | — | 11% · 0.14× | 18% · 0.14× | — | — | — | — | 33% · 0.21× 💀 | — | — | 32% · 0.28× 💀 | 61% · 0.98× 💀 | 38% · 0.42× 💀 | — | — | 5.5 syl/s | 5.5 syl/s |
| faster-whisper-tiny__raw | — | — | 21% · 0.03× | 57% · 0.18× 💀 | — | — | — | — | 44% · 0.04× 💀 | — | — | 100% · 0.27× 💀 | 78% · 0.05× 💀 | 98% · 0.20× 💀 | — | — | 5.5 syl/s | 5.5 syl/s |
| faster-whisper-tiny__vocals | — | — | 24% · 0.03× | 57% · 0.20× 💀 | — | — | — | — | 44% · 0.04× 💀 | — | — | 64% · 0.06× 💀 | 74% · 0.25× 💀 | 59% · 0.06× 💀 | — | — | 5.5 syl/s | 5.5 syl/s |
| faster-whisper-turbo__raw | — | — | 6% · 0.21× | 10% · 0.18× | — | — | — | — | 21% · 0.24× | — | — | 88% · 0.14× 💀 | 33% · 0.58× 💀 | 34% · 0.40× 💀 | — | — | 9.0 syl/s | 9.0 syl/s |
| hf-UsefulSensors-moonshine-base__raw | — | — | 30% · 0.25× 💀 | 29% · 0.10× 💀 | — | — | — | — | 75% · 0.09× 💀 | — | — | 28% · 0.12× 💀 | 68% · 0.10× 💀 | 72% · 0.10× 💀 | — | — | 0.0 syl/s | 0.0 syl/s |
| hf-facebook-wav2vec2-large-960h-lv60-self__raw | — | — | 59% · 0.06× 💀 | 91% · 0.04× 💀 | — | — | — | — | 78% · 0.03× 💀 | — | — | 81% · 0.03× 💀 | 86% · 0.04× 💀 | 88% · 0.03× 💀 | — | — | 0.0 syl/s | 0.0 syl/s |
| mlx-whisper-mlx-community-whisper-large-v3-turbo__raw | 6% · 0.20× | 6% · 0.16× | 7% · 0.04× | 8% · 0.04× | 7% · 0.08× | 6% · 0.06× | 5% · 0.07× | 5% · 0.08× | 22% · 0.05× | 8% · 0.10× | 8% · 0.09× | 39% · 0.05× 💀 | 34% · 0.14× 💀 | 51% · 0.05× 💀 | 7% · 0.12× | 8% · 0.20× | 11.0 syl/s | 11.0 syl/s |
| parakeet-mlx-community-parakeet-tdt-0.6b-v2__raw | 5% · 0.02× | 5% · 0.02× | 11% · 0.06× | 16% · 0.02× | 5% · 0.04× | 6% · 0.02× | 6% · 0.02× | 8% · 0.02× | 33% · 0.02× 💀 | 10% · 0.03× | 12% · 0.03× | 26% · 0.03× 💀 | 52% · 0.02× 💀 | 40% · 0.03× 💀 | 22% · 0.06× | 28% · 0.04× 💀 | 11.0 syl/s | 11.0 syl/s |

Segments ordered easy → hard: synth01-acap-r5.0 (5.0 syl/s), synth01-beat-r5.0 (5.0 syl/s), lose-yourself-v1 (5.5 syl/s), the-way-i-am-v1 (5.5 syl/s), synth01-acap-r6.5 (6.5 syl/s), synth01-beat-r6.5 (6.5 syl/s), synth01-acap-r8.0 (8.0 syl/s), synth01-beat-r8.0 (8.0 syl/s), speedom-em (9.0 syl/s), synth01-acap-r9.5 (9.5 syl/s), synth01-beat-r9.5 (9.5 syl/s), rap-god-fast (9.6 syl/s), worldwide-choppers-twista (10.0 syl/s), godzilla-v3 (10.6 syl/s), synth01-acap-r11.0 (11.0 syl/s), synth01-beat-r11.0 (11.0 syl/s)
