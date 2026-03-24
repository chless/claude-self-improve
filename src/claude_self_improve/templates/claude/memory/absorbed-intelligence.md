# Absorbed Intelligence — Cross-Repo Knowledge Integration

This file is part of the **semantic layer** of the memory hierarchy. It tracks
intelligence extracted from child repository deployments via `/meta-absorb-repo`.

## How to Use

1. **After each absorption:** `/meta-absorb-repo` appends an entry to the Absorption Log
2. **During self-audit:** `/meta-self-audit` reads this file to check whether absorbed principles are effective in practice
3. **Cross-repo patterns:** Principles appearing in 2+ child repos are prime candidates for parent framework hardening
4. **Filter decisions:** Rejected candidates are recorded to prevent re-evaluation of already-assessed patterns

---

## Absorption Log

<!-- Each absorption adds a section with the format below:

### <repo-name> — <YYYY-MM-DD>
- **Signal quality:** N governance commits, N session log entries
- **Signal level:** LOW / MODERATE / HIGH
- **Absorbed:** N anti-patterns, N skills, N insights
- **Filtered:** N candidates rejected (domain-specific)
- **Cross-repo hits:** [principles also seen in previous absorptions]
- **Actions taken:** [list of /meta-evolve and /meta-propose-skill proposals made]

-->

---

## Cross-Repo Patterns

Principles that appeared in 2+ child repos. These have the strongest evidence
for inclusion in the parent framework because multiple independent deployments
discovered the same lesson.

<!-- Format:

### [Abstracted Principle]
- **Pillar:** Motivation / Learning / Memory
- **Seen in:** repo-1 (date), repo-2 (date), ...
- **Evidence strength:** N independent discoveries
- **Status:** proposed / integrated / monitoring
- **Parent location:** [where in parent framework this was integrated, if applicable]

-->

---

## Filter Decisions

Candidates that were evaluated and rejected. Recording these prevents
re-evaluating the same patterns when absorbing from related repos.

<!-- Format:

### [Candidate description]
- **Source:** repo-name (date)
- **Gate failed:** 1 (substitution) / 2 (pillar) / 3 (coverage) / 4 (routing)
- **Reason:** [why it failed the gate]

-->
