---
name: start
description: Set up a brand-new project from this template. Interviews the user about what they want to build, then fills in every project document and introduces their AI team. Use when the template is still untouched or the user asks to start project setup.
---

# /start — Project Setup Interview

Guides the user from a blank template to a fully populated project through a structured, friendly interview. This is the first thing a user runs. Make it feel great.

## When to use it

Run once, at the very beginning of a new project, before any code is written. If the project docs are already filled in with a real product, say so and suggest `/put-me-in-context` instead.

---

## Steps

### Phase 0 — Read the template

Before asking anything, silently read and understand:

- `CLAUDE.md` — project guidance and tool registry
- `docs/project_spec.md` — product requirements template
- `docs/architecture.md` — system design template
- `docs/brainstorm.md` — ideation scratchpad template
- `docs/project_status.md` — milestone tracking template
- `docs/changelog.md` — version history template
- `docs/house_rules.md` — the owner's non-negotiables template
- `docs/decisions.md` — one-line decision log template
- The skill and agent files in `.claude/skills/` and `.claude/agents/`

You now understand the full shape of what needs to be filled in. Keep this in mind throughout the interview.

---

### Phase 1 — Open the conversation

Greet the user warmly and explain what is about to happen in one short paragraph. Then ask the first question:

> **What would you like to build?**
> Describe it in plain English — even one sentence is enough to start.

Wait for the answer before continuing.

---

### Phase 2 — Product interview

Ask questions one topic at a time. Never fire more than two questions in a single message. Wait for each answer before moving on. Adjust follow-up questions based on what the user says — do not ask things that are already obvious from their answer.

Work through the following areas in roughly this order, but skip or reorder as context demands:

#### 2a. The problem
- What problem does this product solve?
- Who has this problem? (target user / customer)
- How are people solving it today, and what's wrong with that?

#### 2b. The product
- What does the product actually do, step by step, from the user's point of view?
- What are the two or three most important things a user must be able to do?
- What is explicitly out of scope — what will this NOT do?

#### 2c. Users and use cases
- Walk me through a typical session: what does the user open, do, and see?
- Are there different types of users (e.g. admin vs. end user, free vs. paid)?
- What does success look like for the user?

#### 2d. Data and content
- What data does the product create, store, or display?
- Does the product need user accounts / authentication?
- Are there any external services, APIs, or data sources it must connect to?

#### 2e. Constraints and context
- Is there a deadline or launch date in mind?
- Are there any platforms the product must support (web, iOS, Android, desktop)?
- Any compliance, accessibility, or legal requirements to be aware of?
- Will this be built by you alone, with a team, or with contractors?

#### 2f. House rules
- Is there a monthly budget ceiling for hosting and services?
- Is there anything I should never do without asking you first? (touch payments, delete data, add paid services…)
- Any hard "always" rules — things that must be true in everything we build?

Keep asking clarifying questions until you can confidently answer all of the following:
- What is this product in one sentence?
- Who is the primary user?
- What are the top 3–5 user stories?
- What data does it handle?
- What external dependencies does it have?
- What is explicitly out of scope for now?

If something is still unclear after two attempts, make a reasonable assumption, state it explicitly ("I'll assume X — let me know if that's wrong"), and move on.

---

### Phase 3 — Technology

Ask:

> **Do you have a preferred technology stack, or would you like a recommendation?**

**If the user has preferences:** ask them to list what they know or want to use, then confirm the choices make sense for the product. Flag any mismatches (e.g. a heavy framework for a simple static site) and suggest alternatives if relevant.

**If the user wants a recommendation:** reason through the best stack based on what you now know about the product. Consider:
- Product type (website, web app, mobile app, API, CLI, data pipeline, etc.)
- Scale and complexity (prototype vs. production, solo dev vs. team)
- User's technical background (if known)
- Ecosystem maturity, hosting options, and cost

Present the recommended stack as a simple table (Layer / Technology / Reason), then ask:

> Does this stack work for you, or would you like to swap anything out?

Adjust based on feedback. Confirm the final stack before moving on.

---

### Phase 4 — Iteration planning

Explain that you will now break the product into delivery iterations. Then propose a plan:

**MVP — the smallest version that delivers real value**
- List only the features absolutely necessary to validate the core idea
- Aim for the shortest possible build time
- Everything else goes in a later version

**Version 1.0 — production-ready**
- Adds features needed for a polished public launch (auth, error handling, onboarding, etc.)
- Includes anything the user mentioned that did not make the MVP cut

**Version 2.0+ — growth and scale**
- Nice-to-have features, integrations, performance improvements, monetisation, etc.

Present the iteration plan and ask:

> Does this breakdown look right? Is anything in the wrong phase, or missing entirely?

Adjust based on feedback. Keep iterating until the user says the plan looks good.

---

### Phase 5 — Write all project files

Once the user approves the iteration plan, update all project files to reflect the real product. Replace all example content, **including deleting the `template-state: untouched-example` sentinel comment at the top of `docs/project_spec.md`** — that marker is how the welcome hook and skills know the template is untouched.

