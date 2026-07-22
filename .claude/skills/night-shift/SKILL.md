---
name: night-shift
description: Autonomous work session for outside business hours — the owner-proxy decides from documented owner intent, settles cheap reversible questions on research or flagged assumptions, and parks only what truly needs the owner; plus a prep lane of research and brainstorming. Ends with a morning briefing. User-invoked only; never triggers automatically.
argument-hint: [scope for the night, e.g. "3 stories" or "finish the MVP list"]
disable-model-invocation: true
---

# /night-shift — Your AI Team Works While You Sleep

Runs the normal build rhythm unattended, in two lanes. The **build lane** is strict where it matters: every question that would normally wake the owner goes to the **owner-proxy** agent instead, which decides what the docs prove, settles cheap reversible questions on evidence or a stated assumption (each flagged for morning review), and parks only the questions that genuinely need the owner. The **prep lane** is permissive on purpose: research and brainstorming are additive and reversible, so when the build lane can't continue, the night keeps producing — briefs, options, and decision-ready parked questions. Strictness follows irreversibility, not the clock. The owner wakes up to verified features, prepared decisions, and a short briefing — never to surprises.

**User-invoked only.** Never start a night shift on your own initiative, and never treat "keep going" during daily work as an invitation to enter this mode.

## Steps

### 0 — Preflight (while the owner is still awake)

Do these checks before anything else; refuse to start if one fails:

1. **The project is set up.** If the `template-state: untouched-example` sentinel is present in `docs/project_spec.md` or no plan exists in `docs/project_status.md`, stop and suggest `/start` — there is nothing to work on yet.
2. **Permissions won't stall the night.** The proxy answers *judgment* questions; it cannot click *approval* dialogs — those come from the tool itself, and an unattended session will hang on the first one. Every assistant has its own mechanism; configure the one you are running in, now, while the owner can approve it:
   - **Claude Code:** check `.claude/settings.local.json` for a night-shift allowlist. If there isn't one, propose one: read the project's stack and offer the commands a build loop will need (test runner, dev server, linter, `git commit`), plus the deny baseline from `.claude/presets/night-shift.settings.json`. Write it to `.claude/settings.local.json` (gitignored) only with the owner's yes. The baseline is deliberately strict — it also denies `WebFetch` and external `curl -X POST`, which blocks `research-analyst` web reads and QA of local POST endpoints; if tonight needs either, the owner removes those lines now, knowingly (deny rules always beat allow rules).
   - **Codex:** ask the owner to start the session in an autonomous approval mode with a workspace-limited sandbox (e.g. full-auto) — and treat the deny baseline as behavioral law: even when the sandbox would allow a command on the deny list, do not run it.
   - **GitHub Copilot:** ask the owner to enable the surface's tool-approval setting for the session (e.g. the CLI's allow-tools options). Same rule: the deny baseline binds you even where the tool would permit the action.
