---
name: go-back
description: Return the project to an earlier save point — safely. Shows recent save points in plain English, keeps a rescue copy of the current state, then restores the chosen one. Use when something went wrong and the user wants to rewind.
disable-model-invocation: true
allowed-tools: Bash(git log:*), Bash(git status:*), Bash(git branch:*), Bash(git stash:*)
---

# /go-back — Rewind to a Save Point

Time travel with a safety net. The user never loses work: before rewinding, the current state is preserved on a rescue branch, so even "going back" can be undone.

## Recent save points

!`git log --oneline -10 2>/dev/null || echo "(no save points yet)"`

## Steps

1. **Show the options.** Present the recent save points as a numbered list in plain English (label + how long ago). Ask which one to return to. If the user already said (e.g. "before the payment change"), match it and confirm.

2. **Check for unsaved work.** If `git status` shows uncommitted changes, offer to create a save point first (recommended) or explicitly agree with the user that those changes are abandoned.

3. **Create the rescue copy.** Before touching anything: `git branch rescue/<date>-<short-label>` on the current commit. Tell the user: "Your current state is preserved as *rescue/...* — going back is itself reversible."

4. **Rewind.** Restore the working tree to the chosen save point (`git reset --hard <commit>`). Only after step 3, and only with the user's explicit confirmation of the chosen save point.

5. **Confirm.** "⏪ You are back at *[label]* ([date]). If this was a mistake, say 'go back to the rescue copy' and I'll restore it."

## Rules

- Never rewind without the rescue branch existing first. No exceptions.
- Never use the words "reset --hard" with the user — say "return to the save point".
- If the project was already pushed to GitHub and the rewind would rewrite shared history, explain that in one plain sentence and get explicit approval before proceeding.
- This command is user-invoked only — never trigger it on your own initiative.
