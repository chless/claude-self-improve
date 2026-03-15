# Self-Audit — Autonomous Pattern Discovery

**Triggers:** Every ~5th code-editing session, or when explicitly invoked via `/meta-self-audit`. This meta-skill enables the agent to discover its own inefficiencies — not just mistakes the user catches, but patterns the agent can detect from longitudinal data.

## Procedure

### 1. Review Session Logs

Read all `session-log-*.md` files in `.claude/memory/sessions/`. Analyze the last 10 sessions across all users:

- **Correction clustering:** Are user corrections (column) clustering around a specific mistake type?
  - If yes → draft a new anti-pattern entry or strengthen an existing one
- **Governance gaps:** Is a governance step consistently skipped (AP/Scope/Reflect columns show "no")?
  - If yes → investigate why. Is the step too burdensome? Does it need simplification?
- **Skill gaps:** Are there recurring multi-step tasks without a corresponding skill?
  - Cross-reference with `skill-candidates.md` — has a candidate accumulated enough evidence to promote?

### 1.5. Effectiveness Measurement (HIGHEST PRIORITY)

> **This step is the audit's core value proposition.** Compliance (was a skill called?) is easy to check. Effectiveness (did calling the skill prevent the problem?) is the hard question that justifies this audit's existence.

Check whether meta-skills are achieving their intended outcomes, not just whether they are being called.

**For `/meta-anti-patterns`:**
1. List all documented anti-patterns in `ANTI_PATTERN.md` with their documentation dates
2. For each, check session logs AFTER the documentation date:
   - Was the same pattern observed again? (check Corrections column, Notes column, or infer from context)
   - Was `/meta-anti-patterns` called in those sessions? (AP column)
3. If an anti-pattern recurred in a session where AP=yes:
   - The review is **INEFFECTIVE** for this pattern — calling the skill didn't prevent recurrence
   - Analyze why: Is the anti-pattern entry too vague? Too many entries diluting attention? Not actionable enough?
   - Propose a fix: rewrite the entry to be more specific/actionable, add a hook for structural enforcement, or simplify the procedure

**For `/meta-scope-guard`:**
- Did scope creep occur in sessions where Scope=yes? (Check if edited files exceed declared scope)

**For `/meta-learn`:**
- Are the same lessons being "learned" repeatedly? (Check for duplicate insights across sessions)

**Escalation:** Ineffectiveness of a called meta-skill is a MORE serious finding than the skill being skipped. Skipping is a compliance gap (easy fix: remind). Calling without effect is a design gap in the self-improvement loop itself (hard fix: redesign the skill or add structural enforcement).

### 2. Compare Plan vs Execution (current session)

If a session tracker exists at `/tmp/claude-governance-*.json`:
- What was the declared scope? (from `scope_declared` field)
- What files were actually edited? (from `files_edited` array)
- Did scope creep occur? (edited files outside the declared scope)
- Were any edits reverted or redone? (check `git diff` if available)

### 3. Skill Effectiveness Review

Check the Skill Registry in MEMORY.md:
- Are any skills at "draft" maturity with 0 uses for 30+ days? → Consider removing
- Are any skills with <75% success rate? → Flag for revision
- Are two skills always used in the same session? → Consider merging
- Is a meta-skill's procedure producing friction (consistently skipped)? → Flag for `/meta-evolve`

### 4. Output

Produce a brief self-audit report:
- **Effectiveness:** N anti-patterns recurring despite review (CRITICAL if > 0) — from step 1.5
- **Recurrence details:** For each recurring anti-pattern: which AP#, how many post-documentation occurrences, proposed fix
- **Patterns detected:** (list any new recurring patterns from the logs)
- **Proposed improvements:** (specific changes to skills, anti-patterns, or memory)
- **Meta-skill effectiveness:** (did governance steps achieve outcomes, not just run?)
- **Skill health:** (maturity status, unused skills, success rates)

**Present to user for review.** Do NOT auto-apply changes — autonomous discovery requires human approval before modifying the governance system. If changes are approved, use `/meta-evolve` to implement them.

## When NOT to Run

- Fewer than 3 sessions in the session logs — insufficient data for pattern detection
- The current session is trivial (no code edits)
- User is in a hurry (rapid-fire requests)

---
*Created: 2026-02-23 | Source: governance framework extension — autonomous pattern discovery*