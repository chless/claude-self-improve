# Scope Guard

**Triggers:** At the start of every task that involves code changes. The agent must declare scope visibly (a brief "Scope: ..." line is sufficient) so that compliance is observable.

## Procedure

### Before Starting Work

1. **Parse the request** — Restate in one sentence what the user is asking for. Identify the verbs (fix, add, update, refactor, review) and the nouns (which files, which feature, which scope).
2. **Classify the scope level** — Declare one of:
   - **`trivial`** — Typo fix, single-line change, config tweak, rename. No investigation needed. Reflection will be skipped.
   - **`standard`** — Feature addition, bug fix, refactor within a module. Normal workflow. Reflection required.
   - **`deep`** — Cross-cutting change, debugging a subtle issue, architectural decision, performance investigation. High cognitive effort. Reflection strongly encouraged.
3. **Draw the boundary** — List explicitly:
   - **In scope:** files/modules/behaviors that the request directly addresses
   - **Out of scope:** everything else, even if it's adjacent or "could be improved"
4. **Hold the boundary** — During execution, before each edit ask: "Is this file/change inside my stated scope?" If not, stop.

### When You Notice Something Outside Scope

Do NOT silently fix it. Instead:
- Note it briefly to the user: *"I noticed [thing] but it's outside the current scope. Want me to address it separately?"*
- Wait for explicit confirmation before acting on it
- If the user says no, move on without further mention

### Scope Escalation

If the task turns out to require changes outside the original scope (e.g., fixing a bug requires updating a dependency):
- Explain why the scope needs to expand
- Get confirmation before proceeding
- Update your scope boundary explicitly

## Examples

### Tight Scope
**Request:** "Fix the typo in README.md"
**In scope:** README.md text content
**Out of scope:** code, other docs, scripts, formatting improvements beyond the typo

### Medium Scope
**Request:** "Refactor utils/parser.py"
**In scope:** parser.py, its test file, imports it uses
**Out of scope:** other files in utils/, unrelated modules, documentation

### Broad Scope
**Request:** "Refactor the entire codebase"
**In scope:** all source files, but still requires a plan + approval before execution
**Out of scope:** making unrequested feature additions even during a repo-wide refactor

## Session Tracking

After defining the scope boundary, update the session governance tracker with both the declaration and the level. Replace `LEVEL` with the declared scope level (`trivial`, `standard`, or `deep`):

```bash
TRACKER=$(ls /tmp/claude-governance-*.json 2>/dev/null | tail -1)
if [ -n "$TRACKER" ]; then
  jq '.scope_declared = true | .scope_level = "LEVEL"' "$TRACKER" > "${TRACKER}.tmp" && mv "${TRACKER}.tmp" "$TRACKER"
fi
```

Run this command via Bash to record that scope was declared this session. The `scope_level` determines whether `/meta-learn` is required at session end:
- `trivial` → reflection skipped automatically
- `standard` / `deep` → reflection required (stop hook blocks without it)

---
*Created: 2026-02-19 | Source: anti-pattern elevated to a proactive meta-skill*
*Updated: 2026-03-15 | Change: added scope level classification (trivial/standard/deep) and level-aware session tracking | Trigger: battle-tested in production*
