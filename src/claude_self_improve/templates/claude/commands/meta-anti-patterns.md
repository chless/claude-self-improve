Read the file `.claude/memory/ANTI_PATTERN.md` and present documented anti-patterns.

## Contextual Filtering

1. If `$ARGUMENTS` is provided, filter to anti-patterns whose **Tags** match the topic "$ARGUMENTS" and explain why they are relevant to the current task.
2. If no arguments are provided, infer the current task context:
   - About to create a new directory/subpackage? → prioritize tags: `creating`, `subpackage`, `documentation`
   - About to edit existing code? → prioritize tags: `scope`, `editing`
   - Debugging an issue? → prioritize tags: `debugging`, `infrastructure`
   - Unclear context? → show all entries (full detail)
3. Always show entries tagged `meta` — these apply universally.

## Presentation

For each relevant anti-pattern, show:
- Title, tags, and date
- One-line summary of the error
- The correct approach
- Why it is relevant to the current task

For non-relevant anti-patterns (wrong tags for current context), list titles only (one line each) so the agent is aware they exist without noise.

After presenting, state which anti-patterns should influence the current approach and how.

This is the single entry point for all anti-pattern knowledge. Skills (positive patterns) are separate — they do not contain anti-pattern references.

## Session Tracking

After completing this skill, update the session governance tracker:

```bash
TRACKER=$(ls /tmp/claude-governance-*.json 2>/dev/null | tail -1)
if [ -n "$TRACKER" ]; then
  jq '.anti_patterns_checked = true' "$TRACKER" > "${TRACKER}.tmp" && mv "${TRACKER}.tmp" "$TRACKER"
fi
```

Run this command via Bash to record that anti-patterns were checked this session.