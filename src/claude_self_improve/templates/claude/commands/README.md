# Skill Library — .claude/commands/

Custom commands encoding reusable problem-solving patterns.
Each `.md` file becomes a slash command invocable as `/filename`.

## Two Tiers: Skills and Meta-Skills

### Skills (domain-specific)
How to do specific tasks. Named descriptively: `refactor.md`, `debug-build.md`.

Examples: "how to troubleshoot a build system", "how to create a subpackage", "how to review code."

### Meta-Skills (agent cognition)
How the agent thinks, learns, and governs itself. Prefixed `meta-`: `meta-learn.md`, `meta-scope-guard.md`.

Examples: "how to stay in scope", "how to learn from a task", "how to avoid past mistakes."

**Why meta-skills matter:** Every user correction is a failure mode — it pulls the user out of their core work to fix agent behavior. Meta-skills exist to eliminate this cost. A better domain skill improves one task type. A better meta-skill improves *all future work* by making the agent self-correcting: it catches its own scope creep, avoids repeated mistakes, and captures lessons without waiting for the user to intervene.

**The recursive loop:** Meta-skills are uniquely self-improving. `/meta-learn` reflects on how the agent worked — including how well its meta-skills performed — and feeds improvements back into those same meta-skills. `/meta-propose-skill` creates better skills, which generate richer reflection material, which produces better meta-skills. This is a deliberate design: as meta-skills compound, the agent's capacity to learn, govern itself, and produce quality work grows beyond what the user could prescribe through direct instructions alone. The ceiling is not the user's ability to dictate — it is the system's ability to learn.

## Skill Template

New skills must follow this format:

```
# [Skill Title]

**Triggers:** When to use this skill (specific conditions)

## Procedure
1. Step-by-step instructions

## Examples
Concrete input → action → result

---
*Created: YYYY-MM-DD | Source: [conversation/anti-pattern/user-request]*
```

## Conventions

- Filenames: kebab-case `.md` (e.g., `debug-build.md`)
- Meta-skills: always prefixed `meta-` (e.g., `meta-learn.md`)
- Don't duplicate built-in commands (/help, /compact, /init, /clear, /review)
- Skills contain ONLY positive patterns
- Anti-patterns are handled separately by `/meta-anti-patterns`
- A skill must have been applied successfully at least once before creation
- New skills require user approval (use `/meta-propose-skill` workflow)
- After creating a skill, update MEMORY.md with a registry entry
