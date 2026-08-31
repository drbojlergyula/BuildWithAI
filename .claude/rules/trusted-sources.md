# Trusted sources — what a session may install without the owner

Sometimes the work needs a tool that is not installed — most often a browser-testing skill when a web UI must be verified. Installing software is a real decision, so this list is the **entire universe** of what an AI session (a night shift especially) may install unattended. Not on this list = not installable without the owner, full stop.

## The rules

- Only **free, open, dev-only** tools: nothing that ships inside the product, nothing paid, nothing that talks to third parties on the project's behalf.
- Every unattended install is **provisional**: it happens on the night branch, is logged and tagged like any night ruling, and the morning merge is the ratification.
- **Smoke-test before relying on it**: after installing, prove the tool works (open a page, click once) before using it for real verification.
- At most **two installs per night** — the same cap as drafted specialists.
- **The owner curates this list.** Sessions use it; they never add to it. If a needed tool is not listed, the session parks the need and says so in the briefing.

## The list

| Source | What may be installed | Typical use |
|---|---|---|
| **Anthropic's official skills repository** (github.com/anthropics/skills) | **any skill in it** — e.g. `webapp-testing` (Playwright browser testing), `frontend-design`, `mcp-builder` | browser-verified UI flows with screenshots and console logs; frontend polish; whatever the work needs |
| **Anthropic's official skill/plugin marketplace** (the store built into Claude Code) | any Anthropic-authored entry | same — the official store is trusted wholesale |
| npm / PyPI — **only** as dependencies a skill above requires | e.g. `playwright` and its Chromium | runtime for the skills |

Anthropic-official is trusted *wholesale*; the four-part test (free / dev-only / reversible / listed) still applies to every individual install — being on this list answers only the "listed" part, never the other three.

**How installing a skill works** (so nobody improvises at 3 AM): copy the skill's folder from the source repo into the project's `.claude/skills/` (e.g. clone `anthropics/skills` shallowly to a temp dir and copy `skills/webapp-testing/`), then install its declared dependencies (for webapp-testing: `pip install playwright && python -m playwright install chromium`), then smoke-test.
