# Meta-Commit — Leverage Git Commit as a Learning Signal

**Triggers:** When the user says `/meta-commit` or asks to commit with learning.

> **Core idea:** A git commit is a natural checkpoint — the work is done, the intent is clear. `/meta-commit` leverages this signal to trigger the agent's reflection loop, capturing knowledge alongside code in one atomic unit. Every commit becomes a learning opportunity.
>
> **Not the same as built-in commit.** The built-in commit just stages and commits. `/meta-commit` adds a reflection phase first — the commit is the signal, learning is the payload.

## Flow

```
/meta-commit
├── Phase 1: Reflect (meta-learn over current session)
│   ├── Skill opportunity?   → propose to user, create if approved
│   ├── Anti-pattern found?  → add to ANTI_PATTERN.md
│   ├── Memory update?       → update MEMORY.md
│   └── Skill evolution?     → propose improvement, edit if approved
├── Phase 2: Commit & Push (code + knowledge together)
│   ├── Stage code changes
│   ├── Stage .claude/ artifacts from Phase 1
│   ├── Draft commit message (conventional format)
│   ├── Execute commit
│   └── Push to remote
└── Phase 3: Confirm
    └── Show commit + push result + summarize what was learned
```

## Phase 1: Reflect

Run the meta-learn reflection over the current session's work.

1. **Review what was done** — Scan the conversation for tasks completed since last commit.
2. **Skill opportunity** — Did a reusable multi-step pattern emerge?
   - If yes and it passes the threshold → propose to user now
   - If approved → create the skill file before committing
3. **Anti-pattern** — Did the user correct the agent's approach?
   - If yes → add to `ANTI_PATTERN.md` before committing
4. **Memory update** — Check each MEMORY.md category:
   - Project insight learned? → add one-liner to "Project Insights"
   - Debugging solution found? → add to "Debugging Solutions" (symptom → cause → fix)
   - User preference expressed? → record in "User Preferences"
5. **Skill evolution** — Did an existing skill prove incomplete or outdated?
   - If yes → propose the improvement, edit if approved

**If nothing was learned** (trivial changes, simple fixes), skip to Phase 1.5 without forcing insights.

## Phase 1.5: Session Metrics Review

Before committing, review the session governance tracker to assess compliance:

1. **Read the tracker** — Find the session tracker at `/tmp/claude-governance-*.json` (most recent file).
2. **Report governance compliance:**
   - Anti-patterns checked? (`anti_patterns_checked`)
   - Scope declared? (`scope_declared`)
   - Learning reflected? (`learning_reflected`)
   - Total edits made and files touched
3. **Catch-up** — If any mandatory step was skipped, run it now before proceeding.
4. **Append to session log** — Add a row to `.claude/memory/sessions/session-log-{git_user}.md`:
   ```
   | YYYY-MM-DD | edits | file-count | yes/no | yes/no | yes/no | N | brief note |
   ```
   The `git_user` field is in the session tracker (set by `session-init.sh`).
   If the user's session-log file doesn't exist, create it with the header row first.
5. **Stage the session log** — Include the user's session-log file in the commit.

## Phase 2: Commit & Push

Follow project git conventions (CLAUDE.md §Git Commits):

1. **`git status`** — Review all changes (code + .claude/ artifacts).
2. **`git diff`** — Understand the full scope of what's being committed.
3. **`git log --oneline -5`** — Match the repository's commit message style.
4. **Stage files by name** — Include:
   - The user's code changes
   - Any `.claude/` files modified in Phase 1 (memory, anti-patterns, skills)
   - Do NOT stage `.claude/settings.local.json` unless explicitly requested
5. **Draft commit message** — Conventional format:
   - Title: `feat:` / `fix:` / `refactor:` / `docs:` / `test:` for the primary change
   - Body: if Phase 1 produced knowledge artifacts, note briefly what was captured
   - Footer: `Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>`
6. **Commit** — Use HEREDOC format for multi-line messages.
7. **Push** — `git push` to the remote. If the branch has no upstream, use `git push -u origin <branch>`.

## Phase 3: Confirm

After commit and push succeed:
- Show commit hash and message
- Show push result (remote URL, branch)
- If Phase 1 captured anything, summarize: "Learned: [new skill / anti-pattern / memory update]"
- Run `git status` to confirm clean state

## $ARGUMENTS

If `$ARGUMENTS` is provided, use it as the commit message title (skip drafting). Phase 1 reflection still runs regardless.

---
*Created: 2026-02-19 | Source: user request — commit as the agent's learning checkpoint*