#!/usr/bin/env bash
# SessionStart hook — orients Claude the moment a session opens.
# Untouched template  -> Claude offers /start.
# Set-up project      -> Claude knows where to find current status.

SPEC="${CLAUDE_PROJECT_DIR:-.}/docs/project_spec.md"

if [ -f "$SPEC" ] && grep -q "A small business owner needs a simple way to collect customer orders" "$SPEC"; then
  cat <<'EOF'
{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"TEMPLATE STATE: untouched — this repository still contains the template's example project. If the user has not asked for something specific, warmly welcome them, mention that this template ships with a ready-made AI team (advisor, spec reviewer, build verifier, research analyst) and guided workflows, and suggest running /start to set up their real project (about 5-10 minutes). Offer it — do not run it unprompted."}}
EOF
else
  cat <<'EOF'
{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"TEMPLATE STATE: project is set up. docs/project_status.md tracks the current phase. If the user seems to need orientation, suggest /put-me-in-context for an instant briefing."}}
EOF
fi

exit 0
