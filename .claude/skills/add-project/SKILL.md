---
name: add-project
description: Add a project to this repository — on first use converts a single-project repo into a portfolio (projects/<name>/ each with its own docs brain; shared standards and a portfolio index at the root), then scaffolds each new project's brain. Use when a repo hosts, or is about to host, more than one project.
argument-hint: [project name, e.g. "webshop"]
disable-model-invocation: true
---

# /add-project — One Repo, Many Projects

Turns this repo into a **portfolio**: every project self-contained in `projects/<name>/` — its code *and* its own full docs brain — with two shared things at the root: `standards.md` (the owner's universal taste, travels between projects) and `portfolio_status.md` (the index of what lives here).

**The mode marker:** a root `portfolio_status.md` means portfolio mode. Without it, everything behaves exactly as the classic single-project template — this skill is the only door into portfolio mode, and it only opens when the owner walks through it.

**The loading rule that keeps this affordable:** sessions always load the root layer (standards + index) and the *active* project's brain — never the other projects. Context cost does not grow with project count.

## Steps

### 0 — Detect state

Root `portfolio_status.md` exists → skip to step 3 (just add the new project). Otherwise this is the **conversion**, done once, with the owner present — never at night, never unattended.

### 1 — The conversion (first use)

1. Run the `/save-point` workflow — the conversion must be one `/go-back` from undone.
2. Explain what will change in plain words, and ask for the existing project's name.
3. **Be honest about the code move before doing it.** Moving code into `projects/<name>/` can break build paths, CI workflows, and imports. Offer both options:
   - **Full move now:** `git mv` the project's code and `docs/` into `projects/<name>/`, then find and fix every path reference (build configs, CI workflows, scripts) — and **prove it: run the build/tests before declaring the conversion done.**
   - **Docs-first, code later:** create the portfolio layer now, note in the index that this project's code still lives at the root ("location: root — move pending"), and do the code move in a later sitting. Working software beats tidy folders.
4. **Split the house rules.** Walk `docs/house_rules.md` line by line with the owner: universal taste (coding principles, stack preferences, AI-budget philosophy, never-do list) moves to root `standards.md`; project-specific rules (this project's budget, client constraints) stay in the project's own `house_rules.md`. Every line lands in exactly one place — zero-loss, like a migration.
5. Create root `portfolio_status.md`: one row per project — name, path, one-line state, active phase, last night-shift scorecard summary.
6. Verify: if code moved, the build/tests run green; then run the `/doc-sync-check` workflow. Record one line in the project's `decisions.md` and finish with `/update-docs-and-commit`.

### 2 — Active-project protocol (state it to the owner once)

From now on, sessions **infer the active project** from the task and working directory and confirm it in their first reply ("we're working on *webshop*, right?"). Switching is just saying so. Portfolio-level questions ("how are all my projects doing?") use the root index.

### 3 — Add a new project

1. Create `projects/<name>/docs/` from the template's **fresh** doc set — shallow-clone the public template at this repo's `.claude/template-version` tag into a temp dir and copy its `docs/` (never copy from another project's filled docs). Example content and the `template-state: untouched-example` sentinel included, so the project's own `/start` interview works exactly as on a fresh clone.
2. Register it in `portfolio_status.md`.
3. Hand off: "Project *[name]* is scaffolded — say `/start` to set it up (the interview will be scoped to this project)."

## Rules

- Conversion is **owner-present only** — never triggered by a night shift, never by another skill.
- Never move code without proving the build still runs afterward — a conversion that breaks the build failed, regardless of how tidy the folders look.
- The standards/house-rules split is zero-loss: every line accounted for, nothing dropped.
- In every assistant this is plain instructions and git — no tool-specific machinery.
