# /update-docs-and-commit Command

<!-- What is this command?
     Run this after completing a meaningful piece of work — a feature, a bug fix,
     a milestone. It updates the project docs to reflect what was done, then
     creates a git commit. Keeps your project history and documentation in sync
     without having to think about it. -->

Updates project documentation to reflect recent work, then commits everything to git.

## When to use it

Run `/update-docs-and-commit` after:
- Completing a feature or milestone
- Fixing a significant bug
- Making a decision that changes the spec or architecture

## Steps

1. Ask: "What did you just complete or change?" — wait for the answer
2. Ask: "Is this part of the MVP, v1.0, or another version?" (skip if obvious from context)
3. Update `docs/changelog.md`:
   - Add a new dated entry (use today's date)
   - Write one bullet per meaningful change under ### Added, ### Changed, or ### Fixed
4. Update `docs/project_status.md`:
   - Mark any completed phases or milestones as done
   - Update the "Next" section to reflect what is coming
5. Check if `docs/project_spec.md` or `docs/architecture.md` needs updating — if yes, update them
6. Stage all changed files with `git add`
7. Write a commit message in this format:
   - First line: short summary of what was done (max 72 characters)
   - Blank line
   - One or two bullet points with more detail if needed
8. Commit and confirm: "Committed. Your docs and git history are up to date."

## Example

```
User runs: /update-docs-and-commit

Claude asks:
  What did you just complete?
  → "Finished the order form — it submits and shows a confirmation message"

  Is this MVP, v1.0, or something else?
  → "MVP"

Claude then:
  → Adds to changelog.md:
      ## 2026-03-29
      ### Added
      - Order form — submits customer details and shows confirmation on success

  → Updates project_status.md:
      MVP: Order form — ✅ COMPLETE
      Next: Owner dashboard

  → Commits:
      git commit -m "Add order form with submission and confirmation"

  → Confirms: "Done — docs updated and committed."
```
