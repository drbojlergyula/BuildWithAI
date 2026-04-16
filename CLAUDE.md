# CLAUDE.md

This file is read by Claude Code at the start of every session. It provides context about the project structure, available tools, and working conventions.

## Overview

This is a business-focused project template for building with AI coding assistants. It includes shared documentation templates plus assistant-specific adapters for Claude Code, Codex, and GitHub Copilot. All files are pre-filled with a generic working example. Run `/start` to replace all example content with the user's real project.

The shared workflow source of truth is `docs/assistant_workflows.md`. Claude-native commands in `.claude/` are the Claude packaging of those shared workflows and should stay aligned with that file.

## Documentation

| File | Purpose |
|---|---|
| [docs/project_spec.md](docs/project_spec.md) | What is being built, who it is for, features, tech stack, API design |
| [docs/architecture.md](docs/architecture.md) | System design, data flow, component breakdown, file structure |
| [docs/brainstorm.md](docs/brainstorm.md) | Scratchpad for ideas before they are ready for the spec |
| [docs/project_status.md](docs/project_status.md) | Current progress, active phase, upcoming milestones |
| [docs/changelog.md](docs/changelog.md) | Version history and notable changes |
| [docs/assistant_workflows.md](docs/assistant_workflows.md) | Shared workflow definitions across Claude, Codex, and Copilot |

**Update docs after every major milestone or addition.** The spec and architecture are the primary source of truth — keep them accurate so context does not need to be re-explained each session.

## Claude Tools

Tools live in `.claude/` as plain-English text files. To create a new tool, add a file to the relevant folder describing what Claude should do, step by step — in plain English.

**Agents** are specialist personas given a specific job. Invoke by asking Claude to "run the [name] agent."
**Commands** are shortcut tasks triggered by typing `/command-name`.
**Skills** are repeatable checklists invoked by asking Claude to "run the [name] skill."

### Commands (`.claude/commands/`)

| Command | When to use | Description |
|---|---|---|
| `/start` | Once, at the very beginning | Interviews the user, populates all project docs, sets up the project from scratch |
| `/new-feature` | Any time you want to add something new | Guided workflow for adding a feature to the spec with user stories and version assignment |
| `/update-docs-and-commit` | After finishing any piece of work | Updates changelog and project status to reflect recent work, then commits to git |
| `/put-me-in-context` | Any time you need a full project summary | Reads all docs and produces a structured brief: what it is, status, next steps, open decisions, risks |

### Agents (`.claude/agents/`)

| Agent | When to use | Description |
|---|---|---|
| `project-advisor` | After setup, after each phase, or when stuck | Senior advisor that reviews the whole project, surfaces blind spots, and recommends what to address next |
| `spec-reviewer` | Before starting to build anything | Reviews the project spec for completeness, clarity, and gaps |

### Skills (`.claude/skills/`)

| Skill | When to use | Description |
|---|---|---|
| `doc-sync-check` | Any time docs feel out of date | Checks all project docs are consistent with each other and free of placeholder text |

## Cross-Tool Compatibility

This repository is designed to support three assistants:

- Claude Code via `CLAUDE.md` and `.claude/`
- Codex via `AGENTS.md`
- GitHub Copilot via `.github/copilot-instructions.md` and `.github/prompts/`

If you update a reusable workflow here, update `docs/assistant_workflows.md` first and then keep the assistant-specific adapters aligned.

## Working conventions

- **One task at a time.** Give Claude a single, specific instruction rather than a list. Results are better and easier to review.
- **Be specific.** "Add a contact form with name, email, and message fields" is better than "add a way for people to get in touch."
- **Ask for explanations.** If Claude does something you don't understand, ask: "Explain what you just did in plain English."
- **Keep docs current.** The more accurate the spec and architecture are, the less context needs to be repeated across sessions.
- **After major changes:** update `docs/changelog.md` and `docs/project_status.md`.
- **After deciding something new:** move it from `docs/brainstorm.md` into `docs/project_spec.md`.
