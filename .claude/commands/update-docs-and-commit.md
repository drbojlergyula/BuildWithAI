# /update-docs-and-commit Command

This file is the Claude Code packaging of the shared `update-docs-and-commit` workflow defined in `docs/assistant_workflows.md`.

## When to use it

Run `/update-docs-and-commit` after completing a meaningful piece of work such as a feature, bug fix, or milestone.

## Instructions

1. Read `docs/assistant_workflows.md` and follow the shared `update-docs-and-commit` workflow exactly.
2. Treat that file as the canonical behavior. If anything in this command appears to conflict with it, follow `docs/assistant_workflows.md`.
3. Use Claude-native interaction patterns:
   - Ask what changed if it is not already clear
   - Update the relevant docs before committing
   - Write a clear commit message
4. Confirm when the docs and git history are up to date.

## Note

Keep this file thin on purpose. The shared workflow in `docs/assistant_workflows.md` is the source of truth for behavior across Claude Code, Codex, and GitHub Copilot.
