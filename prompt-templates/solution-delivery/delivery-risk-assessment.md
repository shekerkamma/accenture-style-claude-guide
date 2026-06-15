---
skill: /delivery-risk-assessment
pack: solution-delivery
chains-from: /raid-log, /solution-blueprint
chains-into: /stage-gate-review, /progress-reporting
---

# Prompt Template: Delivery Risk Assessment

**When to use:** At project start and whenever a major risk surfaces — provides a structured risk register beyond the RAID log's tracking function.

## Copy-paste prompt

```
Run /delivery-risk-assessment for [CLIENT NAME]:

Project: [PROJECT NAME]
Assessment date: [YYYY-MM-DD]
Delivery timeline: [START DATE] → [GO-LIVE DATE]

Project context:
- Complexity level: [HIGH / MEDIUM / LOW] and why
- Team size: [N] — [mix: e.g. "3 client, 5 consulting, 2 vendor"]
- Key dependencies: [BRIEF]
- Previous attempts or prior project history: [BRIEF — e.g. "First attempt at SAP integration failed in 2024"]

Provide risk data across these categories (fill in what you know; I will derive the rest):

Technical risks:
- [BRIEF]

Data risks:
- [BRIEF]

People / organisational risks:
- [BRIEF]

Vendor / third-party risks:
- [BRIEF]

Scope and requirements risks:
- [BRIEF]
```

## Expected output
Risks categorised by type, scored P×I (1–5 each), heat map, top 5 critical risks with mandatory mitigation plans, residual risk assessment, and owner assignments.

## Chain next
- Critical risks (score ≥12) must have active mitigations in `/raid-log`
- Risk profile informs the `/stage-gate-review` exit criteria

## PPTX output

After `/delivery-risk-assessment` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /delivery-risk-assessment output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — Delivery Risk Assessment"
Slides:
- Slide 1: "Risk Heat Map" — layout: 5×5 probability-impact matrix with named risks plotted by category (Technical/Data/People/Vendor/Scope)
  Content: Risk Register — P×I scores and categories for all risks
- Slide 2: "Top 5 Risks — Mitigation Plan" — layout: table (risk, category, P×I score, owner, mitigation, residual risk)
  Content: Top 5 Critical Risks section — items scoring ≥12 only
Footer: "[CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 2-slide branded insert. The heat map is the sponsor conversation tool — items in the top-right quadrant require mandatory mitigation (score ≥12).
