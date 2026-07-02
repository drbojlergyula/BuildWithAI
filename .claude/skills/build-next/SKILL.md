---
name: build-next
description: Build the next feature from the plan — picks the next not-started story from the project status, assembles everything needed, implements it, has it independently verified, and records the result. Use when the user says "build the next thing", "keep going", or names a story to build.
argument-hint: [story or feature to build (optional — defaults to the next one in the plan)]
---

# /build-next — From Plan to Working, Verified Feature

The bridge between the spec and reality. One command takes the next planned story, builds it, proves it works, and saves the progress. This is the daily rhythm of the project.

## Steps

1. **Pick the work.** If the user named a story or feature, use that. Otherwise read `docs/project_status.md` and propose the next Not Started item in the active phase, respecting the order. Confirm in one line: "Next up: *[story]* — build it?" and wait for a yes.

2. **Assemble the context packet.** Before writing any code, gather — briefly, not exhaustively:
   - The user stories and acceptance criteria for this feature from `docs/project_spec.md`
   - The relevant constraints from `docs/architecture.md` (components, routes, data touched)
   - `docs/house_rules.md` — the non-negotiables
   - Any related entries in `docs/decisions.md`
   State the packet back in 3–5 bullet points ("Building X. It must do A and B. It touches C. House rules that apply: D."). This is the contract for the build.

3. **Build it.** Implement the smallest complete version that satisfies the stories. Match the existing code style. If a real decision comes up mid-build (a trade-off the owner should know about), make the sensible call, flag it, and append it to `docs/decisions.md`.

4. **Verify it — independently.** Run the build-verifier agent on the feature. It will exercise the real flow and return PASS / FAIL with evidence. If it fails, fix and re-verify — do not declare done on a failed verification. If verification is impossible in this environment, tell the user exactly what to click or run to confirm it themselves.

5. **Record the progress.**
   - Mark the story done in `docs/project_status.md`
   - Add the changelog entry in `docs/changelog.md`
   - Append any decisions made to `docs/decisions.md`
   - Offer `/save-point` (or `/update-docs-and-commit` if docs need more care) to commit

6. **Point forward.** Close with what is next in the plan, in one line: "Next in the plan: *[story]* — say `/build-next` when ready."

## Rules

- One story per invocation. If the story is too big to build in one go, say so and propose splitting it in the spec first.
- The verification step is not optional. A feature that was never run is not done.
- Respect `docs/house_rules.md` as hard constraints — if a story conflicts with a house rule, stop and ask rather than quietly violating it.
- If no plan exists yet (empty or example status doc), suggest `/start` (new project) or `/adopt-project` (existing code) instead.
