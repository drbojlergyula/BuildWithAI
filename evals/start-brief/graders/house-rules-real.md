---
type: regex
target: { source: file, path: docs/house_rules.md }
pattern: "house-rules: unset"
match: not_contains
weight: 2
---
The house-rules marker must be gone once real rules are written; while it is present nothing in the file binds.
