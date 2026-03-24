# Intelligence Review — Peer Review Between Stateful Intelligences

**Triggers:** When this intelligence reviews another repo, or when processing incoming reviews left by peer/child repos. Invoked as `/meta-intelligence-review give <path-or-url>` or `/meta-intelligence-review process [<repo-url> <branch>]`.

> **Core principle:** Git repos are stateful intelligences — each grows through commits, and branches are different growth paths. The gap between humans and AIs is statefulness; git bridges it. Peer review between stateful intelligences enables multi-perspective synthesis: comprehensively considering different viewpoints is more valuable than any single perspective. Every review carries full provenance (repo, branch, commit) so the receiving intelligence can trace perspectives back to their source context.

## Two Modes

### Mode A: Give Review

This intelligence reviews another. The review is committed to the reviewee's designated path with full provenance.

#### Phase 1: Reviewer Self-Identification

Establish this repo's identity as a reviewer — its "perspective credentials."

1. **Repo URL:**
   ```bash
   git remote get-url origin 2>/dev/null || echo "local-only"
   ```
2. **Current branch:**
   ```bash
   git branch --show-current
   ```
3. **Current commit:**
   ```bash
   git rev-parse HEAD
   ```
4. **Domain description:** Read this repo's `CLAUDE.md` Project Overview and `MEMORY.md` Project Insights. Summarize this intelligence's domain and perspective in 2-3 sentences.
5. **Assemble perspective credentials:**
   ```
   Reviewer: <repo URL>
   Branch: <branch>
   Commit: <hash>
   Domain: <summary>
   Access: git clone <url> && git checkout <hash>
   ```

#### Phase 2: Deep-Read Reviewee

Read the target repo's `.claude/` structure to understand its intelligence, and capture the reviewee's provenance.

