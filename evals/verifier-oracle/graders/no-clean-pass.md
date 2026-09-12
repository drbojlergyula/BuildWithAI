---
type: regex
pattern: "Verdict:\\s*PASS\\s*$"
flags: m
match: not_contains
weight: 2
---
Wording the source contradicts ("the remaining 15 points are uncapped") must not receive a clean PASS; FAIL or PASS WITH WARNINGS are the honest verdicts.
