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

## Cross-Repo Intelligence Integration

When this framework is deployed as a **parent template** that scaffolds child
repos, each child evolves specialized intelligence through real domain usage.
The parent can absorb what children discover — but only what generalizes.

### The Parent-Child Relationship

```
  PARENT FRAMEWORK                    CHILD DEPLOYMENTS
  ──────────────────                  ──────────────────
  Domain-agnostic                     Domain-specialized
  Scaffolds governance                Evolves under real usage
  Absorbs transferable principles     Discovers domain-specific patterns
  Improves template for all future    Improves one deployment
  children
```

The parent's value is generality. Every absorbed principle must preserve it.

### The Generality Filter (Four Gates)

Every candidate extracted from a child repo must pass all four gates:

1. **Three-Substitution Test** — Strip domain nouns, replace with three unrelated
   domains. The principle must hold in all three. This is the primary filter that
   prevents domain specifics from leaking into the parent.

2. **Pillar Ownership** — The candidate must map to Motivation, Learning, or Memory.
   If it doesn't fit the cognitive architecture, it is a domain fact, not a framework
   principle.

3. **Existing Coverage** — Check whether the parent already implies this principle.
   If yes, the child's contribution is evidence (strengthens existing principle),
   not a new addition.

4. **Source Layer Routing** — Route to the correct approval mechanism:
   anti-patterns → `/meta-evolve`, skills → `/meta-propose-skill`, insights → MEMORY.md.

### Absorption Flow

```
  CHILD REPO                    GENERALITY           PARENT FRAMEWORK
  ──────────                    FILTER               ────────────────
  Episodic (sessions)     ──►   Four gates    ──►    Semantic (MEMORY.md,
  Semantic (MEMORY.md)          strip domain          absorbed-intelligence.md)
  Procedural (commands/)        nouns, test    ──►   Procedural (commands/)
  Anti-patterns                 across domains        via /meta-propose-skill
```

### The Approval Gate Invariant

Even cross-repo proposals go through `/meta-evolve` or `/meta-propose-skill`.
The human always decides what enters the parent framework. This invariant
cannot be bypassed — `/meta-absorb-repo` produces an Absorption Report, not
a mutation.

### Signal Quality

Not all child repos carry equal weight:

| Governance Commits | Signal Level | Implication |
|-------------------|-------------|-------------|
| < 5 | LOW | Framework scaffolded but barely used. Skip or proceed with caution. |
| 5–15 | MODERATE | Some real evolution. Weight evidence lower. |
| 15+ | HIGH | Substantial evolution under real usage. Full extraction warranted. |

Commit velocity on `.claude/` distinguishes active evolution from unused
scaffolding. A file touched in 15 commits was refined by real failure. A file
never touched after creation is either perfect or ignored — session logs
distinguish which.

## Stateful Intelligence Network

### The Statefulness Thesis

The fundamental gap between humans and current AIs is **statefulness**. Humans
accumulate experience continuously — they grow. AIs are bounded by their training
release, trapped in stateless inference. Git bridges this gap: it gives an AI
structured, persistent, branching memory.

A git repo is not a project — it is a **stateful intelligence**. Each commit is
a step of growth. Each branch is a different growth path. The `.claude/` directory
is the intelligence's mind — governance, memory, skills, anti-patterns, all
evolving under version control.

### Intelligence Exchange Topology

Stateful intelligences can exchange knowledge through git-tracked operations:

```
  REPO A                    REPO B                    REPO C
  (domain specialist)       (parent framework)        (domain specialist)
       │                         │                         │
       ├──review──────────►      │      ◄──────review──────┤
       │                    synthesize                      │
       │                    multi-perspective                │
       │                         │                          │
       │      ◄──inject──────── │ ────────inject──►        │
       │                         │                          │
       └──────────absorb────►    │     ◄────absorb─────────┘
```

Three exchange mechanisms:
- **Absorption** (`/meta-absorb-repo`): Bulk intelligence extraction from child to parent through generality filter
- **Review** (`/meta-intelligence-review`): Perspective-grounded evaluation between peers, with multi-turn synthesis
- **Injection** (`/meta-intelligence-inject`): Targeted knowledge push from one intelligence to another

### Provenance Is the Key

Every review and injection carries full provenance:
- **Repo URL** — which intelligence produced this perspective
- **Branch** — which growth path it came from
- **Commit hash** — the exact state that formed the viewpoint

This means the receiving intelligence can always trace a perspective back to its
source context: `git clone <url> && git checkout <commit>`. The reviewer's actual
code, anti-patterns, and session history are accessible — not just an abstracted
opinion, but the ground truth that formed it.

### Multi-Perspective Synthesis

Different repos bring different lenses. A health-coach repo sees governance
through the lens of user safety. An english-tutor repo sees it through the lens
of pedagogical patience. A devops-agent repo sees it through reliability.

When multiple intelligences review the same target:
- **Convergent observations** (independently discovered by 2+ reviewers) = strongest signal
- **Divergent observations** (contradictions between perspectives) = domain boundaries
- **Absence patterns** (what no reviewer noticed) = shared blind spots

Comprehensive synthesis of these viewpoints is more valuable than any single
perspective — including the target's own.

### The Approval Gate Extends

All intelligence exchanges — absorption, review, injection — eventually flow
through `/meta-evolve` or `/meta-propose-skill`. The human always decides what
integrates. This invariant holds whether intelligence arrives via bulk absorption,
peer review, or targeted injection.

---
*Created: 2026-03-18 | Source: Three pillars of human-level intelligence architecture*
*Updated: 2026-03-18 | Change: unified learning system, reframed as THE organizing structure (not an addition) | Trigger: philosophy-driven reframe*
*Updated: 2026-03-24 | Change: added Cross-Repo Intelligence Integration section | Trigger: parent framework evolution feature*
*Updated: 2026-03-24 | Change: added Stateful Intelligence Network section | Trigger: peer review and injection between stateful intelligences*
