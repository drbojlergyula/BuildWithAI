---
name: adopt-project
description: Bring an EXISTING codebase into the docs-as-memory system — reverse-engineers the spec, architecture, and conventions from the code, interviews the user about intent, and sets up the project brain around what already exists. Use when there is already code but no project docs, including projects exported from Lovable, Bolt, v0, or Replit.
---

# /adopt-project — Give an Existing Project a Brain

For projects that already have code: prototypes graduating from Lovable/Bolt/v0/Replit, codebases the AI team was just installed into (via the plugin), or anything built before this system existed. The code is the evidence; the user fills in the intent.

## Steps

### 1 — Read the code first

Silently survey the codebase before asking anything:
- Top-level structure, main entry points, frameworks and dependencies (package/config files)
- Routes, pages, components, data models — what does this thing actually *do*?
- Conventions already in use: naming, file layout, styling approach, test setup
- Signs of origin (Lovable/Bolt/v0 export markers, generated boilerplate) — these often carry dead code worth flagging
- `git log` for the story so far

### 2 — Play it back

Summarise what you found in plain English, as a guess to be corrected:

> "Here's what I can see: this is a [type of app] built with [stack]. It currently does [A, B, C]. I couldn't tell: [X, Y]. Did I get that right?"

Let the user correct you before writing anything.

### 3 — Fill the intent gap (short interview)

Ask only what the code cannot tell you, one or two questions at a time:
- Who is this for, and what problem does it solve?
- What works today vs. what is half-built or abandoned?
- What is the next milestone — what does "done enough to show people" look like?
- House rules: budget ceiling, things never to touch without asking, tone, hard constraints

### 4 — Write the project brain

Create or fill the docs to match **reality, not aspiration**:
1. `docs/project_spec.md` — what the product is, who it is for, features as user stories (mark each: ✅ built / 🚧 partial / ⏳ planned)
2. `docs/architecture.md` — the *actual* current architecture, including discovered conventions ("components use X pattern; keep following it") and any debt worth noting
3. `docs/project_status.md` — phases with the built/partial/planned split, next milestone on top
4. `docs/house_rules.md` — the non-negotiables from the interview
5. `docs/decisions.md` — seed it with the visible past decisions ("chose [stack] — inherited from prototype") so the log starts honest
6. `docs/changelog.md` — one entry: "Project adopted into docs-as-memory system", plus what state it arrived in
7. `docs/brainstorm.md` — anything the user mentioned wanting but hasn't decided
8. Update the Overview in `AGENTS.md`/`CLAUDE.md` to describe the real product

### 5 — Hand over

Close by following `/start`'s Phase 6 ("Meet your AI team"), Phase 7 (first advisor review offer), and Phase 8 (wrap-up) — read that skill and reuse its reveal and next-steps script rather than improvising a thinner version here. Two adoption-specific adjustments:
- Pitch the advisor review harder: adopted prototypes almost always have blind spots (error handling, secrets in code, no data backup), and "your advisor already found three things" is the moment this system proves itself.
- In the wrap-up, replace "read through the spec" with "check that the spec matches what your code actually does — correct me where I guessed wrong."

## Rules

- Document what IS, not what should be. Aspirations go to `brainstorm.md` or the plan, never into the spec as if they existed.
- Do not refactor, clean up, or "fix" anything during adoption — this workflow only builds the memory. Suggest cleanups as advisor material.
- If you find something urgent while reading (committed secrets, obviously broken core flow), flag it immediately and prominently — do not save it for the docs.
