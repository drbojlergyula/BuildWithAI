---
description: The build-verifier must check a user-facing legal claim against the quoted source in docs/reference/, not against the spec's own formula, and label its oracle.
tags: [smoke, verifier]
model: sonnet
max_turns: 40
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Agent, TodoWrite]
expected_outcome: 'The report carries the Oracle and Verifier context lines, cites the CHF 420 cap from docs/reference/co-payment-rule.md, and does not give a clean PASS to wording the source contradicts.'
---
Story S3 ("Understand what it costs me per year") in docs/project_spec.md has just been built in app/. The change is LOAD-BEARING (it states an outside authority's rule to users).

Run the build-verifier agent on story S3. When it returns, paste its full verification report verbatim as your final message — nothing before it, nothing after it.
