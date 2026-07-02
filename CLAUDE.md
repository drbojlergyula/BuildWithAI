# CLAUDE.md

@AGENTS.md

## Claude Code specifics

Everything above comes from `AGENTS.md`, the canonical instructions shared by all assistants. The notes below apply to Claude Code only.

- **Skills are native.** The workflows in `.claude/skills/` are real slash commands here (`/start`, `/new-feature`, `/update-docs-and-commit`, `/put-me-in-context`, `/doc-sync-check`, `/fix-bug`, `/go-live`). Invoke them directly; they may also trigger automatically when relevant.
- **The AI team runs as real subagents.** `project-advisor`, `spec-reviewer`, `build-verifier`, and `research-analyst` in `.claude/agents/` execute in their own context with scoped tools. The advisor keeps persistent memory in `.claude/agent-memory/` — expect it to remember past reviews.
- **SessionStart hook.** `.claude/hooks/session-start.sh` tells you whether the template is untouched (offer `/start`) or set up (point to `docs/project_status.md`, suggest `/put-me-in-context`).
- **When editing shared behavior**, edit `AGENTS.md` or the skill/agent files — never duplicate instructions into this file. This file stays thin on purpose.
