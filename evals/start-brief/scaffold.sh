#!/usr/bin/env bash
# Scaffold for the start-brief case: the untouched template as a user would
# clone it — example docs with their sentinels, the rule layer, a git repo.
# Runs in the empty eval workspace (cwd) before Claude starts, only under
# `claude plugin eval --scaffold`.
set -euo pipefail
CASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE_ROOT="$(cd "$CASE_DIR/../.." && pwd)"

cp "$TEMPLATE_ROOT/AGENTS.md" "$TEMPLATE_ROOT/CLAUDE.md" "$TEMPLATE_ROOT/README.md" .
mkdir -p .claude
cp -R "$TEMPLATE_ROOT/.claude/rules" .claude/rules
cp -R "$TEMPLATE_ROOT/docs" docs
rm -rf docs/reference/*.md 2>/dev/null || true
cp "$TEMPLATE_ROOT/docs/reference/README.md" docs/reference/README.md 2>/dev/null || true

grep -q "template-state: untouched-example" docs/project_spec.md || { echo "fixture broken: sentinel missing" >&2; exit 1; }
grep -q "house-rules: unset" docs/house_rules.md || { echo "fixture broken: house-rules marker missing" >&2; exit 1; }

git init -q
git add -A
git -c user.name=eval -c user.email=eval@example.com commit -qm "untouched template"
