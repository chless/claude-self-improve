#!/bin/bash
# motivation-tracker.sh — PostToolUse hook (Bash)
# Checks if motivation goals have been set for the session. If the agent has
# made edits but hasn't set goals via /meta-motivation, nudges it.
#
# Fires on: PostToolUse (Bash)
# Effect:   Reminds agent about motivation/goal-setting if not done

set -euo pipefail

INPUT=$(cat)
SESSION_ID=$(echo "$INPUT" | jq -r '.session_id // empty')

if [ -z "$SESSION_ID" ]; then
  exit 0
fi

TRACKER="/tmp/claude-governance-${SESSION_ID}.json"

# If no tracker, skip
if [ ! -f "$TRACKER" ]; then
  exit 0
fi

EDITS=$(jq -r '.edits // 0' "$TRACKER")
GOALS_SET=$(jq -r '.motivation_goals_set // false' "$TRACKER")

# Only nudge if edits have been made without goal-setting
if [ "$EDITS" -gt 2 ] && [ "$GOALS_SET" != "true" ]; then
  echo "MOTIVATION REMINDER: You've made $EDITS edits without setting quality goals. Consider running /meta-motivation to define what success looks like for this task."
fi

exit 0
