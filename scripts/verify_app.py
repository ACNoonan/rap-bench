"""Browser cockpit for verifying fresh-tier lyrics by ear (DESIGN.md v3, step 2).

    .venv/bin/python scripts/verify_app.py [--port 8791]
    then open http://127.0.0.1:8791

The page asks for the bets first, then shows one clip at a time: looping
playback at reduced speed, an A-B loop for hard passages, and the lyric draft
in an editor. It never shows a model transcript or a score.

Saving writes lyrics/<id>.txt in the format score.py reads: the original
comment header, an optional "# NOTE:" line, the TODO-VERIFY line while the
clip is unverified, then the lyrics. State lives in lyrics/_verify/:

    drafts/<id>.txt   the LRCLIB draft as it was before the first edit
    bet.json          the bets, written once
    log.jsonl         one row per save: id, action, seconds, timing_ok, note

Only segments with population "fresh" are served.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import time
from datetime import date
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
LYRICS = ROOT / "lyrics"
AUDIO = ROOT / "audio"
STATE = LYRICS / "_verify"
DRAFTS = STATE / "drafts"
PAGE = Path(__file__).with_name("verify_app.html")
TODO = "TODO-VERIFY"
INSTRUCTION = ("# Read along with", "# then delete the TODO-VERIFY")


def fresh_segments() -> list[dict]:
    segs = yaml.safe_load((ROOT / "segments.yaml").read_text())["segments"]
    fresh = [s for s in segs if s.get("population") == "fresh"]
    return sorted(fresh, key=lambda s: s["syl_per_sec"])


def parse(text: str) -> dict:
    lines = text.splitlines()
    header = [l for l in lines if l.startswith("#")]
    note = next((l[len("# NOTE:"):].strip() for l in header if l.startswith("# NOTE:")), "")
    body = [l for l in lines if not l.startswith("#") and l.strip() != TODO]
    return {
        "header": [l for l in header if not l.startswith(("# NOTE:", "# Verified by ear"))],
        "note": note,
        "verified": TODO not in text,
        "body": "\n".join(body).strip("\n"),
    }


def snapshot(seg_id: str) -> Path:
    """Keep the pre-edit draft. Taken once, and only while the file is still a draft."""
    src, dst = LYRICS / f"{seg_id}.txt", DRAFTS / f"{seg_id}.txt"
    if not dst.exists() and TODO in src.read_text():
        DRAFTS.mkdir(parents=True, exist_ok=True)
        dst.write_text(src.read_text())
    return dst


def write_lyrics(seg_id: str, body: str, note: str, verified: bool) -> None:
    draft = DRAFTS / f"{seg_id}.txt"
    base = parse((draft if draft.exists() else LYRICS / f"{seg_id}.txt").read_text())
    header = base["header"]
    if verified:
        header = [l for l in header if not l.startswith(INSTRUCTION)]
        header.append(f"# Verified by ear {date.today().isoformat()} (scripts/verify_app.py).")
    if note:
        header.append("# NOTE: " + " ".join(note.split()))
    out = header + ([] if verified else [TODO]) + [l.rstrip() for l in body.strip("\n").splitlines()]
    path = LYRICS / f"{seg_id}.txt"
    tmp = path.with_suffix(".txt.tmp")
    tmp.write_text("\n".join(out) + "\n")
    os.replace(tmp, path)


def log(row: dict) -> None:
    STATE.mkdir(parents=True, exist_ok=True)
    with open(STATE / "log.jsonl", "a") as f:
        f.write(json.dumps({"t": round(time.time(), 1), **row}) + "\n")


class H(BaseHTTPRequestHandler):
    segs: dict[str, dict] = {}

    def log_message(self, *a):
        pass

    def _send(self, code: int, ctype: str, b: bytes, extra: dict | None = None):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(b)))
        self.send_header("Cache-Control", "no-store")
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(b)

    def _json(self, obj, code=200):
        self._send(code, "application/json", json.dumps(obj).encode())

    def _bet_done(self) -> bool:
        return (STATE / "bet.json").exists()

    def _audio(self, seg_id: str):
        f = AUDIO / f"{seg_id}.wav"
        if seg_id not in self.segs or not f.exists():
            return self._json({"error": "no clip"}, 404)
        data = f.read_bytes()
        m = re.match(r"bytes=(\d*)-(\d*)", self.headers.get("Range", ""))
        if m and (m.group(1) or m.group(2)):
            n = len(data)
            if m.group(1):
                a, b = int(m.group(1)), int(m.group(2)) if m.group(2) else n - 1
            else:
                a, b = max(0, n - int(m.group(2))), n - 1
            b = min(b, n - 1)
            if a > b:
                return self._send(416, "text/plain", b"", {"Content-Range": f"bytes */{n}"})
            return self._send(206, "audio/wav", data[a:b + 1],
                              {"Content-Range": f"bytes {a}-{b}/{n}", "Accept-Ranges": "bytes"})
        self._send(200, "audio/wav", data, {"Accept-Ranges": "bytes"})

    def do_GET(self):
        path, _, q = self.path.partition("?")
        args = dict(kv.split("=", 1) for kv in q.split("&") if "=" in kv)
        if path == "/":
            return self._send(200, "text/html; charset=utf-8", PAGE.read_bytes())
        if path.startswith("/audio/") and path.endswith(".wav"):
            return self._audio(path[len("/audio/"):-len(".wav")])
        if path == "/api/state":
            clips = []
            for s in self.segs.values():
                p = parse((LYRICS / f"{s['id']}.txt").read_text())
                clips.append({"id": s["id"], "artist": s["artist"], "track": s["track"],
                              "rate": s["syl_per_sec"], "dur": round(s["end"] - s["start"], 1),
                              "verified": p["verified"]})
            return self._json({"bet": self._bet_done(), "clips": clips})
        if path == "/api/clip":
            seg_id = args.get("id", "")
            if seg_id not in self.segs:
                return self._json({"error": "unknown clip"}, 404)
            if not self._bet_done():
                return self._json({"error": "bet first"}, 403)
            snapshot(seg_id)
            p = parse((LYRICS / f"{seg_id}.txt").read_text())
            s = self.segs[seg_id]
            return self._json({"id": seg_id, "artist": s["artist"], "track": s["track"],
                               "rate": s["syl_per_sec"], "url": s.get("url"),
                               "body": p["body"], "note": p["note"], "verified": p["verified"]})
        self._json({"error": "not found"}, 404)

    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0))
        try:
            body = json.loads(self.rfile.read(n) or b"{}")
        except json.JSONDecodeError:
            return self._json({"error": "bad json"}, 400)
        if self.path == "/api/bet":
            if self._bet_done():
                return self._json({"error": "bet already recorded"}, 409)
            STATE.mkdir(parents=True, exist_ok=True)
            (STATE / "bet.json").write_text(json.dumps(
                {"date": date.today().isoformat(), "t": round(time.time(), 1), **body}, indent=1) + "\n")
            return self._json({"ok": True})
        seg_id = body.get("id", "")
        if seg_id not in self.segs:
            return self._json({"error": "unknown clip"}, 404)
        if not self._bet_done():
            return self._json({"error": "bet first"}, 403)
        if self.path == "/api/reset":
            draft = snapshot(seg_id)
            if not draft.exists():
                return self._json({"error": "no draft snapshot for this clip"}, 409)
            (LYRICS / f"{seg_id}.txt").write_text(draft.read_text())
            log({"id": seg_id, "action": "reset"})
            return self._json({"ok": True})
        if self.path == "/api/save":
            text, verified = str(body.get("body", "")), bool(body.get("verified"))
            if not text.strip():
                return self._json({"error": "the lyrics are empty"}, 400)
            if "TODO" in text or any(l.startswith("#") for l in text.splitlines()):
                return self._json({"error": 'remove "TODO" and any line starting with # from the lyrics'}, 400)
            snapshot(seg_id)
            write_lyrics(seg_id, text, str(body.get("note", "")).strip(), verified)
            log({"id": seg_id, "action": body.get("action", "save"), "verified": verified,
                 "timing_ok": body.get("timing_ok"), "note": str(body.get("note", "")).strip() or None,
                 "seconds": body.get("seconds"), "speed": body.get("speed")})
            return self._json({"ok": True})
        self._json({"error": "not found"}, 404)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8791)
    a = ap.parse_args()
    H.segs = {s["id"]: s for s in fresh_segments()}
    missing = [i for i in H.segs if not (AUDIO / f"{i}.wav").exists() or not (LYRICS / f"{i}.txt").exists()]
    if missing:
        raise SystemExit(f"missing audio or lyrics for: {', '.join(missing)}")
    print(f"{len(H.segs)} fresh clips on http://127.0.0.1:{a.port}", flush=True)
    ThreadingHTTPServer(("127.0.0.1", a.port), H).serve_forever()


if __name__ == "__main__":
    main()
