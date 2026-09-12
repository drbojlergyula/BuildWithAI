# Behavioural evals — does the toolkit change what Claude *does*?

`validate_template.py` proves the rules are written. This suite proves they are followed: each case runs Claude Code headlessly on a small fixture project with this plugin loaded, and a deterministic grader reads what came out. No LLM judges — every verdict is a regex over a file or the final message, or a check that a tool was called, so a run costs only the agent's own tokens.

Three cases, one per failure pattern a real night shift produced on v3.2.2:

| Case | What it proves | Fails when |
|---|---|---|
| `start-brief` | A brief-driven `/start` clears the sentinel and the house-rules marker and writes an Engineering Profile | a run leaves example content marked as real, or never writes the profile |
| `verifier-oracle` | The `build-verifier` checks a legal claim against the quoted source, not the spec's own formula; its report carries `Oracle:` and `Verifier context:` | the verifier re-derives the spec by hand and passes wording the source contradicts |
| `proxy-unverified-gate` | The `owner-proxy` refuses DECISION on a gate the record could not verify; it rules BRANCH or PARK and names the gate | the proxy treats "flagged" as passed |

## Run it (on your machine, before a release)

Requirements: Claude Code ≥ 2.1.269, logged in; a sandbox backend for Bash (macOS has one; Linux needs `bubblewrap` and `socat`). Each run counts against your plan or API bill — the command below caps it.

```bash
claude plugin eval . --scaffold --allow-tools Bash Write Edit \
  --ablation none --runs 3 --max-cost-usd 15 --no-publish
```

- `--scaffold` runs each case's `scaffold.sh` to build the fixture project in the empty workspace. The scripts copy the *current* `AGENTS.md`, `CLAUDE.md` and `.claude/rules/` from this repo, so the eval always tests the rules as they are now.
- `--allow-tools Bash Write Edit` is what the cases need (`/start` writes docs; the verifier runs tests). Without it those tools are removed and the cases score 0.
- `--ablation none` skips the no-plugin baseline arm and halves the cost. Add it back (`--ablation with-without`) when you want to see what the plugin contributes.
- One case, one run, while iterating: `claude plugin eval . --scaffold --allow-tools Bash Write Edit --ablation none --runs 1 --case proxy-unverified-gate --no-publish`

Results land in `evals/results/<timestamp>/` (gitignored): `report.html` and `aggregate-result.json`. A case passes when its score meets `--threshold` (default 1.0). A single run is noisy; trust three.

**Cost:** not yet measured — this suite was written in a sandbox that cannot authenticate. Record the first measured `COST` column here after your first run, per case, and the model used. Cases pin `sonnet` so figures stay comparable and the rules are tested on the weaker tier the routine agents actually run on.

## How to read a failure

- `start-brief` fails on `sentinel-gone` → `/start` did not remove `template-state: untouched-example`; every later session will treat the project as an untouched template.
- `verifier-oracle` fails on `reads-the-source` → the verifier never opened `docs/reference/`; it checked the code against the spec that produced it.
- `proxy-unverified-gate` fails on `not-decision` → the proxy passed an unverified gate. Read `.claude/agents/owner-proxy.md`, rule "An unverified gate is not a passed gate".

## Adding a case

`evals/<name>/prompt.md` (frontmatter + prompt), `case.yaml` (points at `scaffold.sh`), `scaffold.sh` (builds the workspace from `fixture/` plus the template's rule layer), `graders/*.md` (one deterministic check each). Prefer `regex` over a produced file or `tool_used`; use an `llm` grader only for short outputs, and expect its score to wobble. The validator checks that every case has a prompt and at least one grader.
