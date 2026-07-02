# Start Here with Claude Code — the gentle guide

New to all of this? This page gets you from zero to a set-up project in about 15 minutes, using [Claude Code](https://claude.com/claude-code). No coding experience needed.

(Using Codex or GitHub Copilot instead? Everything works there too — see the main [README](../README.md). This guide just picks one tool so there are no forks in the road.)

## 1. Install four things (one time only)

1. **[Git](https://git-scm.com)** — saves and versions your project. Install with the default options.
2. **[VS Code](https://code.visualstudio.com)** — the free editor you will work in.
3. **Claude Code** — in VS Code, open the Extensions panel (the blocks icon on the left), search for "Claude Code", click Install.
4. A free **[GitHub](https://github.com)** account — this is where your project lives online.

## 2. Make this template yours

On this repository's GitHub page, click **"Use this template" → "Create a new repository"**. Give it your project's name. Click Create.

## 3. Get it onto your computer

In VS Code: **View → Terminal**, then type (replace both names):

```
git clone https://github.com/YOUR-USERNAME/YOUR-PROJECT-NAME.git
```

Then **File → Open Folder** and pick the folder that just appeared.

## 4. Say hello

Open Claude Code (the Claude icon in the sidebar). You don't need to know any commands — **the template introduces itself.** Claude will notice this is a fresh project and offer to set everything up. Say yes, or type:

```
/start
```

Claude interviews you about your idea — what it is, who it's for, what matters most — then writes your project documents and introduces your AI team: an advisor, a spec reviewer, a QA engineer, and a researcher.

## 5. Build — one command at a time

Your daily rhythm is one command:

```
/build-next
```

Claude picks the next feature from your plan, builds it, has your QA agent independently verify it actually works, and tells you what's next. You can also just describe things in plain English:

> "Make the confirmation message friendlier."
> "Run the project advisor — what should I focus on next?"

Four habits that keep everything smooth:

- **After anything you'd hate to lose:** type `/save-point` — like a save point in a video game.
- **If something went wrong:** type `/go-back` — safely rewind to an earlier save point.
- **When something breaks:** type `/fix-bug` and describe what you saw.
- **When you come back after a break:** type `/put-me-in-context` — instant briefing on where things stand.

(Already have code — for example from Lovable or Bolt? Run `/adopt-project` instead of `/start` in step 4: it reads your code and builds the project docs around what exists.)

That's the whole system. The [README](../README.md) has the full tour when you're curious.
