# /start Command

This file is the Claude Code packaging of the shared `start` workflow defined in `docs/assistant_workflows.md`.

## When to use it

Run `/start` once, at the very beginning of a new project, before any code is written.

## Instructions

1. Read `docs/assistant_workflows.md` and follow the shared `start` workflow exactly.
2. Treat that file as the canonical behavior. If anything in this command appears to conflict with it, follow `docs/assistant_workflows.md`.
3. Apply the workflow using Claude-native interaction patterns:
   - Ask one or two questions at a time
   - Use plain English
   - Reflect back what you understood before moving on when needed
   - Make assumptions explicit
4. Update the project files named by the shared workflow.
5. When wrapping up, remind the user that in Claude they can continue with:
   - `/new-feature`
   - `/update-docs-and-commit`
   - "run the spec-reviewer agent"
   - "run the project-advisor agent"

## Note

Keep this file thin on purpose. The shared workflow in `docs/assistant_workflows.md` is the source of truth for behavior across Claude Code, Codex, and GitHub Copilot.
