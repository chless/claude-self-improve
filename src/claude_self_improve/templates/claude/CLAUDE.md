# AI Agent Conventions

This document defines conventions that AI agents (Claude, Copilot, etc.)
must follow when contributing to this project. The entire governance system
is organized under **three pillars of human-level intelligence** — everything
the agent does maps to one of them.

> **IMPORTANT: Before making any edits to this codebase, you MUST read
> [ANTI_PATTERN.md](memory/ANTI_PATTERN.md).** This file contains documented
> error patterns from previous agent interactions that must not be repeated.

## Project Overview

<!-- TODO: Describe your project in 1-2 sentences. -->

## Project Structure

<!-- TODO: Paste your project's directory tree here. -->

---

## The Three Pillars

An intelligence that acts like a human being has three reinforcing systems.
See `memory/cognitive-architecture.md` for the full design.

```
  MOTIVATION          LEARNING           MEMORY
  (why)               (how)              (what)
  ────────            ────────           ────────
  Goal formation      Assess before      Episodic layer
  Self-evaluation     Monitor during     Semantic layer
  Scope discipline    Reflect after      Procedural layer
  Quality pursuit     Pattern transfer   Consolidation
```

**The pillars reinforce each other:** Motivation drives the agent to learn
actively. Learning generates episodes for memory. Memory enables better
motivation calibration and situation recognition. The result is compounding
improvement — intelligence that grows.

---

## Pillar 1: Motivation — Why the Agent Acts

The agent doesn't just follow instructions — it forms goals, evaluates its
own performance, and course-corrects when falling short.

### Meta-Skills (Motivation)

| Meta-Skill | When | Purpose |
|------------|------|---------|
| `/meta-motivation` | Before every non-trivial task | Form quality goals, set success criteria, drive self-evaluation |
| `/meta-scope-guard` | Before every task with code changes | Define boundaries, classify scope level, hold discipline |

### Hook (Motivation)

| Hook | Event | Effect |
|------|-------|--------|
| `motivation-tracker.sh` | PostToolUse (Bash) | Nudges agent to set goals if edits made without `/meta-motivation` |

### Task Lifecycle (Motivation)

1. **Start:** `/meta-motivation` → form functional, quality, and learning goals
2. **During:** Self-evaluate at breakpoints — "Am I doing this well?"
3. **End:** Completion assessment — did I meet my goals? Calibrate quality bar.

---

## Pillar 2: Learning — How the Agent Adapts

The agent learns continuously — before, during, and after each task. Not just
post-task reflection, but real-time situational awareness.

### Meta-Skills (Learning)

| Meta-Skill | When | Purpose |
|------------|------|---------|
| `/meta-learn` | Full task lifecycle (Before/During/After) | Assess situation, monitor progress, adapt mid-task, reflect and consolidate |
| `/meta-anti-patterns` | Before every code change | Review documented mistakes — learning from negative examples |
| `/meta-self-audit` | Every ~5 sessions or on demand | Discover patterns across session logs the agent missed in real-time |

### Hook (Learning)

| Hook | Event | Effect |
|------|-------|--------|
| `pre-edit-governance.sh` | PreToolUse (Edit/Write) | Reminds agent to check anti-patterns if not yet done |
| `stop-reflection-gate.sh` | Stop | Blocks session end if edits were made without learning reflection |

### Task Lifecycle (Learning)

1. **Before:** Build mental model, check memory for similar situations, select strategy
2. **During:** Monitor progress, detect when approach isn't working, correct mid-course
3. **After:** Reflect, capture anti-patterns, consolidate episodes into semantic knowledge

### Anti-Patterns Reference

> **MANDATORY:** Before making any code changes, the agent MUST invoke
> `/meta-anti-patterns` to review documented mistakes.

**Auto-Documentation of Mistakes:** When the user corrects the agent's approach:
1. Acknowledge the correction
2. Append to `ANTI_PATTERN.md` using: Title, Tags, Date, Context, Error, Correct approach
3. Confirm to the user that the pattern has been recorded

---

## Pillar 3: Memory — What the Agent Retains

Knowledge is organized in three layers. Each serves retrieval at a different
level of abstraction, and knowledge flows upward through consolidation.

