---
name: doc-sync-check
description: Health check on all project documents — finds stale status entries, contradictions between docs, leftover placeholder text, and undecided brainstorm items. Use whenever the docs might be out of date.
---

# /doc-sync-check — Documentation Health Check

Checks that all project documents are consistent with each other and up to date. Especially useful after a busy build session or before sharing the project with someone new.

## Steps

1. Read the main project docs: `project_spec.md`, `architecture.md`, `project_status.md`, `changelog.md`, `brainstorm.md`.

2. If this repository is a reusable multi-assistant template (it contains `AGENTS.md` or `.github/copilot-instructions.md`), also read those files plus `CLAUDE.md`, `README.md`, and the files in `.claude/agents/` and `.claude/skills/` — and check them for drift against each other.

3. Check for these issues:

   **Stale content**
   - Does `project_status.md` reflect what is actually built? Look for phases marked "In Progress" that seem complete, or "Not Started" that have clearly been worked on.
   - Was `changelog.md` updated after the most recent change? Check `git log` for commits with no matching changelog entry.

   **Inconsistencies**
   - Does the project structure in `project_spec.md` match the component breakdown in `architecture.md`?
   - Are there features in the spec with no corresponding component in the architecture, or vice versa?
   - Do the README's claims about available tools, skills, and agents match the actual files in `.claude/`?
   - In a multi-assistant template: do `AGENTS.md`, `CLAUDE.md`, and `.github/copilot-instructions.md` describe the same workflows without contradicting each other?

   **Leftover placeholders**
   - Any section still containing example text, "TODO", "TBD", or placeholder dates like "YYYY-MM-DD"?

   **Unresolved brainstorm items**
   - Any ideas in `brainstorm.md` marked as undecided that should have been decided by now based on what is built?

4. Report findings under four headings:
   - **Out of date** — docs that need updating to reflect current state
   - **Inconsistent** — things that contradict between files
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
