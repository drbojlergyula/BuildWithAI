#!/usr/bin/env python3
"""Toolkit health check — runs in template repos and in projects built from them.

Two modes, decided by the `template-state: untouched-example` sentinel in
docs/project_spec.md (the same marker the SessionStart hook and /template-update
use):

* TEMPLATE (sentinel present) — everything below, including roster completeness:
  every skill and agent must be named in the hook and the three instruction docs.
* PROJECT (sentinel absent, or no spec at all) — structural checks only. A project
  owns its docs, its own agents and skills, and its own roster; the template must
  never fail a project for having a team of its own.

Structural checks run in both modes: frontmatter, JSON validity, hook
executability, symlinks, migration naming, engineering rules.
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

# --- Mode: is this the template itself, or a project built from it?
# The sentinel is the marker (same convention as the hook and /template-update).
SENTINEL = "template-state: untouched-example"
spec = ROOT / "docs" / "project_spec.md"
hook = ROOT / ".claude" / "hooks" / "session-start.sh"
IS_TEMPLATE = spec.is_file() and SENTINEL in spec.read_text(encoding="utf-8")

# --- Migration files must be named vX.Y.Z.md and non-empty (both modes)
migrations_dir = ROOT / ".claude" / "migrations"
if migrations_dir.is_dir():
    for mig in sorted(migrations_dir.iterdir()):
        if not re.fullmatch(r"v\d+\.\d+\.\d+\.md", mig.name):
            errors.append(f"{mig.relative_to(ROOT)}: migration files must be named vX.Y.Z.md")
        elif not mig.read_text(encoding="utf-8").strip():
            errors.append(f"{mig.relative_to(ROOT)}: empty migration file")

# --- The engineering rule must define all three change tiers (both modes, if present)
rules_dir = ROOT / ".claude" / "rules"
if rules_dir.is_dir():
    eng_rule = rules_dir / "engineering.md"
    if not eng_rule.is_file():
        errors.append(".claude/rules/engineering.md: missing")
    else:
        eng_text = eng_rule.read_text(encoding="utf-8")
        for token in ("ROUTINE", "LOAD-BEARING", "IRREVERSIBLE", "Make the button pink"):
            if token not in eng_text:
                errors.append(f".claude/rules/engineering.md: missing '{token}' — tiers and canonical cases are the executable spec")

# ---------------------------------------------------------------------------
# TEMPLATE-ONLY CHECKS
# A project built from the template legitimately removes the sentinel, adds its
# own agents and skills, and may drop instruction files it does not use. None of
# that is a defect, so none of it is checked outside the template itself.
# ---------------------------------------------------------------------------
if IS_TEMPLATE:
    # The sentinel in the spec and the string the hook greps for must match.
    if hook.is_file() and SENTINEL not in hook.read_text(encoding="utf-8"):
        errors.append(".claude/hooks/session-start.sh: does not grep for the sentinel present in docs/project_spec.md")

    # Plugin and marketplace descriptions must not drift apart
    plugin_json = ROOT / ".claude-plugin" / "plugin.json"
    marketplace_json = ROOT / ".claude-plugin" / "marketplace.json"
    if plugin_json.is_file() and marketplace_json.is_file():
        try:
            plugin_desc = json.loads(plugin_json.read_text(encoding="utf-8")).get("description", "")
            market_plugins = json.loads(marketplace_json.read_text(encoding="utf-8")).get("plugins", [])
            market_desc = market_plugins[0].get("description", "") if market_plugins else ""
            if plugin_desc and market_desc and plugin_desc != market_desc:
                errors.append(".claude-plugin/marketplace.json: plugin description differs from plugin.json — keep them identical")
        except (json.JSONDecodeError, IndexError):
            pass  # parse errors are reported by the JSON check above

    # The template-version stamp must match the plugin version
    version_file = ROOT / ".claude" / "template-version"
    if plugin_json.is_file():
        try:
            plugin_version = json.loads(plugin_json.read_text(encoding="utf-8")).get("version", "")
            if not version_file.is_file():
                errors.append(".claude/template-version: missing — /template-update needs it as the base-version stamp")
            elif version_file.read_text(encoding="utf-8").strip() != f"v{plugin_version}":
                errors.append(f".claude/template-version: '{version_file.read_text(encoding='utf-8').strip()}' does not match plugin.json version 'v{plugin_version}'")
        except json.JSONDecodeError:
            pass

    # Every agent must be mentioned in the SessionStart hook's welcome text
    if hook.is_file():
        hook_text = hook.read_text(encoding="utf-8")
        for agent in agents:
            if agent.stem not in hook_text and agent.stem.replace("-", " ") not in hook_text:
                errors.append(f".claude/hooks/session-start.sh: does not mention agent '{agent.stem}'")

    # Every skill and agent must be mentioned in README, AGENTS.md, and CLAUDE.md
    for doc_name in ("README.md", "AGENTS.md", "CLAUDE.md"):
        doc_path = ROOT / doc_name
        if not doc_path.is_file():
            errors.append(f"{doc_name}: missing from the template")
            continue
        doc = doc_path.read_text(encoding="utf-8")
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

mode = "template" if IS_TEMPLATE else "project"
print(f"Validation passed ({mode} mode): {len(skills)} skills, {len(agents)} agents, configs OK.")
