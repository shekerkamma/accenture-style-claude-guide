---
skill: /ai-use-case-prioritiser
pack: AI & Digital Transformation
vertical: manufacturing
chains-from: /ai-maturity-assessment, /situation-assessment
chains-into: /data-readiness-assessment, /solution-blueprint
---

# Prompt Template: AI Use Case Prioritiser — Manufacturing & Industrial

**When to use:** When a manufacturer has a long list of Industry 4.0 / AI opportunities and must select a funded, OT-feasible, CapEx-approved portfolio with clear OEE or cost impact.

## Copy-paste prompt

```
Run /ai-use-case-prioritiser for [CLIENT NAME]:

Sub-sector: [AUTOMOTIVE / AEROSPACE / PROCESS / DISCRETE / CONSUMER GOODS / INDUSTRIAL EQUIPMENT]
AI maturity level: [1–4 from /ai-maturity-assessment, or UNKNOWN]
Plants in scope: [NUMBER of plants / SPECIFIC PLANT NAMES]

Manufacturing use case long list — mark any already in flight:
Asset Performance & Maintenance:
- [ ] Predictive maintenance (rotating equipment — motors, pumps, compressors)
- [ ] Remaining useful life (RUL) prediction for critical assets
- [ ] Anomaly detection on production line
- [ ] Energy consumption optimisation per asset
- [ ] [OTHER]

Quality & Inspection:
- [ ] Automated visual inspection (camera-based defect detection)
- [ ] Statistical process control (AI-enhanced SPC)
- [ ] Root cause analysis for quality escapes
- [ ] First-pass yield prediction
- [ ] [OTHER]

Production & Scheduling:
- [ ] Production scheduling / sequencing optimisation
- [ ] Demand-driven production planning
- [ ] Bottleneck detection and throughput optimisation
- [ ] Digital twin for process simulation
- [ ] [OTHER]

Supply Chain & Inventory:
- [ ] Demand forecasting (SKU-level, multi-echelon)
- [ ] Supplier risk / lead time prediction
- [ ] Inventory optimisation (safety stock, reorder)
- [ ] Logistics routing optimisation
- [ ] [OTHER]

Energy & Sustainability:
- [ ] Energy demand forecasting and load shifting
- [ ] Scope 1/2 emissions monitoring and reduction
- [ ] Waste and scrap reduction modelling
- [ ] [OTHER]

Workforce & Safety:
- [ ] Operator performance monitoring (without surveillance)
- [ ] Safety incident prediction
- [ ] Knowledge capture from retiring workers (LLM-assisted)
- [ ] [OTHER]

Constraints:
- OT connectivity: [e.g. "60% of assets connected; Line 3 air-gapped"]
- CapEx approval threshold: [e.g. "Projects >£500k require Board approval — 6-month cycle"]
- Plant manager buy-in: [BRIEF — e.g. "Plant A manager supportive; Plant B sceptical"]
- OEE baseline: [BRIEF — e.g. "Group OEE is 72%; benchmark for sector is 85%"]
- Executive sponsor priorities: [e.g. "COO: reduce maintenance cost; CFO: scrap reduction; CSO: Scope 1 emissions"]
- Maintenance crew capacity: [BRIEF — e.g. "Only 2 condition monitoring specialists globally"]
```

## Expected output
Scored register with manufacturing-specific scoring (OEE/Cost Impact × OT Feasibility × CapEx Cycle Alignment), Wave 1/2/3 portfolio with plant-level rollout sequence, OT connectivity gaps flagged as pre-conditions for specific use cases, and recommended thin thread (fastest OEE or cost impact with lowest OT integration complexity).

## Manufacturing-specific quality checks
- Score OT feasibility separately from IT feasibility — an asset with no connectivity scores low regardless of business value
- Wave 1 should start on the most connected, highest-value plant (lighthouse plant approach)
- Predictive maintenance on rotating equipment is almost always the highest-ROI starting point — prioritise it if data exists
- Digital twin use cases are typically Wave 2/3 — require OT integration and simulation capability that is rarely at Level 1 maturity

## Chain next
- Run `/data-readiness-assessment` on PI historian / MES data for Wave 1 asset-level use cases
- Pass Wave 1 into `/solution-blueprint` — OT architecture decisions are the critical design choices

## PPTX output

After `/ai-use-case-prioritiser` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /ai-use-case-prioritiser output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — AI Use Case Portfolio | Manufacturing"
Slides:
- Slide 1: "Manufacturing AI Portfolio — OEE Impact vs OT Feasibility" — layout: 2×2 matrix (OEE/Cost Impact Y, OT Feasibility X; use case IDs plotted; quadrants: Lighthouse / Strategic / Foundational / OT-Constrained)
  Content: Portfolio Map section — denominate value in OEE points, downtime hours, or scrap %
- Slide 2: "Wave 1 — Lighthouse Plant Rollout" — layout: table (use case, plant, OEE impact, OT dependency, data source, owner, timeline)
  Content: Wave 1 Portfolio section — lighthouse plant first approach
Footer: "[FIRM NAME] | [CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 2-slide branded insert. The "lighthouse plant first" framing on Slide 2 resonates strongly with COOs — it shows a proven path to enterprise scale from a single success.