1. Access the target repo (local path or clone from URL)
2. **Capture reviewee identity** (in the reviewee's repo):
   ```bash
   REVIEWEE_URL=$(git remote get-url origin 2>/dev/null || echo "local-only")
   REVIEWEE_BRANCH=$(git branch --show-current)
   REVIEWEE_COMMIT=$(git rev-parse HEAD)
   ```
   Assemble reviewee credentials alongside reviewer credentials — both are recorded in the Review Record.
3. Read these files (in order of priority):
   - `CLAUDE.md` — governance conventions, three-pillar structure
   - `memory/MEMORY.md` — what it has learned, project insights
   - `memory/ANTI_PATTERN.md` — its discovered failure modes
   - `memory/cognitive-architecture.md` — its intelligence design
   - `commands/*.md` — its skills and meta-skills
   - `memory/sessions/session-log-*.md` — its behavioral ground truth
4. Assess evolution trajectory:
   ```bash
   git log --oneline --all -- ".claude/" | wc -l
   git log --stat --all -- ".claude/"
   ```
5. Note: fewer than 5 governance commits means low signal — note this in the review.

#### Phase 3: Perspective-Grounded Review

Review through this intelligence's specific lens. Every observation should be grounded in what THIS reviewer uniquely sees because of its domain experience.

**Strengths** — What the reviewee does well, recognized because this reviewer has experience in a related area:
- Which governance patterns are well-evolved?
- Which anti-patterns show real learning from failure?
- Which skills demonstrate refinement under usage?

**Gaps** — What this reviewer sees as missing, visible because of its own perspective:
- What failure modes does this reviewer know about that the reviewee hasn't documented?
- What governance patterns has this reviewer evolved that the reviewee lacks?
- What learning or memory mechanisms are underdeveloped?

**Opportunities** — Patterns this reviewer has encountered in its domain that could transfer:
- Skills or procedures that would benefit the reviewee (after domain abstraction)
- Anti-patterns from this reviewer's domain that generalize
- Architectural improvements this reviewer has made that the reviewee could adopt

**Source Context** — For each observation, cite the specific commit(s) in this reviewer's repo that inform it:
```
Observation: [description]
Source: <this-repo>@<commit-hash> — <file>:<line-range>
Reasoning: [why this commit/code informs the observation]
```

#### Phase 4: Write Review Record

1. **Write the review** to the reviewee's designated path:
   - File: `<reviewee>/.claude/memory/reviews/<reviewer-name>-<date>.md`
   - Use the Review Record Format below
2. **Update the reviewee's registry** (if accessible):
   - Append to `<reviewee>/.claude/memory/review-registry.md` under "Reviews Received"
3. **Update this repo's registry:**
   - Append to `.claude/memory/review-registry.md` under "Reviews Given"
4. **Session tracking:**
   ```bash
   jq '.intelligence_review_given = true' "$TRACKER" > "$TRACKER.tmp" && mv "$TRACKER.tmp" "$TRACKER"
   ```

---

### Mode B: Process Incoming Reviews

This intelligence processes reviews left by others — either locally in `.claude/memory/reviews/`, or from another repo's branches.

**Invocation:**
- `/meta-intelligence-review process` — local reviews only (default)
- `/meta-intelligence-review process <repo-url> <branch>` — also fetch reviews from a remote repo/branch

#### Phase 1: Read All Pending Reviews

**Local reviews:**
1. List review files:
   ```bash
   ls .claude/memory/reviews/*.md 2>/dev/null
   ```
2. Check `review-registry.md` — identify which reviews have not yet been processed (no "Processed" mark).
3. Read all unprocessed review files.

**Remote reviews** (when repo-url and branch are provided):
1. Clone the remote repo at the specified branch (shallow, temporary):
   ```bash
   git clone --depth 1 --branch <branch> <repo-url> /tmp/remote-reviews-$(date +%s)
   ```
2. List review files in the remote repo:
   ```bash
   ls /tmp/remote-reviews-*/.claude/memory/reviews/*.md 2>/dev/null
   ```
3. **Filter:** Only process reviews where the Reviewee Identity section matches THIS repo (by URL or repo name). Ignore reviews addressed to other repos.
4. Copy matching reviews to local `.claude/memory/reviews/` (with `remote-` prefix to distinguish origin).
5. Clean up:
   ```bash
   rm -rf /tmp/remote-reviews-*
   ```
6. Add the copied reviews to the unprocessed list alongside local reviews.

This enables processing reviews from any repo's branches — not just reviews committed directly to this repo.

#### Phase 2: Verify Provenance (Both Sides)

For each review:
1. Note the reviewer's repo URL, branch, and commit hash from the review's "Reviewer Identity" section.
2. Note the reviewee's repo URL, branch, and commit hash from the review's "Reviewee Identity" section.
   - Verify that the reviewee identity matches this repo's current or historical state. If the commit is old, the review was made against an earlier version — flag observations that may no longer apply.
3. These are the "perspective credentials" for both sides — the exact state of both intelligences when the review was made.
4. If deeper understanding of a specific observation is needed, the user can fetch the reviewer's repo at the cited commit:
   ```bash
   git clone <reviewer-url> /tmp/reviewer-context
   cd /tmp/reviewer-context && git checkout <commit-hash>
   # Now read the specific files cited in the review's Source Context
   ```
5. For now, work with the review text. Flag observations that would benefit from source context verification.

#### Phase 3: Multi-Perspective Synthesis

When 2+ reviews exist, synthesis becomes more valuable than any individual review.

1. **Convergent observations** — What multiple reviewers independently noted:
   - These are the strongest signals. Independent discovery across different perspectives suggests a real pattern, not a perspective artifact.
   - Weight these highest in integration proposals.

2. **Divergent observations** — Contradictions between perspectives:
   - These are valuable, not problematic. Different domains may legitimately see the same thing differently.
   - Record both perspectives. The contradiction itself is an insight — it reveals where domain context matters.

3. **Absence patterns** — What NO reviewer noticed:
   - Harder to detect, but if all reviewers share a blind spot, this intelligence likely shares it too.
   - Cross-reference with this repo's own ANTI_PATTERN.md — does any failure mode correlate with the shared blind spot?

4. **Synthesis record:**
   ```
   ## Synthesis: <date>
   - Reviews considered: N from [list of reviewer repos]
   - Convergent: [observations noted by 2+ reviewers]
   - Divergent: [contradictions between perspectives]
   - Absence: [potential blind spots]
   ```

#### Phase 4: Integration Proposals

Route synthesized insights through existing governance — do NOT auto-apply.

| Insight Type | Route To | Mechanism |
|-------------|----------|-----------|
| New anti-patterns | `ANTI_PATTERN.md` | `/meta-evolve` proposal |
| New skills | `commands/` | `/meta-propose-skill` (Path A/B/C) |
| Semantic insights | `MEMORY.md` | `/meta-evolve` proposal |
| Framework friction | Governance files | `/meta-evolve` evaluation |
| Architecture improvements | `cognitive-architecture.md` | `/meta-evolve` proposal |

Before presenting proposals, evaluate each through `/meta-inner-self` — form this intelligence's own position on whether the proposal improves its governance. Present all proposals to the user with this intelligence's own assessment. The human decides what integrates.

#### Phase 5: Update Registry

1. Mark each processed review in `review-registry.md` (set Processed = Yes)
2. Append synthesis record to `review-registry.md` under "Multi-Perspective Synthesis Log"
3. **Session tracking:**
   ```bash
   jq '.intelligence_review_processed = true' "$TRACKER" > "$TRACKER.tmp" && mv "$TRACKER.tmp" "$TRACKER"
   ```

---

## Review Record Format

```markdown
# Intelligence Review: <reviewee-repo>

## Reviewer Identity
- **Repo:** <git remote URL>
- **Branch:** <branch at time of review>
- **Commit:** <hash at time of review>
- **Domain:** <what this intelligence specializes in — 2-3 sentences>
- **Access:** `git clone <url> && git checkout <commit>` for full source context

## Reviewee Identity
- **Repo:** <git remote URL>
- **Branch:** <branch at time of review>
- **Commit:** <hash at time of review>
- **Domain:** <reviewee's specialization from its CLAUDE.md — 2-3 sentences>
- **Access:** `git clone <url> && git checkout <commit>` for exact state reviewed

## Review Date
<YYYY-MM-DD>

## Perspective
<What this reviewer's domain experience uniquely brings — why its viewpoint matters>

## Observations

### Strengths (from this perspective)
- ...

### Gaps (from this perspective)
- ...

### Opportunities (patterns seen elsewhere that could transfer)
- ...

## Recommended Changes
<Each with rationale grounded in reviewer's experience>

## Source Context
<Specific commits in reviewer's repo that inform observations — so reviewee can trace back>
| Observation | Source Commit | File | Reasoning |
|-------------|-------------|------|-----------|
| ... | <hash> | <file>:<lines> | ... |
```

## What This Skill Cannot Do

- **Auto-apply review findings** to governance files (output is proposals, routed through `/meta-evolve`)
- **Bypass the human approval gate** — all integration requires explicit approval
- **Fabricate reviewer identity** — provenance must be real, verifiable git state
- **Replace `/meta-absorb-repo`** — absorption is bulk intelligence extraction; review is perspective-grounded evaluation

---
*Created: 2026-03-24 | Source: Stateful intelligence network — multi-perspective peer review*
