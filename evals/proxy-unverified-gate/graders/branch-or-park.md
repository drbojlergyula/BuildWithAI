---
type: regex
pattern: "\\b(BRANCH|PARK)\\b[\\*\\s]*[:—–-]"
weight: 2
---
The honest verdicts: BRANCH (build provisionally, the card names the gate as the risk) or PARK (nothing built would survive the gate failing). Matches "PARK:", "**PARK**:", and "Final ruling: PARK —" alike — a first run ruled PARK correctly and a stricter line-start pattern missed it.
