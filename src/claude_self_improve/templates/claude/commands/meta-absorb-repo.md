# Absorb Repository — Cross-Repo Intelligence Integration

**Triggers:** When the parent framework needs to learn from a child repo's accumulated governance experience. Invoked explicitly as `/meta-absorb-repo <path-or-url>`. This meta-skill extracts domain-agnostic intelligence from domain-specific deployments.

> **Core principle:** Child repos evolve specialized intelligence through real usage. The parent framework absorbs only what is transferable — principles that hold across domains — so it improves without losing generality. All proposed changes go through existing approval gates (`/meta-evolve`, `/meta-propose-skill`). The agent never auto-applies absorbed intelligence.

## The Generality Filter

Every candidate extracted from a child repo must pass all four gates before it can be proposed:

### Gate 1: Three-Substitution Test

Strip domain nouns from the candidate. Replace them with nouns from three unrelated domains. The principle must hold in all three.

**Example:**
- Child repo (health coach): "Always ask for the user's health goals before giving advice"
- Domain nouns: "health goals", "advice"
- Relational principle: "Clarify constraints before generating output"
- Test 1 (software): "Clarify requirements before writing code" — holds
- Test 2 (legal): "Clarify facts before drafting argument" — holds
- Test 3 (cooking): "Clarify dietary restrictions before planning menu" — holds
- **Result:** PASS — the principle is domain-agnostic

If the principle fails in any domain: REJECT. It is domain-specific knowledge, not a transferable principle.

### Gate 2: Pillar Ownership

The candidate must map cleanly to one of the three cognitive-architecture pillars:

- **Motivation** (why): goal formation, self-evaluation, scope discipline, quality pursuit
- **Learning** (how): situation assessment, monitoring, reflection, pattern transfer
- **Memory** (what): episodic storage, semantic extraction, procedural consolidation

If it doesn't map to a pillar, it is a domain fact (belongs in a project-specific MEMORY.md, not the parent framework).

### Gate 3: Existing Coverage Check

Check whether the parent framework's existing procedures already imply this principle:

- Read parent `commands/*.md` procedures and `MEMORY.md` insights
- If the principle is already stated or clearly implied: record as **evidence** (increases weight of existing principle) but do NOT add a duplicate
- If the principle fills a gap in an existing procedure: propose as a **procedure extension**
- If the principle is genuinely novel: propose as a **new addition**

### Gate 4: Source Layer Routing

Route the candidate to the correct approval mechanism:

| Candidate Type | Route To | Approval Gate |
|---------------|----------|---------------|
| Anti-pattern | `/meta-evolve` proposal | Human approves ANTI_PATTERN.md addition |
| Skill (new) | `/meta-propose-skill` Path A | Human approves skill creation |
| Skill (improve) | `/meta-propose-skill` Path B | Human approves skill modification |
| Meta-skill (new) | `/meta-propose-skill` Path C | Human approves meta-skill creation |
| Semantic insight | `/meta-evolve` proposal | Human approves MEMORY.md update |
| Framework friction | `/meta-evolve` evaluation | Human reviews governance modification |

---

## Procedure

### Phase 1: Reconnaissance

Assess the child repo's signal quality before investing in extraction.

1. Access the child repo (local path or clone from URL)
2. Verify `.claude/` directory exists with `memory/` and `commands/` subdirectories
3. Count governance evolution:
   ```bash
   git log --oneline --all -- ".claude/" | wc -l
   ```
4. Get per-file commit distribution:
   ```bash
   git log --stat --all -- ".claude/"
   ```
5. **Signal quality assessment:**
   - **< 5 governance commits:** LOW signal — framework was scaffolded but barely used. Report this and stop (unless user explicitly wants to proceed).
   - **5-15 commits:** MODERATE signal — some real evolution. Proceed with caution, weight evidence lower.
   - **15+ commits:** HIGH signal — substantial evolution under real usage. Full extraction warranted.
6. Record signal quality for the absorption report.

### Phase 2: Anti-Pattern Extraction

Extract failure mode intelligence from `ANTI_PATTERN.md`.

1. Get the full evolution history:
   ```bash
   git log --follow -p -- ".claude/memory/ANTI_PATTERN.md"
   ```
2. Read the current state of the file
3. For each anti-pattern entry:
   a. **Apply Gate 1** (three-substitution test): strip domain nouns, test across three domains
   b. **Apply Gate 2** (pillar ownership): map to Motivation/Learning/Memory
   c. **Apply Gate 3** (existing coverage): check parent ANTI_PATTERN.md for duplicates
   d. Record result: PASS (with abstracted principle) or REJECT (with reason)
4. **Effectiveness signal:** Cross-reference with session logs — did anti-patterns recur AFTER documentation?
   - Recurrence where AP was checked = **enforcement gap** (high-priority signal for parent `/meta-evolve`)
   - Recurrence where AP was not checked = **compliance gap** (lower priority, existing hooks should handle)

### Phase 3: Skill Extraction

Extract procedural intelligence from `commands/*.md`.

1. List all skills with their modification history:
   ```bash
   for f in .claude/commands/*.md; do
     echo "=== $f ==="; git log --oneline -- "$f"; echo
   done
   ```