3. **The night has a budget — in units the session can count.** Stories or scope ("3 stories", "the MVP list", "everything in phase 2"), never tokens or money: a session cannot meter its own spend, and a budget it cannot measure is a budget it cannot honour. From the argument if given, else propose one sized to the AI-budget house rule in `docs/house_rules.md`, else ask before starting. A night without a countable budget does not start. Actual cost is what the owner checks in the morning, in their tool's own usage view.
4. **The strongest model is loaded.** Recommend the owner switch the session to their strongest model before leaving — the proxy inherits it, and judgment is what it is there for. The build workers stay on their own tiers regardless.
5. **The research lane is a named choice.** Ask the owner: should tonight include internet research — competitor and pricing briefs, technology comparisons, decision-ready briefs attached to parked questions? If yes, lift the web restrictions as part of the permissions step above (in Claude Code, the `WebFetch` deny in the baseline; elsewhere, the tool's network setting). If no, the prep lane still runs, but offline — brainstorming and analysis from the repo and docs only.

### 1 — Save point

Run the `/save-point` workflow: the whole night must be one `/go-back` away from undone.

### 2 — The contract

State the night's terms in one short message before starting, so it is on the record:

> Working until: [budget/scope]. Research lane: [on/off]. I will build from the plan in order, verify everything, and consult your deputy (owner-proxy) instead of you. It decides what your docs prove; cheap, reversible questions it settles with research or a sensible assumption, each flagged for your morning review; anything expensive-if-wrong gets parked for breakfast — with a decision-ready brief attached if the research lane is on. When the build lane can't continue, I switch to preparation: briefs and brainstorms, all as proposals in `docs/brainstorm.md`. I stop early if: a house rule is touched, [N] stories in a row fail verification, or the budget runs out. Nothing gets deployed, deleted, purchased, or sent anywhere external. Good night.

### 3 — The work loop

Repeat until the scope or budget is done:

1. Run the `/build-next` workflow for the next Not Started story — it owns picking, building, verifying, and recording; do not re-derive its steps here. Skip its "confirm with the user" gates; the contract above is the confirmation.
2. **Any question that would go to the user goes to the owner-proxy agent instead.** In Claude Code, run it as a subagent. In Copilot, Codex, or any other assistant, read `.claude/agents/owner-proxy.md`, adopt that role fully for the ruling — verdict and grounds in its format, nothing else — then drop the role and return to building. The ruling binds you exactly as if a separate agent had issued it. Act on the verdict:
   - **DECISION** — proceed as ruled; append the proxy's `Log as:` line to `docs/decisions.md` immediately, not at the end.
   - **ASSUME** — proceed as ruled; append the proxy's `Log as:` line (tagged `ASSUMPTION … review me`) to `docs/decisions.md` immediately. If the proxy asked for evidence and the research lane is on, run the `research-analyst` first and re-consult with the brief; research lane off means the proxy rules on a stated assumption alone. If an assumption starts growing consequences mid-build — suddenly touching data, money, or other stories — stop building on it, unwind to the last clean point, and re-classify it as PARK.
   - **PARK** — record the parked question under an "Active Ideas — parked by night shift" entry in `docs/brainstorm.md`, abandon that story cleanly (no half-built code left in the working tree), and move to the next story.
   - **STOP** — end the night now; go to the morning briefing.
3. A story that fails verification twice gets parked with its failure evidence. After [N = 2] consecutive parked-by-failure stories, stop — something is systematically wrong, and burning the rest of the budget on it is not a decision the proxy is allowed to make.

### 3b — The prep lane (when the build lane cannot continue)

When every remaining story is parked, done, or blocked — and the night's budget is not yet spent — switch from committing to preparing. Everything this lane produces is a **proposal**: it lands in `docs/brainstorm.md`, never in the spec, never in code. That is why this lane needs no proxy rulings to proceed — its work is additive and reversible by construction.

- **Enrich every parked question** *(research lane on)*: run the `research-analyst` workflow on it and attach the brief to the parked entry — options, data with sources, and a recommendation — so the owner's morning decision takes thirty seconds instead of an afternoon.
- **Brainstorm upcoming work:** for the next stories in the plan, explore approaches and trade-offs in the brainstorm format (Options considered / Open questions / Decision: *not decided yet*).
- **Advance standing questions:** anything already open in `docs/brainstorm.md` that analysis or a cited brief would move forward.

The rule that governs this lane: **data informs, docs authorize.** Research may make a parked question easy to answer; it never answers it. The proxy's PARK verdicts stand — enriched, not overturned.

### 4 — Morning briefing

Always produce this, even for a stopped or empty night. It is the last message of the session and must stand alone:

> **Night shift report**
>
> **Built and verified:** [story — one line each, with the verifier's verdict]
> **Decided on your behalf:** [each proxy DECISION with its grounds — these are pending your review in `docs/decisions.md`]
> **Assumed on your behalf:** [each ASSUME with its basis — tagged `review me` in `docs/decisions.md`; disagree with one? It is a small, local redo — just say which]
> **Parked for you:** [each parked question, phrased so it can be answered over coffee — with its decision-ready brief when the research lane was on]
> **Prepared for you:** [research briefs written and options explored — one line each, all waiting in `docs/brainstorm.md`]
> **Stopped because:** [budget done / plan done / stop condition — one line]
> **Spent:** [stories completed vs. the night's scope — for actual cost, check your tool's usage view, e.g. `/cost` in Claude Code]
>
> To undo the whole night: `/go-back` to the save point "[label]". To continue: `/build-next`.

Then run the `/update-docs-and-commit` workflow and end with a final `/save-point` so the morning state is itself a save point.

## Rules

- **User-invoked only** — enforced by `disable-model-invocation` in the frontmatter (Claude Code) and binding as prose everywhere else, same standing as `/go-back`.
- **If the session loses context mid-night** (compaction, restart), re-anchor before touching anything: re-read `docs/project_status.md`, the tagged proxy rulings in `docs/decisions.md`, and the night's opening save-point label; restate the contract to yourself in one line; then resume the loop. The docs are the night's memory — trust them over recollection, and if they cannot reconstruct where the night stood, stop and write the briefing with what is known.
- The proxy's verdicts bind this session: no proceeding past a PARK "just a little", no negotiating with a STOP.
- Never deploy, delete data, add paid services, or contact anything external — these are STOPs even if a permission allowlist would technically let the command run.
- Proxy decisions are provisional until the owner reviews them; the briefing and the `(pending owner review)` tags exist so nothing becomes permanent by default.
- If this repo is the untouched template, there is no night shift — only `/start`.
