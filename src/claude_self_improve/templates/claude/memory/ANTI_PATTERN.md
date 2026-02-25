# Anti-Patterns for AI Agents

This document records error patterns observed from AI agents working on this project. **Do not repeat these mistakes.**

---

## Format for Adding New Anti-Patterns

When documenting a new anti-pattern, use the following template:


### [Short Title]
- **Tags:** comma-separated tags for contextual filtering
- **Date:** YYYY-MM-DD
- **Context:** What task was being performed
- **Error:** What the agent did wrong
- **Correct approach:** What should have been done instead


---

## Recorded Anti-Patterns

### 1. Skipping mandatory meta-skills at session start
- **Tags:** meta, governance, scope
- **Context:** Agent started a non-trivial task involving code changes.
- **Error:** Agent did not run `/meta-anti-patterns` or `/meta-scope-guard` before starting work. The mandatory meta-skills were documented in MEMORY.md and CLAUDE.md but the agent skipped them silently.
- **Correct approach:** At the start of every task involving code changes, explicitly run: (1) `/meta-anti-patterns`, (2) `/meta-scope-guard`. Do this regardless of whether hooks fire. The hooks are a safety net, not a substitute for following documented procedures.

### 2. Making unrequested changes
- **Tags:** scope, editing, meta
- **Context:** User asked to update documentation.
- **Error:** Agent modified code with "optimizations" that were never requested, going beyond the scope of the task.
- **Correct approach:** Only change what was explicitly requested. If improvements seem useful, mention them but don't implement without permission.

### 3. Skipping README when creating a new directory
- **Tags:** creating, documentation
- **Context:** Agent created a new subdirectory with code but no README.
- **Error:** Project conventions require a README.md in each new directory, yet the agent skipped it until explicitly asked.
- **Correct approach:** When creating a new directory with code, always write a README.md in the same step.
