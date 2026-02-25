#!/bin/bash
# session-init.sh — SessionStart hook
# Initializes a per-session governance tracker and injects a reminder into
# the agent's context.
#
# Fires on: SessionStart (startup|resume)
# Effect:   Creates /tmp/claude-governance-{session_id}.json
#           Outputs governance reminder to stdout (added to agent context)

set -euo pipefail

INPUT=$(cat)
SESSION_ID=$(echo "$INPUT" | jq -r '.session_id // empty')

if [ -z "$SESSION_ID" ]; then
  exit 0
fi

TRACKER="/tmp/claude-governance-${SESSION_ID}.json"

# Resolve git username for per-user session logs
GIT_USER=$(git -C "${CLAUDE_PROJECT_DIR:-.}" config user.name 2>/dev/null \
  | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr -cd 'a-z0-9-')
GIT_USER="${GIT_USER:-anonymous}"

cat > "$TRACKER" <<JSON
{
  "session_id": "$SESSION_ID",
  "started": "$(date -Iseconds)",
  "git_user": "$GIT_USER",
  "edits": 0,
  "files_edited": [],
  "anti_patterns_checked": false,
  "scope_declared": false,
  "learning_reflected": false
}
JSON

# Stdout is injected into agent context for SessionStart hooks
echo "SESSION GOVERNANCE ACTIVE: Before any code changes, you MUST (1) run /meta-anti-patterns, (2) run /meta-scope-guard. Session tracker: $TRACKER"

exit 0
