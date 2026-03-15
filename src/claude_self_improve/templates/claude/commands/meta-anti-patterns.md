Read the file `.claude/memory/ANTI_PATTERN.md` and internalize all documented anti-patterns.

## Contextual Filtering

1. If `$ARGUMENTS` is provided, filter to anti-patterns whose **Tags** match the topic "$ARGUMENTS".
2. If no arguments are provided, infer the current task context from the user's request.
3. Read and internally consider **all** anti-patterns (including `meta`-tagged ones) — but only **display** anti-patterns that are **directly and specifically relevant** to the current task.

### Relevance threshold

An anti-pattern is "directly relevant" only if the current task risks the **specific scenario** described in that anti-pattern's Context/Error fields. Broad tag overlap alone is not enough.

Examples:
- Scope creep (#1): show only when the request is ambiguous and genuinely risks unasked-for changes, not on every editing task
- Missing README: show only when actually creating a new subpackage or directory

## Presentation

**If one or more anti-patterns are directly relevant:**
- For each, show: title, one-line summary, correct approach, and why it applies to this specific task
- State how these anti-patterns should influence the current approach

**If no anti-patterns are directly relevant:**
- Produce **no visible output**. The agent has still read and internalized all patterns — it simply has nothing specific to surface.

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
