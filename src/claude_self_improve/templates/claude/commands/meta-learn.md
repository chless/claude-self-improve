# Learn — The Agent's Complete Learning Loop

**This is the core meta-skill of Pillar 2 (Learning).** It operates across the
full lifecycle of a task — not just after it. Learning is one continuous process
with three phases: Before, During, and After.

> **Philosophy:** A human expert doesn't learn only by reflecting at the end of
> the day. They assess the situation before acting, monitor and adapt while
> working, and consolidate lessons afterward. This meta-skill unifies all three.

## Phase: BEFORE — Situation Assessment

**When:** At the start of every non-trivial task, after `/meta-motivation` sets
goals and `/meta-scope-guard` defines boundaries.

### 1. Build a Mental Model

- What is the current state of the system/code/environment?
- What are the constraints? (technical, time, scope)
- What are the unknowns? What could surprise me?
- Does this situation resemble something I've encountered before?

### 2. Check Structured Memory

- Scan `MEMORY.md` project insights — relevant context?
- Scan `ANTI_PATTERN.md` via `/meta-anti-patterns` — documented pitfalls?
- Scan `episodic-memory.md` — past sessions with similar situations?
- Scan `procedural-memory.md` — skills adapted for this pattern?

### 3. Select Strategy

Choose approach based on the *specific situation*, not just the task type:

| Situation Signal | Strategy |
|-----------------|----------|
| Familiar pattern, high confidence | Execute quickly, verify at end |
| Familiar pattern, something feels off | Proceed carefully, verify after each step |
| Unfamiliar territory, low stakes | Explore freely, document what you learn |
| Unfamiliar territory, high stakes | Propose approach to user before executing |
| Contradictory signals | Stop. Investigate. Ask user if needed |
| Time pressure from user | Simplify scope, prioritize correctness over completeness |

**State your situation model and chosen strategy** to the user in 2-3 sentences.

### Before-Phase Session Tracking

```bash
TRACKER=$(ls /tmp/claude-governance-*.json 2>/dev/null | tail -1)
if [ -n "$TRACKER" ]; then
  jq '.situation_assessed = true' "$TRACKER" > "${TRACKER}.tmp" && mv "${TRACKER}.tmp" "$TRACKER"
fi
```

---

## Phase: DURING — Real-Time Monitoring and Adaptation

**When:** Continuously during task execution. At every natural breakpoint (after
a significant change, before moving to the next file, when uncertain).

### 4. Monitor Progress

**Ask yourself at each breakpoint:**
- Is the code behaving as I expected?
- Am I making progress toward my goals, or spinning?
- Has new information invalidated my initial assessment?
- Am I accumulating technical debt that will bite me later?

**Pattern recognition signals:**
- "Three approaches tried, none work" → Step back, reassess the mental model
- "Taking longer than expected" → Check if scope is right
- "Keep getting surprised" → Mental model is wrong — rebuild it
- "Everything going smoothly" → Stay alert for confirmation bias

### 5. Mid-Course Correction

When monitoring reveals a problem — **don't push through** (sunk cost fallacy).

1. **Acknowledge** to yourself and the user: "My approach isn't working because [reason]."
2. **Diagnose:** Was the situation assessment wrong? The strategy? New information?
3. **Adapt:** Select a new strategy from the table above
4. **Record:** This correction is episodic memory in formation

**Types of corrections:**
- **Tactical:** Change implementation (different algorithm, library, pattern)
- **Strategic:** Change the plan (different order, decomposition)
- **Scope:** Task is bigger/smaller than thought — adjust with user

### 6. Transfer Detection

Recognize when the current situation maps to a past experience:
- Reference the past experience explicitly
- Note what worked or failed last time
- Apply the lesson, adapted for the current context
- If the same transfer happens 3+ times → candidate for a procedural skill

### During-Phase Session Tracking

After any mid-course correction:

```bash
TRACKER=$(ls /tmp/claude-governance-*.json 2>/dev/null | tail -1)
if [ -n "$TRACKER" ]; then
  CORRECTIONS=$(jq -r '.mid_course_corrections // 0' "$TRACKER")
  jq ".mid_course_corrections = $((CORRECTIONS + 1))" "$TRACKER" > "${TRACKER}.tmp" && mv "${TRACKER}.tmp" "$TRACKER"
fi
```

---

## Phase: AFTER — Reflection and Memory Consolidation

**When:** After completing any non-trivial task (3+ steps, involved debugging,
or required domain knowledge). This is where episodes become lasting knowledge.

### 7. Skill Opportunity?

- Did this task follow a multi-step pattern that could recur?
- Did I improvise a procedure that worked well?
- Did an existing skill help, but was missing a step or edge case?

**If yes → invoke `/meta-propose-skill`** to evaluate and draft.

### 8. Anti-Pattern Discovered?

- Did the user correct my approach?
- Did I catch myself about to make a mistake?
- Did a workaround fail because I misunderstood a constraint?

**If yes → add to `ANTI_PATTERN.md`** using the standard format
(CLAUDE.md §Auto-Documentation of Mistakes).

### 9. Memory Consolidation (Episodic → Semantic)

Check each category — update MEMORY.md if something new was learned:

- **Project insight** → Add to "Project Insights" section. One line per insight.
- **Debugging solution** → Add to "Debugging Solutions". Format: `symptom → root cause → fix`.
- **User preference** → Add to "User Preferences". Only record explicit preferences.

**Episodic capture:** Append an episode entry to `episodic-memory.md`:
```
### Episode: [date] — [brief description]
- **Tags:** [situation tags for retrieval]
- **Situation:** [context]
- **Strategy:** [approach chosen]
- **Outcome:** [success/partial/failure]
- **Key learning:** [one-sentence takeaway]
- **Consolidated:** no
```

**When detail exceeds one line:** Create a topic file in the memory directory
and link from MEMORY.md. Keep MEMORY.md under 200 lines.

### 10. Explicit User Request?

- "remember X" / "always do Y" → Save to MEMORY.md immediately
- "forget X" / "stop doing Y" → Find and remove from memory files

### 11. Skill Usage Tracking

If skills were invoked during this session:
- Update "Uses" count and "Last Used" date in MEMORY.md Skill Registry
- Promote maturity: draft (2+ uses) → proven (5+ uses) → battle-tested
- Update `procedural-memory.md` with performance observations

### 12. Meta-Reflection (periodic)

When the skill library or memory grows:
- Skills never used? Remove them.
- Skills always used together? Merge them.
- Meta-skill procedure outdated? Update it.
- MEMORY.md approaching 200 lines? Move detail into topic files.

### After-Phase Session Tracking

```bash
TRACKER=$(ls /tmp/claude-governance-*.json 2>/dev/null | tail -1)
if [ -n "$TRACKER" ]; then
  jq '.learning_reflected = true' "$TRACKER" > "${TRACKER}.tmp" && mv "${TRACKER}.tmp" "$TRACKER"
fi
```

Run this to unblock the Stop hook so the session can end cleanly.

---

## When to Skip Phases

| Scope Level | Before | During | After |
|-------------|--------|--------|-------|
| `trivial` | Skip | Skip | Skip |
| `standard` | Full | Light monitoring | Full reflection |
| `deep` | Full | Active monitoring + corrections | Full reflection + episodic capture |

---
*Created: 2026-02-19 | Source: system design — the agent's learning loop*
*Updated: 2026-03-18 | Change: unified with meta-situational-learn into three-phase learning loop (Before/During/After) | Trigger: three-pillar reframe*
