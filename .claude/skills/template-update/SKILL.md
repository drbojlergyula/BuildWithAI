---
name: template-update
description: Bring a project created from the BuildWithAI template up to the latest template version — updates the AI team, skills, and rules via three-way comparison against the recorded base version, and runs the template's versioned structural migrations (doc restructuring with zero-loss verification) when the jump includes them. Never rewrites or deletes the project's own content. Use when the template has new releases the project should benefit from.
argument-hint: [optional target version, e.g. v2.6.0 — defaults to the latest release]
---

# /template-update — Roll Template Improvements Into This Project

The template evolves; projects born from it should not be left behind. This skill pulls the toolkit improvements (skills, agents, rules, safety machinery) from the public template into this project — deterministically, with consent, and without ever touching what makes this project *this project*.

Projects that installed the AI team as a **plugin** don't need this — `/plugin update` is their channel. This skill is for **template clones**, where the toolkit files live in the repo itself (which is what makes them work in Codex and Copilot too).

## Steps

### 1 — Find the base version

Read `.claude/template-version` — the version this project's toolkit currently matches.

If the file is missing (a clone from before v2.6.0): do the archaeology once. List the template's release tags (`git ls-remote --tags https://github.com/drbojlergyula/BuildWithAI`), fetch the closest candidates, and compare this project's `.claude/` files against each until the best match is found. Confirm the conclusion with the user ("your toolkit matches v2.3.0 — treating that as the base"), then write it to `.claude/template-version` so this never has to be guessed again.

### 2 — Fetch both versions, without touching this repo's git state

Shallow-clone the public template twice into a temp directory — the base tag and the target (latest release unless the user named one):

```
git clone --depth 1 --branch <base>   https://github.com/drbojlergyula/BuildWithAI <tmp>/base
git clone --depth 1 --branch <target> https://github.com/drbojlergyula/BuildWithAI <tmp>/latest
```

Never add remotes or tags to the project's own repository.

### 3 — The ownership boundary

**Template-owned** (may be updated by this skill):
`.claude/` — skills, agents, rules, hooks, output-styles, presets, `statusline.sh`, `settings.json`, `template-version` — plus `.claude-plugin/` (if present), `.github/copilot-instructions.md`, the validator workflow and script, `AGENTS.md`, and `CLAUDE.md`.

**Project-owned — never touched by the file sync:**
everything in `docs/`, `README.md`, all source code, `.env*`, `settings.local.json`, and **any file that does not exist in the base template** — if the user created it, it is theirs.

One sanctioned exception: **structural migrations** (step 4b) may *restructure* project docs — move, split, consolidate — under zero-loss verification. They never rewrite content, never delete it, and run only with the owner's yes to the dry-run.

### 4 — Three-way comparison, file by file

For every template-owned file, compare three states — *base*, *local*, *latest*:

- **Local identical to base** → the user never touched it → update to latest cleanly, no questions.
- **Local differs from base** → the user customized it → **conflict**: explain what they changed and what the template changed, in plain English, and ask — keep yours / take the update / merge both. Never resolve silently.
- **In latest but not in base** → new template file → add it.
- **In base but not in latest** → the template removed it → list it in the report and propose removal; the user decides.

**Special case — `AGENTS.md` and `CLAUDE.md`:** these are template-owned files that legitimately carry project-specific Overview content written by `/start`. Merge them section-wise: adopt the template's changes to the shared sections (skills/agents tables, conventions), keep the project's Overview untouched. Show the result before writing.

### 4b — Structural migrations (when the jump includes them)

Scan `<tmp>/latest/.claude/migrations/` for files with versions in the range `(base, target]`. Each is a versioned instruction file the template shipped **with** the structural change it describes — the updater executes, it never guesses. If the range holds several, they chain in version order, so a v2.3 project jumping to the latest runs every migration between, deterministically.

At this stage, *plan* them: read each migration file against the project's actual docs and compute the before/after for the dry-run report (which files split, what consolidates, what the shelf gains — and, often, "this project is small; migration X changes nothing"). Execution happens only in step 6, after the owner's yes, in this per-migration sequence:

1. Package the migration as a work packet — the migration file plus the project's affected docs — and execute it through the **`builder`** agent (Claude Code: subagent, fresh context; Codex/Copilot: adopt the builder role, execute, drop the role). Migrations *restructure*: they move, split, and consolidate. They never rewrite content, never delete it, and never "improve" anything along the way.
2. Run the migration's **zero-loss verification**: every heading and entry of the old docs accounted for as moved, merged, or in place — deleted must be 0. A migration that cannot prove zero loss is rolled back to the save point and reported, not negotiated.
3. Run `doc-sync-check` as the independent verifier on the result.

### 5 — The dry-run report (nothing is touched yet)

Present the plan and wait for a yes:

> **Template update: v[base] → v[target]**
> **What's new for you** (from the template's changelog, in plain English): [2–5 bullets — the features, not the file names]
> **Files to update cleanly:** [N] · **New files:** [N] · **Removed:** [N]
> **Your customizations detected:** [list, each with keep/update/merge question]
> **Structural migrations:** [none — or, per migration, the before/after in plain English: "your 400-line spec becomes a 40-line index + 5 domain pages; your decision log drops from 180 to 60 active lines; every line accounted for — moved, merged, or kept, zero deleted. Every session after this loads less context."]
> **Never touched:** your code, README, and [N] files you created yourself; your docs are restructured only by the migrations above, under zero-loss verification.
> Proceed?

If the template's changelog marks any version in the range as needing **migration** (a change to doc structure or conventions, not just files), surface it explicitly and follow its instructions — file sync alone does not cover behavioral changes.

### 6 — Apply, verify, record

1. Run the `/save-point` workflow first — the whole update must be one `/go-back` from undone.
2. Apply the file sync exactly as approved, including conflict resolutions.
3. Execute the structural migrations in version order, per the sequence in step 4b — builder executes, zero-loss verifies, doc-sync-check confirms, each one.
4. Write the new version to `.claude/template-version`.
5. If the project has the validator (`.github/scripts/validate_template.py`), run it.
6. Record: one line in `docs/decisions.md` (`date — updated template v[base] → v[target] — [why]`), a changelog entry, then the `/update-docs-and-commit` workflow.

## Rules

- **Consent before change:** the dry-run report is mandatory; nothing is written before the user's yes.
- **The ownership boundary is absolute.** A bug in this skill that touches `docs/` or user files is the worst possible outcome — when in doubt whether a file is template-owned, treat it as the user's and ask.
- **Deterministic before clever:** the three-way comparison decides what changed; AI judgment is only for explaining conflicts and merging the two shared instruction files.
- **Works in every assistant:** this is plain git against a public repo plus instructions — no Claude Code-specific machinery. In Codex or Copilot, follow it exactly as written.
- If this repo *is* the template itself (the `template-state: untouched-example` sentinel plus the template's own changelog), say so and stop — the template doesn't update from itself.
