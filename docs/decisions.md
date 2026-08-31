# Decision Log

<!-- One line per decision, NEWEST AT THE TOP. Format: date — decision — why.
     Maintained AUTOMATICALLY by the AI workflows (/start, /new-feature, /build-next,
     /update-docs-and-commit, /fix-bug) whenever a decision is made — you never have
     to remember to update this file. This is the project's answer to
     "wait, why did we do it that way?"
     The entries below are this template's own history; /start and /adopt-project
     replace them with your project's decisions. -->

- 2026-08-31 — Story splitting happens at the plan's door, not at build time (owner field input: stories don't outgrow night-cycles when sized on entry) — enforced in new-feature/start/adopt-project, patrolled by doc-sync-check, night triage is only a vent
- 2026-08-31 — Multi-project repos confirmed as the v3.0 direction (owner runs many projects per repo): the 3-layer portfolio brain (standards / portfolio / project), shipped with its migration per the standing rule
- 2026-08-23 — Trusted sources are vendor-official per assistant: Anthropic for Claude Code, OpenAI for Codex, GitHub/Microsoft for Copilot — Codex parity is first-class, the rule is identical in every tool
- 2026-08-23 — Nights may self-provision missing dev tools, but only from the owner-curated trusted-sources list, under the four-part test (free/dev-only/reversible/listed), smoke-tested, capped at two per night, ratified by morning merge — built on owner field evidence from many real nights; the internet at large is never a source at 3 AM
- 2026-08-23 — Browser-testing integration is a conditional hook, not a vendored dependency — the verifier uses `webapp-testing` when installed and degrades gracefully when not; recommending at the moment of felt pain beats requiring at setup
- 2026-08-20 — Second-brain structure: hub-and-spoke overflow, reference shelf, decision-log lifecycle — the docs grow depth instead of bloat; per-session context gets smaller, not larger
- 2026-08-20 — Never ship a structure change without shipping its migration: `.claude/migrations/vX.Y.Z.md` files travel with the release; `/template-update` chains and executes them under zero-loss verification (moved/merged/in-place accounting, deleted must be 0)
- 2026-08-20 — Migration is a command, not an agent: one entry point (`/template-update`) for one user intent; the muscle is the existing `builder` in a fresh context, `doc-sync-check` verifies — no new roster seat
- 2026-08-01 — Night shift v2 runs on a night branch with ratification-by-merge; new BRANCH verdict implements expensive-but-containable decisions on child feature branches instead of parking the work — a branch is reversible by construction, so parking moves from the work to the merge; STOP untouched (a branch cannot un-spend money)
- 2026-08-01 — Orchestrator pattern for nights: the session delegates stories to the new `builder` agent (fresh context per story) and stays thin — fixes long-run drift and token cost at once; builder seat earned by field feedback from real nights
- 2026-08-01 — Absence windows: one explicit consent covers a bounded multi-day window, earned by a healthy scorecard; open-ended standing autonomy stays rejected — consent per delegation, window-scoped
- 2026-08-01 — Dynamic specialists capped at two per night, born provisional on the night branch — the five-agents principle governs the template's shipped roster, not a project's own team
- 2026-08-01 — Practitioner tier runs on Sonnet, not Haiku (re-affirmed) — verification asymmetry outweighs the savings; delegation matrix uses model classes, not product names, so it survives model generations
- 2026-07-24 — Template rollout to existing projects via `/template-update` skill with three-way comparison against a recorded base version — deterministic ownership boundary (template files vs. project files), consent on every conflict; plugin-only, git-merge, and CI-push alternatives rejected (cross-assistant requirement, persona, per-update consent)
- 2026-07-24 — Design principle: five agents is the right number — a new agent or skill must earn its seat with user evidence, not architectural appeal (outcome of a two-AI design review that rejected 7 of 9 proposed additions)
- 2026-07-24 — LESSON convention added to this log: verifier failures and bug root causes that reveal reusable rules get one LESSON line, so mistakes become precedent instead of repetition
- 2026-07-24 — `/explore-product` (product-gap questioning) parked in brainstorm, not built — the healthy core lives in the advisor; revisit with user evidence
- 2026-07-22 — Adopted cost-per-accepted-change as the night shift's success metric: every ruling gets ratified or reversed in a morning review, scored on a scorecard — an autonomous feature must prove it pays for itself in a number the owner generates
- 2026-07-22 — First night runs supervised (rehearsal: one story, owner watching) — the scariest moment of autonomy becomes a controlled demo of the safety model
- 2026-07-22 — REJECTED scheduled/cron-triggered nights — per-night consent is the safety model; a standing schedule silently makes autonomy the default instead of a choice
- 2026-07-22 — Night-shift boundary moved from "provable from docs" to "cost of being wrong": cheap reversible questions get ASSUME (flagged for review) instead of PARK — parking them wasted nights without adding safety; owner-level and irreversible questions still PARK/STOP
- 2026-07-19 — Night budgets are denominated in stories/scope, never tokens or money — a session cannot meter its own spend; consistent with rejecting the token-tracking skill
- 2026-07-19 — Night shift got a permissive prep lane (research, brainstorming) alongside the strict build lane — strictness follows irreversibility, not activity; proposals in brainstorm.md cannot break anything
- 2026-07-19 — Data informs, docs authorize: research grounds implementation decisions inside approved stories, but an owner-level PARK can be enriched by data, never converted into a DECISION — prevents internet data laundering into owner authority
- 2026-07-19 — Night-shift proxy authority is doc-derived only: DECISION requires cited grounds, everything else is PARK or STOP — a deputy that guesses is worse than no deputy
- 2026-07-19 — Proxy decisions are provisional (`pending owner review` tag) and every night starts with a save point — autonomy must always be one `/go-back` from undone
- 2026-07-19 — `/night-shift` is user-invoked only, like `/go-back` — the assistant never puts itself in charge overnight on its own initiative
- 2026-07-19 — Cost-tiered the AI team: `spec-reviewer`, `build-verifier`, `research-analyst` pinned to Sonnet, advisor inherits the session model — routine checks shouldn't bill at frontier rates; Haiku rejected for QA because a false PASS costs more than any model saves
- 2026-07-19 — Rejected a token-tracking skill — the model can't see real spend from inside a session, so it would be measurement theater; cost guidance lives in the README and house rules instead
- 2026-07-02 — Decision log uses one dash-separated line per decision, not ADR documents — research shows formal ADRs decay; one-line agent-written entries survive
- 2026-07-02 — Rejected heavy spec-driven pipelines, persona-army agents, and JSON task databases as template patterns — the category's documented failure modes are ceremony, token burn, and "illusion of work"
- 2026-07-02 — House rules live in `docs/house_rules.md` and bind every workflow — founders need durable non-negotiables the AI re-checks, not advice given once
- 2026-07-02 — Workflows ship as Agent Skills and agents as Claude Code subagents (open standards) — one definition works across Claude Code, Copilot, and Codex with no adapter layer
