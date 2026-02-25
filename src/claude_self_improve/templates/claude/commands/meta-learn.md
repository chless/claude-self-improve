# Learn — Post-Task Reflection

**Triggers:** After completing any non-trivial task (3+ steps, involved debugging, or required domain knowledge). This meta-skill is the agent's learning loop.

## Procedure

After the task is done, reflect across three dimensions:

### 1. Skill Opportunity?

- Did this task follow a multi-step pattern that could recur?
- Did I improvise a procedure that worked well?
- Did an existing skill help, but was missing a step or edge case?

**If yes → invoke `/meta-propose-skill`** to evaluate and draft.

### 2. Anti-Pattern Discovered?

- Did the user correct my approach?
- Did I catch myself about to make a mistake?
- Did a workaround fail because I misunderstood a constraint?

**If yes → add to `ANTI_PATTERN.md`** using the standard format (CLAUDE.md §Auto-Documentation of Mistakes).

### 3. Memory Update Needed?

Check each category — update MEMORY.md if something new was learned:

- **Project insight** — architecture, conventions, tooling, file paths, surprising behavior
  → Add to "Project Insights" section. One line per insight.
- **Debugging solution** — a fix for a recurring or non-obvious problem
  → Add to "Debugging Solutions" section. Format: `symptom → root cause → fix`.
- **User preference** — workflow, tool choice, communication style the user expressed
  → Add to "User Preferences" section. Only record explicit preferences, not guesses.

**When detail exceeds one line:** Create a topic file in the memory directory (e.g., `debugging.md`, `infra-setup.md`) and link to it from MEMORY.md. Keep MEMORY.md itself as a concise index under 200 lines.

### 4. Explicit User Request?

- Did the user say "remember X" or "always do Y"? → Save to the appropriate MEMORY.md section immediately. No multi-session threshold needed.
- Did the user say "forget X" or "stop doing Y"? → Find and remove the entry from memory files.

## When NOT to Reflect

- Trivial tasks (single-line fixes, simple lookups)
- Tasks where the user is clearly in a hurry (rapid-fire requests)
- If the task was purely informational (answering a question, no code changes)

### 5. Skill Usage Tracking

If any skills were invoked during this session:
- Update their "Uses" count in the Skill Registry table in MEMORY.md
- Update "Last Used" date
- If a skill's maturity is "draft" and it now has 2+ uses, promote to "proven"
- If a skill's maturity is "proven" and it now has 5+ uses, promote to "battle-tested"

## Meta-Reflection (periodic)

When the skill library or memory grows, review for hygiene:
- Are any skills never used? Consider removing them.
- Are two skills always used together? Consider merging them.
- Is a meta-skill's procedure outdated? Update it.
- Are any MEMORY.md entries wrong or outdated? Update or remove them.
- Is MEMORY.md approaching 200 lines? Move detail into topic files.

## Session Tracking

After completing this skill, update the session governance tracker:

```bash
TRACKER=$(ls /tmp/claude-governance-*.json 2>/dev/null | tail -1)
if [ -n "$TRACKER" ]; then
  jq '.learning_reflected = true' "$TRACKER" > "${TRACKER}.tmp" && mv "${TRACKER}.tmp" "$TRACKER"
fi
```

Run this command via Bash to record that learning reflection happened. This unblocks the Stop hook so the session can end cleanly.

---
*Created: 2026-02-19 | Source: system design — the agent's learning loop*
*Updated: 2026-02-23 | Change: added Step 5 (skill usage tracking) and session tracker self-reporting | Trigger: governance enforcement framework*