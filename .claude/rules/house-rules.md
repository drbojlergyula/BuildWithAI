# House rules are binding

`docs/house_rules.md` holds the owner's non-negotiables. This rule is the single normative statement of how they are enforced; skills state only their workflow-specific consequence.

**First, check whether they exist at all.** If `docs/house_rules.md` still carries the `house-rules: unset` marker — or still describes the template's example product — then **this project has no house rules yet, and nothing in that file binds anything.** The owner's current instructions govern instead. Measured why: a field run was given a $5/month budget while the untouched example file said $20/month and forbade adding dependencies; a literal agent would have budgeted $20, or stopped to ask an owner who had explicitly said not to ask. Placeholder content must never sit behind a rule that says *binding*.

- Re-read `docs/house_rules.md` before: adding any service, dependency, or cost; touching anything on its never-do list; choosing between approaches that differ in money, time, or risk.
- If a task conflicts with a house rule: **stop and ask the owner** — never quietly violate, never quietly comply with the conflicting request.
- Workflow-specific escalations (defined in the skills/agents themselves): `/go-live` treats a violation as an automatic launch blocker; the project-advisor reports violations as High-priority findings.
- When the owner explicitly changes a rule, update `docs/house_rules.md` in the same piece of work and add a line to `docs/decisions.md`.
