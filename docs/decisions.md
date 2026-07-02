# Decision Log

<!-- One line per decision, newest first. Maintained AUTOMATICALLY by the AI
     workflows (/start, /new-feature, /update-docs-and-commit, /fix-bug) whenever
     a decision is made — you never have to remember to update this file.
     This is the project's answer to "wait, why did we do it that way?"
     Format: date — decision — why. One line. No ceremony. -->

| Date | Decision | Why |
|---|---|---|
| 2026-03-30 | Orders stored in SQLite, not a hosted database *(example)* | Zero cost, zero ops, plenty for one shop's volume |
| 2026-03-29 | No customer accounts in MVP *(example)* | Biggest source of build complexity; owner confirmed customers won't register just to order |
| 2026-03-28 | Node.js + plain HTML over a React stack *(example)* | Solo non-technical owner; simplest thing that works wins |
