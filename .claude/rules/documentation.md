# Documentation conventions

The docs in `docs/` are this project's long-term memory. Keeping them accurate is part of every task, not an afterthought.

- After completing a feature, fix, or milestone: update `docs/changelog.md` and `docs/project_status.md` (or run `/update-docs-and-commit`, which does both plus the commit).
- When a decision is made: move it from `docs/brainstorm.md` into `docs/project_spec.md`. Brainstorm entries are for undecided ideas only.
- When the system design changes (new component, route, or data): update `docs/architecture.md` in the same piece of work.
- `docs/project_spec.md` and `docs/architecture.md` are the source of truth. If code and docs disagree, flag it — do not silently pick one.
- Write docs in plain English. The reader may be non-technical.
