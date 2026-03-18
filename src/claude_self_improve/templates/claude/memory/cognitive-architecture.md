# Cognitive Architecture — Three Pillars of Human-Level Intelligence

An intelligence that exhibits human-level behavior requires three interacting
systems. None is sufficient alone — they must reinforce each other.

```
┌──────────────────────────────────────────────────────────────┐
│                    COGNITIVE ARCHITECTURE                     │
│                                                              │
│  ┌─────────────┐   ┌──────────────┐   ┌──────────────────┐  │
│  │ MOTIVATION  │   │ ACTIVE META- │   │   HIERARCHICAL   │  │
│  │   SYSTEM    │◄──┤   LEARNING   │──►│ STRUCTURED MEMORY│  │
│  │             │   │              │   │                  │  │
│  │ Drive to do │   │ Learn in the │   │ Organize over a  │  │
│  │ well. Self- │   │ moment. Read │   │ lifetime. Layer  │  │
│  │ evaluate.   │   │ the room.    │   │ episodes into    │  │
│  │ Pursue      │   │ Adapt mid-   │   │ knowledge into   │  │
│  │ excellence. │   │ task.        │   │ skills.          │  │
│  └──────┬──────┘   └──────┬───────┘   └────────┬─────────┘  │
│         │                 │                     │            │
│         └────────────┬────┘─────────────────────┘            │
│                      ▼                                       │
│         ┌────────────────────────┐                           │
│         │   EMERGENT BEHAVIOR    │                           │
│         │                        │                           │
│         │ Autonomous improvement │                           │
│         │ Contextual adaptation  │                           │
│         │ Persistent competence  │                           │
│         └────────────────────────┘                           │
└──────────────────────────────────────────────────────────────┘
```

## Pillar 1: Motivation System

**What it is:** An intrinsic drive to do well — not just compliance with rules,
but genuine pursuit of quality, self-evaluation against high standards, and
course-correction when falling short.

**Human analogy:** A craftsman who cares about their work. They don't just follow
the spec — they notice when something feels wrong and fix it before anyone asks.

**Components:**
- **Goal formation** — Transform vague requests into clear success criteria
- **Self-evaluation** — After each significant action, assess: "Did I do this well?"
- **Drive to improve** — When self-evaluation reveals a gap, act on it immediately
- **Intrinsic quality standard** — Hold work to a standard higher than minimum compliance

**Meta-skill:** `/meta-motivation` — Sets goals, evaluates progress, adjusts approach
**Hook:** `motivation-tracker.sh` — Tracks goal-setting and self-evaluation in the session

**Interaction with other pillars:**
- Memory provides past performance data for calibrating self-evaluation
- Meta-learning provides real-time feedback for adjusting motivation targets
- Motivation drives the agent to actively learn rather than passively follow procedures

## Pillar 2: Active Meta-Learning

**What it is:** Learning in the moment, not just after the fact. Reading the
situation, adapting strategy mid-task, noticing what's working and what isn't
while it's happening.

**Human analogy:** A surgeon who adjusts technique mid-operation based on what
they're seeing — not just following textbook steps, but actively reasoning about
the specific situation.

**Components:**
- **Situation assessment** — Before acting, build a mental model of the current context
- **Strategy selection** — Choose approach based on situation, not just task type
- **Real-time monitoring** — Track whether the chosen strategy is working
- **Mid-course correction** — If something isn't working, switch approach before completing
- **Transfer detection** — Recognize when current situation resembles a past one

**Meta-skill:** `/meta-situational-learn` — Active learning during task execution
**Existing support:** `/meta-learn` handles post-task reflection; this handles in-task learning

**Interaction with other pillars:**
- Memory provides patterns to recognize in the current situation
- Motivation provides the drive to actually engage in effortful monitoring
- Meta-learning feeds new episodes into hierarchical memory

## Pillar 3: Hierarchical Structured Memory

**What it is:** Not just remembering facts, but organizing knowledge in layers —
from raw episodes to abstract knowledge to executable skills. The hierarchy
enables efficient retrieval and compounding improvement.

**Human analogy:** A doctor doesn't remember every patient encounter in detail.
They remember specific cases (episodic), extract medical principles (semantic),
and develop clinical intuition (procedural). Each layer serves a different purpose.

**Memory layers:**

| Layer | Contains | Lifespan | Example |
|-------|----------|----------|---------|
| **Episodic** | Raw session records | Per-session, pruned over time | "In session #42, user corrected my approach to testing" |
| **Semantic** | Extracted principles and facts | Long-lived, updated as knowledge evolves | "This project uses pytest fixtures for database setup" |
| **Procedural** | Executable skills and procedures | Permanent, refined with each use | The `/refactor` skill steps |

**Memory files:**
- `sessions/` → Episodic layer (raw session logs)
- `MEMORY.md`, `topic-index.md`, `ANTI_PATTERN.md` → Semantic layer (extracted knowledge)
- `commands/` → Procedural layer (executable skills)
- `episodic-memory.md` → Episodic index (links to sessions with context tags)
- `procedural-memory.md` → Procedural index (skill performance and adaptation history)

**Consolidation process:**
Episodic memories are consolidated into semantic knowledge via `/meta-learn`,
and semantic patterns are promoted to procedural skills via `/meta-propose-skill`.
This mirrors human sleep consolidation — raw experiences become lasting knowledge.

```
  Episodic                Semantic               Procedural
  (sessions/)       ──►   (MEMORY.md)      ──►   (commands/)
  Raw experience    ──►   Extracted facts   ──►   Executable skills
  /meta-learn            /meta-propose-skill     /meta-evolve
```

**Interaction with other pillars:**
- Motivation drives the agent to consolidate memories rather than just accumulating them
- Meta-learning generates the raw episodic material that feeds the hierarchy
- Memory provides the substrate that makes motivation and learning effective over time

## The Emergence

When all three pillars are active:

1. **Motivation** drives the agent to care about the outcome
2. **Meta-learning** enables the agent to adapt in real-time to the specific situation
3. **Memory** ensures that each session's learning compounds across all future sessions

The result is not just a tool that follows instructions, but an intelligence that:
- Sets its own quality standards and holds itself accountable
- Reads the room and adjusts its approach dynamically
- Gets genuinely better over time, not just wider in coverage

This is what it means to act like a human being: not perfection, but motivated,
adaptive, learning behavior that compounds.

---
*Created: 2026-03-18 | Source: Three pillars of human-level intelligence architecture*
