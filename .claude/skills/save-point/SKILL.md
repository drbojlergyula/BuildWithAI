---
name: save-point
description: Save the project's current state — like a save point in a video game. Commits all current work to git with a plain-English label so the user can always come back to this exact moment. Use when the user wants to save progress quickly.
argument-hint: [optional label, e.g. "order form working"]
allowed-tools: Bash(git add:*), Bash(git commit:*), Bash(git status:*), Bash(git log:*), Bash(head:*), Bash(echo:*)
---

# /save-point — Save Your Game

A fast, safe "save game" for the whole project. No git knowledge needed. (For a fuller save that also refreshes the docs, use `/update-docs-and-commit` — this one is the quick version.)

## Current state

- Changes since last save: !`git status --short 2>/dev/null | head -20`
- Recent save points: !`git log --oneline -5 2>/dev/null || echo "(no save points yet)"`

## Steps

1. If there are no changes to save, say so ("Everything is already saved — last save point: [message]") and stop.
2. Stage all changes (`git add -A`) — but if anything looks like a secret (`.env`, keys, credentials), stop and warn the user before committing anything, exactly as `/update-docs-and-commit` would.
3. Commit with a clear label: use the user's label if given, otherwise write one that describes the state in plain words ("Order form working, confirmation message added").
4. Confirm in one friendly line: "💾 Save point created: *[label]*. You can always come back to this exact state with `/go-back`."

## Rules

- Never commit secrets or `.env` files.
- Keep it fast — no doc editing, no questions unless something looks wrong. This command should feel instant.
