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

Plus a negative control, so "passing" cannot mean "checks are switched off":
a genuinely broken skill must still fail, in both modes.
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SENTINEL = "template-state: untouched-example"


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

if failures:
    print(f"Project-mode eval FAILED ({len(failures)} problem(s)):\n")
    for f in failures:
        print(f"  ✗ {f}\n")
    sys.exit(1)

print("Project-mode eval passed: template validates, a finished project validates, real breakage still fails.")
