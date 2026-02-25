#!/bin/bash
# post-edit-tracker.sh — PostToolUse hook for Edit|Write
# Records each edited file in the session tracker. Completely silent.
#
# Fires on: PostToolUse (matcher: Edit|Write)
# Effect:   Increments edit count, appends file path to tracker

set -euo pipefail

INPUT=$(cat)
SESSION_ID=$(echo "$INPUT" | jq -r '.session_id // empty')
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

if [ -z "$SESSION_ID" ]; then
  exit 0
fi

TRACKER="/tmp/claude-governance-${SESSION_ID}.json"

if [ -f "$TRACKER" ] && [ -n "$FILE_PATH" ]; then
  jq --arg fp "$FILE_PATH" \
    '.edits += 1 | .files_edited += [$fp] | .files_edited |= unique' \
    "$TRACKER" > "${TRACKER}.tmp" && mv "${TRACKER}.tmp" "$TRACKER"
fi

exit 0