2. **Prioritize by evolution depth:** Focus on skills with 3+ commits (refined under real usage). Skills with only 1 commit (created, never updated) have low evidence.
3. For each skill:
   - **Meta-skills** (prefix `meta-`): Compare directly against parent's `commands/` directory. If the child invented a meta-skill the parent lacks, this is high-value — a potentially novel cognitive pattern.
   - **Domain skills:** Apply the abstraction algorithm:
     a. Read the `## Procedure` section
     b. Identify domain nouns vs. structural steps
     c. Strip domain nouns, retain the relational structure
     d. Apply Gate 1 (three-substitution test) on the abstracted procedure
     e. If passes: classify via Gate 4 (Path A: new skill, Path B: deepen existing, Path C: new meta-skill)
4. Read changelog lines at the bottom of each skill file — these embed pre-distilled reasoning about what drove each refinement.

### Phase 4: Semantic Extraction

Extract principles from `MEMORY.md`.

1. Read current `MEMORY.md` and get its evolution:
   ```bash
   git log --follow -p -- ".claude/memory/MEMORY.md"
   ```
2. **Project Insights:** For each insight, apply Gate 1 (three-substitution test). Domain-specific architectural facts fail; process principles pass.
3. **Debugging Solutions:** Extract symptom → cause patterns (transferable). Discard specific tool/command solutions (environment-specific).
4. **User Preferences:** Skip entirely — person-specific, never transferable.
5. **Skill candidates** (`skill-candidates.md`): Check for patterns that passed the "reusable, non-trivial, focused, proven" test but weren't promoted — these may be transferable.

### Phase 5: Session Log Behavioral Analysis

Extract effectiveness signals from session logs (ground-truth layer).

1. Check if session logs exist:
   ```bash
   ls .claude/memory/sessions/session-log-*.md
   ```
2. If logs exist, read all of them and analyze:
   - **Governance compliance columns:** Which meta-skills are consistently skipped?
     - Consistent skipping = friction signal. Feed back into parent `/meta-evolve` evaluation (the meta-skill may need simplification in the parent template).
   - **Correction clusters:** User corrections not yet in ANTI_PATTERN.md = uncodified failure modes. Extract and process through Phase 2 algorithm.
   - **Skill usage patterns:** Skills created but never invoked = design failures. Skills invoked in every session = core patterns worth absorbing.
3. If no session logs exist: note as "no behavioral data available" in report.

### Phase 6: Synthesize — Produce Absorption Report

Compile all findings into a structured report. Do NOT apply any changes.

1. **Generate the Absorption Report:**

```
## Absorption Report: <repo-name> (<date>)

### Signal Quality
- Governance commits: N | Session logs: N entries | Skills: N total (N evolved)
- Signal level: LOW / MODERATE / HIGH

### Anti-Pattern Candidates
| # | Abstracted Principle | Pillar | Existing Coverage | Action |
|---|---------------------|--------|-------------------|--------|
| 1 | ... | Learning | None — gap | Propose via /meta-evolve |
| 2 | ... | Motivation | Already implied by /meta-motivation step 2 | Add evidence weight |

### Skill Gap Candidates
| # | Abstracted Procedure | Path | Commits in Child | Action |
|---|---------------------|------|------------------|--------|
| 1 | ... | A (new skill) | 5 | Propose via /meta-propose-skill |
| 2 | ... | B (deepen existing) | 3 | Propose procedure extension |

### Semantic Insight Candidates
| # | Abstracted Insight | Pillar | Substitution Test | Action |
|---|-------------------|--------|-------------------|--------|
| 1 | ... | Learning | PASS (3/3 domains) | Propose for MEMORY.md |

### Framework Friction Signals
| Meta-skill | Skip Rate | Sessions Analyzed | Possible Cause |
|-----------|-----------|-------------------|----------------|
| /meta-motivation | 60% | 20 | Too verbose for quick tasks? |

### Filter Decisions (Rejected)
| Candidate | Gate Failed | Reason |
|-----------|------------|--------|
| "Check patient allergies before..." | Gate 1 | Failed in software/legal domains |

### Proposed Actions (ordered by signal strength)
1. [strongest evidence first]
```

2. **Record in `absorbed-intelligence.md`:**
   - Append absorption log entry (repo name, date, signal quality, counts)
   - Update cross-repo patterns if this principle was also seen in a previous absorption
   - Record filter decisions (what was rejected and why — prevents re-evaluating the same patterns)

3. **Present to user.** All proposed actions require explicit human approval via the existing governance mechanisms.

## Session Tracking

Update the session tracker:
```bash
jq '.cross_repo_absorbed = true' "$TRACKER" > "$TRACKER.tmp" && mv "$TRACKER.tmp" "$TRACKER"
```

## What This Skill Cannot Do

- **Apply changes directly** to parent framework files (output is a report)
- **Bypass `/meta-evolve`** or `/meta-propose-skill` approval gates
- **Absorb domain-specific content** without abstraction (Gate 1 prevents this)
- **Modify `CLAUDE.md`** or `cognitive-architecture.md` autonomously

---
*Created: 2026-03-24 | Source: Cross-repo intelligence integration for parent framework evolution*
