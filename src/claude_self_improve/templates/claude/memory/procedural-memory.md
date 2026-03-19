# Procedural Memory — Pillar 3: Memory (Top Layer)

This file tracks how skills perform in practice and how they've been adapted
over time. It sits at the top of the memory hierarchy: episodic (sessions/) →
semantic (MEMORY.md) → procedural (here + commands/).

## How to Use

1. When a skill is invoked, `/meta-learn` records its performance here
2. When `/meta-self-audit` runs, it reads this file to assess skill health
3. When `/meta-evolve` proposes changes, it uses adaptation history to justify modifications
4. Patterns that appear 3+ times across episodes get promoted to skills tracked here

## Skill Performance Format

```
### Skill: /[skill-name]
- **Total invocations:** N
- **Success rate:** N% (fully successful / total)
- **Adaptation count:** N (times the skill procedure was modified)
- **Last adaptation:** [date] — [what changed and why]
- **Common triggers:** [situations that lead to invoking this skill]
- **Known limitations:** [situations where this skill underperforms]
```

## Skill Performance Records

<!-- Records are added/updated by /meta-learn after skill invocations. -->

## Promotion Pipeline

Patterns that are candidates for becoming procedural skills:

| Pattern | Occurrences | Source Episodes | Status |
|---------|-------------|-----------------|--------|
<!-- Populated by /meta-self-audit when it detects recurring patterns in episodic memory -->

## Adaptation Principles

When modifying a skill, follow these principles (from cognitive science):

1. **Preserve what works** — Don't rewrite a skill that's mostly effective. Patch the specific failure mode.
2. **Version, don't replace** — When making significant changes, note what the old procedure was.
3. **Test the adaptation** — After modifying a skill, track the next 3 invocations for regression.
4. **Consolidate duplicates** — If two skills handle overlapping situations, merge or create a clear routing rule.

---
*Created: 2026-03-18 | Source: Pillar 3 of cognitive architecture — procedural memory layer*
