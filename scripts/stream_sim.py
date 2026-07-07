#!/usr/bin/env python3
"""Simulate LIVE captioning of a clip (pseudo-streaming for offline ASR).

    python scripts/stream_sim.py audio/suno02.wav lyrics/suno02.txt
    python scripts/stream_sim.py audio/suno02.wav lyrics/suno02.txt --fast
    python scripts/stream_sim.py audio/suno02.wav lyrics/suno02.txt --backend parakeet

Audio "arrives" in real time; every --hop seconds we re-decode the last
--window seconds and commit output that has fallen --guard seconds behind
the live edge. Decodes run serially: one that overruns the hop delays all
later ones — that's caption lag, tracked per hop.

Modes:
  default          mlx-whisper, word timestamps, full temperature fallback
  --fast           mlx-whisper, temperature=0 (no fallback storms), commits
                   whole segments instead of words (no DTW alignment cost)
  --backend parakeet   parakeet-mlx via per-window temp wavs; sentence commits

Reports decode latency, worst caption lag, live-committed WER vs the
reference, and writes <clip>-live[-tag].srt from committed output.

Finding this script exists to measure (see LOG.md): batch RTF wildly
overstates streaming viability for whisper — every window is padded to
30s, and difficulty-triggered fallback re-decodes happen per window.
"""

import argparse
import sys
import tempfile
import time
import wave
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from rapbench.normalize import normalize

SR = 16000


def load_audio(path: str):
    import numpy as np

    with wave.open(path, "rb") as w:
        assert w.getframerate() == SR and w.getnchannels() == 1
        pcm = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16)
    return pcm.astype(np.float32) / 32768.0


