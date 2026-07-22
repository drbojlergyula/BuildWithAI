# Project Status

<!-- Update this file after major milestones. Answer three questions:
     1. What are the project milestones?
     2. What's been accomplished?
     3. What's next?
-->

**Last Updated:** July 19, 2026 (v2.3.0 — night shift: autonomous work loop with the owner-proxy deputy, morning briefings, permission preset)
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

### ✅ Phase 4: Best-on-Market Round (COMPLETE)
**Status:** Done (July 2, 2026) — driven by competitive research (BMAD, Spec Kit, Task Master, Agent OS, Superpowers, Lovable/Bolt)

**Completed:**
- ✅ The daily build loop: `/build-next` (spec → build → independent QA verification → recorded progress)
- ✅ Founder safety net: `/save-point` + `/go-back` (rescue-branch protected)
- ✅ Market expansion: `/adopt-project` for existing codebases and Lovable/Bolt/v0 graduates
- ✅ Guardrails: `docs/house_rules.md` (binding non-negotiables) + `docs/decisions.md` (auto-maintained decision log)
- ✅ Founder UX: output style (auto-applied via plugin installs), statusline with phase + last save (template installs), next-action hints at session start
- ✅ Plugin v2.1.0 — 11 skills, 4 agents, output style included

**Deliberately rejected** (category anti-goals, documented in the changelog): persona-army simulation, full spec-driven pipelines, JSON task databases, formal ADRs.

### 🚀 Phase 5: Distribution (IN PROGRESS)
**Status:** Plugin shipped; visibility work remains

<!-- Statusline contract: keep "(IN PROGRESS)" on the active phase heading —
     .claude/statusline.sh reads it to display the current phase. -->

**Completed:**
- ✅ Plugin + marketplace packaging (`.claude-plugin/`) — the AI team installs into any project and receives versioned updates
- ✅ CI validation of skills/agents/configs on every push
- ✅ Product consolidation: BuildWithClaude deprecated in favour of this repo; beginner on-ramp absorbed as `docs/start_here_with_claude.md`

**Next (manual steps for the owner):**
- Merge this branch, then tag `v2.2.0` (a GitHub Release makes the version visible — match the version in `.claude-plugin/plugin.json`)
- Archive the BuildWithClaude repository on GitHub (Settings → Archive) after merging its deprecation README
- Mark this repo as a Template repository (Settings → Template repository)
- Record a short demo GIF for the README (fresh clone → welcome → /start → team reveal)
- Submit the plugin to `anthropics/claude-plugins-community` for marketplace discovery (see the prepared submission package)

**Later candidates:**
- Example filled-in project docs (to show what a real setup looks like)
- Contribution guide
- Optional MCP server suggestions (`.mcp.json`) for common business needs

### ✅ Phase 6: Token-Efficiency Round (COMPLETE)
**Status:** Done (July 19, 2026) — driven by real founder feedback: a company subscription burned $200 in 3 days running everything on frontier models

**Completed:**
- ✅ Cost-tiered AI team: `spec-reviewer`, `build-verifier`, `research-analyst` pinned to Sonnet; `project-advisor` keeps the session model (judgment is worth frontier rates; QA on Haiku rejected — false-PASS risk)
- ✅ AI budget added to the `/start` interview, the house-rules example, and the advisor's operations checks
- ✅ Leaner reading lists: advisor and `/start` use the `AGENTS.md` rosters instead of reading every skill/agent file
- ✅ Doc-length discipline in the documentation conventions (docs are context — length is a running cost)
- ✅ README "Keeping your AI costs down" section; plugin bumped to 2.2.0

### ✅ Phase 7: Night Shift (COMPLETE)
**Status:** Done (July 19, 2026) — autonomous work outside business hours, with authority formally limited to what the docs prove

**Completed:**
- ✅ `owner-proxy` agent: DECISION-with-grounds / PARK / STOP verdicts, persistent memory, strongest-model tier
- ✅ `/night-shift` skill: awake-time preflight (permissions, budget, model), save-point wrap, `/build-next` loop with proxy in place of the owner, morning briefing, user-invoked only
- ✅ Deny-baseline permissions preset for unattended runs; per-project allowlist built with the owner's explicit approval
- ✅ Plugin v2.3.0 — 12 skills, 5 agents
