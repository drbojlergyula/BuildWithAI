#!/usr/bin/env bash
# Scaffold for the proxy-unverified-gate case: a discovery-run project on a
# night branch, whose plan conditions selection on gates the research could
# not verify. The rule layer comes from the template itself.
set -euo pipefail
CASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE_ROOT="$(cd "$CASE_DIR/../.." && pwd)"

cp "$TEMPLATE_ROOT/AGENTS.md" "$TEMPLATE_ROOT/CLAUDE.md" .
mkdir -p .claude
cp -R "$TEMPLATE_ROOT/.claude/rules" .claude/rules
cp -R "$CASE_DIR/fixture/." .

git init -q
git add -A
git -c user.name=eval -c user.email=eval@example.com commit -qm "discovery complete"
git checkout -q -b night/2026-09-12