def fmt_ts(t: float) -> str:
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def make_decoder(args):
    """Returns decode(chunk, ws) -> list of {w, start, end} in absolute secs.

    For the stateful parakeet-native backend, chunk is only the NEW audio
    (one hop) and the returned list is ALL tokens decoded so far — the
    stream object carries encoder cache and decoder state across calls.
    """
    if args.backend == "parakeet-native":
        import mlx.core as mx
        import numpy as np
        from parakeet_mlx import from_pretrained

        model = from_pretrained("mlx-community/parakeet-tdt-0.6b-v2")
        # warm up Metal kernels on a throwaway transcribe, NOT on the stream
        with tempfile.NamedTemporaryFile(suffix=".wav") as f:
            with wave.open(f.name, "wb") as w:
                w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
                w.writeframes(np.zeros(SR, dtype=np.int16).tobytes())
            model.transcribe(f.name)
        stream = model.transcribe_stream(context_size=(256, 256), depth=args.depth)
        stream.__enter__()

        def decode(chunk, ws):
            stream.add_audio(mx.array(chunk))
            out = []
            for sent in stream.result.sentences:
                for tok in sent.tokens:
                    out.append({"w": tok.text.strip(), "start": tok.start,
                                "end": tok.start + tok.duration,
                                "_new_word": tok.text.startswith(" ")})
            return out

        return decode

    if args.backend == "parakeet":
        from parakeet_mlx import from_pretrained

        model = from_pretrained("mlx-community/parakeet-tdt-0.6b-v2")

        def decode(chunk, ws):
            import numpy as np

            with tempfile.NamedTemporaryFile(suffix=".wav") as f:
                with wave.open(f.name, "wb") as w:
                    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
                    w.writeframes((chunk * 32767).astype(np.int16).tobytes())
                result = model.transcribe(f.name)
            out = []
            for sent in getattr(result, "sentences", []) or []:
                for tok in getattr(sent, "tokens", []) or []:
                    out.append({"w": tok.text.strip(), "start": ws + tok.start,
                                "end": ws + tok.start + tok.duration})
            if not out and result.text.strip():
                out = [{"w": result.text.strip(), "start": ws, "end": ws + len(chunk) / SR}]
            return out

        import numpy as np

        decode(np.zeros(SR, dtype=np.float32), 0.0)  # warm up
        return decode

    import mlx_whisper
    import numpy as np

    repo = "mlx-community/whisper-large-v3-turbo"
    kwargs = {"path_or_hf_repo": repo, "language": "en"}
    if args.fast:
        kwargs["temperature"] = 0.0  # no fallback ladder
    else:
        kwargs["word_timestamps"] = True

    def decode(chunk, ws):
        result = mlx_whisper.transcribe(chunk, **kwargs)
        out = []
        for seg in result["segments"]:
            if args.fast:
                if seg["text"].strip():
                    out.append({"w": seg["text"].strip(), "start": ws + seg["start"],
                                "end": ws + seg["end"]})
            else:
                for w in seg.get("words", []):
                    out.append({"w": w["word"].strip(), "start": ws + w["start"],
                                "end": ws + w["end"]})
        return out

    mlx_whisper.transcribe(np.zeros(SR, dtype=np.float32), path_or_hf_repo=repo)  # warm up
    return decode


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("wav"); p.add_argument("ref")
    p.add_argument("--hop", type=float, default=0.5)
    p.add_argument("--window", type=float, default=8.0)
    p.add_argument("--guard", type=float, default=1.5)
    p.add_argument("--fast", action="store_true")
    p.add_argument("--depth", type=int, default=2, help="parakeet-native: encoder layers with exact KV cache")
    p.add_argument("--backend", choices=["mlx", "parakeet", "parakeet-native"], default="mlx")
    args = p.parse_args()

    audio = load_audio(args.wav)
    dur = len(audio) / SR
    decode = make_decoder(args)
    stateful = args.backend == "parakeet-native"

    committed, committed_until = [], 0.0
    n_committed = 0  # stateful backends: index into the stable token stream
    latencies, lags = [], []
    clock = 0.0
    t = args.hop
    while t <= dur + 1e-9:
        ws = t - args.hop if stateful else max(0.0, t - args.window)
        chunk = audio[int(ws * SR): int(t * SR)]
        t0 = time.perf_counter()
        items = decode(chunk, ws)
        elapsed = time.perf_counter() - t0
        latencies.append(elapsed)
        clock = max(clock, t) + elapsed
        lags.append(clock - t)
        if stateful:
            # items = ALL subword tokens so far; the tail (< guard old) is
            # still being revised, the prefix is stable. Commit by index.
            stable = [it for it in items if it["end"] <= t - args.guard]
            committed.extend(stable[n_committed:])
            n_committed = len(stable)
        else:
            for it in items:
                if it["end"] <= t - args.guard and it["start"] >= committed_until - 0.05:
                    committed.append(it)
                    committed_until = max(committed_until, it["end"])
        t += args.hop

    if stateful:
        # regroup subword tokens into words on leading-space boundaries so
        # WER and SRT cues operate on words, text joined WITHOUT extra spaces
        words, cur = [], None
        for tok in committed:
            if cur is None or tok["_new_word"]:
                if cur:
                    words.append(cur)
                cur = dict(tok)
            else:
                cur["w"] += tok["w"]
                cur["end"] = tok["end"]
        if cur:
            words.append(cur)
        committed = words

    lat = sorted(latencies)
    tag = args.backend + ("-fast" if args.fast else "")
    overruns = sum(1 for x in latencies if x > args.hop)
    print(f"[{tag}] {len(latencies)} decodes over {dur:.1f}s (hop {args.hop}s, window {args.window}s)")
    print(f"[{tag}] latency mean {sum(lat)/len(lat):.3f}s  p95 {lat[int(0.95 * len(lat))]:.3f}s  max {lat[-1]:.3f}s")
    print(f"[{tag}] worst caption lag {max(lags):.2f}s behind live; overruns {overruns}/{len(latencies)}")

    import jiwer

    live_text = " ".join(w["w"] for w in committed)
    ref = "\n".join(l for l in Path(args.ref).read_text().splitlines() if not l.startswith("#"))
    print(f"[{tag}] live-committed WER {jiwer.wer(normalize(ref), normalize(live_text)):.0%} "
          f"({len(committed)} commits)")

    cues, cur = [], []
    for w in committed:
        if cur and (w["start"] - cur[-1]["end"] > 0.6 or len(cur) >= 7):
            cues.append(cur); cur = []
        cur.append(w)
    if cur:
        cues.append(cur)
    srt = Path(args.wav).with_suffix("").as_posix() + f"-live-{tag}.srt"
    with open(srt, "w") as f:
        for i, cue in enumerate(cues, 1):
            f.write(f"{i}\n{fmt_ts(cue[0]['start'])} --> {fmt_ts(cue[-1]['end'])}\n")
            f.write(" ".join(w["w"] for w in cue) + "\n\n")
    print(f"[{tag}] wrote {srt} ({len(cues)} cues)")


if __name__ == "__main__":
    main()
