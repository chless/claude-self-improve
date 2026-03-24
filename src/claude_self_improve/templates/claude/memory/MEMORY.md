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
| `meta-inner-self` | Motivation | Critical evaluation of suggestions before adoption — inner inertia | On governance/architecture suggestions | 2026-03-24 |
| `meta-learn` | Learning | Three-phase learning: Before (assess), During (monitor), After (reflect) | Yes — full lifecycle for non-trivial tasks | 2026-02-19 |
| `meta-anti-patterns` | Learning | Review ANTI_PATTERN.md before code changes | Yes — before every code edit | 2026-02-19 |
| `meta-self-audit` | Learning | Autonomous pattern discovery across session logs | Every ~5 sessions | 2026-02-23 |
| `meta-absorb-repo` | Learning | Extract transferable intelligence from child repos via generality filter | On demand | 2026-03-24 |
| `meta-intelligence-review` | Learning | Multi-perspective peer review between stateful intelligences | On demand | 2026-03-24 |
| `meta-intelligence-inject` | Memory | Push knowledge with provenance into another stateful intelligence | On demand | 2026-03-24 |
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
| Semantic | `MEMORY.md` (this file), `ANTI_PATTERN.md`, `topic-index.md`, `absorbed-intelligence.md`, `review-registry.md` | Extracted principles, facts, patterns | `/meta-learn [After]` (update), `/meta-evolve` (restructure), `/meta-absorb-repo` (cross-repo) |
| Procedural | `commands/`, `procedural-memory.md` | Executable skills with performance tracking | `/meta-propose-skill` (create), `/meta-evolve` (refine) |

Consolidation: episodic → semantic via `/meta-learn [After]`; semantic → procedural via `/meta-propose-skill`.
Cross-repo integration: child `.claude/` → parent semantic via `/meta-absorb-repo`.
Peer intelligence: review records and injections via `/meta-intelligence-review` and `/meta-intelligence-inject`.

---

## Project Insights

<!-- Format: one line per insight -->
- Governance hooks enforce meta-skills via `.claude/settings.json` (SessionStart, PreToolUse, PostToolUse, Stop)
- Session tracker: `/tmp/claude-governance-{session_id}.json` (ephemeral); session logs: `.claude/memory/sessions/` (persistent, per-user)
- Three pillars organize ALL agent behavior: Motivation (why), Learning (how), Memory (what)
- Cross-repo intelligence: `/meta-absorb-repo` extracts domain-agnostic principles from child repos; `absorbed-intelligence.md` tracks absorption history and cross-repo patterns
- Stateful intelligence network: git repos are stateful intelligences; `/meta-intelligence-review` enables multi-perspective peer review with full provenance for BOTH reviewer and reviewee; `/meta-intelligence-inject` enables knowledge push; `reviews/` stores incoming perspectives; Mode B supports cross-repo review processing
- Inner self: `/meta-inner-self` evaluates incoming suggestions against accumulated experience before adoption — the intelligence forms its own position, states it once, then follows the user's decision; override data feeds future self-audits

## Debugging Solutions

<!-- Format: symptom → root cause → fix -->

## User Preferences

<!-- Explicit preferences expressed by the user across sessions -->
