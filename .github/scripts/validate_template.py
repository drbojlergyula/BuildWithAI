#!/usr/bin/env python3
"""Template health check.

Validates that every skill and agent has the frontmatter the AI tools
require, that JSON config files parse, and that the README's tool roster
matches the files on disk. Runs in CI on every push.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
errors = []


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith(" ") and not line.startswith("#"):
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
    return fields


# --- Skills: every .claude/skills/<name>/SKILL.md needs name + description
skills_dir = ROOT / ".claude" / "skills"
skills = sorted(p for p in skills_dir.iterdir() if p.is_dir()) if skills_dir.is_dir() else []
if not skills:
    errors.append("No skills found in .claude/skills/")
for skill in skills:
    md = skill / "SKILL.md"
    if not md.is_file():
        errors.append(f"{skill.relative_to(ROOT)}: missing SKILL.md")
        continue
    fm = frontmatter(md)
    for field in ("name", "description"):
        if not fm.get(field):
            errors.append(f"{md.relative_to(ROOT)}: missing '{field}' in frontmatter")
    if fm.get("name") and fm["name"] != skill.name:
        errors.append(f"{md.relative_to(ROOT)}: frontmatter name '{fm['name']}' != folder '{skill.name}'")

# --- Agents: every .claude/agents/*.md needs name + description
agents_dir = ROOT / ".claude" / "agents"
agents = sorted(agents_dir.glob("*.md")) if agents_dir.is_dir() else []
if not agents:
    errors.append("No agents found in .claude/agents/")
for agent in agents:
    fm = frontmatter(agent)
    for field in ("name", "description"):
        if not fm.get(field):
            errors.append(f"{agent.relative_to(ROOT)}: missing '{field}' in frontmatter")

# --- JSON configs must parse
for rel in (".claude/settings.json", ".claude/hooks/hooks.json",
            ".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"):
    path = ROOT / rel
    if path.is_file():
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{rel}: invalid JSON — {exc}")

# --- Hook scripts referenced by configs must exist and be executable
for script in (ROOT / ".claude" / "hooks").glob("*.sh"):
    if not script.stat().st_mode & 0o111:
        errors.append(f"{script.relative_to(ROOT)}: not executable (chmod +x)")

# --- Plugin default locations (root symlinks) must resolve
for link, probe in (("agents", "project-advisor.md"), ("output-styles", "founder.md")):
    link_path = ROOT / link
    if link_path.exists() and not (link_path / probe).is_file():
        errors.append(f"{link}/ symlink does not resolve into .claude/")

# --- Output styles need name + description frontmatter
styles_dir = ROOT / ".claude" / "output-styles"
for style in sorted(styles_dir.glob("*.md")) if styles_dir.is_dir() else []:
    fm = frontmatter(style)
    for field in ("name", "description"):
        if not fm.get(field):
            errors.append(f"{style.relative_to(ROOT)}: missing '{field}' in frontmatter")

# --- The untouched-template sentinel must exist exactly where the hook greps for it
spec = ROOT / "docs" / "project_spec.md"
hook = ROOT / ".claude" / "hooks" / "session-start.sh"
if spec.is_file() and hook.is_file():
    sentinel = "template-state: untouched-example"
    if sentinel in hook.read_text(encoding="utf-8") and sentinel not in spec.read_text(encoding="utf-8"):
        errors.append("docs/project_spec.md: missing the 'template-state: untouched-example' sentinel the SessionStart hook greps for")

# --- Every skill and agent must be mentioned in README, AGENTS.md, and CLAUDE.md
for doc_name in ("README.md", "AGENTS.md", "CLAUDE.md"):
    doc = (ROOT / doc_name).read_text(encoding="utf-8")
    for skill in skills:
        if skill.name not in doc:
            errors.append(f"{doc_name}: does not mention skill '{skill.name}'")
    for agent in agents:
        if agent.stem not in doc:
            errors.append(f"{doc_name}: does not mention agent '{agent.stem}'")

if errors:
    print(f"Template validation FAILED ({len(errors)} problem(s)):\n")
    for err in errors:
        print(f"  ✗ {err}")
    sys.exit(1)

print(f"Template validation passed: {len(skills)} skills, {len(agents)} agents, configs OK.")
