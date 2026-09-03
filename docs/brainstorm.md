# Brainstorm

This is a scratchpad for exploring ideas **before** they are ready for [project_spec.md](docs/project_spec.md).

Use it to think through a feature, weigh options, and settle on an approach. Once a decision is made, move the outcome into the spec and clear or archive the entry here. A research brief still worth reading *after* its decision is made moves to the reference shelf (`docs/reference/`) instead of the archive.

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

### Competitive-research harvest *(deep market scan, parked 2026-08-23)*

Full landscape reviewed (Spec Kit, BMAD v6, Agent OS, Kiro, Cline Memory Bank, Taskmaster, Ralph loops, claude-flow). Positioning confirmed: nobody combines non-technical persona + earned autonomy + cross-assistant single definition. Five refinements worth keeping, none urgent:

1. ~~**Coverage check**~~ — *built in v2.9.1* (doc-sync-check: spec↔plan coverage, orphan stories, dependency validation)
2. ~~**Doc gardening in the prep lane**~~ — *built in v2.9.1* (nights prepare consolidations/pruning/splits as morning-ratified proposals)
3. **Scale-adaptive ceremony** (from BMAD): planning/ritual depth scales with task size — generalizes the parked preflight-compression debt. *After real-night feedback.*
4. ~~**Story-splitting guard**~~ — *superseded and built in v2.9.1 as the sizing rule at the plan's door* (owner field input: split on entry, not at build)
5. **Cross-project owner profile** (from Agent OS 3-layer): *promoted to the v3.0 "Portfolio brain" direction* — owner evidence: many projects per repo, growing complexity. Design round pending.

**Decision:** *items 1, 2, 4 built (v2.9.1); item 5 is the v3.0 direction; item 3 waits for night feedback*

### `/verification-record` — a shareable audit trail *(parked 2026-09-03, one strong data point)*

**The idea:** compose the raw material the brain already holds (decisions, changelog, validation logs, test output, rejected options) into a single shareable HTML record: what was decided, what was rejected and why, what the tests caught, what is *not* verified.

**Evidence for:** an operator asked for exactly this by hand after an autonomous build, and the result was the most credible artifact the project has produced — precisely because it documented two abandoned products, four caught bugs and seven unverified claims. "A build log with no rejections and no failures is a marketing document."

**Evidence against:** its quality came from that run's specific content. A generic composer might produce a generic document, and the raw material is already in the brain for anyone who wants it. Also a 15th skill — the seat must be earned.

**Decision:** *(not decided — revisit if a second operator asks for the same artifact by hand)*

### Per-category auto-accept — the autonomy ladder's next rung *(template's own idea, parked 2026-08-01)*

**The idea:**
The morning review currently ratifies every ruling individually. Once a decision *category* (e.g. naming, copy wording) shows a long streak of acceptance in the scorecard, the owner could grant that category standing auto-accept — shrinking the morning review to genuinely contested items. This is the "cheaper ratification" answer to the 24/7 bottleneck: autonomy grows where trust is proven, per category, not globally.

**Open questions:**
- What streak length earns auto-accept, and what revokes it (one reversal? two?)
- Where is the grant recorded so it binds sessions — house rules, or a scorecard annex?

**Decision:** *(not decided — needs several weeks of real scorecard data first; building it before the data exists would be trust theater)*

### `/explore-product` — product-gap questioning *(template's own idea, parked 2026-07-24)*

**The idea:**
The template is good at asking "how should I build this?" but only the advisor occasionally asks "should we build this at all?" A dedicated capability could walk the user journey and ask: what is leaking that nobody noticed? What does the current system make possible that the spec never mentions?

**Options considered:**

| Option | Pros | Cons |
|---|---|---|
| Extend project-advisor (add a product-discovery dimension) | No new seat; advisor already owns "problem clarity" | Advisor reviews are already seven dimensions — risk of dilution |
| New `/explore-product` skill | Focused, invokable on demand | 13th skill; surface-area creep; partially duplicates the advisor |
| Do nothing | Zero cost | The "what's missing?" question stays half-covered |

**Open questions:**
- Do real users ever ask this question, or do founders arrive with too many ideas rather than too few?
- Outcome of a two-AI design review (2026-07-24): parked by agreement — the healthy core lives in the advisor; a new seat must earn itself with user evidence.

**Decision:** *(not decided — revisit after the first five real users)*

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
