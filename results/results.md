# rap-bench results

Cells are `WER · RTF` after lyric normalization; survival threshold 25%. 💀 = WER over threshold, 🐢 = accurate but slower than real time. **max clean rate** = fastest syl/sec transcribed accurately; **max live rate** = fastest syl/sec transcribed accurately AND faster than the rapper (RTF < 1) — the golden standard.

| model | lose-yourself-v1 | the-way-i-am-v1 | speedom-em | rap-god-fast | worldwide-choppers-twista | godzilla-v3 | max clean rate | max live rate |
|---|---|---|---|---|---|---|---|---|
| faster-whisper-large-v3__raw | 6% · 0.73× | 9% · 0.63× | 23% · 0.98× | 28% · 3.09× 💀 | 22% · 1.39× 🐢 | 26% · 1.53× 💀 | 10.0 syl/s | 9.0 syl/s |
| faster-whisper-tiny__raw | 21% · 0.03× | 57% · 0.18× 💀 | 44% · 0.04× 💀 | 100% · 0.27× 💀 | 78% · 0.05× 💀 | 98% · 0.20× 💀 | 5.5 syl/s | 5.5 syl/s |

Segments ordered easy → hard: lose-yourself-v1 (5.5 syl/s), the-way-i-am-v1 (5.5 syl/s), speedom-em (9.0 syl/s), rap-god-fast (9.6 syl/s), worldwide-choppers-twista (10.0 syl/s), godzilla-v3 (10.6 syl/s)
