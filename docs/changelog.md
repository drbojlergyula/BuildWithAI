# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

<!-- Add a new dated section each time you make significant changes.
     Use ### Added, ### Changed, ### Fixed, ### Removed as needed.
     Example entry below — delete it when you add your first real entry. -->

---

## v2.3.0 — 2026-07-19: Night shift (autonomous work with a deputy)

The owner's scarcest resource is attended hours. This round lets the build loop run unattended — with a deputy whose authority is formally limited to what the project docs can prove.

### Added
- **`owner-proxy` agent** — deputy owner for autonomous sessions. Rules on judgment questions with exactly three verdicts: DECISION (only with cited grounds from the spec, house rules, or decision log), PARK (no proof — the owner decides at breakfast), STOP (house-rule contact, money, deletion, external comms, deployment). Persistent memory keeps rulings consistent night to night. Strongest-model tier, same as the advisor — it is pure judgment
- **`/night-shift` skill** — user-invoked only. Preflight while the owner is awake (project set up, permission allowlist approved, budget agreed, strongest model loaded), save point first, a stated contract, then the `/build-next` loop with the proxy replacing the owner. Parked stories go to `docs/brainstorm.md`; proxy decisions land in `docs/decisions.md` tagged `pending owner review`; two consecutive verification failures stop the night. Ends with a morning briefing and a final save point — the whole night is one `/go-back` from undone
- **Night-shift permissions preset** (`.claude/presets/night-shift.settings.json`) — the deny baseline for unattended runs (destructive git, deploys, publishing, secrets, plus strict web limits); the preflight builds the per-project allowlist into gitignored `settings.local.json` with the owner's explicit yes
- **Prep lane** — when the build lane parks or finishes, the night switches to preparation: `research-analyst` briefs on parked and standing questions, brainstorming for upcoming stories, all landing in `docs/brainstorm.md` as proposals. Enriched parking means every parked question arrives at breakfast with options, sourced data, and a recommendation — a thirty-second decision instead of an afternoon. Governing rule: **data informs, docs authorize** — research grounds implementation decisions inside approved stories, but never converts an owner-level PARK into a DECISION. The research lane is a named on/off choice in preflight

### Changed
- **Cost tiering** — `owner-proxy` joins `project-advisor` in the strongest-model tier
- **Cross-assistant** — night shift works in Claude Code, Copilot, and Codex: the proxy runs as a subagent in Claude Code and as an adopted role elsewhere (stated in `AGENTS.md`); the skill's preflight covers each tool's own approval mechanism; without native agent memory, the proxy's tagged rulings in `docs/decisions.md` serve as its memory
- **Plugin** bumped to 2.3.0 (12 skills, 5 agents)

---

## v2.2.0 — 2026-07-19: Token-efficiency round

AI spend is a real cost for founders — a company subscription can burn through its limits in days when everything runs on a frontier model. This round makes the template cheap to run without touching what it is good at.

### Added
- **Cost-tiered AI team** — `spec-reviewer`, `build-verifier`, and `research-analyst` are now pinned to Sonnet (`model: sonnet`); `project-advisor` keeps inheriting the session model because judgment is what is worth paying up for. Haiku was considered for QA and rejected: a false PASS from a too-small model is the most expensive token in the system. The tiering principle is stated in `AGENTS.md` so it works in every assistant: Claude Code enforces it via the frontmatter automatically; Copilot and Codex users apply it through their tool's model picker (Copilot note added to `.github/copilot-instructions.md`)
- **AI budget as a house rule** — `/start` now asks about AI spend alongside the hosting budget, the example `docs/house_rules.md` shows what the rule looks like, and the advisor's operations dimension checks it like any other non-negotiable
- **README "Keeping your AI costs down"** — model-to-moment guidance (mid-tier for the daily rhythm, frontier for interviews, architecture, and advisor reviews), `/cost` and `/model` pointers, and why docs-as-memory is itself token optimization

### Changed
- **`project-advisor` reads less** — the skill/agent rosters in `AGENTS.md` replace reading every file in `.claude/skills/` and `.claude/agents/`; multi-assistant adapters are read only when the template-consistency dimension actually runs
- **`/start` Phase 0 reads less** — docs only; the team roster comes from `AGENTS.md` instead of eleven skill files
- **Documentation conventions** — docs are context, so length is a running cost: spec and status stay current-state only, history goes to the changelog
- **Plugin** bumped to 2.2.0

