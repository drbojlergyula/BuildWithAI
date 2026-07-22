# Decision Log

<!-- One line per decision, NEWEST AT THE TOP. Format: date — decision — why.
     Maintained AUTOMATICALLY by the AI workflows (/start, /new-feature, /build-next,
     /update-docs-and-commit, /fix-bug) whenever a decision is made — you never have
     to remember to update this file. This is the project's answer to
     "wait, why did we do it that way?"
     The entries below are this template's own history; /start and /adopt-project
     replace them with your project's decisions. -->

- 2026-07-19 — Night-shift proxy authority is doc-derived only: DECISION requires cited grounds, everything else is PARK or STOP — a deputy that guesses is worse than no deputy
- 2026-07-19 — Proxy decisions are provisional (`pending owner review` tag) and every night starts with a save point — autonomy must always be one `/go-back` from undone
- 2026-07-19 — `/night-shift` is user-invoked only, like `/go-back` — the assistant never puts itself in charge overnight on its own initiative
- 2026-07-19 — Cost-tiered the AI team: `spec-reviewer`, `build-verifier`, `research-analyst` pinned to Sonnet, advisor inherits the session model — routine checks shouldn't bill at frontier rates; Haiku rejected for QA because a false PASS costs more than any model saves
- 2026-07-19 — Rejected a token-tracking skill — the model can't see real spend from inside a session, so it would be measurement theater; cost guidance lives in the README and house rules instead
- 2026-07-02 — Decision log uses one dash-separated line per decision, not ADR documents — research shows formal ADRs decay; one-line agent-written entries survive
- 2026-07-02 — Rejected heavy spec-driven pipelines, persona-army agents, and JSON task databases as template patterns — the category's documented failure modes are ceremony, token burn, and "illusion of work"
- 2026-07-02 — House rules live in `docs/house_rules.md` and bind every workflow — founders need durable non-negotiables the AI re-checks, not advice given once
- 2026-07-02 — Workflows ship as Agent Skills and agents as Claude Code subagents (open standards) — one definition works across Claude Code, Copilot, and Codex with no adapter layer
