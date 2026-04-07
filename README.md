# BuildWithClaude

A starter template for building software with Claude Code — Anthropic's AI coding assistant. Designed for business owners and non-technical users.

---

## Quick start

**1. Get the tools**

- [Git](https://git-scm.com) — saves and versions your project
- [VS Code](https://code.visualstudio.com) — free code editor
- Claude Code — install from the VS Code Extensions panel (search "Claude Code")
- A free account at [github.com](https://github.com)

**2. Copy this template**

On the GitHub page, click **"Use this template" → "Create a new repository"**, give it a name, and click Create.

**3. Download to your computer**

Open VS Code, open the Terminal (**View → Terminal**), and run:

```
git clone https://github.com/YOUR-USERNAME/YOUR-PROJECT-NAME.git
```

Then open the downloaded folder in VS Code (**File → Open Folder**).

**4. Run /start**

Open Claude Code in VS Code and type:

```
/start
```

Claude will interview you about what you want to build and fill in all the project documents automatically. The whole thing takes about 5–10 minutes.

**5. Start building**

Once `/start` is done, give Claude plain-English instructions to start building:

> "Build the order form described in the project spec."
> "Add a login page for the owner dashboard."

---

## How to work day to day

Once your project is set up, the rhythm is simple:

| When | What to do |
|---|---|
| Adding a new feature | Type `/new-feature` — Claude will ask what it does and add it to the spec |
| After finishing something | Type `/update-docs-and-commit` — Claude updates the docs and saves your progress |
| Feeling stuck or unsure | Ask Claude to "run the project-advisor agent" — it reviews everything and tells you what to focus on |
| Spec feels incomplete | Ask Claude to "run the spec-reviewer agent" — it checks for gaps before you build |
| Docs feel out of sync | Ask Claude to "run the doc-sync-check skill" — it finds inconsistencies and placeholders |

---

## What's in this template?

```
BuildWithClaude/
├── CLAUDE.md                          ← Instructions Claude reads every session
├── docs/
│   ├── project_spec.md                ← What you are building and why
│   ├── architecture.md                ← How the project is structured
│   ├── brainstorm.md                  ← Scratchpad for ideas
│   ├── project_status.md              ← Progress and milestones
│   └── changelog.md                   ← History of changes
└── .claude/
    ├── agents/
    │   ├── project-advisor.md         ← Reviews the whole project for blind spots
    │   └── spec-reviewer.md           ← Checks the spec is complete before building
    ├── commands/
    │   ├── start.md                   ← /start — sets up a new project from scratch
    │   ├── new-feature.md             ← /new-feature — adds a feature to the spec
    │   └── update-docs-and-commit.md  ← /update-docs-and-commit — saves progress
    └── skills/
        └── doc-sync-check/            ← Checks all docs are consistent
```

All files are pre-filled with a working example. `/start` replaces everything with your actual project.

---

## Questions or issues?

Describe what you expected to happen and what happened instead — Claude can diagnose and fix most problems directly.
