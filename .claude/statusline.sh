#!/usr/bin/env bash
# Founder statusline: current phase · last save · model.
# Reads Claude Code's statusline JSON on stdin; degrades gracefully if anything is missing.

INPUT=$(cat)

# Project dir from the statusline JSON (fall back to cwd)
DIR=$(printf '%s' "$INPUT" | sed -n 's/.*"project_dir"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')
[ -z "$DIR" ] && DIR=$(printf '%s' "$INPUT" | sed -n 's/.*"current_dir"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')
[ -z "$DIR" ] && DIR="."

# Model display name
MODEL=$(printf '%s' "$INPUT" | sed -n 's/.*"display_name"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')

# Current phase: first heading marked IN PROGRESS in project_status.md, else first phase heading
STATUS_FILE="$DIR/docs/project_status.md"
PHASE=""
if [ -f "$STATUS_FILE" ]; then
  PHASE=$(grep -m1 -E '^### .*(IN PROGRESS|In Progress)' "$STATUS_FILE" | sed -E 's/^### *//; s/\((IN PROGRESS|In Progress)\)//; s/[✅🚀⏳🔧]//g; s/\*\(example\)\*//; s/^ *//; s/ *$//')
  [ -z "$PHASE" ] && PHASE=$(grep -m1 -E '^### ' "$STATUS_FILE" | sed -E 's/^### *//; s/[✅🚀⏳🔧]//g; s/^ *//; s/ *$//' | cut -c1-40)
fi

# Last save point age
SAVE=""
if git -C "$DIR" rev-parse --git-dir >/dev/null 2>&1; then
  LAST=$(git -C "$DIR" log -1 --format=%ct 2>/dev/null)
  if [ -n "$LAST" ]; then
    NOW=$(date +%s); AGE=$(( (NOW - LAST) / 60 ))
    if [ "$AGE" -lt 60 ]; then SAVE="saved ${AGE}m ago"
    elif [ "$AGE" -lt 1440 ]; then SAVE="saved $((AGE / 60))h ago"
    else SAVE="saved $((AGE / 1440))d ago"; fi
  fi
fi

OUT=""
[ -n "$PHASE" ] && OUT="🚀 $PHASE"
[ -n "$SAVE" ] && OUT="${OUT:+$OUT · }💾 $SAVE"
[ -n "$MODEL" ] && OUT="${OUT:+$OUT · }🤖 $MODEL"
[ -z "$OUT" ] && OUT="🧰 BuildWithAI — run /start or /adopt-project"

printf '%s\n' "$OUT"
