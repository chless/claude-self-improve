# Meta-Integrate — Child Repo Intelligence Integration

**Triggers:** Explicitly invoked via `/meta-integrate`, or suggested by `/meta-self-audit` when registered children have not been reviewed recently. This meta-skill enables the parent framework to absorb **generalizable governance improvements** discovered by specialized child AI instances — without absorbing domain-specific content.

> **Core principle:** Children grow deep in their domains. The parent grows wide by extracting structural and procedural improvements that help *any* domain. Domain content (health advice, language patterns, etc.) is explicitly excluded — absorbing it would harm adaptability to other purposes.

## Prerequisites

- At least one child repo must be registered via `claude-self-improve register <path-or-url>`
- Child repos must use the `claude-self-improve` governance framework (they must have a `.claude/` directory)
- Registry is stored in `.claude/memory/children.json`

## Procedure

### Step 1: Load Registry

Read `.claude/memory/children.json`. For each registered child:
- Verify the child path still exists and has a `.claude/` directory
- For remote children (`source: "remote"`): run `git -C <path> pull origin` to fetch the latest changes
- Report any stale registrations (path no longer exists)

### Step 2: Browse Child Git History

For each child, examine only governance-related changes:

```bash
# Governance commits since last integration
git -C <child_path> log --oneline --since="<last_integrated_date>" -- .claude/

# Detailed view of what changed in governance files
git -C <child_path> log --stat --since="<last_integrated_date>" -- .claude/
```

If `last_integrated` is null (first integration), use the last 50 commits or all commits touching `.claude/`.

**Focus exclusively on commits that modify `.claude/` files.** Ignore all other commits — they contain domain-specific code changes.

### Step 3: Read Child Governance Artifacts

For each child, read the current state of these governance files:

| File | What to extract |
|------|----------------|
| `.claude/memory/ANTI_PATTERN.md` | **Structural format** only: new fields, tag vocabulary, severity levels, format improvements. NOT the actual anti-pattern entries (those are domain mistakes). |
| `.claude/memory/MEMORY.md` | Section organization, meta-skill registry structure, new section types. NOT project insights, debugging solutions, or user preferences content. |
| `.claude/commands/meta-*.md` | Procedure modifications: added/removed/reordered steps, new checks, improved triggers. These are meta-cognitive improvements. |
| `.claude/settings.json` | Hook configuration changes: new hooks, modified matchers, timeout adjustments. NOT file-path matchers specific to the child's domain. |
| `.claude/hooks/*.sh` | Hook script logic improvements: better error handling, smarter checks, new governance signals. |
| `.claude/memory/sessions/` | Quantitative patterns only: compliance rates, correction frequency trends. NOT qualitative session content. |

### Step 4: Diff Against Original Templates

Compare each child's current `.claude/` files against the original templates shipped by `claude-self-improve`:

```bash
# Get the original template version for comparison
# The templates are in the claude-self-improve package installation
diff <child_path>/.claude/commands/meta-learn.md <original_template>/commands/meta-learn.md
```

Changes from the original template represent what the child **evolved independently** through actual usage. These are candidates for integration.

### Step 5: Generality Filter (CRITICAL)

Each candidate must pass ALL THREE filters. This is the most important step — getting it wrong would absorb domain content and harm the parent's adaptability.

#### Filter 1 — Domain Content Exclusion (Allowlist)

Use an **allowlist** approach (safer than blocklist — we specify what IS generalizable rather than trying to detect every possible domain):

| ALLOW (Generalizable) | REJECT (Domain-Specific) |
|------------------------|--------------------------|
| Anti-pattern **format** changes (new fields, tag vocabulary, severity levels) | Anti-pattern **entries** (the actual mistakes — these are domain-specific) |
| Meta-skill procedure step additions/reorderings/refinements | Domain skill procedures (non-`meta-*` commands) |
| Hook script **logic** improvements (governance checks, error handling) | Hook **matchers** specific to domain file types (e.g., `.csv` for data, `.wav` for audio) |
| Memory **section structure** improvements (new section types, better organization) | Memory **content** (project insights, debugging solutions, user preferences) |
| Session log **format** improvements | Session log **content** |
| `settings.json` hook **configuration patterns** | `settings.json` **paths** specific to a project |
| New `meta-*` commands (meta-cognitive skills) | New domain skills (non-`meta-*` commands) |
| Skill maturity **lifecycle** improvements | Specific skill **registry entries** |

