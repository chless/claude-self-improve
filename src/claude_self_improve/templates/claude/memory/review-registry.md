# Review & Injection Registry

Tracks intelligence exchanges between stateful repos. Each review or injection
is a git-tracked record with full provenance (repo URL, branch, commit hash).

## How to Use

1. `/meta-intelligence-review` appends entries after giving or processing reviews
2. `/meta-intelligence-inject` appends entries after injecting knowledge
3. `/meta-self-audit` reads this to check multi-perspective synthesis status
4. Review and injection files live in `reviews/` — this registry indexes them

## Reviews Received

<!-- Format:
| Date | Reviewer Repo | Branch | Commit | File | Processed? |
|------|--------------|--------|--------|------|------------|
-->

## Reviews Given

<!-- Format:
| Date | Reviewee Repo | Branch | Commit | File | Synthesis Done? |
|------|--------------|--------|--------|------|-----------------|
-->

## Injections Sent

<!-- Format:
| Date | Target Repo | Knowledge Summary | Source Commit | File |
|------|------------|-------------------|---------------|------|
-->

## Injections Received

<!-- Format:
| Date | Source Repo | Knowledge Summary | Source Commit | File | Integrated? |
|------|-----------|-------------------|---------------|------|-------------|
-->

## Multi-Perspective Synthesis Log

<!-- After processing 2+ reviews, record synthesis results here:

### Synthesis: <date>
- **Reviews considered:** N from [list of reviewer repos]
- **Convergent observations:** [what multiple reviewers independently noted]
- **Divergent observations:** [contradictions between perspectives]
- **Actions taken:** [proposals made through /meta-evolve or /meta-propose-skill]
-->
