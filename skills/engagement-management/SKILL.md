---
name: engagement-management
description: 6 consulting engagement management frameworks — win strategy, commercial structuring, kick-off, stakeholder cadence, progress reporting, and closeout. Covers the full arc of how a consulting engagement is won and run.
version: 1.0.0
triggers:
  - /engagement-management
  - /win-strategy
  - /commercial-structuring
  - /engagement-kickoff
  - /stakeholder-cadence
  - /progress-reporting
  - /engagement-closeout
---

# engagement-management — 6 Engagement Management Frameworks

## When To Use

Use across the full consulting engagement lifecycle — from qualifying and winning the work through delivery and closeout. These skills run in parallel with strategy-consulting and solution-delivery; they govern how the engagement operates, not what it produces.

## The 6 Skills

### Domain 1 — Pursuit
| Trigger | When to Use |
|---|---|
| `/win-strategy` | Opportunity qualified — define competitive positioning before proposal writing |
| `/commercial-structuring` | Win strategy set — design the fee model, margin analysis, negotiation brief |

### Domain 2 — Delivery
| Trigger | When to Use |
|---|---|
| `/engagement-kickoff` | Week before start — agenda, governance, ways of working, 30-day plan |
| `/stakeholder-cadence` | Kick-off — design steering / working group / sponsor 1:1 meeting architecture |
| `/progress-reporting` | Weekly / monthly — RAG dashboard, milestone tracker, decisions needed |

### Domain 3 — Closeout
| Trigger | When to Use |
|---|---|
| `/engagement-closeout` | Final 2 weeks — deliverable sign-off, client satisfaction, reference case, follow-on |

## Chain Position

```
engagement-management runs ACROSS all other packs:

/win-strategy → /commercial-structuring  (before engagement starts)
      ↓
/engagement-kickoff → /stakeholder-cadence  (Day 1)
      ↓
/progress-reporting  (every week/month throughout)
   ↕
[strategy-consulting + ai-transformation + solution-delivery running in parallel]
      ↓
/engagement-closeout  (final 2 weeks)
      ↓
continuous-improvement  (post-exit)
```

## Dispatch Logic

1. Individual trigger (e.g. `/win-strategy`) — read `skills/01-pursuit/win-strategy.md` and execute inline.
2. Top-level with argument — same as above.
3. No argument — ask which phase (Pursuit / Delivery / Closeout), then which skill, then execute.

**Execution**: Read skill `.md` from `~/.claude/skills/engagement-management/skills/<domain>/<skill>.md`, load its Workflow and Output Format, apply to user context. Do not invoke Skill tool — run inline.

## Chaining Out

- `/win-strategy` → `/narrative-builder` (strategy-consulting) to build the proposal narrative
- `/commercial-structuring` → `/business-case-builder` (strategy-consulting) for client ROI framing
- `/stakeholder-cadence` → `/stakeholder-alignment` (strategy-consulting) for exec alignment
- `/engagement-closeout` → `/post-implementation-review` (solution-delivery) for the final value read