### Deliberately rejected
- **A token-tracking/optimizer skill** — the model cannot see actual spend from inside a session; a skill that pretends to measure it would be theater. Cost visibility stays with the harness (`/cost`, usage dashboards); the template's job is structural efficiency

---

## v2.1.0 — 2026-07-02: Competitive round (best-on-market push)

Based on a competitive teardown of BMAD-method, GitHub Spec Kit, Task Master, Agent OS, Superpowers, and the Lovable/Bolt founder market. Everything added passes three tests: founder-readable, agent-maintained, zero ceremony.

### Added
- **`/build-next`** — the spec→build→verify chain: picks the next planned story, assembles a context packet (stories + architecture constraints + house rules), builds it, has `build-verifier` independently prove it works, records progress, points at what's next
- **`/save-point` and `/go-back`** — git as a video-game save system for non-technical users; `/go-back` always creates a rescue branch first and is user-invoked only
- **`/adopt-project`** — brings an existing codebase (incl. Lovable/Bolt/v0 exports) into the docs-as-memory system: reverse-engineers spec/architecture/conventions from code, interviews for intent, documents what IS
- **`docs/house_rules.md`** — the owner's ~10 non-negotiables (budget ceiling, never-without-asking list); every workflow re-checks it, violations are automatic blockers in `/go-live` and High findings for the advisor
- **`docs/decisions.md`** — one-line decision log (date — decision — why), appended automatically by the workflows; deliberately not ADRs (those decay)
- **Founder output style** (`.claude/output-styles/founder.md`) — plain-English, business-first communication with 💡 business insights; auto-applies for plugin installs (`force-for-plugin`), opt-in in the template
- **Founder statusline** (`.claude/statusline.sh`) — shows current phase · last save age · model; wired via `settings.json`
- **"What to say next"** — the SessionStart hook now has Claude offer 2–3 concrete next actions based on the project status
- **MIT LICENSE file** — declared in `plugin.json` since v2.0.0 and required for marketplace review; now actually present
- **Template sentinel** — untouched-template detection now uses one machine-readable marker (`template-state: untouched-example` in `docs/project_spec.md`) shared by the hook and skills, instead of fragile prose matching
- **Canonical house-rules enforcement rule** — `.claude/rules/house-rules.md` is the single normative statement; skills carry only their workflow-specific consequence

### Changed
- **`/start`** — interviews for house rules, writes the two new docs, ends with an offered first advisor review ("your advisor already found three things") and hands off to `/build-next`
- **`/new-feature`** — explicit clarify-ambiguities step before writing stories; house-rules conflict check; appends to the decision log
- **`/doc-sync-check`** — new code-vs-spec drift section: verifies top user stories actually exist in code, and recent work honours the house rules
- **`/go-live`** — house-rules compliance is a blocker-level check; offers a one-click deploy button for the user's app
- **`/put-me-in-context`** — briefing now includes house rules in force and the key decisions so far
- **Plugin** bumped to 2.1.0 (ships the output style; 11 skills, 4 agents)

---

## v2.0.0 — 2026-07-02: Plugin packaging & consolidation

### Added
- **Plugin packaging** — `.claude-plugin/plugin.json` + `marketplace.json` make this repo an installable Claude Code plugin marketplace: `/plugin marketplace add drbojlergyula/BuildWithAI` then `/plugin install buildwithai-team@buildwithai` adds the AI team (7 skills, 4 agents, welcome hook) to *any* existing project, with versioned updates. Verified end-to-end with a local install: all components resolve
- **`agents` root symlink** → `.claude/agents/` — required because the plugin system only discovers agents in its default location (custom manifest paths for agents fail silently in current Claude Code; found by testing)
- **Smarter welcome hook** — third state for plugin installs: in a project without `docs/`, it introduces the toolkit and offers `start` to create the docs-as-memory structure
- **CI validation** — `.github/workflows/validate-template.yml` + `validate_template.py` check every skill/agent has required frontmatter, JSON configs parse, hook scripts are executable, and the README/AGENTS.md rosters match the files on disk
- **`docs/start_here_with_claude.md`** — gentle 15-minute beginner guide (absorbs the former BuildWithClaude on-ramp)

### Changed
- **Product consolidation** — BuildWithClaude is deprecated and merged into this repo; its README now points here. One product, one place for improvements

---

## 2026-07-02: Modernization on open standards

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
