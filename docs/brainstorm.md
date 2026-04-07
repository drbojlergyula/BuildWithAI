# Brainstorm

This is a scratchpad for exploring ideas **before** they are ready for [project_spec.md](docs/project_spec.md).

Use it to think through a feature, weigh options, and settle on an approach. Once a decision is made, move the outcome into the spec and clear or archive the entry here.

---

## How to use this file

1. **Add an idea** — write it down roughly, even if it's just a sentence
2. **Explore it** — list options, pros/cons, open questions
3. **Decide** — mark the chosen direction
4. **Promote** — copy the decision into `project_spec.md` under the right section
5. **Clear it** — move it to the Archive section below

---

## Active Ideas

<!-- Add ideas here. One H3 heading per idea.
     Example below — delete when you add your own. -->

### User notifications *(example — delete when you start)*

**The idea:**
When a new order comes in, automatically notify the owner rather than them having to check the dashboard manually.

**Options considered:**

| Option | Pros | Cons |
|---|---|---|
| Email notification on each submission | Simple, no extra service needed | Can get noisy with high volume |
| Daily digest email | Less noise | Owner might miss urgent orders |
| SMS via Twilio | Instant, hard to miss | Costs money, extra integration |

**Open questions:**
- How many orders per day is the owner expecting?
- Does "immediately" matter, or is checking once a day enough for now?

**Decision:** *(not decided yet — ask the owner before adding to spec)*

---

## Archive

<!-- Move resolved ideas here once they have been added to project_spec.md. -->

### Order status labels *(example resolved idea)*

**Decision:** Keep it simple — two statuses only: **New** and **Handled**. No "In Progress" or custom labels for now.

**Why:** Adding more statuses adds complexity to the dashboard filter and the database schema. If the owner needs more granularity later, it can be added in v2.

**Added to spec:** Features & User Stories → Owner Dashboard, and System Design Preferences (no complex state machine needed for MVP).
