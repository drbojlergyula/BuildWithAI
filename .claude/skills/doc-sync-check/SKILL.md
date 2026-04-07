# Doc Sync Check Skill

<!-- What is this skill?
     A quick health check on all project documents. Run it any time you want to
     make sure the docs reflect reality — especially useful after a busy build
     session or before sharing the project with someone new. -->

Checks that all project documents are consistent with each other and up to date.

## Steps

1. Read all five docs: `project_spec.md`, `architecture.md`, `project_status.md`, `changelog.md`, `brainstorm.md`
2. Check for these issues:

   **Stale content**
   - Does `project_status.md` reflect what is actually built? Look for phases marked "In Progress" that seem complete, or "Not Started" that have clearly been worked on.
   - Was `changelog.md` updated after the most recent change? Check git log for commits that don't have a matching changelog entry.

   **Inconsistencies**
   - Does the project structure in `project_spec.md` match the component breakdown in `architecture.md`?
   - Are there features in the spec that have no corresponding component in the architecture, or vice versa?

   **Leftover placeholders**
   - Any section still containing example text, "TODO", "TBD", or placeholder dates like "YYYY-MM-DD"?

   **Unresolved brainstorm items**
   - Any ideas in `brainstorm.md` marked as undecided that should have been decided by now based on what is built?

3. Report findings:
   - **Out of date** — docs that need updating to reflect current state
   - **Inconsistent** — things that contradict between files
   - **Placeholder text remaining** — sections not yet filled in
   - **All good** — if nothing needs attention

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
