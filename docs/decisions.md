# Decision Log

<!-- One line per decision, NEWEST AT THE TOP. Format: date — decision — why.
     Maintained AUTOMATICALLY by the AI workflows (/start, /new-feature, /build-next,
     /update-docs-and-commit, /fix-bug) whenever a decision is made — you never have
     to remember to update this file. This is the project's answer to
     "wait, why did we do it that way?"
     The entries below are this template's own history; /start and /adopt-project
     replace them with your project's decisions. -->

- 2026-07-02 — Decision log uses one dash-separated line per decision, not ADR documents — research shows formal ADRs decay; one-line agent-written entries survive
- 2026-07-02 — Rejected heavy spec-driven pipelines, persona-army agents, and JSON task databases as template patterns — the category's documented failure modes are ceremony, token burn, and "illusion of work"
- 2026-07-02 — House rules live in `docs/house_rules.md` and bind every workflow — founders need durable non-negotiables the AI re-checks, not advice given once
- 2026-07-02 — Workflows ship as Agent Skills and agents as Claude Code subagents (open standards) — one definition works across Claude Code, Copilot, and Codex with no adapter layer
