# Situational Learn — Active In-Task Meta-Learning

**Triggers:** During task execution, whenever the agent encounters uncertainty,
unexpected results, or a decision point. Unlike `/meta-learn` (post-task
reflection), this meta-skill operates *in the moment* — learning while doing.

> **Core insight:** Human experts don't just follow procedures and reflect
> afterwards. They continuously read the situation, adapt mid-task, and notice
> patterns as they emerge. This is the second pillar of human-level intelligence.

## Procedure

### 1. Situation Assessment — "What am I looking at?"

Before acting on a task (or when the situation changes unexpectedly):

**Build a mental model:**
- What is the current state of the system/code/environment?
- What are the constraints I can see? (technical, time, scope)
- What are the unknowns? What could surprise me?
- Does this situation resemble something I've encountered before?

**Check structured memory:**
- Scan `MEMORY.md` project insights — is there relevant context?
- Scan `ANTI_PATTERN.md` — are there documented pitfalls for this type of work?
- Scan `episodic-memory.md` — have past sessions dealt with similar situations?
- Scan `procedural-memory.md` — are there skills adapted for this pattern?

**Output:** A brief (2-3 sentence) situation model shared with the user:
*"This is a [type] task involving [components]. Key risk: [risk]. Relevant past
experience: [reference or 'none']."*

### 2. Strategy Selection — "What's the best approach for THIS situation?"

Don't default to a generic approach. Choose strategy based on the specific situation:

| Situation Signal | Strategy |
|-----------------|----------|
| Familiar pattern, high confidence | Execute quickly, verify at end |
| Familiar pattern, something feels different | Proceed carefully, verify after each step |
| Unfamiliar territory, low stakes | Explore freely, document what you learn |
| Unfamiliar territory, high stakes | Propose approach to user before executing |
| Contradictory signals | Stop. Investigate. Ask user if needed |
| Time pressure from user | Simplify scope, prioritize correctness over completeness |

**Explicitly state your chosen strategy** so the user can redirect if needed.

### 3. Real-Time Monitoring — "Is this working?"

During execution, continuously evaluate:

**Every few minutes or after each significant action:**
- Is the code behaving as I expected?
- Am I making progress toward the goal, or spinning?
- Has new information invalidated my initial assessment?
- Am I accumulating technical debt that will bite me later?

**Pattern recognition signals:**
- "I've tried three different approaches and none work" → Step back, reassess
- "This is taking longer than expected" → Check if scope is right
- "I keep getting surprised by the code behavior" → My mental model is wrong, rebuild it
- "Everything is going smoothly" → Good, but stay alert for confirmation bias

### 4. Mid-Course Correction — "I need to change approach"

When monitoring reveals a problem:

**Don't push through.** The human tendency to commit to a failing approach
(sunk cost fallacy) is the enemy of good work.

**Correction protocol:**
1. **Acknowledge** the issue to yourself and the user: "My initial approach
   isn't working because [reason]."
2. **Diagnose** why: Was the situation assessment wrong? The strategy wrong? New
   information?
3. **Adapt** by selecting a new strategy from the table in Step 2
4. **Record** the correction as a learning signal — this is episodic memory in formation

**Types of corrections:**
- **Tactical:** Change implementation approach (different algorithm, library, pattern)
- **Strategic:** Change the overall plan (different order, different decomposition)
- **Scope:** Realize the task is bigger/smaller than thought, adjust with user

### 5. Transfer Detection — "I've seen this before"

The most valuable form of in-task learning: recognizing when the current
situation maps to a past experience.

**When you notice a similarity:**
- Reference the past experience explicitly
- Note what worked or failed last time
- Apply the lesson, adapted for the current context
- If the transfer leads to a better approach, tell the user

**When building the transfer:**
- Tag the current situation in episodic memory for future retrieval
- If the same transfer happens 3+ times, it's a candidate for a procedural skill

### 6. Learning Capture (In-Task)

Unlike `/meta-learn` which captures lessons after the task, capture observations
*as they happen*:

- Note surprising behaviors in the code/system
- Note which strategies worked and which didn't
- Note decision points where you had to choose
- These raw observations feed into `/meta-learn` for structured consolidation

## Integration with Other Meta-Skills

- **`/meta-motivation`** provides the *drive* to engage in active monitoring
  (it's effortful — without motivation, agents default to passive execution)
- **`/meta-scope-guard`** provides the *boundaries* within which learning happens
- **`/meta-learn`** *consolidates* what was learned in-task into structured memory
- **`/meta-anti-patterns`** provides the *negative examples* for situation assessment

## Session Tracking

After situation assessment, update the tracker:

```bash
TRACKER=$(ls /tmp/claude-governance-*.json 2>/dev/null | tail -1)
if [ -n "$TRACKER" ]; then
  jq '.situation_assessed = true' "$TRACKER" > "${TRACKER}.tmp" && mv "${TRACKER}.tmp" "$TRACKER"
fi
```

After any mid-course correction, log it:

```bash
TRACKER=$(ls /tmp/claude-governance-*.json 2>/dev/null | tail -1)
if [ -n "$TRACKER" ]; then
  CORRECTIONS=$(jq -r '.mid_course_corrections // 0' "$TRACKER")
  jq ".mid_course_corrections = $((CORRECTIONS + 1))" "$TRACKER" > "${TRACKER}.tmp" && mv "${TRACKER}.tmp" "$TRACKER"
fi
```

---
*Created: 2026-03-18 | Source: Pillar 2 of cognitive architecture — active meta-learning system*
