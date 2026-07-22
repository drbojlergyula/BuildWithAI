#!/usr/bin/env bash
# SessionStart hook — orients Claude the moment a session opens.
# Untouched template          -> Claude offers /start.
# Set-up project with docs/   -> Claude knows where to find current status.
# No docs/ (plugin install)   -> Claude offers to set up the docs-as-memory structure.

PROJECT="${CLAUDE_PROJECT_DIR:-.}"
SPEC="$PROJECT/docs/project_spec.md"

# Single source of truth for "untouched template": the sentinel comment at the
# top of docs/project_spec.md. /start and /adopt-project remove it when they
# write the real spec. Skills reference the same marker.
if [ -f "$SPEC" ] && grep -q "template-state: untouched-example" "$SPEC"; then
  cat <<'EOF'
{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"TEMPLATE STATE: untouched — this repository still contains the template's example project. If the user has not asked for something specific, warmly welcome them, mention that this template ships with a ready-made AI team (advisor, spec reviewer, build verifier, research analyst, and an owner-proxy deputy for autonomous night shifts) and guided workflows, and suggest running /start to set up their real project (about 5-10 minutes). Offer it — do not run it unprompted."}}
EOF
elif [ -f "$SPEC" ]; then
  cat <<'EOF'
{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"TEMPLATE STATE: project is set up. docs/project_status.md tracks the current phase. When greeting the user (or if they seem unsure what to do), glance at docs/project_status.md and offer 2-3 concrete next actions tailored to where they are — e.g. '/build-next to build [the next planned story]', 'run the build-verifier agent on [the just-finished feature]', '/go-live if you are ready to launch', or /put-me-in-context for a full briefing. Suggest, do not push."}}
EOF
else
  cat <<'EOF'
{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"BUILDWITHAI TOOLKIT: active in a project without the docs-as-memory structure (no docs/project_spec.md). The AI team (project-advisor, spec-reviewer, build-verifier, research-analyst, owner-proxy) and skills work regardless. If there is existing code, /adopt-project reverse-engineers the project docs from it (the right choice for Lovable/Bolt/v0 exports and any established codebase); for a brand-new empty project, /start interviews the user from scratch. Mention the fitting one once if relevant — do not push."}}
EOF
fi

exit 0
