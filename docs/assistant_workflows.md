# Assistant Workflows

This document is the shared source of truth for the reusable workflows in this template. Claude Code, Codex, and GitHub Copilot should all follow the same intent even if the packaging differs by tool.

## Goal

The assistant should detect the workflow the user wants and adapt to the conventions of the tool in use:

- Claude Code: native `.claude/commands`, `.claude/agents`, `.claude/skills`
- Codex: `AGENTS.md` instructions and plain-language execution
- GitHub Copilot: repository instructions plus prompt files

If the user uses Claude-style names like `/start`, `/new-feature`, or "run the spec-reviewer agent", Codex and Copilot should still understand that request and execute the equivalent workflow.

This does not mean all assistants support the same command syntax. Claude has native slash commands in this template. Codex and GitHub Copilot should translate those names into the equivalent workflow when the user refers to them.

## Preferred User Phrases

To keep behavior consistent across tools, these plain-English phrases should be treated as preferred aliases:

| Shared workflow | Preferred plain-English phrase |
|---|---|
| `start` | "start project setup" |
| `new-feature` | "add a new feature to the spec" |
| `update-docs-and-commit` | "update docs and commit" |
| `project-advisor` | "run the project advisor" |
| `spec-reviewer` | "review the spec" |
| `doc-sync-check` | "check the docs for consistency" |
| `put-me-in-context` | "put me in context" |

## Workflow Mapping

| Shared workflow | Claude Code | Codex | GitHub Copilot |
|---|---|---|---|
| `start` | `/start` | plain-English setup workflow; if the user types `/start`, interpret the intent and continue | `start.prompt.md` or plain-English request |
| `new-feature` | `/new-feature` | plain-English feature-planning workflow; if the user types `/new-feature`, interpret the intent and continue | `new-feature.prompt.md` or plain-English request |
| `update-docs-and-commit` | `/update-docs-and-commit` | plain-English maintenance workflow; if the user types `/update-docs-and-commit`, interpret the intent and continue | `update-docs-and-commit.prompt.md` or plain-English request |
| `project-advisor` | agent | advisory review workflow | advisory review workflow |
| `spec-reviewer` | agent | spec review workflow | spec review workflow |
| `doc-sync-check` | skill | doc consistency check | doc consistency check |
| `put-me-in-context` | `/put-me-in-context` | plain-English context brief; if the user says "put me in context", execute the workflow | `put-me-in-context.prompt.md` or plain-English request |

## Detection Rules

When the user begins a workflow, the assistant should identify the environment and adapt:

1. If the tool already knows it is Claude Code, use the Claude-native command or agent style.
2. If the tool already knows it is Codex, use `AGENTS.md` behavior and execute the shared workflow directly.
3. If the tool already knows it is GitHub Copilot, use `.github/copilot-instructions.md` and the prompt files when available.
4. If the user references another tool's convention, translate it instead of rejecting it.
5. If the user uses one of the preferred plain-English phrases above, treat it as a direct request for that workflow.

The important behavior is workflow compatibility, not exact command syntax parity.

## Shared Workflow: start

Purpose: take the repo from generic example content to a real project definition.

Behavior:

1. Read the full template and understand the repo shape.
2. Interview the user one or two questions at a time.
3. Clarify the problem, target user, core flows, data, external dependencies, and constraints.
4. Confirm or recommend a stack.
5. Propose MVP, v1.0, and later iterations.
6. Update `docs/brainstorm.md`, `docs/project_spec.md`, `docs/architecture.md`, `docs/project_status.md`, and `docs/changelog.md`.
7. Update the assistant-facing overview files if the project description needs to be reflected there.
8. Explain what changed and what the user should review next.

## Shared Workflow: new-feature

Purpose: add a new feature to the spec before implementation.

Behavior:

1. Ask what the feature does.
2. Ask who it is for and what problem it solves.
3. Write one to three user stories.
4. Confirm the wording.
5. Place the feature in MVP, v1.0, or later.
6. Update `docs/project_spec.md`.
7. Update `docs/architecture.md` if the change affects the system design.

## Shared Workflow: update-docs-and-commit

Purpose: keep docs and git history aligned after meaningful work.

Behavior:

1. Ask what changed if it is not already clear.
2. Update `docs/changelog.md`.
3. Update `docs/project_status.md`.
4. Update `docs/project_spec.md` or `docs/architecture.md` if needed.
5. Commit changes if the tool and user flow support that action.

## Shared Workflow: project-advisor

Purpose: review the overall project and identify blind spots, risk, and next priorities.

Behavior:

1. Read the key project docs.
2. Ask one grounding question if needed.
3. Produce a short prioritized advisory report.
4. Offer to update the docs or create a new reusable workflow immediately.

When reviewing a multi-assistant template, also inspect:

- `AGENTS.md`
- `CLAUDE.md`
- `.github/copilot-instructions.md`
- files in `.github/prompts/`
- files in `.claude/agents/`, `.claude/commands/`, and `.claude/skills/`

## Shared Workflow: spec-reviewer

Purpose: review `docs/project_spec.md` for completeness, clarity, and scope discipline before implementation.

Output sections:

- Must fix
- Worth clarifying
- Looks good

## Shared Workflow: doc-sync-check

Purpose: make sure the docs agree with each other and do not contain stale placeholders.

Check for:

- outdated progress tracking
- inconsistencies between spec and architecture
- placeholder text
- brainstorm items that should already be decided

When this repository is being used as a template, also check for drift between:

- `docs/assistant_workflows.md`
- `AGENTS.md`
- `CLAUDE.md`
- `.github/copilot-instructions.md`
- `.github/prompts/`
- `.claude/commands/`, `.claude/agents/`, and `.claude/skills/`

## Shared Workflow: put-me-in-context

Purpose: give any team member, newcomer, or returning contributor instant full context on the project with a single prompt. Replaces onboarding conversations, status emails, and manual documentation hunting.

Behavior:

1. Read all files in `docs/`: `project_spec.md`, `architecture.md`, `project_status.md`, `changelog.md`, and `brainstorm.md`.
2. Produce a structured context brief with these sections:
   - **What this project is** — one paragraph, plain English
   - **Current status** — active phase, what is done, what is in progress
   - **Next steps** — top 3 priorities
   - **Open decisions or unresolved questions**
   - **Known risks or blockers**
3. Close with: "Ask me anything about this project."
