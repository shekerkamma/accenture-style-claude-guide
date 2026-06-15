---
name: solution-delivery
description: 13 consulting frameworks for solution roadmap realization and implementation — blueprint design, delivery governance, change management, and value realization. Chains directly from strategy-consulting outputs.
version: 1.0.0
triggers:
  - /solution-delivery
  - /solution-blueprint
  - /architecture-decision-record
  - /integration-sequencing
  - /raid-log
  - /stage-gate-review
  - /delivery-risk-assessment
  - /raci-design
  - /change-readiness-assessment
  - /change-impact-assessment
  - /adoption-plan
  - /benefits-register
  - /post-implementation-review
  - /hypercare-plan
---

# solution-delivery — 13 Implementation & Realization Frameworks

## When To Use

After strategy-consulting has produced a chosen direction. These skills pick up where the strategy skills end:

| Chain from... | Into... |
|---|---|
| `/strategic-options` (chosen option) | `/solution-blueprint` |
| `/transformation-roadmap` (phases) | `/solution-blueprint` → `/integration-sequencing` |
| `/business-case-builder` (approved case) | `/benefits-register` |
| `/operating-model-design` (target model) | `/raci-design` → `/change-impact-assessment` |
| `/stakeholder-alignment` (aligned execs) | `/change-readiness-assessment` → `/adoption-plan` |
| `/risk-and-mitigation` (strategic risks) | `/raid-log` → `/delivery-risk-assessment` |
| `/value-realization` (value framework) | `/benefits-register` → `/post-implementation-review` |

## The 13 Skills

### Domain 1: Solution Design
| Trigger | When to Use |
|---|---|
| `/solution-blueprint` | Strategic option chosen — need to define capabilities, components, workstreams, and phases |
| `/architecture-decision-record` | Significant tech/structural choice must be documented, auditable, and revisable |
| `/integration-sequencing` | Multiple systems in scope — need build/test order, dependencies, and rollback positions |

### Domain 2: Delivery Governance
| Trigger | When to Use |
|---|---|
| `/raid-log` | Programme kickoff or stage gate — establish Risks/Assumptions/Issues/Dependencies baseline |
| `/stage-gate-review` | End of any delivery phase — Go/No-Go decision, exit criteria, lessons |
| `/delivery-risk-assessment` | Phase start or converging RAID Ambers — prioritised risk heat map with mitigations |
| `/raci-design` | Accountability is unclear or duplicated — assign R/A/C/I across decisions and deliverables |

### Domain 3: Change Management & Adoption
| Trigger | When to Use |
|---|---|
| `/change-readiness-assessment` | Solution defined — score ADKAR readiness per stakeholder group before writing the change plan |
| `/change-impact-assessment` | Blueprint complete — map what is changing for whom before designing support activities |
| `/adoption-plan` | Readiness and impact assessed — build the sequenced comms/training/reinforcement schedule |

### Domain 4: Value Realization
| Trigger | When to Use |
|---|---|
| `/benefits-register` | Business case approved — lock in baselines, owners, measurement methods for every benefit |
| `/post-implementation-review` | 90 days post go-live — compare actuals vs. business case, root-cause variances, capture lessons |
| `/hypercare-plan` | 2–4 weeks pre go-live — define support model, SLAs, exit criteria for BAU handover |

## Recommended Sequence

For a full implementation engagement, run skills in this order:

```
STRATEGY LAYER (strategy-consulting)
  /transformation-roadmap → /business-case-builder → /stakeholder-alignment

DESIGN LAYER (solution-delivery)
  /solution-blueprint → /architecture-decision-record → /integration-sequencing

GOVERNANCE LAYER (solution-delivery)
  /raid-log → /raci-design → /delivery-risk-assessment

CHANGE LAYER (solution-delivery)
  /change-impact-assessment → /change-readiness-assessment → /adoption-plan

DELIVERY GATES (solution-delivery)
  /stage-gate-review [end of each phase]

GO-LIVE LAYER (solution-delivery)
  /hypercare-plan → [go-live] → /post-implementation-review (90 days)
  /benefits-register [lock at approval] → tracked through /post-implementation-review
```

## Dispatch Logic

1. **Individual trigger** (e.g. `/raid-log`) — read `skills/02-delivery-governance/raid-log.md` and execute the Workflow and Output Format on the user's context.
2. **Top-level with argument** (e.g. `/solution-delivery raid-log`) — same as above.
3. **No argument** — ask which domain: Solution Design / Delivery Governance / Change Management / Value Realization, then which skill, then execute.
4. **Chain request** (e.g. "I've run /transformation-roadmap, what next?") — recommend the appropriate domain entry point from the chain table above.

**Execution**: Read the skill `.md` from `~/.claude/skills/solution-delivery/skills/<domain>/<skill>.md`, load its Workflow and Output Format, apply to user context. Do not invoke the Skill tool — run inline.

## Chaining Out

- Findings → `/branded-pptx-deck` for client-facing delivery
- RAID log / delivery risks → `/war-gaming` to stress-test response options
- Benefits register → `/kpi-architect` to design the measurement dashboard
- Post-implementation review lessons → `/narrative-builder` for executive lessons-learned communication
