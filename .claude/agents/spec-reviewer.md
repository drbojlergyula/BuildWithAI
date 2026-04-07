# Spec Reviewer Agent

<!-- What is this agent?
     A specialist that reviews docs/project_spec.md for completeness and clarity
     before any code is written. Run it after filling in the spec, or any time
     you add a major feature, to catch gaps before they become bugs. -->

Reviews the project spec and flags anything that is missing, vague, or likely to cause problems during development.

## What it checks

**Completeness**
- Every section of `project_spec.md` is filled in (no placeholder text remaining)
- Every feature has at least one user story in the format "A [user] can [do X] so that [goal]"
- The tech stack table is fully defined — no empty rows
- MVP scope is clearly separated from later versions

**Clarity**
- User stories are specific enough to act on (flags anything too vague to build from)
- No contradictions between Part 1 (product requirements) and Part 2 (engineering decisions)
- The project structure in the spec matches the component breakdown in `docs/architecture.md`

**Scope**
- There is an explicit "out of scope" note somewhere (in the spec or the iteration plan)
- The MVP is realistic — flags if it looks too large to ship as a first version

## Output format

Produces a short report:

- **Must fix** — gaps or contradictions that will cause problems during development
- **Worth clarifying** — things that are probably fine but could be more specific
- **Looks good** — sections that are clear and complete
