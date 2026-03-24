# claude-self-improve

Scaffold a `.claude/` governance framework that makes AI coding agents self-improving.

## What it does

`claude-self-improve init` creates a `.claude/` directory in your git repo containing:

- **4 hook scripts** that enforce governance automatically (session tracking, anti-pattern reminders, edit tracking, reflection gates)
- **7 meta-skill commands** that teach the agent to learn from mistakes, stay in scope, and improve its own skills
- **Memory files** for persistent learning across sessions (anti-patterns, skill registry, session logs)
- **CLAUDE.md** template with governance rules pre-configured

## How it works

```
Hooks fire automatically         Meta-skills guide agent cognition
────────────────────────         ─────────────────────────────────
SessionStart → remind agent      /meta-anti-patterns → avoid past mistakes
PreToolUse   → check compliance  /meta-scope-guard   → stay within request
PostToolUse  → track edits       /meta-learn         → reflect after work
Stop         → enforce learning  /meta-commit        → learn + commit atomically

                    Memory persists across sessions
                    ───────────────────────────────
                    MEMORY.md      → skill registry, insights
                    ANTI_PATTERN.md → documented mistakes
                    session logs    → longitudinal patterns
```

The agent improves itself: `/meta-learn` captures lessons, `/meta-self-audit` discovers patterns across sessions, and `/meta-evolve` proposes governance improvements — all with human approval.

## Install

```bash
pip install claude-self-improve
```

## Quick start

```bash
cd your-project
claude-self-improve init
git add .claude/
git commit -m "feat: add AI agent governance framework"

# One-time setup per developer machine:
claude-self-improve link
```

## What gets created

```
.claude/
├── CLAUDE.md                  # Agent conventions (customize for your project)
├── settings.json              # Hook configuration
├── hooks/                     # 4 governance enforcement scripts
│   ├── session-init.sh        # SessionStart: init tracker + reminder
│   ├── pre-edit-governance.sh # PreToolUse: anti-pattern reminder
│   ├── post-edit-tracker.sh   # PostToolUse: track edited files
│   └── stop-reflection-gate.sh# Stop: block if no learning reflection
├── commands/                  # 7 meta-skill slash commands
│   ├── meta-anti-patterns.md  # Review documented mistakes before edits
│   ├── meta-scope-guard.md    # Define and hold scope boundaries
│   ├── meta-learn.md          # Post-task reflection loop
│   ├── meta-commit.md         # Reflect + commit atomically
│   ├── meta-propose-skill.md  # Create/improve reusable skills
│   ├── meta-self-audit.md     # Discover patterns across sessions
│   └── meta-evolve.md         # Propose governance improvements
└── memory/                    # Persistent learning across sessions
    ├── MEMORY.md              # Skill registry + project insights
    ├── ANTI_PATTERN.md        # Documented error patterns
    ├── skill-candidates.md    # Patterns awaiting promotion
    ├── topic-index.md         # Index of detailed memory files
    └── sessions/              # Per-user session logs
```

## Customization

After `init`, customize these files for your project:

- **`.claude/CLAUDE.md`** — Add your project overview, directory structure, and conventions
- **`.claude/memory/MEMORY.md`** — Will auto-populate as the agent learns your project
- **`.claude/commands/`** — Add domain-specific skills alongside the meta-skills (e.g., `debug-build.md`, `deploy.md`)

## CLI reference

```
claude-self-improve init [--target DIR] [--force]
    Scaffold .claude/ governance framework.
    --target DIR   Target directory (default: current directory)
    --force        Overwrite existing .claude/ directory

claude-self-improve link [--target DIR]
    Create memory symlink for Claude Code's native memory system.
    --target DIR   Project directory containing .claude/ (default: current directory)
```

## Requirements

- Python >= 3.9
- A git repository (recommended, not required)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) or compatible AI coding agent
- `jq` (used by governance hooks for JSON parsing — install via your system package manager)

## License

MIT
