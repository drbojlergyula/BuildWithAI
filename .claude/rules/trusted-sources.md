# Trusted sources — what a session may install without the owner

Sometimes the work needs a tool that is not installed — most often a browser-testing skill when a web UI must be verified. Installing software is a real decision, so this list is the **entire universe** of what an AI session (a night shift especially) may install unattended. Not on this list = not installable without the owner, full stop.

## The rules

- Only **free, open, dev-only** tools: nothing that ships inside the product, nothing paid, nothing that talks to third parties on the project's behalf.
- Every unattended install is **provisional**: it happens on the night branch, is logged and tagged like any night ruling, and the morning merge is the ratification.
- **Smoke-test before relying on it**: after installing, prove the tool works (open a page, click once) before using it for real verification.
- At most **two installs per night** — the same cap as drafted specialists.
- **The owner curates this list.** Sessions use it; they never add to it. If a needed tool is not listed, the session parks the need and says so in the briefing.

## The list

**The principle: vendor-official is trusted wholesale.** The official repository and store of the assistant vendor you are *running in* is a trusted source — this keeps the rule identical across every assistant the template supports:

| You are running in | Trusted source | What may be installed |
|---|---|---|
| **Claude Code** | Anthropic's official skills repository (github.com/anthropics/skills) and the official store built into Claude Code (Anthropic-authored entries) | any skill/tool in them — e.g. `webapp-testing` (Playwright browser testing), `frontend-design` |
| **Codex** | OpenAI's official repositories (github.com/openai) and Codex's official extensions/tooling | any official skill/tool — plus the Anthropic skills repo above, since Agent Skills are an open standard and run in Codex too |
| **GitHub Copilot** | GitHub's and Microsoft's official repositories and Copilot's official extensions | any official skill/tool — plus the Anthropic skills repo, same reason |
| any | npm / PyPI — **only** as dependencies a skill above declares | e.g. `playwright` and its Chromium |

Vendor-official answers only the **"listed"** part of the four-part test (free / dev-only / reversible / listed) — the other three must still hold for every individual install.

**How installing a skill works** (so nobody improvises at 3 AM): copy the skill's folder from the source repo into the project's `.claude/skills/` (e.g. clone `anthropics/skills` shallowly to a temp dir and copy `skills/webapp-testing/`), then install its declared dependencies (for webapp-testing: `pip install playwright && python -m playwright install chromium`), then smoke-test.
