#!/bin/bash
# pre-edit-governance.sh — PreToolUse hook for Edit|Write
# Checks the session tracker and reminds the agent about anti-patterns
# if they haven't been checked yet. Never blocks — only injects context.
#
# Fires on: PreToolUse (matcher: Edit|Write)
# Effect:   Injects additionalContext if anti-patterns not yet checked

set -euo pipefail

INPUT=$(cat)
SESSION_ID=$(echo "$INPUT" | jq -r '.session_id // empty')
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // "unknown"')

if [ -z "$SESSION_ID" ]; then
  echo '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"allow"}}'
  exit 0
fi

TRACKER="/tmp/claude-governance-${SESSION_ID}.json"

# If no tracker exists, allow silently (session-init may not have fired)
if [ ! -f "$TRACKER" ]; then
  echo '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"allow"}}'
  exit 0
fi

AP_CHECKED=$(jq -r '.anti_patterns_checked' "$TRACKER")

if [ "$AP_CHECKED" != "true" ]; then
  # Remind the agent — allow the edit but inject context
  cat <<EOF
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "additionalContext": "GOVERNANCE: Anti-patterns have NOT been checked this session. You should run /meta-anti-patterns before making further edits to avoid repeating documented mistakes."
  }
}
EOF
else
  echo '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"allow"}}'
fi

exit 0