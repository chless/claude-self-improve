#!/bin/bash
# stop-reflection-gate.sh — Stop hook
# Blocks the agent from stopping if code edits were made but no learning
# reflection (/meta-learn) was run. Prevents infinite loops via
# stop_hook_active check.
#
# Fires on: Stop
# Effect:   Blocks with reason if edits > 0 and learning_reflected is false

set -euo pipefail

INPUT=$(cat)
SESSION_ID=$(echo "$INPUT" | jq -r '.session_id // empty')
STOP_HOOK_ACTIVE=$(echo "$INPUT" | jq -r '.stop_hook_active // false')

# Prevent infinite loop — if we already blocked once, let agent stop
if [ "$STOP_HOOK_ACTIVE" = "true" ]; then
  exit 0
fi

if [ -z "$SESSION_ID" ]; then
  exit 0
fi

TRACKER="/tmp/claude-governance-${SESSION_ID}.json"

# If no tracker, let agent stop
if [ ! -f "$TRACKER" ]; then
  exit 0
fi

EDITS=$(jq -r '.edits // 0' "$TRACKER")
REFLECTED=$(jq -r '.learning_reflected // false' "$TRACKER")

if [ "$EDITS" -gt 0 ] && [ "$REFLECTED" != "true" ]; then
  FILES=$(jq -r '.files_edited | join(", ")' "$TRACKER")
  cat <<EOF
{
  "decision": "block",
  "reason": "You made $EDITS file edit(s) this session ($FILES) but haven't run the learning reflection. Run /meta-learn to reflect on what was done, or explicitly state that no reflection is needed for this session."
}
EOF
  exit 0
fi

exit 0
