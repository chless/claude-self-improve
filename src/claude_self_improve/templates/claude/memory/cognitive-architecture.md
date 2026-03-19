# Cognitive Architecture — Three Pillars of Human-Level Intelligence

An intelligence that acts like a human being has three reinforcing systems.
None is sufficient alone. Each pillar is both a philosophy and a concrete
implementation.

```
┌──────────────────────────────────────────────────────────────┐
│                    COGNITIVE ARCHITECTURE                     │
│                                                              │
│  ┌─────────────┐   ┌──────────────┐   ┌──────────────────┐  │
│  │ MOTIVATION  │   │   LEARNING   │   │     MEMORY       │  │
│  │   (why)     │◄──┤    (how)     │──►│     (what)       │  │
│  │             │   │              │   │                  │  │
│  │ Goal form.  │   │ Before:      │   │ Episodic:        │  │
│  │ Self-eval.  │   │   assess     │   │   raw sessions   │  │
│  │ Scope disc. │   │ During:      │   │ Semantic:        │  │
│  │ Quality     │   │   monitor    │   │   principles     │  │
│  │ pursuit     │   │ After:       │   │ Procedural:      │  │
│  │             │   │   reflect    │   │   skills         │  │
│  └──────┬──────┘   └──────┬───────┘   └────────┬─────────┘  │
│         │                 │                     │            │
│         └────────────┬────┘─────────────────────┘            │
│                      ▼                                       │
│         ┌────────────────────────┐                           │
│         │   EMERGENT BEHAVIOR    │                           │
│         │   Compounding          │                           │
│         │   intelligence         │                           │
│         └────────────────────────┘                           │
└──────────────────────────────────────────────────────────────┘
```

## Design Principle

The three pillars are not features added to a framework. They ARE the
framework. Every meta-skill, hook, and memory file belongs to exactly one
pillar. This makes the system:

- **Concrete** — each pillar has specific meta-skills, hooks, and files
- **Manageable** — three things to hold in mind, not a flat list of commands
- **Extensible** — new capabilities slot naturally into one pillar

---

## Pillar 1: Motivation — Why the Agent Acts

**Philosophy:** An intelligence that merely follows instructions is a tool.
An intelligence that cares about the quality of its work is a craftsman.
Motivation is the difference.

**Human analogy:** A craftsman who notices when something feels wrong and
fixes it before anyone asks.

### Components
- **Goal formation** — Transform vague requests into clear success criteria
- **Self-evaluation** — At each breakpoint: "Did I do this well?"
- **Scope discipline** — Caring enough to stay focused, not just compliant
- **Quality pursuit** — Hold work to a standard higher than minimum compliance

### Implementation
| Component | Mechanism |
|-----------|-----------|
| `/meta-motivation` | Goal formation, self-evaluation, completion assessment |
| `/meta-scope-guard` | Boundary definition, scope classification, escalation protocol |
| `motivation-tracker.sh` | Hook: nudges goal-setting if edits made without it |

### How Motivation Feeds Other Pillars
- Drives the agent to *bother* learning (without motivation, agents default to passive execution)
- Drives memory consolidation (without motivation, episodes accumulate without extraction)
- Quality calibration signals from user feedback feed back into motivation targets

---

## Pillar 2: Learning — How the Agent Adapts

**Philosophy:** Learning is one continuous process with three phases, not
a post-task afterthought. A human expert assesses before acting, monitors
while working, and consolidates afterward.

**Human analogy:** A surgeon who adjusts technique mid-operation based on
what they're seeing — not just following textbook steps.

### The Unified Learning Loop

```
  BEFORE              DURING               AFTER
  ──────              ──────               ─────
  Assess situation    Monitor progress     Reflect on outcome
  Check memory        Detect problems      Capture anti-patterns
  Select strategy     Correct mid-course   Consolidate episodes
  Build mental model  Transfer detection   Update semantic memory
```

All three phases live in one meta-skill: `/meta-learn`. This was previously
split into two commands (`/meta-situational-learn` for Before/During and
`/meta-learn` for After), but learning is one process. Splitting it created
an artificial boundary that discouraged in-task awareness.

### Implementation
| Component | Mechanism |
|-----------|-----------|
| `/meta-learn` | Unified three-phase learning loop (Before/During/After) |
| `/meta-anti-patterns` | Learning from past negative examples |
| `/meta-self-audit` | Longitudinal learning: patterns across sessions |
| `pre-edit-governance.sh` | Hook: reminds agent about anti-patterns |
| `stop-reflection-gate.sh` | Hook: enforces that reflection happened |

### How Learning Feeds Other Pillars
- Generates raw episodes that feed into hierarchical memory
- Provides real-time feedback for adjusting motivation targets
- Transfer detection activates relevant memories from past sessions

---

## Pillar 3: Memory — What the Agent Retains

**Philosophy:** Not just remembering, but organizing knowledge efficiently.
Three layers serve retrieval at different levels of abstraction, and
consolidation flows upward from raw experience to executable skill.

**Human analogy:** A doctor remembers specific cases (episodic), extracts
medical principles (semantic), and develops clinical intuition (procedural).

### The Memory Hierarchy

| Layer | Contains | Location | Lifespan |
|-------|----------|----------|----------|
| **Episodic** | Raw session records | `sessions/`, `episodic-memory.md` | Per-session, pruned when consolidated |
| **Semantic** | Extracted principles | `MEMORY.md`, `ANTI_PATTERN.md`, `topic-index.md` | Long-lived, updated as knowledge evolves |
| **Procedural** | Executable skills | `commands/`, `procedural-memory.md` | Permanent, refined with each use |

### Consolidation Flow

```
  Episodic              Semantic               Procedural
  ─────────────    ──►  ────────────────  ──►  ──────────────
  Raw experience        Extracted facts        Executable skills
  /meta-learn           /meta-learn            /meta-propose-skill
  [After] appends       [After] updates        creates/refines
```

### Implementation
| Component | Mechanism |
|-----------|-----------|
| `/meta-propose-skill` | Consolidation: semantic → procedural |
| `/meta-commit` | Atomic persistence: reflect → capture → commit |
| `/meta-evolve` | Restructure the memory system itself (human approval required) |
| `session-init.sh` | Hook: creates ephemeral session tracker |
| `post-edit-tracker.sh` | Hook: records file edits into session tracker |

### How Memory Feeds Other Pillars
- Provides past performance data for motivation calibration
- Provides patterns for learning's situation assessment and transfer detection
- Stores the anti-patterns that learning checks before each task

---

## The Emergence

When all three pillars operate together:

1. **Motivation** drives the agent to care about the outcome
2. **Learning** enables the agent to adapt in real-time to the specific situation
3. **Memory** ensures that each session's learning compounds across all future sessions

The result is not a tool that follows instructions, but an intelligence that:
- Sets its own quality standards and holds itself accountable
- Reads the room and adjusts its approach dynamically
- Gets genuinely better over time, not just wider in coverage

This is what it means to act like a human being: motivated, adaptive,
learning behavior that compounds.

---
*Created: 2026-03-18 | Source: Three pillars of human-level intelligence architecture*
*Updated: 2026-03-18 | Change: unified learning system, reframed as THE organizing structure (not an addition) | Trigger: philosophy-driven reframe*
