---
name: new-feature
description: Add a new feature to the project spec before building it. Guides the user through what it does, who it is for, user stories, and which version it belongs in, then updates the docs.
argument-hint: [short description of the feature]
---

# /new-feature — Add a Feature to the Spec

Adds a new feature to `docs/project_spec.md` the right way: understood first, written as user stories, placed in the correct version — before any code is written.

If the user provided a description as an argument, treat it as the answer to "what does the feature do?" and skip straight to the follow-up questions.

## Steps

1. **Understand the feature.** Ask (one or two questions at a time):
   - What does the feature do, from the user's point of view?
   - Who is it for, and what problem does it solve?
   - How will you know it is working — what does success look like?

2. **Write the user stories.** Draft one to three user stories in the format
   *"A [user] can [do X] so that [goal]."*
   Show them to the user and confirm the wording before writing anything into the spec.

3. **Place it in a version.** Recommend whether this belongs in the MVP, v1.0, or a later version — and say why. If it displaces something else, say that too. Confirm with the user.

4. **Update the docs.**
   - Add the feature and its user stories to the right section of `docs/project_spec.md`.
   - Update `docs/architecture.md` if the feature changes the system design (new components, routes, data).
   - Add the feature to the right milestone in `docs/project_status.md`, marked Not Started.
   - If related undecided ideas exist in `docs/brainstorm.md`, resolve or link them.

5. **Confirm and offer next steps.** Tell the user what changed, then offer:
   - "Build it now" — start implementing immediately
   - "Review first" — run the spec-reviewer agent to sanity-check the addition

## Rules

- Never add a feature to the spec that you could not build from as written. Vague stories get clarified first.
- Keep the MVP honest — if the user wants everything in MVP, push back gently with the cost.
- Plain English, no jargon.
