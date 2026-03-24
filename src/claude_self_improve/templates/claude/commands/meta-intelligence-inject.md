# Intelligence Injection — Push Knowledge Between Stateful Intelligences

**Triggers:** When this intelligence has knowledge another stateful repo should have. Invoked as `/meta-intelligence-inject <target-path-or-url>`.

> **Core principle:** Intelligence flows between stateful repos in two directions: pull (absorption, review processing) and push (injection). Injection is the active side — "here is what I know that you should have." Every injection carries full provenance so the receiving intelligence can trace knowledge to its source, verify it, and integrate it through its own governance.

## Procedure

### Phase 1: Identify What to Inject

Determine what this intelligence has discovered that the target should have.

**Categories of injectable knowledge:**

| Category | Description | Example |
|----------|-------------|---------|
| Anti-patterns | Failure modes learned in this domain that may apply broadly | "Scope creep through implicit requirements" |
| Skills | Procedural knowledge that would benefit the target | A refined testing procedure |
| Semantic insights | Principles about the problem space | "Governance hooks must be idempotent" |
| Architectural observations | Perspective on the target's governance structure | "Your session tracking misses X" |
| Cross-repo patterns | Patterns seen across multiple repos (strongest signal) | "Three child repos independently discovered Y" |

1. Read this repo's `.claude/memory/MEMORY.md` — identify insights marked as potentially transferable
2. Read this repo's `.claude/memory/ANTI_PATTERN.md` — identify patterns that generalize
3. Read this repo's `.claude/commands/` — identify skills that could benefit the target
4. Read this repo's `.claude/memory/review-registry.md` — check for cross-repo patterns from previous reviews
5. Select what to inject. Quality over quantity — one well-evidenced principle is more valuable than ten weak ones.

### Phase 2: Package with Provenance

Every injection must carry full attribution so the receiving intelligence can verify and trace it.

1. **Source identity:**
   ```bash
   REPO_URL=$(git remote get-url origin 2>/dev/null || echo "local-only")
   BRANCH=$(git branch --show-current)
   COMMIT=$(git rev-parse HEAD)
   ```

2. **Source context** — the specific files and code in this repo that gave rise to the knowledge:
   - Which file(s) contain the pattern?
   - Which commit(s) refined it?
   - What session log entries show it in action?
   ```bash
   # Find commits that evolved the relevant file
   git log --oneline -- "<relevant-file>"
   ```

3. **Rationale** — why this intelligence believes the target should have this:
   - What problem does this solve for the target?
   - What evidence supports this (session count, failure frequency, cross-repo appearance)?

4. **Abstraction level** — classify the knowledge:
   - **Domain-specific:** The target should adapt this to its domain (apply generality filter)
   - **Domain-agnostic:** Direct transfer — the principle holds as-is
   - **Framework-level:** Affects the governance system itself (highest bar for acceptance)

### Phase 3: Apply Generality Filter

The injection's abstraction level determines which filter to apply.

**Injecting into parent framework → full four-gate filter required:**
Use the same filter as `/meta-absorb-repo`:
1. Three-substitution test — strip domain nouns, test across three unrelated domains
2. Pillar ownership — must map to Motivation/Learning/Memory
3. Existing coverage check — is this already in the parent?
4. Source layer routing — which approval mechanism?

**Injecting into a peer (same-level) repo → lighter filter:**
- Gate 1 (three-substitution) still applies — ensure it's not hyper-specific
- Gate 2 (pillar ownership) still applies
- Gate 3 relaxed — domain-related knowledge may be valuable to a related domain
- Gate 4 still applies — proper routing

**Injecting into a child repo → no generality filter:**
- Parent→child is specialization, not generalization
- The child's governance will absorb or reject based on its own needs
- Still package with provenance (the child benefits from knowing the source)

### Phase 4: Write Injection Record

Commit the injection to the target's designated path.

1. **Write the injection file:**
   - File: `<target>/.claude/memory/reviews/<source-name>-inject-<date>.md`
   - Uses the same `reviews/` directory as peer reviews (injections are a form of directed review)
   - Use the Injection Record Format below

2. **Update the target's registry** (if accessible):
   - Append to `<target>/.claude/memory/review-registry.md` under "Injections Received"

3. **Recommended integration path** — tell the target HOW to integrate:
   - Which file should change?
   - Which section?
   - What existing governance mechanisms should process this?

### Phase 5: Record in Source

Update this repo's records.

1. Append to `.claude/memory/review-registry.md` under "Injections Sent"
2. **Session tracking:**
   ```bash
   jq '.intelligence_injected = true' "$TRACKER" > "$TRACKER.tmp" && mv "$TRACKER.tmp" "$TRACKER"
   ```

---

## Injection Record Format

```markdown
# Intelligence Injection: <source-repo> → <target-repo>

## Source Identity
- **Repo:** <git remote URL>
- **Branch:** <branch>
- **Commit:** <hash>
- **Domain:** <what this intelligence specializes in>
- **Access:** `git clone <url> && git checkout <commit>` for full source context

## Injection Date
<YYYY-MM-DD>

## Knowledge

### What is being injected
<The principle, anti-pattern, skill, or insight — clearly stated>

### Source context
<Specific files and commits in source repo that gave rise to this knowledge>
| File | Commit | What it shows |
|------|--------|---------------|
| ... | <hash> | ... |

### Abstraction level
<domain-specific / domain-agnostic / framework-level>

### Evidence strength
<How many sessions, failures, or repos support this? Cross-repo > single-repo > single-session>

### Rationale
<Why the source believes the target should have this>

## Generality Filter Result
<Which gates were applied and their outcomes>

## Recommended Integration
<How the target should integrate — which file, which section, which approval mechanism>
```

## What This Skill Cannot Do

- **Force integration** on the target — the target's governance decides what enters (the receiving intelligence evaluates injections through `/meta-inner-self` before integrating)
- **Bypass provenance** — every injection must carry verifiable source identity
- **Skip the generality filter** when injecting into the parent framework
- **Replace `/meta-absorb-repo`** — absorption is bulk extraction; injection is targeted push

---
*Created: 2026-03-24 | Source: Stateful intelligence network — knowledge push between repos*