```
  Episodic              →  Semantic             →  Procedural
  sessions/                MEMORY.md               commands/
  episodic-memory.md       ANTI_PATTERN.md         procedural-memory.md
  Raw experience           Extracted principles    Executable skills
  ─────────────────        ────────────────────    ──────────────────
  /meta-learn (After)      /meta-learn (After)     /meta-propose-skill
  append                   update                  create/refine
```

### Meta-Skills (Memory)

| Meta-Skill | When | Purpose |
|------------|------|---------|
| `/meta-propose-skill` | When a pattern recurs 3+ times | Consolidate semantic knowledge into procedural skills |
| `/meta-commit` | When session involved non-trivial work | Atomic persistence: reflect → capture → commit |
| `/meta-evolve` | After self-audit or on demand | Propose modifications to the governance system itself |

### Hooks (Memory)

| Hook | Event | Effect |
|------|-------|--------|
| `session-init.sh` | SessionStart | Creates session tracker, injects governance reminder |
| `post-edit-tracker.sh` | PostToolUse (Edit/Write) | Silently records each edited file for episodic memory |

### Memory Consolidation

- **Episodic → Semantic:** `/meta-learn` (After phase) extracts principles from episodes
- **Semantic → Procedural:** `/meta-propose-skill` promotes patterns to executable skills
- **Procedural refinement:** `/meta-evolve` restructures the system (requires user approval)

---

## Session Lifecycle

Every task follows this flow, organized by pillar:

```
SESSION START
│
├─ Pillar 3: session-init.sh creates tracker (Memory)
│
├─ Pillar 1: /meta-motivation — set goals (Motivation)
├─ Pillar 1: /meta-scope-guard — define boundaries (Motivation)
├─ Pillar 2: /meta-anti-patterns — check past mistakes (Learning)
├─ Pillar 2: /meta-learn [Before] — assess situation, select strategy (Learning)
│
├─ EXECUTION
│  ├─ Pillar 1: self-evaluate at breakpoints (Motivation)
│  ├─ Pillar 2: /meta-learn [During] — monitor, adapt, correct (Learning)
│  └─ Pillar 3: post-edit-tracker.sh records files (Memory)
│
├─ Pillar 1: completion assessment (Motivation)
├─ Pillar 2: /meta-learn [After] — reflect, capture insights (Learning)
├─ Pillar 3: /meta-commit — persist learning (Memory)
│
SESSION END
└─ stop-reflection-gate.sh enforces that learning happened
```

---

## Session Tracker

Each session creates `/tmp/claude-governance-{session_id}.json` tracking:
- Edit count and files touched
- Whether goals were set, scope declared, situation assessed, and learning reflected

Meta-skills update this tracker by self-reporting. Hooks read it to enforce.

## Session Logs

Per-user session logs at `.claude/memory/sessions/session-log-{git-user}.md`.
Appended by `/meta-commit`, read by `/meta-self-audit` for longitudinal patterns.

---

## Mandatory Conventions

### Code Style
- Follow your language's standard style guidelines
- Use type hints / type annotations where applicable
- Write docstrings for all public functions and classes
- Maximum line length: 88 characters (Black / Prettier compatible)

### Testing
- All new features must have corresponding tests
- Test files mirror source structure
- Run tests before committing

### Git Commits
- Use conventional commit messages: `feat:`, `fix:`, `docs:`, `test:`, `refactor:`
- Keep commits atomic and focused

### Dependencies
- Document new dependencies in your package manager config
- Pin major versions only

### File Naming
- Python modules: `snake_case.py`
- Test files: `test_*.py`
- Configuration files: `config_*.yaml` or `*.toml`

### When Adding New Modules
1. Check for directory README first
2. Create the module in the appropriate directory
3. Write unit tests
4. Add usage example if user-facing
5. Update relevant README sections

---

## Skill Library

This project maintains a reusable skill library at `.claude/commands/`.
For creation conventions and templates, see [`commands/README.md`](commands/README.md).

> **The agent's growth ceiling is not the user's ability to dictate —
> it is the system's ability to learn.** Meta-skills make the agent
> self-correcting. Each improvement compounds across all future work.

### Discovering Skills
1. Check the skill registry in MEMORY.md (always loaded in system prompt)
2. If a skill matches the current task, invoke it via `/skill-name`
3. Run mandatory meta-skills from all three pillars
