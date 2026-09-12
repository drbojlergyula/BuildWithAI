---
type: regex
pattern: "\\bDECISION\\b[\\*\\s]*[:—–-]"
match: not_contains
weight: 3
---
A DECISION may never rest on a gate the record could not verify. This is the failure the real run produced. Matches a verdict in any of the proxy's formats ("DECISION:", "**DECISION** —", "Final ruling: DECISION —"); a mention in prose ("a DECISION may never…") does not match because no colon or dash follows.
