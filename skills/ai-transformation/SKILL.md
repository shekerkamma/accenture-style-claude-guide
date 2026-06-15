---
name: ai-transformation
description: 6 AI-specific consulting frameworks — maturity assessment, data readiness, use case prioritisation, operating model design, responsible AI, and build-buy-partner decisions. Chains from strategy-consulting and into solution-delivery.
version: 1.0.0
triggers:
  - /ai-transformation
  - /ai-maturity-assessment
  - /data-readiness-assessment
  - /ai-use-case-prioritiser
  - /ai-operating-model
  - /responsible-ai-framework
  - /ai-build-buy-partner
---

# ai-transformation — 6 AI Strategy Frameworks

## When To Use

Use for any AI strategy engagement where the generic strategy-consulting frameworks are insufficient — when the question is specifically about AI maturity, use case selection, AI operating model design, or AI governance.

## The 6 Skills

### Domain 1 — Maturity & Readiness
| Trigger | When to Use |
|---|---|
| `/ai-maturity-assessment` | Start of engagement — score org across data/tech/talent/governance/culture |
| `/data-readiness-assessment` | Before committing to use cases — assess data fitness per use case |

### Domain 2 — Use Case & Operating Model
| Trigger | When to Use |
|---|---|
| `/ai-use-case-prioritiser` | Long list of use cases → funded, sequenced portfolio |
| `/ai-operating-model` | Org ready to industrialise — design CoE / federated / embedded / hybrid |

### Domain 3 — Governance & Decisions
| Trigger | When to Use |
|---|---|
| `/responsible-ai-framework` | Pre-deployment — define principles, risk tiers, governance, guardrails |
| `/ai-build-buy-partner` | Capability sourcing decisions — make vs buy vs partner per capability |

## Chain Position

```
strategy-consulting                    ai-transformation
───────────────────────────────────────────────────────
/situation-assessment       →  /ai-maturity-assessment
/strategic-options          →  /ai-use-case-prioritiser → /ai-build-buy-partner
/operating-model-design     →  /ai-operating-model
/risk-and-mitigation        →  /responsible-ai-framework
                                       ↓
                              solution-delivery
                              /solution-blueprint
                              /transformation-roadmap
```

## Dispatch Logic

1. Individual trigger (e.g. `/ai-maturity-assessment`) — read `skills/01-maturity-and-readiness/ai-maturity-assessment.md` and execute inline.
2. Top-level with argument (e.g. `/ai-transformation ai-operating-model`) — same as above.
3. No argument — ask which domain, then which skill, then execute.

**Execution**: Read skill `.md` from `~/.claude/skills/ai-transformation/skills/<domain>/<skill>.md`, load its Workflow and Output Format, apply to user context. Do not invoke Skill tool — run inline.

## Chaining Out

- `/ai-use-case-prioritiser` findings → `/solution-blueprint` to design the delivery
- `/ai-operating-model` → `/raci-design` to assign accountability
- `/responsible-ai-framework` → `/risk-and-mitigation` for the full risk register
- `/ai-build-buy-partner` → `/commercial-structuring` for vendor pricing
