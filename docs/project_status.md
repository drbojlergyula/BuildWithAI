# Project Status

<!-- Update this file after major milestones. Answer three questions:
     1. What are the project milestones?
     2. What's been accomplished?
     3. What's next?
-->

**Last Updated:** July 2, 2026 (v2.1.0 — competitive round: build-next loop, save points, adopt-project, house rules, founder UX)
**Project Start:** April 2026

---

## Current Phase

### ✅ Phase 1: Template Foundation (COMPLETE)
**Status:** Done

**Completed:**
- ✅ Shared workflow layer (`docs/assistant_workflows.md`)
- ✅ Claude Code adapter (`CLAUDE.md`, `.claude/` commands, agents, skills)
- ✅ Codex adapter (`AGENTS.md`)
- ✅ GitHub Copilot adapter (`.github/copilot-instructions.md`, `.github/prompts/`)
- ✅ Core workflows: `start`, `new-feature`, `update-docs-and-commit`, `project-advisor`, `spec-reviewer`, `doc-sync-check`
- ✅ Multi-assistant compatibility layer with plain-English alias mapping

### ✅ Phase 2: Context and Onboarding (COMPLETE)
**Status:** Done

**Completed:**
- ✅ `put-me-in-context` shared workflow — structured context brief from all project docs
- ✅ `/put-me-in-context` Claude Code command
- ✅ Codex and Copilot adapters for the new workflow
- ✅ README "Why this exists" section explaining the bus-factor motivation
- ✅ Repo description metadata and footer tagline

### ✅ Phase 3: Modernization — Open Standards & AI Team (COMPLETE)
**Status:** Done (July 2, 2026)

**Completed:**
- ✅ Compatibility layer rebuilt on open standards: `AGENTS.md` canonical, `CLAUDE.md` imports it, skills in the Agent Skills format discovered natively by Claude Code, Copilot, and Codex
- ✅ Legacy `.claude/commands/`, `.github/prompts/`, and `docs/assistant_workflows.md` retired — one definition of every workflow
- ✅ Agents upgraded to real Claude Code subagents (frontmatter, scoped tools, persistent advisor memory)
- ✅ AI team expanded: `build-verifier` (independent QA) and `research-analyst` (web research)
- ✅ New skills: `fix-bug`, `go-live`; `put-me-in-context` now a skill
- ✅ SessionStart welcome hook, modular rules, safe permission defaults
- ✅ README rewritten as the standards-based flagship; BuildWithClaude repositioned as the Claude-only on-ramp sharing the identical `.claude/` toolkit

### ✅ Phase 5: Best-on-Market Round (COMPLETE)
**Status:** Done (July 2, 2026) — driven by competitive research (BMAD, Spec Kit, Task Master, Agent OS, Superpowers, Lovable/Bolt)

**Completed:**
- ✅ The daily build loop: `/build-next` (spec → build → independent QA verification → recorded progress)
- ✅ Founder safety net: `/save-point` + `/go-back` (rescue-branch protected)
- ✅ Market expansion: `/adopt-project` for existing codebases and Lovable/Bolt/v0 graduates
- ✅ Guardrails: `docs/house_rules.md` (binding non-negotiables) + `docs/decisions.md` (auto-maintained decision log)
- ✅ Founder UX: output style (auto-applied via plugin), phase/save statusline, next-action hints at session start
- ✅ Plugin v2.1.0 — 11 skills, 4 agents, output style included

**Deliberately rejected** (category anti-goals, documented in the changelog): persona-army simulation, full spec-driven pipelines, JSON task databases, formal ADRs.

### 🚀 Phase 4: Distribution (IN PROGRESS)
**Status:** Plugin shipped; visibility work remains

**Completed:**
- ✅ Plugin + marketplace packaging (`.claude-plugin/`) — the AI team installs into any project and receives versioned updates
- ✅ CI validation of skills/agents/configs on every push
- ✅ Product consolidation: BuildWithClaude deprecated in favour of this repo; beginner on-ramp absorbed as `docs/start_here_with_claude.md`

**Next (manual steps for the owner):**
- Merge this branch, then tag `v2.0.0` (a GitHub Release makes the version visible)
- Archive the BuildWithClaude repository on GitHub (Settings → Archive) after merging its deprecation README
- Mark this repo as a Template repository (Settings → Template repository)
- Record a short demo GIF for the README (fresh clone → welcome → /start → team reveal)
- Submit the plugin to `anthropics/claude-plugins-community` for marketplace discovery

**Later candidates:**
- Example filled-in project docs (to show what a real setup looks like)
- Contribution guide
- Optional MCP server suggestions (`.mcp.json`) for common business needs
