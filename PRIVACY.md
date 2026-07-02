# Privacy Policy — BuildWithAI (buildwithai-team plugin)

**Last updated:** July 2, 2026

BuildWithAI is a set of local instructions (skills, agents, hooks, and an output style) for AI coding assistants. It is designed to process everything locally and collect nothing.

## What the plugin collects

**Nothing.** The plugin has no telemetry, no analytics, no accounts, and no servers of its own. It never transmits your code, your documents, or any information about you to the plugin's author or to any third party.

## What the plugin does on your machine

- **Reads and writes files only inside your project** — the documentation it maintains (`docs/`), and the AI team's memory (`.claude/agent-memory/`), all stored in your repository under your control.
- **Runs a small local hook and statusline script** at session start; these only read local project files (for example, checking whether the project docs are set up) and produce local output. They make no network requests.
- **Wraps git commands** (status, log, add, commit, and — only in `/go-back`, with your confirmation — reset) so you can save and rewind your work. Nothing is pushed anywhere unless you push it.

## Network access

The plugin itself makes no network calls. Two things around it can, both under your control:

- **Your AI assistant** (e.g. Claude Code) processes your prompts and files according to its own privacy policy — see [Anthropic's privacy policy](https://www.anthropic.com/legal/privacy) for Claude. The plugin does not change what your assistant sends or stores.
- **The `research-analyst` agent** performs web searches and fetches public web pages *only when you explicitly ask for research*, using your assistant's built-in tools. Your project files are not uploaded as part of a search.

## Data retention and deletion

Everything the plugin produces lives in your repository as plain text files. Deleting the repository (or the files) deletes everything. Uninstalling the plugin (`/plugin uninstall buildwithai-team`) removes the plugin itself; your project documents remain yours.

## Changes to this policy

Any change to this policy will appear in this file's git history in the public repository, so changes are transparent and auditable.

## Contact

Questions or concerns: open an issue at [github.com/drbojlergyula/BuildWithAI](https://github.com/drbojlergyula/BuildWithAI/issues) or email **marci737@gmail.com**.
