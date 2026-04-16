<!-- repo-description: A starter template for building software with AI — keeps every decision in AI-readable format so anyone can get up to speed with one prompt. -->

# BuildWithAI

A starter template for building software with AI coding assistants. It works with Claude Code, Codex, and GitHub Copilot while keeping one shared project structure and one shared project setup flow.

---

## Why this exists

Most project knowledge lives in one place: someone's head. When they are sick, you call them. When they leave, it is gone. Documentation is a snapshot — accurate the day it was written, stale the day after.

This template gives every project a brain. Every decision, idea, and change lives in AI-readable Markdown, structured from day one. The result is one prompt that answers everything: "put me in context."

Built for teams using Claude Code, GitHub Copilot, or Codex. Works the same across all three.

Clone it. Run `/start`. See what happens.

---

## Quick start

**1. Get the tools**

- [Git](https://git-scm.com) — saves and versions your project
- [VS Code](https://code.visualstudio.com) — free code editor
- One AI coding assistant:
  - Claude Code
  - Codex
  - GitHub Copilot
- A free account at [github.com](https://github.com)

**2. Copy this template**

On the GitHub page, click **"Use this template" → "Create a new repository"**, give it a name, and click Create.

**3. Download to your computer**

Open VS Code, open the Terminal (**View → Terminal**), and run:

```
git clone https://github.com/YOUR-USERNAME/YOUR-PROJECT-NAME.git
```

Then open the downloaded folder in VS Code (**File → Open Folder**).

**4. Start the project setup**

Use the setup entrypoint that matches your tool:

```
Claude Code: /start
Codex: ask it in plain English to "start project setup"
GitHub Copilot: ask it in plain English to "start project setup"
```

Your assistant should interview you about what you want to build and fill in the project documents automatically. The whole thing should take about 5–10 minutes.

Important: only Claude Code has a native `/start` slash command in this template. Codex and GitHub Copilot use equivalent workflows, but not the same slash-command mechanism.

If you are using Codex or GitHub Copilot, these are good example prompts:

```text
Start project setup.
Help me add a new feature to the spec.
Review the spec for gaps before we build.
Check whether the project docs are out of sync.
```

**5. Start building**

Once setup is done, give your assistant plain-English instructions to start building:

> "Build the order form described in the project spec."
> "Add a login page for the owner dashboard."

---

## How to work day to day

Once your project is set up, the rhythm is simple:

| When | What to do |
|---|---|
| Need a full project summary | Ask the assistant to run `put-me-in-context` — in Claude this is `/put-me-in-context`; in Codex or Copilot say "put me in context" |
| Adding a new feature | Ask the assistant to run `new-feature` — in Claude this is `/new-feature`; in Codex or Copilot ask in plain English |
| After finishing something | Ask the assistant to run `update-docs-and-commit` — it updates docs and saves progress |
| Feeling stuck or unsure | Ask it to run `project-advisor` — it reviews the whole project and recommends what to focus on |
| Spec feels incomplete | Ask it to run `spec-reviewer` — it checks for gaps before you build |
| Docs feel out of sync | Ask it to run `doc-sync-check` — it finds inconsistencies and placeholders |

In Codex and GitHub Copilot, plain-English requests are the safest option:

- "Put me in context."
- "Start project setup."
- "Add a new feature to the spec."
- "Run the project advisor."
- "Review the spec."
- "Check the docs for consistency."

---

## What's in this template?

```
BuildWithAI/
├── AGENTS.md                          ← Instructions Codex reads every session
├── CLAUDE.md                         ← Instructions Claude Code reads every session
├── docs/
│   ├── project_spec.md                ← What you are building and why
│   ├── architecture.md                ← How the project is structured
│   ├── brainstorm.md                  ← Scratchpad for ideas
│   ├── project_status.md              ← Progress and milestones
│   ├── changelog.md                   ← History of changes
│   └── assistant_workflows.md         ← Shared behavior across assistants
├── .claude/
    ├── agents/
    │   ├── project-advisor.md         ← Reviews the whole project for blind spots
    │   └── spec-reviewer.md           ← Checks the spec is complete before building
    ├── commands/
    │   ├── start.md                   ← /start — sets up a new project from scratch
    │   ├── new-feature.md             ← /new-feature — adds a feature to the spec
    │   ├── update-docs-and-commit.md  ← /update-docs-and-commit — saves progress
    │   └── put-me-in-context.md       ← /put-me-in-context — full project context brief
    └── skills/
        └── doc-sync-check/            ← Checks all docs are consistent
└── .github/
    ├── copilot-instructions.md        ← Instructions GitHub Copilot reads in this repo
    └── prompts/
        ├── start.prompt.md            ← Optional setup helper for supported Copilot editors
        ├── new-feature.prompt.md      ← Optional feature-planning helper
        ├── update-docs-and-commit.prompt.md
        ├── project-advisor.prompt.md  ← Optional advisory-review helper
        ├── spec-reviewer.prompt.md    ← Optional spec-review helper
        ├── doc-sync-check.prompt.md   ← Optional doc-consistency helper
        └── put-me-in-context.prompt.md ← Optional context-brief helper
```

All files are pre-filled with a working example. The setup workflow replaces everything with your actual project.

## How compatibility works

This repo now uses a shared workflow layer plus tool-specific adapters:

- `docs/assistant_workflows.md` is the source of truth for setup, feature planning, and project maintenance behavior
- `CLAUDE.md` points Claude Code to the shared workflows and Claude-native commands
- `AGENTS.md` tells Codex how to interpret the same workflows in Codex terms
- `.github/copilot-instructions.md` does the same for GitHub Copilot
- `.github/prompts/` contains optional helper prompts for Copilot environments that support prompt files

The goal is consistent behavior, not identical command syntax. Each assistant has different capabilities and conventions, so the template teaches each one how to behave in its own native format.

The practical rule is simple:

- Claude Code: use the built-in slash commands and Claude tool files
- Codex: use normal chat requests and `AGENTS.md`
- GitHub Copilot: use normal chat requests by default; prompt files are optional helpers in supported editors

---

## Questions or issues?

Describe what you expected to happen and what happened instead. Any of the supported assistants should be able to diagnose and fix most problems directly.

---
*Built to solve the bus factor problem. One prompt: "put me in context."*