Update these files in order:

1. **`docs/brainstorm.md`** — clear the example content; add any open questions or undecided ideas that came up during the interview under Active Ideas.

2. **`docs/project_spec.md`** — fill in every section:
   - What Is This Product (one clear paragraph)
   - Who Is It For (user types with descriptions)
   - Features & User Stories (written as "A [user] can [do X] so that [goal]", grouped by area)
   - Tech Stack table
   - System Design Preferences
   - API Design (any endpoints identified)
   - Project Structure (folder and file layout for this specific product)

3. **`docs/architecture.md`** — describe the system design: components, data flow, how the parts connect. Tailor it to the chosen stack and product type.

4. **`docs/project_status.md`** — set up milestones matching the iteration plan (MVP, v1.0, v2.0+). Mark all as Not Started.

5. **`docs/changelog.md`** — add the first entry: project initialized, date, summary of what was decided.

6. **`docs/house_rules.md`** — replace the example with the user's real non-negotiables from the interview (budget ceiling, never-without-asking list, always rules, tone). Keep it under ~10 rules.

7. **`docs/decisions.md`** — clear the example rows and seed the log with the real decisions just made (stack choice, MVP cut lines, anything debated) — one line each: date, decision, why.

8. **The assistant-facing overview files** — update the Overview section of `CLAUDE.md` (and `AGENTS.md` if this repo has one) to describe the real product. The tools sections do not need changing — the AI team applies to every project.

After writing all files, tell the user what was updated and what they should review.

---

### Phase 6 — Meet your AI team

This is the reveal. Introduce the team that now works for the user. Present it warmly and concretely — these are specialists they can call at any time:

> **Your project comes with an AI team. Here's who works for you:**
>
> 🧭 **project-advisor** — your senior advisor. Reviews the whole project, surfaces blind spots, and tells you what to focus on next. It remembers its past advice between sessions.
> 🔍 **spec-reviewer** — your requirements analyst. Checks the spec for gaps before you build, so problems get caught on paper instead of in code.
> ✅ **build-verifier** — your QA engineer. After something is built, it independently tests that the feature actually does what the spec says.
> 🌐 **research-analyst** — your market researcher. Investigates competitors, pricing, technology choices, or anything else on the live web, and files a cited brief.
>
> And your shortcut commands: `/build-next` builds the next planned feature (and has QA verify it), `/save-point` and `/go-back` are your save game and rewind, `/new-feature` adds to the plan, `/update-docs-and-commit` saves progress with fresh docs, `/put-me-in-context` briefs anyone instantly, `/doc-sync-check` keeps the docs honest, `/fix-bug` when something breaks, and `/go-live` when you're ready to launch.

Then ask:

> Based on your project, are there any other repeatable tasks worth automating? For example: adding a new record, running a regular check, publishing content, generating a report?

If the user identifies something, create a new skill or agent for it in `.claude/` — briefly explain which type fits and why, then write the file.

---

### Phase 7 — First advisor review (the payoff)

Offer the immediate wow moment:

> **One last thing — your advisor is ready for a first review.** It will read everything we just wrote and tell you what we might have missed: risks, gaps, blind spots. Takes about a minute. Want the review now? (Recommended.)

If yes, run the project-advisor agent. Its first findings — delivered minutes after setup — are the moment this system proves it is a team, not a template.

---

### Phase 8 — Wrap up

Confirm everything is done. Give the user a clear next step:

> Your project is set up. Here is how to move forward:
>
> **Right now:**
> 1. Read through `docs/project_spec.md` — does it capture what you want to build?
> 2. Check `docs/house_rules.md` — those are the rules I will hold us both to.
>
> **Before the first build:**
> 3. Ask me to "run the spec-reviewer agent" — it checks the spec for gaps while they are still cheap to fix on paper. (If you took the advisor review above, this is the quick second opinion on the spec itself.)
>
> **When you are ready to build:**
> 4. Type `/build-next` — I'll build the first feature in the plan and have your QA engineer verify it works.
>
> **As you go:**
> - `/build-next` to keep shipping the plan, one verified feature at a time
> - `/save-point` after anything you'd hate to lose; `/go-back` if something goes wrong
> - `/new-feature` any time you want to add something new to the plan
> - `/put-me-in-context` whenever you (or a teammate) need instant full context
> - "run the project-advisor agent" any time you want a senior review of where things stand

---

## Rules for the interview

- **Ask one or two questions at a time.** Never present a wall of questions.
- **Use plain English.** Avoid technical jargon unless the user uses it first.
- **Reflect back what you heard.** Before moving to the next topic, briefly restate what you understood. Give the user a chance to correct you.
- **Make assumptions explicit.** If you fill in a gap, say so. ("I'm assuming this will be a web app — is that right?")
- **Never stop early.** Do not write the project files until you can answer all the questions in Phase 2 with confidence.
- **Be encouraging.** This is the start of a project. Keep the tone energetic and collaborative.
