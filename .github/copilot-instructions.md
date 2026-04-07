# GitHub Copilot Repository Instructions

This repository is a multi-assistant project template. Follow the shared workflow definitions in `docs/assistant_workflows.md`.

## Compatibility Goal

Users may refer to Claude Code conventions such as `/start`, `/new-feature`, `project-advisor`, `spec-reviewer`, or `doc-sync-check`.

When they do, translate those requests into the shared workflow instead of saying the command is unsupported.

Do not imply that GitHub Copilot supports the same native slash-command mechanism as Claude in this repository. Treat those names as workflow aliases.

## How To Behave

- Treat `docs/assistant_workflows.md` as the canonical workflow definition.
- Keep `docs/project_spec.md`, `docs/architecture.md`, `docs/brainstorm.md`, `docs/project_status.md`, and `docs/changelog.md` up to date.
- Ask one or two setup questions at a time.
- Use plain English.
- Make assumptions explicit.
- Prefer updating docs over leaving important decisions only in chat.

## Copilot-Specific Mapping

- `start` maps to `.github/prompts/start.prompt.md`
- `new-feature` maps to `.github/prompts/new-feature.prompt.md`
- `update-docs-and-commit` maps to `.github/prompts/update-docs-and-commit.prompt.md`
- `project-advisor` maps to `.github/prompts/project-advisor.prompt.md`
- `spec-reviewer` maps to `.github/prompts/spec-reviewer.prompt.md`
- `doc-sync-check` maps to `.github/prompts/doc-sync-check.prompt.md`

Prompt files in `.github/prompts/` are optional helpers. Prefer normal chat requests by default.

If prompt files are unavailable in the current Copilot environment, execute the equivalent workflow directly from the shared instructions.

Preferred plain-English aliases are:

- "start project setup"
- "add a new feature to the spec"
- "update docs and commit"
- "run the project advisor"
- "review the spec"
- "check the docs for consistency"
