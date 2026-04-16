# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

<!-- Add a new dated section each time you make significant changes.
     Use ### Added, ### Changed, ### Fixed, ### Removed as needed.
     Example entry below — delete it when you add your first real entry. -->

---

## 2026-04-16

### Added
- **`put-me-in-context` workflow** — New shared workflow in `docs/assistant_workflows.md` that reads all project docs and produces a structured context brief (what it is, status, next steps, open decisions, risks). Closes with "Ask me anything about this project."
- **`/put-me-in-context` command** — Claude Code slash command in `.claude/commands/put-me-in-context.md`
- **`put-me-in-context.prompt.md`** — GitHub Copilot prompt file in `.github/prompts/`
- **Why this exists section** — Added to `README.md` explaining the bus-factor motivation for the template
- **Repo description comment** — HTML comment at the top of `README.md` with a one-line repo description
- **Footer** — Added closing tagline to `README.md`: "Built to solve the bus factor problem. One prompt: 'put me in context.'"

### Changed
- **`AGENTS.md`** — Added "put me in context" to preferred plain-English aliases and `put-me-in-context` to the available workflows list
- **`.github/copilot-instructions.md`** — Added `put-me-in-context` to the Copilot-specific mapping and plain-English aliases
- **`CLAUDE.md`** — Added `/put-me-in-context` to the commands table
- **`docs/assistant_workflows.md`** — Added `put-me-in-context` to the preferred phrases table, workflow mapping table, and added the full shared workflow definition
- **`README.md`** — Updated day-to-day table and file tree to include the new workflow