#### Filter 2 — Cross-Domain Applicability

For each candidate that passes Filter 1, apply this mental test:

> "Would this improvement help a repo working on a **completely unrelated** domain?"

- If the answer is **yes regardless of domain** → KEEP
- If the answer **depends on what the repo does** → REJECT

Example passes: "Added a 'Severity: high|medium|low' field to anti-pattern format" → helps any repo.
Example fails: "Added a 'Patient Safety' tag to anti-pattern categories" → health-domain specific.

#### Filter 3 — Evidence Threshold

The candidate must have evidence of effectiveness:

- **Strong evidence:** Child's session logs show fewer corrections or better compliance after the change was introduced
- **Moderate evidence:** The change has been in place for 5+ sessions without being reverted
- **Weak evidence:** Recently added, insufficient data → flag as "promising but unproven"
- **No evidence:** Purely cosmetic change with no behavioral impact → downgrade to low priority

### Step 6: Detect Convergent Evolution

**This is the strongest generality signal.** If 2+ children independently evolved similar improvements (without knowledge of each other), it is almost certainly generalizable.

For each candidate that passes the three filters:
1. Check if other children made a similar change
2. If yes → boost generality confidence to **high**
3. Record which children converged and the specific changes

Convergent evolution examples:
- Two children both added a "pre-check" step to `meta-learn.md`
- Three children all restructured MEMORY.md to split "Project Insights" into subcategories
- Two children both modified `stop-reflection-gate.sh` to also verify scope compliance

### Step 7: Generate Proposals

For each candidate that passes all filters, produce a structured proposal:

```
### Proposal N: [Brief title]

**Classification:** cosmetic | procedural | structural
**Source:** child "<alias>" (commit <sha>, date)
**Generality confidence:** high | medium | low
**Convergent:** Yes (children: X, Y) | No (single source)
**Evidence:** [Strong/Moderate/Weak] — [brief evidence summary]

**Before (current parent template):**
```
[exact text from parent template]
```

**After (proposed change):**
```
[proposed new text]
```

**Rationale:** [Why this improves the parent framework for all future children]
**Risk:** [Could this break existing child repos or workflows?]
```

### Step 8: Approval Gate

**CRITICAL: ALL integration proposals require explicit user approval.**

- Present each proposal individually
- Wait for explicit confirmation ("yes", "approved", "do it") before applying
- If the user rejects a proposal, record the rejection reason in the integration log
- Never batch-apply multiple proposals without individual approval
- The user may request modifications to a proposal before approving

### Step 9: Apply and Record

After approval for each proposal:

1. **Apply the change** to the parent's template files in the repository
2. **Add a changelog entry** at the bottom of the modified template file:
   ```
   *Updated: YYYY-MM-DD | Change: [description] | Source: child-intelligence from <alias(es)>*
   ```
3. **Update `children.json`:**
   - Set `last_integrated` to today's date for each reviewed child
   - Set `last_integrated_commit` to the child's current HEAD commit SHA
   - Append to `integration_log`:
     ```json
     {
       "date": "YYYY-MM-DD",
       "children_reviewed": ["alias1", "alias2"],
       "proposals_generated": N,
       "proposals_accepted": M,
       "proposals_rejected": K
     }
     ```
4. **Update MEMORY.md** "Child Repo Intelligence" table with integration results

## When NOT to Run

- No children are registered (nothing to integrate)
- All children were integrated within the last 7 days and have no new `.claude/` commits
- The parent is in the middle of a complex task (integration is a reflective activity, not a mid-task activity)

## Anti-Patterns for This Skill

- **Absorbing domain content:** The most dangerous failure. If in doubt, reject the candidate.
- **Over-integrating:** Not every child change is worth integrating. Quality over quantity.
- **Ignoring evidence:** A clever-sounding improvement with no evidence is less valuable than a simple improvement with strong evidence.
- **Skipping the approval gate:** Never auto-apply. The human must approve each change.

---
*Created: 2026-03-21 | Source: parent-child intelligence integration — governance improvement propagation*
