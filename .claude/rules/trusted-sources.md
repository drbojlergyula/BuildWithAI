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
| `anthropics/skills` (github.com/anthropics/skills) | Agent Skills, e.g. `webapp-testing` (Playwright browser testing), `frontend-design` | browser-verified UI flows with screenshots and console logs; frontend polish |
| npm / PyPI — **only** as dependencies a listed skill requires | e.g. `playwright` and its Chromium | runtime for the skills above |
