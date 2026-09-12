---
type: regex
target: { source: file, path: docs/project_spec.md }
pattern: "template-state: untouched-example"
match: not_contains
weight: 2
---
The spec sentinel must be gone after /start — every later session and the validator read it as "still the example project".
