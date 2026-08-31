---
name: doc-sync-check
description: Health check on all project documents — finds stale status entries, contradictions between docs, leftover placeholder text, and undecided brainstorm items. Use whenever the docs might be out of date.
---

# /doc-sync-check — Documentation Health Check

Checks that all project documents are consistent with each other and up to date. Especially useful after a busy build session or before sharing the project with someone new.

## Steps

1. Read the main project docs: `project_spec.md`, `architecture.md`, `project_status.md`, `changelog.md`, `brainstorm.md`, `house_rules.md`, `decisions.md`.

2. If this repository is a reusable multi-assistant template (it contains `AGENTS.md` or `.github/copilot-instructions.md`), also read those files plus `CLAUDE.md`, `README.md`, and the files in `.claude/agents/` and `.claude/skills/` — and check them for drift against each other.

3. Check for these issues:

   **Stale content**
   - Does `project_status.md` reflect what is actually built? Look for phases marked "In Progress" that seem complete, or "Not Started" that have clearly been worked on.
   - Was `changelog.md` updated after the most recent change? Check `git log` for commits with no matching changelog entry.

   **Inconsistencies**
   - Does the project structure in `project_spec.md` match the component breakdown in `architecture.md`?
   - Are there features in the spec with no corresponding component in the architecture, or vice versa?
   - **Hub-and-spoke integrity** *(if `docs/spec/` or `docs/architecture/` pages exist)*: every spoke page is linked from its hub's index line, every hub link resolves to a real file, and no spoke duplicates content that also lives in the hub.
   - **Reference shelf** *(if `docs/reference/` exists)*: the README table lists exactly the files on the shelf — no unlisted files, no dead rows.

   **Plan coverage and story health**
   - Every feature in `project_spec.md` has at least one story in `project_status.md`'s plan — and every planned story traces back to something in the spec. Flag features with no story and orphan stories.
   - Story dependencies make sense: if stories note "depends on", the dependency exists, is not circular, and is not scheduled later than the story that needs it.
   - **Oversized stories:** flag any planned story that is not one independently verifiable outcome buildable in a single sitting — it should have been split at the plan's door (`/new-feature`, `/start`); propose the split.

   **Portfolio integrity** *(if a root `portfolio_status.md` exists)*
   - The index lists exactly the project directories under `projects/` — no ghost rows, no unlisted projects.
   - Root `standards.md` and any project's `house_rules.md` do not contradict each other; a project may tighten a standard, never silently loosen one.

   **Decision-log lifecycle**
   - Is `docs/decisions.md` past ~100 lines? Flag it for consolidation per the documentation conventions: old ratified night-shift rulings fold into thematic one-liners; LESSON lines, reversals, and house-rule changes stay verbatim.
   - Do the README's claims about available tools, skills, and agents match the actual files in `.claude/`?
   - In a multi-assistant template: do `AGENTS.md`, `CLAUDE.md`, and `.github/copilot-instructions.md` describe the same workflows without contradicting each other?

   **Leftover placeholders**
   - Any section still containing example text, "TODO", "TBD", or placeholder dates like "YYYY-MM-DD"?

   **Unresolved brainstorm items**
   - Any ideas in `brainstorm.md` marked as undecided that should have been decided by now based on what is built?

   **Code vs. spec drift** *(if application code exists)*
   - Pick the 3–5 most important user stories in the spec and check the code actually implements them — routes exist, components exist, error states exist where promised.
   - Look the other way too: significant code (new routes, models, pages) that the spec and architecture never mention.
   - Check recent work against `docs/house_rules.md` — flag anything that quietly violates a house rule (new paid service, unprotected admin page, missing error state).

4. Report findings under five headings:
   - **Out of date** — docs that need updating to reflect current state
   - **Inconsistent** — things that contradict between files
   - **Code drift** — where the code and the spec/house rules disagree
   - **Placeholder text remaining** — sections not yet filled in
   - **All good** — if nothing needs attention

5. Offer to fix everything found, and fix it if the user agrees.

## Example output

```
doc-sync-check complete

Out of date:
  - project_status.md: "Order form" is marked In Progress but appears complete
    based on changelog entry from 2026-03-29 — mark as done

Inconsistent:
  - project_spec.md lists a /api/orders/export endpoint but architecture.md
    has no corresponding route — add it to the routes section

Placeholder text remaining:
  - changelog.md still contains "YYYY-MM-DD" example entry — replace or delete

All other docs look consistent and up to date.
```
