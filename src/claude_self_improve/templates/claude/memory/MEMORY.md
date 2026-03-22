# Project Memory

## Session Startup Protocol (MANDATORY)

Run these steps at the start of every task involving code changes.
Do NOT skip them even if hooks don't fire — hooks are a safety net, not a substitute.

1. **`/meta-anti-patterns`** — Read ANTI_PATTERN.md, present relevant entries
2. **`/meta-scope-guard`** — Declare scope boundary visibly (in-scope / out-of-scope)
3. After task completion: **`/meta-learn`** — Reflect, update memory/skills/anti-patterns

> See anti-pattern #1: "Skipping mandatory meta-skills at session start"

## Meta-Skill Registry

Meta-skills govern how the agent thinks — they compound across all tasks.

| Meta-Skill | Description | Mandatory? | Created |
|------------|-------------|------------|---------|
| `meta-anti-patterns` | Review ANTI_PATTERN.md before code changes | Yes — before every code edit | — |
| `meta-scope-guard` | Define and hold scope boundaries | Yes — before every task | — |
| `meta-learn` | Post-task reflection: capture skills, anti-patterns, insights | Yes — after non-trivial tasks | — |
| `meta-propose-skill` | Evaluate, create, deepen, or merge skills | On demand | — |
| `meta-commit` | Leverage git commit as learning signal: reflect → capture → commit | On user request | — |
| `meta-self-audit` | Autonomous pattern discovery across session logs | Every ~5 sessions or on demand | — |
| `meta-evolve` | Propose modifications to meta-skills and hooks (requires user approval) | After self-audit or on demand | — |
| `meta-integrate` | Review child repos' governance evolution, extract generalizable improvements (requires user approval) | Periodically or on demand | — |

## Skill Registry

Skills are domain-specific procedures for recurring tasks.
Maturity levels: **draft** (0-1 uses) → **proven** (2-4 uses) → **battle-tested** (5+ uses, updated ≥1x).

| Skill | Description | Maturity | Uses | Last Used | Created |
|-------|-------------|----------|------|-----------|---------|

<!-- Add your domain-specific skills here as they are created. -->

## Skill Candidates

See `skill-candidates.md` for patterns observed but not yet promoted.

## Project Insights

<!-- Format: one line per insight -->
- Governance hooks enforce meta-skills via `.claude/settings.json` (SessionStart, PreToolUse, PostToolUse, Stop)
- Session tracker: `/tmp/claude-governance-{session_id}.json` (ephemeral); session logs: `.claude/memory/sessions/` (persistent, per-user)

## Debugging Solutions

<!-- Format: symptom → root cause → fix -->

## Child Repo Intelligence

Registered child repos and integration status are tracked in `children.json`.
Use `/meta-integrate` to review child repos for generalizable governance improvements.

| Child | Source | Last Integrated | Proposals Adopted |
|-------|--------|----------------|-------------------|

<!-- Populated automatically by /meta-integrate -->

## User Preferences

<!-- Explicit preferences expressed by the user across sessions -->
