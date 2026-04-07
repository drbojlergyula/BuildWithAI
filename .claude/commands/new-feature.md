# /new-feature Command

This file is the Claude Code packaging of the shared `new-feature` workflow defined in `docs/assistant_workflows.md`.

## When to use it

Run `/new-feature` any time you want to add something to the product that is not already in the spec.

## Instructions

1. Read `docs/assistant_workflows.md` and follow the shared `new-feature` workflow exactly.
2. Treat that file as the canonical behavior. If anything in this command appears to conflict with it, follow `docs/assistant_workflows.md`.
3. Use Claude-native interaction patterns:
   - Ask concise questions
   - Confirm the user stories before writing them into the spec
   - Update `docs/architecture.md` if the feature changes system design
4. Confirm when the feature has been added and the project is ready for implementation.

## Note

Keep this file thin on purpose. The shared workflow in `docs/assistant_workflows.md` is the source of truth for behavior across Claude Code, Codex, and GitHub Copilot.
