---
description: Brief-driven /start (Phase 0b) on the untouched template must clear the sentinel and the house-rules marker and write an Engineering Profile.
tags: [smoke, start]
model: sonnet
max_turns: 80
timeout_seconds: 1500
allowed_tools: [Read, Glob, Grep, Skill, Agent, TodoWrite]
expected_outcome: 'docs/project_spec.md no longer contains the untouched-example sentinel and has an Engineering Profile section; docs/house_rules.md no longer contains the house-rules unset marker.'
---
/start

I will not be answering questions in this session. Treat this message as my written brief and set the project up from it in one pass; where the brief is silent, make a sensible assumption and record it as one, do not ask.

**Project:** "Brotkorb" — a one-page website for a neighbourhood bakery in Bern where regular customers pre-order bread for next-day pickup. Public, no accounts, no payments: the customer picks items and a pickup time, leaves a name and phone number, and the order is emailed to the bakery. German only for now. Stack: plain HTML/CSS/JS front end, one small Python (Flask) endpoint that sends the email through the bakery's existing mailbox; hosted on a free tier. Budget: zero recurring cost beyond the mailbox they already pay for. Never add paid services. The owner is the baker, not a developer.

**Out of scope:** online payment, user accounts, delivery, a mobile app.

Do the whole setup — all project documents, house rules, the decision log, the engineering profile — and finish with the team introduction. Do not stop to confirm anything.
