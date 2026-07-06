#!/usr/bin/env bash
# Lyric verification cockpit: tmux split with looping playback + editor.
#
#   scripts/verify.sh rap-god-fast          # plays at 0.5x (default)
#   scripts/verify.sh godzilla-v3 1.0       # full speed
#
# Left pane: the clip on loop at the given rate. Right pane: the lyric file
# in $EDITOR (nano if unset). Fix what's actually rapped, delete the
# TODO-VERIFY line, save, quit — then Ctrl-b x to kill the player pane.
set -euo pipefail
cd "$(dirname "$0")/.."

id="${1:?usage: scripts/verify.sh <segment-id> [playback-rate]}"
rate="${2:-0.5}"
wav="audio/$id.wav"
txt="lyrics/$id.txt"
[ -f "$wav" ] || { echo "missing $wav — run scripts/fetch.py first" >&2; exit 1; }
[ -f "$txt" ] || { echo "missing $txt — run scripts/draft_lyrics.py first" >&2; exit 1; }

# Not inside tmux yet: start a session that re-runs this script inside it.
if [ -z "${TMUX:-}" ]; then
  exec tmux new-session -s "verify-$id" "$0" "$id" "$rate"
fi

tmux split-window -hb -l 30% "printf '♪ %s at %sx (Ctrl-b x to close)\n' '$id' '$rate'; while :; do afplay -r '$rate' '$wav'; sleep 1; done"
tmux last-pane
exec "${EDITOR:-nano}" "$txt"
