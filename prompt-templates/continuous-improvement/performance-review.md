---
skill: /performance-review
pack: continuous-improvement
chains-from: /operating-rhythm-design, /benefits-register
chains-into: /continuous-improvement-backlog, /growth-barriers (if underperforming)
---

# Prompt Template: Performance Review

**When to use:** Monthly or quarterly — run the formal performance review against KPI targets and drive corrective actions for anything more than 10% off track.

## Copy-paste prompt

```
Run /performance-review for [CLIENT NAME]:

Solution / capability: [NAME]
Review period: [MONTH/QUARTER ending DATE]
Review type: [MONTHLY check-in / QUARTERLY business review (QBR)]

KPI actuals (fill in what you have; flag missing data):
| KPI | Target | Actual | Variance | Trend vs Prior Period |
|---|---|---|---|---|
| [KPI 1] | [TARGET] | [ACTUAL] | | |
| [KPI 2] | [TARGET] | [ACTUAL] | | |
[continue for all KPIs from /benefits-register...]

Benefits realisation update:
- Benefits on track: [LIST]
- Benefits at risk (>10% below target): [LIST with variance]
- Benefits overperforming: [LIST — to understand and replicate]

Known factors affecting performance this period:
- [e.g. "Volume spike in October increased processing load — manual workaround in place"]
- [e.g. "Model accuracy dropped after data schema change on 2026-10-12"]

Open actions from prior review:
| Action | Owner | Due | Status |
|---|---|---|---|
| [ACTION] | [NAME] | [DATE] | [OPEN/CLOSED/DELAYED] |
```

## Expected output
KPI scorecard with RAG and trend arrows, benefits update (on-track/at-risk/overperforming), variance root-cause analysis for any >10% miss, forward corrective actions (with owners and dates), and trend assessment.

## Chain next
- Structural underperformance (2+ consecutive quarters) → `/growth-barriers` (strategy-consulting)
- Enhancement opportunities → `/continuous-improvement-backlog`

## PPTX output

After `/performance-review` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /performance-review output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — Performance Review: [PERIOD]"
Slides:
- Slide 1: "KPI Scorecard — [PERIOD]" — layout: table (KPI, target, actual, variance %, trend arrow, RAG, owner)
  Content: KPI Scorecard section — all KPIs with actuals and RAG
- Slide 2: "Corrective Actions" — layout: table (KPI at risk, root cause, corrective action, owner, due date)
  Content: Forward Corrective Actions section — KPIs more than 10% off target only; omit this slide if all KPIs are on track
Footer: "[FIRM NAME] | [CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 1–2-slide QBR pack insert. Replace both slides each review cycle. Slide 2 only when corrective action is required.
