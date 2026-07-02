---
name: update-docs-and-commit
description: Update the changelog, project status, and any affected docs to reflect recent work, then commit everything to git with a clear message. Use after finishing any meaningful piece of work.
allowed-tools: Bash(git add:*), Bash(git commit:*), Bash(git status:*), Bash(git log:*), Bash(git diff:*), Bash(echo:*)
---

# /update-docs-and-commit — Save Your Progress

Keeps the docs and git history aligned after meaningful work. This is the *full* save: docs refreshed first, then everything committed. (For an instant, code-only save, use `/save-point`.)

## Current repository state

- Working tree: !`git status --short`
- Recent commits: !`git log --oneline -5 2>/dev/null || echo "(no commits yet)"`

## Steps

1. **Work out what changed.** Use the repository state above plus the conversation so far. If it is still unclear what was accomplished, ask the user — one question, plain English.

2. **Update the docs:**
   - `docs/changelog.md` — add a dated entry (### Added / Changed / Fixed / Removed) describing the work in user-visible terms.
   - `docs/project_status.md` — update phase progress; mark finished items done, refresh "Last Updated".
   - `docs/project_spec.md` or `docs/architecture.md` — only if the work changed what the product does or how it is built.
   - `docs/decisions.md` — if any real decision was made in this piece of work (trade-off chosen, approach picked, something cut), add one line at the top: `date — decision — why`. This log is maintained by you, never by the user.
   - If a decision was made that is still sitting in `docs/brainstorm.md`, promote it into the spec and archive the brainstorm entry.

3. **Commit.**
   - Stage the relevant files (`git add`).
   - Write a clear, descriptive commit message: what changed and why, in one line a teammate would understand. Do not mention the AI assistant in the message.
   - Commit.

4. **Confirm.** Tell the user in one or two sentences what was documented and committed. If anything was intentionally left uncommitted, say so.

## Rules

- Never commit secrets, credentials, or `.env` files. If one is staged, stop and warn the user.
- If there is nothing meaningful to document, say so instead of inventing an entry.
- One commit per invocation unless the user asks otherwise.
