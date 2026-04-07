# /new-feature Command

<!-- What is this command?
     A shortcut for adding a new feature to the project spec in a structured way.
     Run it any time you want to add something new — it asks the right questions,
     writes the user stories, and places everything in the right section of the spec.
     Works for any project type. -->

Guides you through adding a new feature to `docs/project_spec.md`.

## When to use it

Run `/new-feature` any time you want to add something to the product that is not already in the spec — before asking Claude to build it.

## Steps

1. Ask the user to describe the feature in one or two sentences
2. Ask: who is this for, and what problem does it solve for them?
3. Write 1–3 user stories in the format: "A [user] can [do X] so that [goal]"
4. Show the stories to the user and ask: does this capture what you meant?
5. Ask: which version does this belong to — MVP, v1.0, or a later release?
6. Check `docs/project_spec.md` for any conflicts with existing features
7. Add the feature under the correct section and version in the spec
8. Ask: does `docs/architecture.md` need updating to reflect this feature?
9. If yes, update the architecture doc too
10. Confirm: "Feature added to the spec. Ready to build when you are."

## Example

```
User runs: /new-feature

Claude asks:
  What should the new feature do?
  → "I want users to be able to export their orders as a CSV file"

  Who is this for, and why do they need it?
  → "The business owner — they want to import orders into their accounting software"

Claude writes:
  User story: "The owner can download all orders as a CSV file so they can
  import them into their accounting software without manual data entry."

  Which version? → v1.0 (not MVP, but needed for launch)

Claude then:
  → Adds the feature to project_spec.md under Owner Dashboard, v1.0
  → Notes that a /api/orders/export endpoint needs adding to architecture.md
  → Updates architecture.md with the new endpoint
  → Confirms: "Done — feature added to v1.0 scope."
```
