# GitHub Copilot Repository Instructions

The canonical instructions for this repository live in [`AGENTS.md`](../AGENTS.md) — read and follow that file. This file only adds Copilot-specific notes.

- **Skills:** Copilot discovers the shared skills in `.claude/skills/` natively (Agent Skills standard). When the user asks for a workflow by name or in plain English — "start project setup", "put me in context", "add a feature to the spec", "check the docs for consistency", "fix this bug", "are we ready to go live" — run the matching skill. If skills are unavailable in the current Copilot surface, open the skill's `SKILL.md` and follow it as instructions.
- **The AI team:** the personas in `.claude/agents/` (`project-advisor`, `spec-reviewer`, `build-verifier`, `research-analyst`) are not Copilot-native agents. When the user asks to run one, read its file and adopt the role for that task.
- **Slash-command names:** users may type Claude-style commands like `/start` or `/new-feature`. Treat them as requests for the matching skill — never reply that the command is unsupported.
- Keep `docs/` up to date after meaningful work, ask one or two questions at a time in interview workflows, and use plain English — the user may be non-technical.
