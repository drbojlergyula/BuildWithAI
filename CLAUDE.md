# CLAUDE.md

@AGENTS.md

## Claude Code specifics

Everything above comes from `AGENTS.md`, the canonical instructions shared by all assistants. The notes below apply to Claude Code only.

- **Skills are native.** The workflows in `.claude/skills/` are real slash commands here (`/start`, `/adopt-project`, `/build-next`, `/new-feature`, `/save-point`, `/go-back`, `/update-docs-and-commit`, `/put-me-in-context`, `/doc-sync-check`, `/fix-bug`, `/go-live`). Invoke them directly; they may also trigger automatically when relevant — except `/go-back`, which only the user may invoke.
- **Founder experience.** A statusline (`.claude/statusline.sh`) shows the current phase and last save point; a Founder output style lives in `.claude/output-styles/` (auto-applied for plugin installs, opt-in via `/config` here).
- **The AI team runs as real subagents.** `project-advisor`, `spec-reviewer`, `build-verifier`, and `research-analyst` in `.claude/agents/` execute in their own context with scoped tools. The advisor keeps persistent memory in `.claude/agent-memory/` — expect it to remember past reviews.
- **SessionStart hook.** `.claude/hooks/session-start.sh` tells you whether the template is untouched (offer `/start`) or set up (point to `docs/project_status.md`, suggest `/put-me-in-context`).
- **When editing shared behavior**, edit `AGENTS.md` or the skill/agent files — never duplicate instructions into this file. This file stays thin on purpose.
