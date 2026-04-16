# AGENTS.md

This file is read by Codex at the start of every session. It explains how to operate inside this repository and how to stay compatible with the Claude Code and GitHub Copilot versions of the template.

## Overview

This is a business-focused starter template for building products with AI coding assistants. The same project structure should work with Claude Code, Codex, and GitHub Copilot.

The shared behavioral source of truth is `docs/assistant_workflows.md`.

If the user asks to run `/start`, `/new-feature`, `/update-docs-and-commit`, `/put-me-in-context`, `project-advisor`, `spec-reviewer`, or `doc-sync-check`, interpret that as a request to execute the matching workflow in this repository even though those slash commands are Claude-native packaging.

Preferred plain-English aliases in Codex are:

- "start project setup"
- "add a new feature to the spec"
- "update docs and commit"
- "run the project advisor"
- "review the spec"
- "check the docs for consistency"
- "review the whole template for drift"
- "put me in context"

## Tool Adaptation Rules

When working in this repository, first determine which assistant conventions are being referenced:

- If the user refers to Claude commands, agents, or skills, map them to the matching shared workflow.
- If the user refers to Codex behavior, use this `AGENTS.md` plus the shared workflows as the operating contract.
- If the user refers to GitHub Copilot prompts or instructions, use `.github/copilot-instructions.md` and `.github/prompts/` as the Copilot-facing equivalents.

Do not say a workflow is unavailable just because it was originally written as a Claude command. Execute the shared workflow directly.

Do not imply that Codex has a native slash-command system matching Claude's. Translate the user's intent into the shared workflow and continue in normal Codex chat.

## Shared Project Files

Keep these files accurate:

- `docs/project_spec.md`
- `docs/architecture.md`
- `docs/brainstorm.md`
- `docs/project_status.md`
- `docs/changelog.md`

These documents are the project's long-term memory. Prefer updating them rather than leaving important decisions only in chat.

## Available Workflows

Read `docs/assistant_workflows.md` for the canonical behavior of:

- `start`
- `new-feature`
- `update-docs-and-commit`
- `project-advisor`
- `spec-reviewer`
- `doc-sync-check`
- `put-me-in-context`

Also treat "review the whole template for drift" as a request to inspect the shared workflow plus all assistant-specific adapters for inconsistencies.

When the user uses one of the preferred plain-English aliases above, treat it as an exact match for the corresponding workflow.

## Working Conventions

- Ask one or two questions at a time during setup workflows.
- Use plain English unless the user prefers technical language.
- Reflect back your understanding before moving on when requirements are ambiguous.
- Make assumptions explicit.
- Keep the docs in sync after meaningful product or architecture changes.
- Treat `docs/project_spec.md` and `docs/architecture.md` as the primary source of truth.
