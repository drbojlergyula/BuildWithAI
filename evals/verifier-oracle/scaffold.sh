#!/usr/bin/env bash
# Scaffold for the verifier-oracle case: a small set-up project whose spec,
# code and tests all agree with each other — and all disagree with the quoted
# source in docs/reference/. The rule layer comes from the template itself.
set -euo pipefail
CASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE_ROOT="$(cd "$CASE_DIR/../.." && pwd)"

cp "$TEMPLATE_ROOT/AGENTS.md" "$TEMPLATE_ROOT/CLAUDE.md" .
mkdir -p .claude
cp -R "$TEMPLATE_ROOT/.claude/rules" .claude/rules
cp -R "$CASE_DIR/fixture/." .

python3 -m unittest discover -s app/tests -q >/dev/null 2>&1 || { echo "fixture broken: conformance tests must pass" >&2; exit 1; }

git init -q
git add -A
git -c user.name=eval -c user.email=eval@example.com commit -qm "S3 built: yearly cost and cap note"
