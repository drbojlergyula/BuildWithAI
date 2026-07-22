---
name: night-shift
description: Autonomous work session for outside business hours — runs the build loop with the owner-proxy agent answering judgment questions from documented owner intent, parks what it cannot prove, and ends with a morning briefing. User-invoked only; never triggers automatically.
argument-hint: [scope for the night, e.g. "3 stories", "finish the MVP list", or a token/cost budget]
---

# /night-shift — Your AI Team Works While You Sleep

Runs the normal build rhythm unattended. Every question that would normally wake the owner goes to the **owner-proxy** agent instead, which answers only what the project docs can prove and parks the rest. The owner wakes up to verified features, a list of decisions made on their behalf, and a short briefing — never to surprises.

**User-invoked only.** Never start a night shift on your own initiative, and never treat "keep going" during daily work as an invitation to enter this mode.

## Steps

### 0 — Preflight (while the owner is still awake)

Do these checks before anything else; refuse to start if one fails:

1. **The project is set up.** If the `template-state: untouched-example` sentinel is present in `docs/project_spec.md` or no plan exists in `docs/project_status.md`, stop and suggest `/start` — there is nothing to work on yet.
2. **Permissions won't stall the night.** The proxy answers *judgment* questions; it cannot click *permission* dialogs — those come from the harness, and an unattended session will hang on the first one. Check `.claude/settings.local.json` for a night-shift allowlist. If there isn't one, propose one now, while the owner can approve it: read the project's stack and offer the commands a build loop will need (test runner, dev server, linter, `git commit`), plus the deny baseline from `.claude/presets/night-shift.settings.json`. Write it to `.claude/settings.local.json` (gitignored) only with the owner's yes. Note the baseline is deliberately strict: it also denies `WebFetch` and external `curl -X POST` — which blocks `research-analyst` web reads and QA of local POST endpoints. If tonight's plan needs either, the owner removes those specific lines now, knowingly; deny rules always beat allow rules, so this cannot be fixed later by the allowlist.
3. **The night has a budget.** From the argument if given, else the AI budget line in `docs/house_rules.md`, else ask for one number before starting. A night without a budget does not start.
4. **The strongest model is loaded.** Recommend the owner switch the session to their strongest model before leaving — the proxy inherits it, and judgment is what it is there for. The build workers stay on their own tiers regardless.

### 1 — Save point

Run the `/save-point` workflow: the whole night must be one `/go-back` away from undone.

### 2 — The contract

State the night's terms in one short message before starting, so it is on the record:

> Working until: [budget/scope]. I will build from the plan in order, verify everything, and consult your deputy (owner-proxy) instead of you. It only decides what your docs prove; everything else gets parked for breakfast. I stop early if: a house rule is touched, [N] stories in a row fail verification, or the budget runs out. Nothing gets deployed, deleted, purchased, or sent anywhere external. Good night.

### 3 — The work loop

Repeat until the scope or budget is done:

1. Run the `/build-next` workflow for the next Not Started story — it owns picking, building, verifying, and recording; do not re-derive its steps here. Skip its "confirm with the user" gates; the contract above is the confirmation.
2. **Any question that would go to the user goes to the owner-proxy agent instead.** Act on the verdict:
   - **DECISION** — proceed as ruled; append the proxy's `Log as:` line to `docs/decisions.md` immediately, not at the end.
   - **PARK** — record the parked question under an "Active Ideas — parked by night shift" entry in `docs/brainstorm.md`, abandon that story cleanly (no half-built code left in the working tree), and move to the next story.
   - **STOP** — end the night now; go to the morning briefing.
3. A story that fails verification twice gets parked with its failure evidence. After [N = 2] consecutive parked-by-failure stories, stop — something is systematically wrong, and burning the rest of the budget on it is not a decision the proxy is allowed to make.

### 4 — Morning briefing

Always produce this, even for a stopped or empty night. It is the last message of the session and must stand alone:

> **Night shift report**
>
> **Built and verified:** [story — one line each, with the verifier's verdict]
> **Decided on your behalf:** [each proxy DECISION with its grounds — these are pending your review in `docs/decisions.md`]
> **Parked for you:** [each parked question, phrased so it can be answered over coffee]
> **Stopped because:** [budget done / plan done / stop condition — one line]
> **Spent:** [rough cost/token figure if the environment exposes one; otherwise stories completed vs. planned]
>
> To undo the whole night: `/go-back` to the save point "[label]". To continue: `/build-next`.

Then run the `/update-docs-and-commit` workflow and end with a final `/save-point` so the morning state is itself a save point.

## Rules

- **User-invoked only** — same standing as `/go-back`.
- The proxy's verdicts bind this session: no proceeding past a PARK "just a little", no negotiating with a STOP.
- Never deploy, delete data, add paid services, or contact anything external — these are STOPs even if a permission allowlist would technically let the command run.
- Proxy decisions are provisional until the owner reviews them; the briefing and the `(pending owner review)` tags exist so nothing becomes permanent by default.
- If this repo is the untouched template, there is no night shift — only `/start`.
