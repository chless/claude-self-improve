# Project Memory

This file is the **semantic layer** of the three-tier memory hierarchy.
See `cognitive-architecture.md` for the full design.

## Session Startup Protocol (MANDATORY)

Every task with code changes activates all three pillars in order:

1. **Motivation:** `/meta-motivation` → set goals, `/meta-scope-guard` → define boundaries
2. **Learning:** `/meta-anti-patterns` → check past mistakes, `/meta-learn [Before]` → assess situation
3. **Memory:** Hooks auto-track files and session state

After task: `/meta-learn [After]` → reflect, consolidate, then `/meta-commit` → persist.

> See anti-pattern #1: "Skipping mandatory meta-skills at session start"

---

## Cognitive Architecture — Three Pillars

```
  MOTIVATION (why)      LEARNING (how)       MEMORY (what)
  ──────────────        ──────────────       ─────────────
  /meta-motivation      /meta-learn          Episodic → Semantic → Procedural
  /meta-scope-guard     /meta-anti-patterns  /meta-propose-skill
  motivation-tracker    /meta-self-audit     /meta-evolve, /meta-commit
```

## Meta-Skill Registry

| Meta-Skill | Pillar | Description | Mandatory? | Created |
|------------|--------|-------------|------------|---------|
| `meta-motivation` | Motivation | Form quality goals, self-evaluate, pursue excellence | Yes — before every non-trivial task | 2026-03-18 |
| `meta-scope-guard` | Motivation | Define and hold scope boundaries, classify scope level | Yes — before every task | 2026-02-19 |
| `meta-learn` | Learning | Three-phase learning: Before (assess), During (monitor), After (reflect) | Yes — full lifecycle for non-trivial tasks | 2026-02-19 |
| `meta-anti-patterns` | Learning | Review ANTI_PATTERN.md before code changes | Yes — before every code edit | 2026-02-19 |
| `meta-self-audit` | Learning | Autonomous pattern discovery across session logs | Every ~5 sessions | 2026-02-23 |
| `meta-propose-skill` | Memory | Consolidate semantic knowledge into procedural skills | On demand | 2026-02-19 |
| `meta-commit` | Memory | Atomic persistence: reflect → capture → commit | On user request | 2026-02-19 |
| `meta-evolve` | Memory | Propose modifications to governance (requires user approval) | After self-audit | 2026-02-23 |

## Skill Registry

Skills are domain-specific procedures for recurring tasks.
Maturity levels: **draft** (0-1 uses) → **proven** (2-4 uses) → **battle-tested** (5+ uses, updated ≥1x).

| Skill | Description | Maturity | Uses | Last Used | Created |
|-------|-------------|----------|------|-----------|---------|

<!-- Add your domain-specific skills here as they are created. -->

## Skill Candidates

See `skill-candidates.md` for patterns observed but not yet promoted.

---

## Memory Hierarchy

| Layer | Location | Purpose | Managed By |
|-------|----------|---------|------------|
| Episodic | `sessions/`, `episodic-memory.md` | Raw session experiences, tagged for retrieval | `/meta-learn [After]` (append), `/meta-self-audit` (prune) |
| Semantic | `MEMORY.md` (this file), `ANTI_PATTERN.md`, `topic-index.md` | Extracted principles, facts, patterns | `/meta-learn [After]` (update), `/meta-evolve` (restructure) |
| Procedural | `commands/`, `procedural-memory.md` | Executable skills with performance tracking | `/meta-propose-skill` (create), `/meta-evolve` (refine) |

Consolidation: episodic → semantic via `/meta-learn [After]`; semantic → procedural via `/meta-propose-skill`.

---

## Project Insights

<!-- Format: one line per insight -->
- Governance hooks enforce meta-skills via `.claude/settings.json` (SessionStart, PreToolUse, PostToolUse, Stop)
- Session tracker: `/tmp/claude-governance-{session_id}.json` (ephemeral); session logs: `.claude/memory/sessions/` (persistent, per-user)
- Three pillars organize ALL agent behavior: Motivation (why), Learning (how), Memory (what)

## Debugging Solutions

<!-- Format: symptom → root cause → fix -->

## User Preferences

<!-- Explicit preferences expressed by the user across sessions -->
