# Documentation conventions

The docs in `docs/` are this project's long-term memory. Keeping them accurate is part of every task, not an afterthought.

- After completing a feature, fix, or milestone: update `docs/changelog.md` and `docs/project_status.md` (or run `/update-docs-and-commit`, which does both plus the commit).
- When a decision is made: move it from `docs/brainstorm.md` into `docs/project_spec.md`, and add one line at the top of `docs/decisions.md` (`date — decision — why`, newest first). The decision log is maintained by the assistant, automatically, as part of the work — never left as homework for the user.
- House rules are binding: see `.claude/rules/house-rules.md`.
- When the system design changes (new component, route, or data): update `docs/architecture.md` in the same piece of work.
- `docs/project_spec.md` and `docs/architecture.md` are the source of truth. If code and docs disagree, flag it — do not silently pick one.
- Write docs in plain English. The reader may be non-technical.
- Docs are loaded into the AI's context constantly, so their length is a running cost. Keep `docs/project_spec.md` and `docs/project_status.md` current-state only — completed phases get one summary line, and history lives in `docs/changelog.md`. A doc that has doubled in size since last month is due for pruning.
