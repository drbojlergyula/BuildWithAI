# AGENTS.md

Project instructions for AI coding assistants, following the open [AGENTS.md standard](https://agents.md). Codex, GitHub Copilot, Cursor, and other agents read this file natively; Claude Code loads it through `CLAUDE.md`.

## What this repository is

A business-focused starter template for building products with AI coding assistants. It ships with documentation templates and a pre-built AI team of skills and agents. All files are pre-filled with a generic working example; the `start` skill replaces the example with the user's real project.

If `docs/project_spec.md` still describes the example order-management product, this template is untouched — welcome the user and offer to run the `start` workflow before anything else.

## Project documentation

These documents are the project's long-term memory. Prefer updating them over leaving important decisions only in chat.

| File | Purpose |
|---|---|
| `docs/project_spec.md` | What is being built, who it is for, features, tech stack, API design |
| `docs/architecture.md` | System design, data flow, component breakdown, file structure |
| `docs/house_rules.md` | The owner's non-negotiables — re-read before adding costs, dependencies, or touching anything sensitive |
| `docs/decisions.md` | One-line decision log — appended automatically by the workflows whenever a decision is made |
| `docs/brainstorm.md` | Scratchpad for ideas before they are ready for the spec |
| `docs/project_status.md` | Current progress, active phase, upcoming milestones |
| `docs/changelog.md` | Version history and notable changes |
| `docs/reference/` | Durable knowledge shelf — research briefs and domain notes worth keeping; opened on demand, never loaded by default |

The spec and architecture are the source of truth. After meaningful work: update the changelog and status. After a decision: promote it from brainstorm to spec and append one line to the decision log. `docs/house_rules.md` is binding: if a task conflicts with a house rule, stop and ask. Complex projects split oversized docs hub-and-spoke: the main files stay short indexes, depth lives in `docs/spec/` and `docs/architecture/` pages opened only when the work touches them. Documentation conventions: `.claude/rules/documentation.md`.

**Engineering by risk** (`.claude/rules/engineering.md`): every project carries a plain-English Engineering Profile in its spec, inferred — never asked as a questionnaire. Each change is tiered — ROUTINE (build and verify, nothing added), LOAD-BEARING (evidence gates: tests, secret scan, lockfile, dependency audit, migration rehearsal), IRREVERSIBLE (owner approval) — with deterministic path triggers as the floor. Agents make claims; gates produce evidence; every evidence line says who ran it. Business questions are asked only when risky *and* not inferable *and* decisive, at feature entry, once. Go-live judges *fitness for intended use* and says plainly when a product is above what the template can honestly certify.

**Portfolio mode** (repos hosting many projects — marker: a root `portfolio_status.md`): every project is self-contained in `projects/<name>/` with its own full docs brain; the root holds only the shared layer — `standards.md` (the owner's universal taste, traveling between projects) and `portfolio_status.md` (the index). **Loading rule:** sessions always load the root layer plus the *active* project's brain, never the other projects — context cost does not grow with project count. **Active-project protocol:** infer from the task and working directory, confirm once in the first reply; switching is just saying so. Without the root marker, everything behaves as the classic single-project template. **Path resolution:** in portfolio mode, every `docs/...` path in skills and agents means the *active project's* docs (`projects/<name>/docs/...`); the only root-level docs are `standards.md` and `portfolio_status.md`. The `.claude/` toolkit is shared by all projects — one team, many brains.

## Skills — shared workflows (all assistants)

Reusable workflows live in `.claude/skills/<name>/SKILL.md` in the [Agent Skills](https://agentskills.io) open standard. Claude Code, GitHub Copilot, and Codex all discover skills from `.claude/skills/` natively — one definition works everywhere.

| Skill | Use it when |
|---|---|
| `start` | Once, at the beginning — interview that populates all project docs |
| `adopt-project` | There is already code but no docs — reverse-engineers the project brain from an existing codebase (incl. Lovable/Bolt/v0 exports) |
| `build-next` | Building the plan — picks the next story, builds it, has QA verify it, records progress |
| `new-feature` | Adding anything new — clarify ambiguities, user stories, version placement, spec update |
| `save-point` | Quick save — commits everything with a plain-English label |
| `go-back` | Something went wrong — safely rewind to an earlier save point (user-invoked only) |
| `update-docs-and-commit` | After finishing work — refresh docs and decision log, commit with a clear message |
| `put-me-in-context` | Anyone needs an instant, structured project briefing |
| `doc-sync-check` | Docs feel out of date — find drift, contradictions, placeholders, code-vs-spec gaps |
| `fix-bug` | Something is broken — reproduce, fix, verify, record |
| `go-live` | Before launch — readiness check against the engineering profile; fitness report (FIT / NOT YET FIT for the intended use) with accepted-risk cards and the ceiling flag |
| `night-shift` | Autonomous work outside business hours — an orchestrator on a dedicated night branch delegates stories to tiered builders; owner-proxy rules on every question (decide / assume / implement-on-branch / park / stop); supports multi-day absence windows; morning briefing, ratification by merge (user-invoked only) |
| `template-update` | The template released new versions — pulls toolkit improvements into this project via three-way comparison against the recorded base version; never touches the project's docs, code, or customizations |
| `add-project` | The repo hosts (or will host) more than one project — converts to portfolio mode on first use (owner-present only), then scaffolds each new project's brain |

If the user invokes a skill by slash command (`/start`), by name, or by plain English ("start project setup", "put me in context", "add a feature to the spec"), execute the matching skill. If your environment does not surface skills automatically, read the skill's `SKILL.md` and follow it as instructions.

## Agent personas — the AI team

Specialist personas live in `.claude/agents/*.md`. Claude Code runs them as native subagents; **every other assistant should treat them as role instructions**: when the user asks to "run the project-advisor" (or the request clearly matches an agent's description below), read that agent's file and adopt it for the task.

| Agent | Job |
|---|---|
| `project-advisor` | Senior advisor — reviews the whole project, surfaces blind spots, prioritises next steps |
| `spec-reviewer` | Requirements analyst — checks the spec for gaps and vagueness before building |
| `build-verifier` | Independent QA — runs what was built and verifies it against the spec |
| `research-analyst` | Web researcher — investigates competitors, pricing, tech choices; cites sources |
| `owner-proxy` | Deputy owner — during `night-shift` runs: decides what the docs prove, assumes what is cheap, implements expensive-but-containable calls on provisional feature branches, parks what is meaningless without the owner, stops on danger |
| `builder` | Implementation specialist — takes a self-contained work packet and builds exactly that in a fresh context, reporting back with evidence; the workhorse the night-shift orchestrator delegates stories to |

**The team is cost-tiered.** `spec-reviewer`, `build-verifier`, `research-analyst`, and `builder` do routine work and are meant to run on a mid-tier model; `project-advisor` and `owner-proxy` deserve your strongest model, because judgment is what is worth paying for.

**The delegation matrix** (used by the `night-shift` orchestrator, and good guidance any time work is delegated). Tiers are model *classes*, not product names, so the matrix survives model generations:

| Tier | Work | Anthropic (Claude Code enforces via agent `model`) | OpenAI-class (Codex / Copilot guidance) |
|---|---|---|---|
| Expert | architecture, orchestration, proxy rulings | your strongest model (`inherit`) | your strongest reasoning model, high effort |
| Senior | complex stories, hard debugging | newest Opus (`opus`) | a strong reasoning model |
| Junior | routine stories, QA, research, most building | Sonnet (`sonnet`) | a mid-tier model |
| Practitioner | mechanical edits, boilerplate | Sonnet too — Haiku is deliberately not used: a wrong cheap edit that slips past review costs more than the savings; truly mechanical work is done in place rather than delegated | mid or small — small only for truly mechanical work |

Codex and Copilot cannot switch models per task inside one session: honour the tier by running the session at the model class matching the night's dominant tier, or split the work across sessions by tier. A task smaller than its own handoff packet is done in place, never delegated.

**`night-shift` works in every assistant.** Claude Code runs it as a true orchestrator — `builder` and `owner-proxy` as subagents with fresh contexts; every other assistant plays the roles itself, sequentially: adopt `builder` for each delegated story (packet in, evidence-backed report out), adopt `owner-proxy` for each ruling — bound by the ruling exactly as if a separate agent had issued it. All night work lives on the `night/<date>` branch in every tool; the branch name is the night-mode marker. Approval mechanics are per-tool (the skill's preflight covers Claude Code permission modes, Codex approval modes, and Copilot tool approvals), tool provisioning follows the vendor-official trusted-sources rule (`.claude/rules/trusted-sources.md` — Anthropic in Claude Code, OpenAI in Codex, GitHub in Copilot), and where native agent memory is unavailable, the proxy's tagged rulings in `docs/decisions.md` serve as its memory.

## Working conventions

- Ask one or two questions at a time during interview-style workflows.
- Use plain English; the user may be non-technical. Explain technical trade-offs simply.
- Reflect back your understanding before acting on ambiguous requirements; make assumptions explicit.
- Verify work by running it whenever possible — do not declare something done on the strength of having written it.
- Never commit secrets or `.env` files.
- One task at a time; keep changes reviewable.

## Adding new tools

To add a workflow, create `.claude/skills/<name>/SKILL.md` with `name` and `description` frontmatter — it becomes available to every supported assistant at once. To add a specialist persona, create `.claude/agents/<name>.md` with YAML frontmatter (`name`, `description`, optionally `tools`, `model`). Plain-English instructions are the norm in this repo.
