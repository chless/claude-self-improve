# Project Memory

## Session Startup Protocol (MANDATORY)

Run these steps at the start of every task involving code changes.
Do NOT skip them even if hooks don't fire — hooks are a safety net, not a substitute.

1. **`/meta-anti-patterns`** — Read ANTI_PATTERN.md, present relevant entries
2. **`/meta-scope-guard`** — Declare scope boundary visibly (in-scope / out-of-scope)
3. After task completion: **`/meta-learn`** — Reflect, update memory/skills/anti-patterns

> See anti-pattern #1: "Skipping mandatory meta-skills at session start"

## Cognitive Architecture — Three Pillars

This agent operates on three reinforcing pillars of human-level intelligence.
See `cognitive-architecture.md` for the full design document.

1. **Motivation** — Intrinsic drive to do well (`/meta-motivation`)
2. **Active Meta-Learning** — Learn in the moment, adapt mid-task (`/meta-situational-learn`)
3. **Hierarchical Memory** — Episodic → Semantic → Procedural (`episodic-memory.md` → `MEMORY.md` → `procedural-memory.md`)

## Meta-Skill Registry

Meta-skills govern how the agent thinks — they compound across all tasks.

| Meta-Skill | Description | Pillar | Mandatory? | Created |
|------------|-------------|--------|------------|---------|
| `meta-motivation` | Form quality goals, self-evaluate, pursue excellence | Motivation | Yes — before every non-trivial task | 2026-03-18 |
| `meta-anti-patterns` | Review ANTI_PATTERN.md before code changes | Memory | Yes — before every code edit | — |
| `meta-scope-guard` | Define and hold scope boundaries | Motivation | Yes — before every task | — |
| `meta-situational-learn` | Assess situation, select strategy, adapt mid-task | Learning | Yes — during every non-trivial task | 2026-03-18 |
| `meta-learn` | Post-task reflection: capture skills, anti-patterns, insights | Learning + Memory | Yes — after non-trivial tasks | — |
| `meta-propose-skill` | Evaluate, create, deepen, or merge skills | Memory | On demand | — |
| `meta-commit` | Leverage git commit as learning signal: reflect → capture → commit | All three | On user request | — |
| `meta-self-audit` | Autonomous pattern discovery across session logs | Learning + Memory | Every ~5 sessions or on demand | — |
| `meta-evolve` | Propose modifications to meta-skills and hooks (requires user approval) | All three | After self-audit or on demand | — |

## Skill Registry

Skills are domain-specific procedures for recurring tasks.
Maturity levels: **draft** (0-1 uses) → **proven** (2-4 uses) → **battle-tested** (5+ uses, updated ≥1x).

| Skill | Description | Maturity | Uses | Last Used | Created |
|-------|-------------|----------|------|-----------|---------|

<!-- Add your domain-specific skills here as they are created. -->

## Skill Candidates

See `skill-candidates.md` for patterns observed but not yet promoted.

## Memory Hierarchy

This file is the **semantic layer** of the three-tier memory hierarchy:

| Layer | Location | Purpose | Managed By |
|-------|----------|---------|------------|
| Episodic | `sessions/`, `episodic-memory.md` | Raw session experiences, tagged for retrieval | `/meta-learn` (append), `/meta-self-audit` (prune) |
| Semantic | `MEMORY.md` (this file), `ANTI_PATTERN.md`, `topic-index.md` | Extracted principles, facts, patterns | `/meta-learn` (update), `/meta-evolve` (restructure) |
| Procedural | `commands/`, `procedural-memory.md` | Executable skills with performance tracking | `/meta-propose-skill` (create), `/meta-evolve` (refine) |

Consolidation flow: episodic → semantic via `/meta-learn`; semantic → procedural via `/meta-propose-skill`.

## Project Insights

<!-- Format: one line per insight -->
- Governance hooks enforce meta-skills via `.claude/settings.json` (SessionStart, PreToolUse, PostToolUse, Stop)
- Session tracker: `/tmp/claude-governance-{session_id}.json` (ephemeral); session logs: `.claude/memory/sessions/` (persistent, per-user)

## Debugging Solutions

<!-- Format: symptom → root cause → fix -->

## User Preferences

<!-- Explicit preferences expressed by the user across sessions -->
