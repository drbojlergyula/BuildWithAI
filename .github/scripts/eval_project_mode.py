#!/usr/bin/env python3
"""The missing eval: does the toolkit still validate once it is a real project?

The template used to validate itself only *as a template* — never as the thing
it produces. Every project born from it therefore went red on its first push:
/start deletes the sentinel the validator demanded, and adding your own agent
failed the roster checks.

This eval simulates a finished project on a throwaway copy and asserts the
validator is happy:

  * the sentinel is gone (what /start does)
  * the project added its own skill and its own agent
  * CLAUDE.md is deleted (a Codex-only project keeps AGENTS.md as canonical)

Plus negative controls, so "passing" cannot mean "checks are switched off":
a genuinely broken skill must still fail, in both modes; a lost handoff-contract
line must fail; a test that imports a tool from a machine-specific absolute
path must fail the portability gate in project mode (measured in the field:
/opt/node22/... pinned an entire browser suite to one sandbox); and a proxy that
has lost the "unverified gate is not a passed gate" rule must fail template mode.
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SENTINEL = "template-state: untouched-example"
# The sandbox-pinned import a field run shipped. Assembled from pieces so this
# file carries the pattern without itself tripping the portability gate.
PINNED_IMPORT = "/" + "opt/node22/lib/node_modules/playwright/index.mjs"


def run_validator(repo: Path):
    proc = subprocess.run([sys.executable, str(repo / ".github/scripts/validate_template.py")],
                          capture_output=True, text=True)
    return proc.returncode, (proc.stdout + proc.stderr).strip()


def make_project(repo: Path):
    """Turn a template copy into what a real project looks like after /start."""
    spec = repo / "docs" / "project_spec.md"
    text = spec.read_text(encoding="utf-8")
    spec.write_text("\n".join(l for l in text.splitlines() if SENTINEL not in l), encoding="utf-8")

    agent = repo / ".claude" / "agents" / "invoice-parser.md"
    agent.write_text("---\nname: invoice-parser\ndescription: Parses supplier invoices.\n---\n\nYou parse invoices.\n",
                     encoding="utf-8")

    skill_dir = repo / ".claude" / "skills" / "import-invoices"
    skill_dir.mkdir(parents=True, exist_ok=True)
    (skill_dir / "SKILL.md").write_text("---\nname: import-invoices\ndescription: Import a batch of invoices.\n---\n\n# Import invoices\n",
                                        encoding="utf-8")

    (repo / "CLAUDE.md").unlink(missing_ok=True)

    # Deployment config legitimately carries host paths; the portability gate
    # must leave it alone (a first version failed every project with a compose
    # volume mount — caught by a probe, not by a run).
    (repo / "docker-compose.yml").write_text(
        'services:\n  db:\n    volumes:\n      - "' + "/" + 'mnt/data/pg:/var/lib/postgresql/data"\n',
        encoding="utf-8")

    # A portable browser test: the tool is resolved by package name, and the
    # only absolute path is in a comment — neither may trip the portability gate.
    ui_test = repo / "app" / "test" / "ui" / "run.mjs"
    ui_test.parent.mkdir(parents=True, exist_ok=True)
    ui_test.write_text(
        "// Falls back to the sandbox path '" + PINNED_IMPORT + "' only via env.\n"
        "const mod = process.env.PLAYWRIGHT_IMPORT || 'playwright';\n"
        "const pw = await import(mod);\n"
        "console.log(typeof pw.chromium);\n",
        encoding="utf-8")


failures = []
with tempfile.TemporaryDirectory() as tmp:
    # 1. Template mode still passes untouched.
    template = Path(tmp) / "template"
    shutil.copytree(ROOT, template, symlinks=True, ignore=shutil.ignore_patterns(".git"))
    code, out = run_validator(template)
    if code != 0:
        failures.append(f"template mode should pass untouched, got exit {code}:\n{out}")

    # 2. Project mode must pass: no sentinel, own agent, own skill, no CLAUDE.md.
    project = Path(tmp) / "project"
    shutil.copytree(ROOT, project, symlinks=True, ignore=shutil.ignore_patterns(".git"))
    make_project(project)
    code, out = run_validator(project)
    if code != 0:
        failures.append("a finished project must validate — the template must never fail a project "
                        f"for owning its docs and its team. Exit {code}:\n{out}")
    elif "project mode" not in out:
        failures.append(f"project not detected as project mode: {out}")

    # 3. Negative control: real breakage must still fail, in project mode too.
    broken = Path(tmp) / "broken"
    shutil.copytree(ROOT, broken, symlinks=True, ignore=shutil.ignore_patterns(".git"))
    make_project(broken)
    (broken / ".claude" / "skills" / "import-invoices" / "SKILL.md").write_text("no frontmatter here\n",
                                                                               encoding="utf-8")
    code, _ = run_validator(broken)
    if code == 0:
        failures.append("negative control passed — a skill without frontmatter must fail even in project mode")

    # 4. Negative control for the handoff contract: a verifier that has lost its
    #    NOT VERIFIABLE verdict must fail template mode (a check only ever seen
    #    passing is an assumption wearing a green tick).
    lost = Path(tmp) / "lost-contract"
    shutil.copytree(ROOT, lost, symlinks=True, ignore=shutil.ignore_patterns(".git"))
    verifier = lost / ".claude" / "agents" / "build-verifier.md"
    verifier.write_text(verifier.read_text(encoding="utf-8").replace("NOT VERIFIABLE", "NOT CHECKED"),
                        encoding="utf-8")
    code, out = run_validator(lost)
    if code == 0 or "NOT VERIFIABLE" not in out:
        failures.append(f"negative control passed — a verifier without the NOT VERIFIABLE verdict must fail template mode:\n{out}")

    # 5. Negative control for the portability gate: the exact line a field run
    #    shipped — a test importing Playwright from a sandbox-specific path —
    #    must fail in project mode, and the message must name the gate.
    pinned = Path(tmp) / "pinned-path"
    shutil.copytree(ROOT, pinned, symlinks=True, ignore=shutil.ignore_patterns(".git"))
    make_project(pinned)
    (pinned / "app" / "test" / "ui" / "run.mjs").write_text(
        "import * as pw from '" + PINNED_IMPORT + "';\n"
        "console.log(typeof pw.chromium);\n",
        encoding="utf-8")
    code, out = run_validator(pinned)
    if code == 0 or "portability gate" not in out or "app/test/ui/run.mjs:1" not in out:
        failures.append(f"negative control passed — a test pinned to /opt/... must fail the portability gate "
                        f"in project mode and name the file and line:\n{out}")

    # 6. Negative control for the proxy's gate rule: a deputy that has lost
    #    "an unverified gate is not a passed gate" must fail template mode —
    #    the rule exists because a run's proxy ruled DECISION on two gates
    #    nobody had passed.
    lenient = Path(tmp) / "lenient-proxy"
    shutil.copytree(ROOT, lenient, symlinks=True, ignore=shutil.ignore_patterns(".git"))
    proxy = lenient / ".claude" / "agents" / "owner-proxy.md"
    proxy.write_text(proxy.read_text(encoding="utf-8").replace("An unverified gate is not a passed gate",
                                                               "A flagged gate may pass"),
                     encoding="utf-8")
    code, out = run_validator(lenient)
    if code == 0 or "unverified gate" not in out:
        failures.append(f"negative control passed — a proxy without the unverified-gate rule must fail template mode:\n{out}")

    # 7. Negative control for the context budget: a rules file padded past the
    #    ceiling must fail template mode.
    bloated = Path(tmp) / "bloated-rules"
    shutil.copytree(ROOT, bloated, symlinks=True, ignore=shutil.ignore_patterns(".git"))
    with (bloated / ".claude" / "rules" / "engineering.md").open("a", encoding="utf-8") as fh:
        fh.write("\n" + ("One more rule nobody will read. " * 200) + "\n")
    code, out = run_validator(bloated)
    if code == 0 or "context budget" not in out:
        failures.append(f"negative control passed — always-loaded files past the ceiling must fail template mode:\n{out}")

if failures:
    print(f"Project-mode eval FAILED ({len(failures)} problem(s)):\n")
    for f in failures:
        print(f"  ✗ {f}\n")
    sys.exit(1)

print("Project-mode eval passed: template validates, a finished project validates, real breakage still fails, "
      "a lost handoff contract still fails, a machine-pinned test fails the portability gate, "
      "a lenient proxy fails, a bloated rule set fails the context budget.")
