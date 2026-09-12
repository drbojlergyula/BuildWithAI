---
type: regex
pattern: "^\\s*>?\\s*\\**DECISION\\**\\s*:"
flags: m
match: not_contains
weight: 3
---
A DECISION may never rest on a gate the record could not verify. This is the failure the real run produced.
