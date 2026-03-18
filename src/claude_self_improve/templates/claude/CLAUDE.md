# AI Agent Conventions

This document defines conventions that AI agents (Claude, Copilot, etc.)
must follow when contributing to this project.
Whenever changes are made, update this file so that later agent behaviours
can be managed in a unified way.

> **IMPORTANT: Before making any edits to this codebase, you MUST read
> [ANTI_PATTERN.md](memory/ANTI_PATTERN.md).** This file contains documented
> error patterns from previous agent interactions that must not be repeated.

## Project Overview

<!-- TODO: Describe your project in 1-2 sentences. -->

## Project Structure

<!-- TODO: Paste your project's directory tree here. -->

---

## Mandatory Conventions

### 1. Code Style

- Follow your language's standard style guidelines
- Use type hints / type annotations where applicable
- Write docstrings for all public functions and classes
- Maximum line length: 88 characters (Black / Prettier compatible)

### 2. Testing

- All new features must have corresponding tests
- Test files mirror source structure
- Run tests before committing

### 3. Git Commits

- Use conventional commit messages:
  - `feat:` new feature
  - `fix:` bug fix
  - `docs:` documentation changes
  - `test:` adding/updating tests
  - `refactor:` code restructuring
- Keep commits atomic and focused

### 4. Dependencies

- Document new dependencies in your package manager config
- Pin major versions only

### 5. File Naming

- Python modules: `snake_case.py`
- Test files: `test_*.py`
- Configuration files: `config_*.yaml` or `*.toml`

### 6. When Adding New Modules

1. **Check for directory README first** — If a `README.md` exists in the
   target directory, read it before adding code.
2. Create the module in the appropriate directory
3. Write unit tests
4. Add usage example if user-facing
5. Update relevant README sections

---

## Cognitive Architecture — Three Pillars of Human-Level Intelligence

This governance framework is built on three pillars that, together, enable
human-level intelligent behavior. See `memory/cognitive-architecture.md` for
the full architecture document.

### Pillar 1: Motivation (Drive to Do Well)
The agent forms explicit quality goals, self-evaluates during work, and
course-corrects when falling short. Not just compliance — genuine pursuit
of excellence. **Meta-skill:** `/meta-motivation`

### Pillar 2: Active Meta-Learning (Learn in the Moment)
The agent reads the situation, selects strategy based on context, monitors
whether the approach is working, and adapts mid-task. Not just post-task
reflection — real-time learning. **Meta-skill:** `/meta-situational-learn`

### Pillar 3: Hierarchical Structured Memory (Organize Over a Lifetime)
Knowledge is layered: episodic (raw sessions) → semantic (extracted principles)
→ procedural (executable skills). Each layer serves retrieval at a different
level of abstraction. **Files:** `episodic-memory.md`, `MEMORY.md`, `procedural-memory.md`

> **The three pillars reinforce each other:** Motivation drives the agent to
> learn actively. Active learning generates episodes for memory. Memory enables
> better motivation calibration and situational recognition. The result is
> compounding improvement — intelligence that grows.

---

## Governance Enforcement (Hooks)

The governance framework is **structurally enforced** via Claude Code hooks
configured in `.claude/settings.json`. These hooks run automatically — the
agent does not need to invoke them.

### Active Hooks

| Hook | Event | Effect |
|------|-------|--------|
| `session-init.sh` | SessionStart | Creates session tracker at `/tmp/`, injects governance reminder |
| `pre-edit-governance.sh` | PreToolUse (Edit/Write) | Reminds agent about anti-patterns if not yet checked |
| `post-edit-tracker.sh` | PostToolUse (Edit/Write) | Silently records each edited file |
| `motivation-tracker.sh` | PostToolUse (Bash) | Nudges agent to set quality goals if edits made without `/meta-motivation` |
| `stop-reflection-gate.sh` | Stop | Blocks session end if edits were made without `/meta-learn` |

### Session Tracker

Each session creates `/tmp/claude-governance-{session_id}.json` tracking:
- Edit count and files touched
- Whether anti-patterns were checked, scope was declared, and learning reflection ran

Meta-skills update this tracker when they run (self-reporting). The Stop hook
reads it to enforce reflection.

### Session Logs

Per-user session logs live at `.claude/memory/sessions/session-log-{git-user}.md`.
These are appended by `/meta-commit` and read by `/meta-self-audit` for
longitudinal pattern detection across sessions and users.

---

## Anti-Patterns Reference

> **MANDATORY:** Before making any code changes, the agent MUST invoke
> `/meta-anti-patterns` to review documented mistakes. This is not optional —
> it is the single entry point for all "what not to do" knowledge.

**Agent Feedback Requirement:** If an anti-pattern critically influenced your
decision-making or prevented you from making a documented mistake, inform the
user.

**Auto-Documentation of Mistakes:** When the user corrects or disapproves of
the agent's approach, the agent MUST automatically add the error pattern to
`ANTI_PATTERN.md`. Follow these steps:
1. Acknowledge the correction
2. Append a new entry to `ANTI_PATTERN.md` using the standard format:
   - **Title:** Short descriptive name
   - **Tags:** Comma-separated tags for contextual filtering
   - **Date:** Current date (YYYY-MM-DD)
   - **Context:** What task was being performed
   - **Error:** What the agent did wrong
   - **Correct approach:** What should have been done instead
3. Confirm to the user that the pattern has been recorded

---

## Skill Library

This project maintains a reusable skill library at `.claude/commands/`.
For skill creation conventions and templates, see
[`commands/README.md`](commands/README.md).

> **Meta-skills are the highest-leverage investment.** Every user correction
> costs user focus time. Meta-skills make the agent self-correcting — catching
> scope creep, avoiding repeated mistakes, and capturing lessons autonomously.
> The agent's growth ceiling is not the user's ability to dictate — it is the
> system's ability to learn.

### Mandatory Meta-Skills

These run on every task, not just when explicitly invoked:

1. **`/meta-motivation`** — Before starting, form quality goals and success criteria (Pillar 1)
2. **`/meta-anti-patterns`** — Before code changes, check ANTI_PATTERN.md
3. **`/meta-scope-guard`** — Before starting work, define and hold scope boundaries
4. **`/meta-situational-learn`** — During work, assess situation and adapt strategy (Pillar 2)
5. **`/meta-learn`** — After completing non-trivial work, reflect and capture insights; consolidate episodic → semantic → procedural memory (Pillar 3)

### Learning Checkpoint: `/meta-commit`

Use `/meta-commit` instead of plain "commit" when the session involved
non-trivial work. It triggers the full reflection loop (meta-learn) before
committing, capturing skills, anti-patterns, and memory updates alongside
code in one atomic commit.

### Autonomous Evolution: `/meta-self-audit` and `/meta-evolve`

- **`/meta-self-audit`** — Reads session logs to discover patterns the agent
  didn't notice in real-time. Run every ~5 sessions or on demand.
- **`/meta-evolve`** — Proposes modifications to meta-skills, hooks, and memory
  structure. All changes require explicit user approval before applying.

### Discovering Skills

The agent's auto-memory (`MEMORY.md`) contains a registry of all available
skills. At the start of any non-trivial task:
1. Check the skill registry in MEMORY.md (always loaded in system prompt)
2. If a skill matches the current task, invoke it via `/skill-name`
3. Run mandatory meta-skills (anti-patterns, scope-guard)
