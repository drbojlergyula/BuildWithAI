---
mode: ask
description: Review the project and surface the highest-priority blind spots.
---

# Project Advisor

Use the shared `project-advisor` workflow from `docs/assistant_workflows.md`.

If the user asks to run the `project-advisor` agent, treat it as a request for this workflow and produce a short prioritized review of the project.

After reading the project docs, scan the actual file structure beyond `docs/`. Compare it against `docs/architecture.md` and flag anything that exists in code but not in docs, or is described in docs but missing from code. Include findings in the advisory report under a section called "Reality check". If no application code exists yet, state that clearly and skip the scan.
