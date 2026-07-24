# Project Status

<!-- Update this file after major milestones. Answer three questions:
     1. What are the project milestones?
     2. What's been accomplished?
     3. What's next?
     Per the documentation conventions: completed phases get ONE summary line —
     full detail lives in docs/changelog.md. -->

**Last Updated:** July 22, 2026 (v2.5.0 — earning trust: supervised first night, morning ratification, accept-rate scorecard)
**Project Start:** April 2026

---

## Completed phases

One line each — the full story is in `docs/changelog.md`.

- ✅ **Phase 1 — Template Foundation** (Apr 2026): shared workflow layer plus Claude Code, Codex, and Copilot adapters; core workflows
- ✅ **Phase 2 — Context & Onboarding** (Apr 2026): `put-me-in-context` briefing workflow; bus-factor positioning in the README
- ✅ **Phase 3 — Modernization on Open Standards** (Jul 2026): `AGENTS.md` canonical, workflows as Agent Skills, agents as real subagents, team expanded, welcome hook
- ✅ **Phase 4 — Best-on-Market Round** (Jul 2026): `build-next` loop, save points, `adopt-project`, house rules + auto-maintained decision log, founder UX; category anti-goals documented
- ✅ **Phase 6 — Token-Efficiency Round** (Jul 2026, v2.2.0): cost-tiered AI team, AI budget as a house rule, leaner workflow reads, README cost guidance
- ✅ **Phase 7 — Night Shift** (Jul 2026, v2.3.0): `owner-proxy` deputy (doc-derived authority), `/night-shift` with strict build lane + permissive prep lane, permissions preset, morning briefings — *experimental pending real-user nights*
- ✅ **Phase 8 — The Impact Test** (Jul 2026, v2.4.0): ASSUME verdict — cheap reversible questions settled on evidence or flagged assumptions; PARK reserved for owner-level, expensive-if-wrong questions
- ✅ **Phase 9 — Earning Trust** (Jul 2026, v2.5.0): supervised first night (rehearsal), morning ratification ritual, accept-rate scorecard with honesty gate; reversals become proxy precedent; scheduled nights rejected

---

## Current Phase

### 🚀 Phase 5: Distribution (IN PROGRESS)
**Status:** Plugin shipped and v2.2.0 released; visibility work remains

<!-- Statusline contract: keep "(IN PROGRESS)" on the active phase heading —
     .claude/statusline.sh reads it to display the current phase. -->

**Completed:**
- ✅ Plugin + marketplace packaging (`.claude-plugin/`) with versioned updates; CI validation on every push
- ✅ v2.2.0 through v2.4.0 tagged and released (via the create-release Actions helper)
- ✅ Product consolidation: BuildWithClaude deprecated; beginner on-ramp absorbed as `docs/start_here_with_claude.md`

**Next (manual steps for the owner):**
- Merge the current branch, then tag `v2.5.0` (match the version in `.claude-plugin/plugin.json`)
- Archive the BuildWithClaude repository on GitHub (Settings → Archive) after merging its deprecation README
- Mark this repo as a Template repository (Settings → Template repository)
- Record a short demo GIF for the README (fresh clone → welcome → /start → team reveal)
- Submit the plugin to `anthropics/claude-plugins-community` for marketplace discovery (see the prepared submission package)
- **Get 5 real non-technical users through /start and a second session** — the next feature round should be driven by what they hit, not by new ideas

**Later candidates:**
- Example filled-in project docs (to show what a real setup looks like)
- Contribution guide
- Optional MCP server suggestions (`.mcp.json`) for common business needs
- Cross-tool smoke-test checklist per release (verify skill discovery in Copilot and Codex)
