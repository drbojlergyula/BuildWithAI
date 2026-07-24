<!-- repo-description: A starter template that gives your project an AI team and keeps every decision in AI-readable format — works with Claude Code, Codex, and GitHub Copilot from one set of files. -->

# BuildWithAI

**One project brain. One AI team. Every assistant.**

A starter template for building software with AI coding assistants. It gives your project a documentation "brain" that any assistant can read, plus a pre-built team of AI specialists — and thanks to the open standards the industry converged on ([AGENTS.md](https://agents.md), [Agent Skills](https://agentskills.io), both under the Linux Foundation), the *same files* work in **Claude Code, OpenAI Codex, and GitHub Copilot**. No adapters, no duplication, no drift.

> **New to all of this?** Read the [gentle start-here guide](docs/start_here_with_claude.md) — zero to a set-up project in 15 minutes, no experience needed. (It replaces the former BuildWithClaude repo, which has merged into this one.)
>
> **Already have a project?** You don't need the template — install the AI team as a plugin:
>
> ```
> /plugin marketplace add drbojlergyula/BuildWithAI
> /plugin install buildwithai-team@buildwithai
> ```

---

## Why this exists

Most project knowledge lives in one place: someone's head. When they are sick, you call them. When they leave, it is gone. Documentation is a snapshot — accurate the day it was written, stale the day after.

This template gives every project a brain. Every decision, idea, and change lives in AI-readable Markdown, structured from day one. The result is one prompt that answers everything: **"put me in context."**

And because your team may not all use the same AI tool, everything here is built on the open standards all major assistants now share:

| Standard | What it does here | Who reads it |
|---|---|---|
| **AGENTS.md** | The project's canonical instructions | Codex, Copilot, Cursor, Zed, Jules, … (Claude Code via `CLAUDE.md` import) |
| **Agent Skills** (`.claude/skills/`) | The guided workflows — one definition, every tool | Claude Code, Copilot, Codex natively |
| **Subagents** (`.claude/agents/`) | The AI team — native in Claude Code, role instructions everywhere else | All, per AGENTS.md |

Clone it. Say hello. See what happens.

---

## What makes it different

Most templates give you empty folders. This one gives you **staff**:

| Your team member | What they do |
|---|---|
| 🧭 **project-advisor** | Senior advisor. Reviews everything, surfaces blind spots, tells you what to focus on next — and remembers its advice between sessions. |
| 🔍 **spec-reviewer** | Requirements analyst. Catches gaps in your plan on paper, where they are cheap to fix. |
| ✅ **build-verifier** | QA engineer. After a feature is built, independently runs it and proves it works. |
| 🌐 **research-analyst** | Market researcher. Investigates competitors, pricing, and technology choices on the live web and files a cited brief. |
| 🌙 **owner-proxy** | Your deputy. During a `night-shift` it decides what your docs prove, settles cheap reversible questions with research or a flagged assumption, and parks only what truly needs you. |

Plus guided workflows for the whole life of the project — including `build-next`, the daily rhythm that builds the next planned feature and has QA verify it, and `save-point`/`go-back`, git wrapped in video-game language:

`start` (or `adopt-project`) → `build-next` → `save-point` → `new-feature` → `fix-bug` → `put-me-in-context` → `doc-sync-check` → `go-live`

And when the day runs out: **`night-shift`** *(experimental in this release — share your first morning briefing!)* runs the same build loop unattended — the owner-proxy makes the calls your docs can prove, settles cheap reversible questions with research or a flagged assumption, and parks only what truly needs you: expensive-if-wrong stays yours. It briefs you at breakfast — and your first night is supervised: you watch the deputy work before you ever sleep on it. Every night is scored, too: the morning review tracks how much of the night's work you actually kept, so the night shift has to prove it pays for itself. When the build lane runs dry, the night switches to preparation: research briefs and brainstorms that turn every parked question into a thirty-second morning decision — data informs, you authorize. Every night starts with a save point, has a budget, and ends one `go-back` from undone.

---

## Quick start

**1. Get the tools**

- [Git](https://git-scm.com) and [VS Code](https://code.visualstudio.com)
- One (or more) AI coding assistants: [Claude Code](https://claude.com/claude-code), [Codex](https://developers.openai.com/codex), or [GitHub Copilot](https://github.com/features/copilot)
- A free account at [github.com](https://github.com)

**2. Copy this template**

On the GitHub page, click **"Use this template" → "Create a new repository"**, name it, and click Create.

**3. Download it**

```
git clone https://github.com/YOUR-USERNAME/YOUR-PROJECT-NAME.git
```

Open the folder in VS Code (**File → Open Folder**).

**4. Start the setup interview**

| Tool | Do this |
|---|---|
| Claude Code | Just open it — the template greets you and offers `/start` |
| Codex | Run the `start` skill, or say "start project setup" |
| GitHub Copilot | Run the `start` skill, or say "start project setup" |

Your assistant interviews you about your idea (5–10 minutes), fills in every project document, proposes a stack and an MVP plan, then introduces your AI team.

**5. Build — one verified feature at a time**

> `/build-next`

Your assistant picks the next story from the plan, builds it, has the QA agent independently verify it works, records the progress, and tells you what's next. That's the daily rhythm.

**Already have code?** (Including a Lovable / Bolt / v0 export that hit the wall.) Run `adopt-project` instead of `start` — it reverse-engineers the docs from your codebase and sets up the memory system around what exists.

---

## Day to day

Skills answer to slash commands, their names, or plain English — whichever your tool supports:

| When | Workflow | Plain English |
|---|---|---|
| Build the next thing in the plan | `build-next` | "build the next feature" |
| Save your progress (like a game) | `save-point` | "save my progress" |
| Something went wrong — rewind | `go-back` | "go back to before X" |
| Need a full project summary | `put-me-in-context` | "put me in context" |
| Adding something new | `new-feature` | "add a feature to the spec" |
| Something is broken | `fix-bug` | "fix this bug" |
| Finished a piece of work | `update-docs-and-commit` | "update docs and commit" |
| Bringing existing code in | `adopt-project` | "adopt this project" |
| Feeling stuck or unsure | agent: `project-advisor` | "run the project advisor" |
| About to build from the spec | agent: `spec-reviewer` | "review the spec" |
| Just built a feature | agent: `build-verifier` | "verify the build" |
| Need outside facts | agent: `research-analyst` | "research what competitors charge" |
| Docs feel stale | `doc-sync-check` | "check the docs for consistency" |
| Ready to launch | `go-live` | "are we ready to go live?" |
| Leaving for the night | `night-shift` | "do the night shift" / "work autonomously until morning" |

---

## Keeping your AI costs down

AI assistants bill by the token, and the fastest way to burn a monthly budget is running every small task on a frontier model. This template is built to be cheap to run:

- **The team is cost-tiered.** `spec-reviewer`, `build-verifier`, and `research-analyst` do routine work — checklist reviews, QA runs, web research — and are meant to run on a mid-tier model; only `project-advisor` deserves your strongest one, because judgment is the thing worth paying up for. Claude Code enforces this automatically (the agents are pinned to Sonnet); in Copilot or Codex, honour the tier with your tool's model picker — the rule is stated in `AGENTS.md`, which every assistant reads. (We deliberately skipped Haiku for QA: a false "PASS" is the most expensive token in the system.)
- **The docs brain is itself the token saver.** A tight `project_status.md` read at session start replaces re-explaining your project in chat every day. Keep the docs pruned — the conventions in `.claude/rules/documentation.md` enforce this.
- **Match the model to the moment.** Run the daily `/build-next` rhythm on a mid-tier model; switch up for the `/start` interview, architecture decisions, and advisor reviews. Every tool has a switch: `/model` in Claude Code (`/cost` shows session usage), the model picker in Copilot, `/model` in Codex.
- **AI spend is a house rule.** The `/start` interview asks for your AI budget alongside hosting, it lands in `docs/house_rules.md`, and the advisor checks it like any other non-negotiable.

---

## What's in the box

```
BuildWithAI/
├── AGENTS.md                    ← Canonical instructions (open standard — Codex, Copilot, Cursor, …)
├── CLAUDE.md                    ← Claude Code entry point; imports AGENTS.md
├── docs/                        ← Your project's long-term memory
│   ├── start_here_with_claude.md ← Gentle 15-minute guide for beginners
│   ├── project_spec.md          ← What you are building and why
│   ├── architecture.md          ← How it is structured
│   ├── house_rules.md           ← Your non-negotiables — every workflow re-checks them
│   ├── decisions.md             ← One-line decision log, maintained by the AI automatically
│   ├── brainstorm.md            ← Ideas before they are decisions
│   ├── project_status.md        ← Progress and milestones
│   └── changelog.md             ← History of changes
├── .claude/
│   ├── skills/                  ← Guided workflows (Agent Skills standard — read by all three tools)
│   ├── agents/                  ← Your AI team (native subagents in Claude Code)
│   ├── output-styles/           ← "Founder" style — plain-English, business-first communication
│   ├── rules/                   ← Modular conventions
│   ├── hooks/                   ← Welcome-on-open magic (Claude Code)
│   ├── statusline.sh            ← Statusline: current phase · last save · model
│   └── settings.json            ← Safe permission defaults + statusline + hook wiring
├── .claude-plugin/              ← Makes this repo installable as a Claude Code plugin
├── agents → .claude/agents      ← Symlink so the plugin finds the team in its standard location
└── .github/
    ├── copilot-instructions.md  ← Copilot-specific notes (points to AGENTS.md)
    └── workflows/               ← CI that validates every skill/agent on each push
```

### Two ways to use it

| You have | Do this |
|---|---|
| **A new project** | Use this repo as a template (button above) — you get the docs brain *and* the AI team |
| **An existing project** | Install the plugin (commands at the top) — you get the AI team and can run `start` to add the docs brain |

The plugin is versioned (currently `2.5.0`); when you update this repo and bump the version, everyone who installed it gets the update via `/plugin update`.

---

## How it compares

Honest positioning — these are all good tools; they solve different problems:

| | BuildWithAI | BMAD-method | GitHub Spec Kit | Task Master | Lovable / Bolt |
|---|---|---|---|---|---|
| Built for | **Founders & business owners** | Dev teams | Dev teams | Devs with a PRD | Anyone (hosted) |
| Process weight | Light — 7 docs, no ceremony | Heavy (12+ personas) | Heavy (spec pipeline) | Medium | None |
| Project memory | **Docs + decision log + agent memory, maintained automatically** | Story files | Specs | tasks.json | Weak — the famous "wall" |
| Verification | Independent QA agent runs your feature | QA persona | — | — | You click around |
| Works in | Claude Code, Codex, Copilot, Cursor… | Multiple | 30+ agents | Multiple | Their platform only |
| Best at | **Week 2 and beyond** — still remembering your project | Big planned builds | Greenfield specs | Task plumbing | Minute 5 — instant demo |

The honest pitch: prototype in Lovable if you like — then `adopt-project` here when it stops remembering what you built. This is the tool for the long haul.

All files are pre-filled with a working example. The `start` workflow replaces the example with your actual project.

## How compatibility works now

Earlier versions of this template kept a hand-written workflow document plus per-tool adapter files. The industry has since standardized, so this template now has **one definition of everything**:

- `AGENTS.md` is the single source of project instructions — most assistants read it natively; Claude Code imports it via `CLAUDE.md`.
- Workflows are **skills** in `.claude/skills/` — Claude Code, Copilot, and Codex all discover that folder natively.
- The AI team lives in `.claude/agents/` — Claude Code runs them as true subagents (own context, scoped tools, persistent memory); other assistants adopt them as role instructions, as directed by `AGENTS.md`.

Same behavior, a fraction of the files, and nothing to keep in sync by hand.

---

## Questions or issues?

Describe what you expected and what happened instead — any supported assistant can diagnose and fix most problems directly. If the docs ever drift from reality, run `doc-sync-check`.

---
*Built to solve the bus-factor problem. One prompt: "put me in context."*
