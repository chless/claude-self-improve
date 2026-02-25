# Meta-Evolve — Self-Modification Protocol

**Triggers:** After `/meta-self-audit` finds governance friction, or when explicitly invoked. This is the mechanism by which the governance framework improves itself — the agent proposes changes to its own meta-skills, hooks, and memory structure.

> **Core principle:** The agent can *discover* that it needs to change and *propose* specific changes, but a human must approve before any governance rule is modified. This keeps the system genuinely self-improving while maintaining human oversight.

## Procedure

### 1. Evaluate Meta-Skill Effectiveness

For each mandatory meta-skill (`meta-anti-patterns`, `meta-scope-guard`, `meta-learn`):
- Is it being invoked consistently? (check session logs)
- When invoked, does it produce useful output or is it mostly noise?
- Are its steps still accurate for current project conventions?
- Is there friction that causes the agent to skip it?
- Does the procedure match what actually works in practice?

### 2. Evaluate Hook Effectiveness

For each hook in `.claude/settings.json`:
- Is it firing correctly? (check session tracker files in `/tmp/`)
- Is it causing false positives (blocking or reminding when not needed)?
- Is it causing friction without proportional benefit?
- Could the hook be more targeted (better matcher, smarter logic)?

### 3. Evaluate Memory Structure

- Is MEMORY.md approaching 200 lines? → Move detail to topic files
- Is the topic index (`topic-index.md`) accurate? → Update tags and descriptions
- Are anti-pattern tags producing useful filtering? → Adjust tag vocabulary
- Is the session log format capturing the right data? → Propose column changes

### 4. Propose Modifications

For each proposed change:
- **Classify:** cosmetic (wording) | procedural (add/remove step) | structural (new file, new hook)
- **Before/after:** Show the specific text or config being changed
- **Rationale:** What evidence from session logs or self-audit supports this change?
- **Risk:** Could this change break existing workflows?

### 5. Approval Gate

**CRITICAL: ALL governance modifications require explicit user approval.**

- Present each proposed change individually
- Wait for explicit confirmation ("yes", "approved", "do it") before applying
- If the user rejects a change, record the rejection reason as a governance insight in MEMORY.md
- Never batch-apply multiple changes without individual approval

### 6. Apply and Record

After approval for each change:
- Make the modification to the target file
- Add a changelog entry at the bottom of the modified file:
  ```
  *Updated: YYYY-MM-DD | Change: [brief description] | Trigger: [what prompted this]*
  ```
- Update MEMORY.md if the skill/meta-skill registry metadata changed
- If a hook script was modified, remind the user to restart the Claude Code session for hooks to take effect

## What Can Be Modified

| Target | Example Changes |
|--------|----------------|
| Meta-skill procedures | Add/remove/reorder steps, update examples |
| Hook scripts | Change logic, adjust matchers, modify output messages |
| Hook configuration | Add/remove hooks, change timeouts |
| Anti-pattern format | Add fields, change tag vocabulary |
| Memory structure | Create topic files, restructure MEMORY.md sections |
| Skill registry | Update maturity, archive unused skills |

## What Cannot Be Modified (Without Escalation)

- CLAUDE.md core conventions (code style, testing, imports) — these are project rules, not agent governance
- `.claude/settings.local.json` — user-specific permissions
- The approval gate itself — self-modification must always require human approval

---
*Created: 2026-02-23 | Source: governance framework extension — meta-skill self-modification protocol*