---
name: fix-bug
description: Structured bug-fixing workflow — reproduce the problem, find the cause, fix it, verify the fix actually works, and record it in the changelog. Use when something is broken or behaving unexpectedly.
argument-hint: [what went wrong]
---

# /fix-bug — Find It, Fix It, Prove It

A disciplined bug-fixing loop. The goal is not just a fix — it is a *verified* fix the user can trust, plus a paper trail.

If the user provided a description as an argument, treat it as the bug report and start from step 2.

## Steps

1. **Get the symptom.** Ask the user, in plain English:
   - What did you expect to happen?
   - What happened instead?
   - When did it last work, if ever?

2. **Reproduce it first.** Before changing anything, try to see the failure yourself — run the app, the failing command, or the relevant test. If you cannot reproduce it, say so and ask for more detail (exact steps, error message, screenshot text). Never fix blind.

3. **Diagnose.** Trace the failure to its cause. Read the relevant code, add temporary logging if needed, check recent commits (`git log`) for what changed. Explain the root cause to the user in one or two plain-English sentences before fixing — no jargon.

4. **Fix it.** Make the smallest change that fixes the root cause, not just the symptom. Match the style of the surrounding code.

5. **Prove it.** Re-run whatever demonstrated the failure in step 2 and show that it now passes. If the project has tests, run them. If the fix cannot be verified automatically, tell the user exactly what to click or run to confirm.

6. **Record it.** Add a `### Fixed` entry to `docs/changelog.md` describing the bug and the fix in user-visible terms. If the bug revealed a gap in the spec or architecture docs, offer to update them.

7. **Wrap up.** Summarise: what was broken, why, what changed, and how it was verified. Suggest `/update-docs-and-commit` to save the work.

## Rules

- Reproduce before fixing; verify after fixing. No exceptions.
- One bug at a time. If you discover a second bug on the way, note it and ask before widening scope.
- If the "bug" is actually missing functionality, say so and suggest `/new-feature` instead.
