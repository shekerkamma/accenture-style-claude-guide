---
name: strategy-consulting
description: 21 Accenture-style consulting frameworks — situation assessment, market mapping, competitive intel, business case, operating model design, war gaming, and more. Pass a skill name as the argument or omit to pick interactively.
version: 1.0.0
triggers:
  - /strategy-consulting
  - /situation-assessment
  - /growth-barriers
  - /assumption-audit
  - /market-mapping
  - /competitive-intel
  - /customer-segmentation
  - /profit-pool-analysis
  - /strategic-options
  - /business-case-builder
  - /portfolio-review
  - /pricing-strategy
  - /operating-model-design
  - /transformation-roadmap
  - /initiative-prioritizer
  - /kpi-architect
  - /risk-and-mitigation
  - /value-realization
  - /war-gaming
  - /decision-memo
  - /narrative-builder
  - /stakeholder-alignment
---

# strategy-consulting — 21 Accenture-Style Consulting Frameworks

## When To Use

Any time you need to apply a structured consulting methodology:
- Strategy work (situation assessment, market analysis, competitive intel, strategic options)
- Financial and investment decisions (business case, portfolio review, pricing strategy)
- Execution planning (operating model design, transformation roadmap, initiative prioritization)
- Performance and risk governance (KPI architecture, risk register, value realization, war gaming)
- Executive communication (decision memo, narrative builder, stakeholder alignment)

## How To Invoke

**Single-skill invocation** (most common):
```
/situation-assessment  [context]
/war-gaming            [strategy to stress-test]
/business-case-builder [investment decision]
```

**Top-level with skill name**:
```
/strategy-consulting situation-assessment
/strategy-consulting war-gaming
```

**Without arguments** — Claude will ask which framework to apply.

## The 21 Skills

### Domain 1: Diagnosis & Framing
| Trigger | Skill | When to Use |
|---------|-------|-------------|
| `/situation-assessment` | [Situation Assessment](skills/01-diagnosis-and-framing/situation-assessment.md) | Business reviews, turnaround diagnosis, board prep |
| `/growth-barriers` | [Growth Barriers](skills/01-diagnosis-and-framing/growth-barriers.md) | Stalled growth, revenue plateau, funnel issues |
| `/assumption-audit` | [Assumption Audit](skills/01-diagnosis-and-framing/assumption-audit.md) | Board reviews, major investments, strategy pressure test |

### Domain 2: Market & Competitive Intelligence
| Trigger | Skill | When to Use |
|---------|-------|-------------|
| `/market-mapping` | [Market Mapping](skills/02-market-and-competitive-intelligence/market-mapping.md) | Market entry, expansion, TAM/SAM/SOM |
| `/competitive-intel` | [Competitive Intel](skills/02-market-and-competitive-intelligence/competitive-intel.md) | Market entry, pricing changes, product launches |
| `/customer-segmentation` | [Customer Segmentation](skills/02-market-and-competitive-intelligence/customer-segmentation.md) | ICP work, go-to-market focus, retention strategy |
| `/profit-pool-analysis` | [Profit Pool Analysis](skills/02-market-and-competitive-intelligence/profit-pool-analysis.md) | Market entry, product portfolio, channel strategy |

### Domain 3: Strategic Choice & Economics
| Trigger | Skill | When to Use |
|---------|-------|-------------|
| `/strategic-options` | [Strategic Options](skills/03-strategic-choice-and-economics/strategic-options.md) | Strategy choices, build-buy-partner decisions |
| `/business-case-builder` | [Business Case Builder](skills/03-strategic-choice-and-economics/business-case-builder.md) | Investment decisions, ROI/NPV, board cases |
| `/portfolio-review` | [Portfolio Review](skills/03-strategic-choice-and-economics/portfolio-review.md) | Capital allocation, where to invest or exit |
| `/pricing-strategy` | [Pricing Strategy](skills/03-strategic-choice-and-economics/pricing-strategy.md) | Price increases, discount leakage, packaging redesign |

### Domain 4: Operating Model & Execution
| Trigger | Skill | When to Use |
|---------|-------|-------------|
| `/operating-model-design` | [Operating Model Design](skills/04-operating-model-and-execution/operating-model-design.md) | Transformations, new BUs, functional redesigns |
| `/transformation-roadmap` | [Transformation Roadmap](skills/04-operating-model-and-execution/transformation-roadmap.md) | Transformation programs, digital transformation |
| `/initiative-prioritizer` | [Initiative Prioritizer](skills/04-operating-model-and-execution/initiative-prioritizer.md) | Annual planning, too many projects, OKR planning |

### Domain 5: Risk, Performance & Value Governance
| Trigger | Skill | When to Use |
|---------|-------|-------------|
| `/kpi-architect` | [KPI Architect](skills/05-risk-performance-and-value-governance/kpi-architect.md) | Metrics cleanup, dashboards, OKRs, performance management |
| `/risk-and-mitigation` | [Risk & Mitigation](skills/05-risk-performance-and-value-governance/risk-and-mitigation.md) | Strategy approval, launch risk, board risk review |
| `/value-realization` | [Value Realization](skills/05-risk-performance-and-value-governance/value-realization.md) | Transformation value, synergy capture, benefits tracking |
| `/war-gaming` | [War Gaming](skills/05-risk-performance-and-value-governance/war-gaming.md) | Strategy pressure test, competitive response, scenario planning |

### Domain 6: Alignment & Executive Communication
| Trigger | Skill | When to Use |
|---------|-------|-------------|
| `/decision-memo` | [Decision Memo](skills/06-alignment-and-executive-communication/decision-memo.md) | Board memos, investment recommendations |
| `/narrative-builder` | [Narrative Builder](skills/06-alignment-and-executive-communication/narrative-builder.md) | Board deck, strategy story, Pyramid Principle |
| `/stakeholder-alignment` | [Stakeholder Alignment](skills/06-alignment-and-executive-communication/stakeholder-alignment.md) | Executive buy-in, board approval, change management |

## Dispatch Logic

When this skill is invoked:

1. **Check the argument** — if a skill name was passed (e.g. `/war-gaming` or `/strategy-consulting war-gaming`), read that skill's `.md` file directly and execute it.

2. **No argument** — ask the user which domain they're working in, then which skill, then execute.

3. **Ambiguous** — if the user describes a problem ("I need to figure out why growth is stalling"), map it to the most relevant skill and confirm before proceeding.

**Execution**: Read the skill's `.md` file from `~/.claude/skills/strategy-consulting/skills/<domain>/<skill>.md`, load its Workflow and Output Format, and apply it to the user's context.

## Chaining

These skills chain naturally into `/branded-pptx-deck` for deliverable output:
- Run the consulting framework → produce structured findings
- Pass findings to `/branded-pptx-deck` to build the client-facing deck

They also chain into `/ai-strategy-researcher` (for market data) and `/grill-me` (to stress-test the strategy with follow-up questions).
