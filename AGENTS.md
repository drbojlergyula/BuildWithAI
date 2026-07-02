# AGENTS.md

Project instructions for AI coding assistants, following the open [AGENTS.md standard](https://agents.md). Codex, GitHub Copilot, Cursor, and other agents read this file natively; Claude Code loads it through `CLAUDE.md`.

## What this repository is

A business-focused starter template for building products with AI coding assistants. It ships with documentation templates and a pre-built AI team of skills and agents. All files are pre-filled with a generic working example; the `start` skill replaces the example with the user's real project.

If `docs/project_spec.md` still describes the example order-management product, this template is untouched — welcome the user and offer to run the `start` workflow before anything else.

## Project documentation

These documents are the project's long-term memory. Prefer updating them over leaving important decisions only in chat.

| File | Purpose |
|---|---|
| `docs/project_spec.md` | What is being built, who it is for, features, tech stack, API design |
| `docs/architecture.md` | System design, data flow, component breakdown, file structure |
| `docs/brainstorm.md` | Scratchpad for ideas before they are ready for the spec |
| `docs/project_status.md` | Current progress, active phase, upcoming milestones |
| `docs/changelog.md` | Version history and notable changes |

The spec and architecture are the source of truth. After meaningful work: update the changelog and status. After a decision: promote it from brainstorm to spec. Documentation conventions: `.claude/rules/documentation.md`.

## Skills — shared workflows (all assistants)

Reusable workflows live in `.claude/skills/<name>/SKILL.md` in the [Agent Skills](https://agentskills.io) open standard. Claude Code, GitHub Copilot, and Codex all discover skills from `.claude/skills/` natively — one definition works everywhere.

| Skill | Use it when |
|---|---|
| `start` | Once, at the beginning — interview that populates all project docs |
| `new-feature` | Adding anything new — user stories, version placement, spec update |
| `update-docs-and-commit` | After finishing work — refresh docs, commit with a clear message |
| `put-me-in-context` | Anyone needs an instant, structured project briefing |
| `doc-sync-check` | Docs feel out of date — find drift, contradictions, placeholders |
| `fix-bug` | Something is broken — reproduce, fix, verify, record |
| `go-live` | Before launch — readiness check with a Go / No-Go report |

If the user invokes a skill by slash command (`/start`), by name, or by plain English ("start project setup", "put me in context", "add a feature to the spec"), execute the matching skill. If your environment does not surface skills automatically, read the skill's `SKILL.md` and follow it as instructions.

## Agent personas — the AI team

Specialist personas live in `.claude/agents/*.md`. Claude Code runs them as native subagents; **every other assistant should treat them as role instructions**: when the user asks to "run the project-advisor" (or the request clearly matches an agent's description below), read that agent's file and adopt it for the task.

| Agent | Job |
|---|---|
| `project-advisor` | Senior advisor — reviews the whole project, surfaces blind spots, prioritises next steps |
| `spec-reviewer` | Requirements analyst — checks the spec for gaps and vagueness before building |
| `build-verifier` | Independent QA — runs what was built and verifies it against the spec |
| `research-analyst` | Web researcher — investigates competitors, pricing, tech choices; cites sources |

## Working conventions

- Ask one or two questions at a time during interview-style workflows.
- Use plain English; the user may be non-technical. Explain technical trade-offs simply.
- Reflect back your understanding before acting on ambiguous requirements; make assumptions explicit.
- Verify work by running it whenever possible — do not declare something done on the strength of having written it.
- Never commit secrets or `.env` files.
- One task at a time; keep changes reviewable.

## Adding new tools

To add a workflow, create `.claude/skills/<name>/SKILL.md` with `name` and `description` frontmatter — it becomes available to every supported assistant at once. To add a specialist persona, create `.claude/agents/<name>.md` with YAML frontmatter (`name`, `description`, optionally `tools`, `model`). Plain-English instructions are the norm in this repo.
