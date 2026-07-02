# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

<!-- Add a new dated section each time you make significant changes.
     Use ### Added, ### Changed, ### Fixed, ### Removed as needed.
     Example entry below — delete it when you add your first real entry. -->

---

## 2026-07-02 (later the same day)

### Added
- **Plugin packaging** — `.claude-plugin/plugin.json` + `marketplace.json` make this repo an installable Claude Code plugin marketplace: `/plugin marketplace add drbojlergyula/BuildWithAI` then `/plugin install buildwithai-team@buildwithai` adds the AI team (7 skills, 4 agents, welcome hook) to *any* existing project, with versioned updates. Verified end-to-end with a local install: all components resolve
- **`agents` root symlink** → `.claude/agents/` — required because the plugin system only discovers agents in its default location (custom manifest paths for agents fail silently in current Claude Code; found by testing)
- **Smarter welcome hook** — third state for plugin installs: in a project without `docs/`, it introduces the toolkit and offers `start` to create the docs-as-memory structure
- **CI validation** — `.github/workflows/validate-template.yml` + `validate_template.py` check every skill/agent has required frontmatter, JSON configs parse, hook scripts are executable, and the README/AGENTS.md rosters match the files on disk
- **`docs/start_here_with_claude.md`** — gentle 15-minute beginner guide (absorbs the former BuildWithClaude on-ramp)

### Changed
- **Product consolidation** — BuildWithClaude is deprecated and merged into this repo; its README now points here. One product, one place for improvements

---

## 2026-07-02

### Added
- **AI team expansion** — Two new agents: `build-verifier` (independent QA that actually runs what was built) and `research-analyst` (cited web research briefs via live search)
- **New skills** — `/fix-bug` (reproduce → fix → verify → record) and `/go-live` (launch readiness check with a Go/No-Go report)
- **Welcome-on-open** — SessionStart hook (`.claude/hooks/session-start.sh`) detects an untouched template and has Claude offer `/start`; on set-up projects it points to current status
- **Modular rules** — Documentation conventions moved to `.claude/rules/documentation.md`
- **Safe permission defaults** — `.claude/settings.json` pre-approves read-only git commands and web search, and denies reading `.env` files

### Changed
- **Compatibility layer rebuilt on open standards** — `AGENTS.md` (Linux Foundation standard, read natively by Codex, Copilot, Cursor and others) is now the canonical instruction file; `CLAUDE.md` imports it via `@AGENTS.md`. Workflows are Agent Skills in `.claude/skills/`, which Claude Code, Copilot, and Codex all discover natively — one definition, every tool
- **Commands became skills** — All workflows migrated from legacy `.claude/commands/` to the Agent Skills standard (`.claude/skills/<name>/SKILL.md` with YAML frontmatter); skills are now self-contained rather than pointers to a separate workflow document
- **Agents are real subagents now** — All agent files gained the YAML frontmatter Claude Code requires (tools, model, memory, color); `project-advisor` keeps persistent cross-session memory
- **README and CLAUDE.md** rewritten around the "AI team in a box" experience and the standards-based compatibility story

### Removed
- **`docs/assistant_workflows.md`** — replaced by self-contained skills (the skills *are* the shared workflow layer now)
- **`.github/prompts/`** (7 files) — redundant since Copilot discovers `.claude/skills/` natively
- **`.claude/commands/`** — migrated to `.claude/skills/`

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
