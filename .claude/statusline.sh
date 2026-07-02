#!/usr/bin/env bash
# Founder statusline: current phase · last save · model.
# Reads Claude Code's statusline JSON on stdin; degrades gracefully if anything is missing.
# Contract: the active phase is the docs/project_status.md heading marked "(IN PROGRESS)".
# Portability: LC_ALL=C + byte-safe parsing (BSD sed on macOS chokes on emoji classes).
export LC_ALL=C

INPUT=$(cat)

json_field() { # first occurrence wins; good enough for Claude Code's flat payload
  printf '%s' "$INPUT" | grep -o "\"$1\"[[:space:]]*:[[:space:]]*\"[^\"]*\"" | head -1 | sed 's/.*:[[:space:]]*"//; s/"$//'
}

DIR=$(json_field "project_dir")
[ -z "$DIR" ] && DIR=$(json_field "current_dir")
[ -z "$DIR" ] && DIR="."
MODEL=$(json_field "display_name")

# Current phase: the heading marked IN PROGRESS. If none, show no phase —
# a missing segment beats a wrong one.
PHASE=""
STATUS_FILE="$DIR/docs/project_status.md"
if [ -f "$STATUS_FILE" ]; then
  PHASE=$(grep -m1 '^### .*(IN PROGRESS' "$STATUS_FILE" \
    | sed -e 's/^### *//' -e 's/ *(IN PROGRESS.*//' -e 's/^[^A-Za-z0-9]*//' \
    | cut -c1-40)
fi

# Last save point age (single git call; silent when not a repo yet)
SAVE=""
LAST=$(git -C "$DIR" log -1 --format=%ct 2>/dev/null)
if [ -n "$LAST" ]; then
  AGE=$(( ($(date +%s) - LAST) / 60 ))
  if [ "$AGE" -lt 60 ]; then SAVE="saved ${AGE}m ago"
  elif [ "$AGE" -lt 1440 ]; then SAVE="saved $((AGE / 60))h ago"
  else SAVE="saved $((AGE / 1440))d ago"; fi
fi

OUT=""
[ -n "$PHASE" ] && OUT="🚀 $PHASE"
[ -n "$SAVE" ] && OUT="${OUT:+$OUT · }💾 $SAVE"
[ -n "$MODEL" ] && OUT="${OUT:+$OUT · }🤖 $MODEL"
[ -z "$OUT" ] && OUT="🧰 BuildWithAI — run /start or /adopt-project"

printf '%s\n' "$OUT"
