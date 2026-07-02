---
name: put-me-in-context
description: Produce an instant, structured briefing on the whole project — what it is, current status, next steps, open decisions, and risks. Use when the user (or a new teammate) needs to get up to speed fast.
---

# /put-me-in-context — Instant Project Briefing

One prompt replaces onboarding meetings, status emails, and documentation hunting. This is the template's signature move — make the briefing sharp.

## Steps

1. **Read everything relevant:**
   - All files in `docs/`: `project_spec.md`, `architecture.md`, `project_status.md`, `changelog.md`, `brainstorm.md`
   - Recent git history (`git log --oneline -15`) to catch work the docs may not mention yet
   - If application code exists, glance at the top-level structure so the briefing reflects reality, not just the docs

2. **Produce the context brief** with exactly these sections:

   - **What this project is** — one paragraph, plain English, no jargon
   - **Current status** — active phase, what is done, what is in progress
   - **Next steps** — the top 3 priorities, in order
   - **Open decisions** — unresolved questions someone needs to answer
   - **Known risks or blockers** — anything that could derail progress

3. **Close with:** "Ask me anything about this project."

4. **Feedback loop.** Ask whether the brief matches the user's understanding and what is missing or wrong. If the docs and reality have drifted, offer to update the docs on the spot — and do it if they agree.

## Rules

- Be concrete. "MVP order form is built and committed; dashboard is not started" beats "good progress has been made."
- If the docs contradict each other or the git history, say so in the brief rather than papering over it.
- If the template is still untouched (example content everywhere), say that plainly and suggest `/start` instead of inventing a briefing.
