# Propose a New Skill

**Triggers:** After completing a non-trivial task, when noticing a reusable multi-step pattern, or when the user asks to save a pattern.

## Evaluation Criteria

A pattern qualifies for skill creation when **at least one** of the following paths applies:

### Path A: New Skill (no existing skill covers this)

ALL of these must be true:

1. **Reusable** — The pattern applies to more than one specific instance
2. **Non-trivial** — It requires 3+ steps or domain-specific knowledge
3. **Focused** — It targets a specific task type, not general coding
4. **Proven** — The pattern has been successfully applied at least once

### Path B: Deepen / Improve an Existing Skill

Even if a skill with similar keywords already exists, a new or revised skill is warranted when ANY of these is true:

1. **Gap found** — The existing skill misses a step or edge case that the current task revealed
2. **Specialization needed** — The existing skill is too broad; a more focused variant would be more actionable (e.g., `debug-build` exists but `debug-docker-build` would capture a deeper, specific pattern)
3. **Outdated** — The existing skill's procedure no longer matches current project conventions or tooling
4. **Merge opportunity** — Two or more related skills could be consolidated into a stronger, unified skill

**Action for Path B:** First check the existing skill. Then decide:
- **Improve in-place** — Edit the existing `.md` file if the change is additive and doesn't break the original scope
- **Create a deeper variant** — Create a new skill file if the pattern is specific enough to stand on its own
- **Merge** — Replace multiple skills with one consolidated skill, deleting the old files

### Path C: New or Improved Meta-Skill

Meta-skills (prefixed `meta-`) govern how the agent thinks, not what it does. They qualify when:

1. **Cognitive pattern** — The pattern is about reasoning, planning, scoping, learning, or self-evaluation — not domain-specific procedures
2. **Cross-domain** — It applies regardless of whether the task is about databases, Python packaging, or anything else
3. **Compounding** — Improving this pattern makes all future work better, not just one task type

Meta-skills use the same approval process but are filed as `meta-*.md`.

## Procedure

1. **Describe the pattern** — Write a one-paragraph summary of what was done and why.
2. **Classify** — Is this a domain skill or a meta-skill? Domain skills are about "how to do X." Meta-skills are about "how to think about doing X."
3. **Check existing skills** — List commands in `.claude/commands/`. For each skill with similar keywords, read and compare.
4. **Determine path** — Path A (new), Path B (deepen/improve/merge), or Path C (meta)?
5. **Draft the change** — Follow the template in `.claude/commands/README.md`.
6. **Present to user for approval** — Show the draft (new file, edit diff, or merge plan) and ask for confirmation.
7. **On approval, execute** — Create/edit/merge the skill file(s).
8. **Update the memory index** — Reflect changes in `.claude/memory/MEMORY.md`.

## Important

- **Always get user approval** before creating or modifying a skill file
- Patterns that don't pass criteria go to `memory/skill-candidates.md` for future consideration
- Keep skills focused — one pattern per file
- Skills evolve: don't treat existing skills as frozen artifacts
- Meta-skills deserve extra care — they affect all future agent behavior

---
*Created: 2026-02-19 | Source: system design*