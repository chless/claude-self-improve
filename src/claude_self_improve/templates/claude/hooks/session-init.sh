#!/bin/bash
# session-init.sh — SessionStart hook (Pillar 3: Memory)
# Initializes a per-session governance tracker and injects the three-pillar
# startup reminder into the agent's context.
#
# Fires on: SessionStart (startup|resume)
# Effect:   Creates /tmp/claude-governance-{session_id}.json
#           Outputs three-pillar governance reminder to stdout

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
  "motivation_goals_set": false,
  "scope_declared": false,
  "anti_patterns_checked": false,
  "situation_assessed": false,
  "mid_course_corrections": 0,
  "self_evaluation_done": false,
  "learning_reflected": false
}
JSON

# Stdout is injected into agent context for SessionStart hooks
cat <<EOF
THREE-PILLAR GOVERNANCE ACTIVE. Before any code changes:
  1. MOTIVATION: /meta-motivation (set goals), /meta-scope-guard (define boundaries)
  2. LEARNING:   /meta-anti-patterns (check past mistakes), /meta-learn [Before] (assess situation)
  3. MEMORY:     Session tracker created at $TRACKER
EOF

exit 0
