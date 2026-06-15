---
skill: /architecture-decision-record
pack: solution-delivery
chains-from: /solution-blueprint
chains-into: /solution-blueprint (updated), /raid-log
---

# Prompt Template: Architecture Decision Record

**When to use:** Any time a major technical decision is made during delivery — one ADR per significant decision. Typical triggers: model selection, data storage architecture, integration pattern, build-vs-buy for a component.

## Copy-paste prompt

```
Run /architecture-decision-record for [CLIENT NAME]:

Decision title: [SHORT TITLE — e.g. "Vector database selection for enterprise RAG"]

Context:
- What problem are we solving: [BRIEF]
- Why this decision matters now: [BRIEF]
- What are the constraints: [LIST — e.g. "Must run in Azure, must be enterprise-supported, budget < £X/month"]

Options under consideration:
1. [OPTION A] — [brief description]
2. [OPTION B] — [brief description]
3. [OPTION C, if any]

Our current lean:
- Preferred option: [A / B / C / UNDECIDED]
- Reason for lean: [BRIEF]

Stakeholders who need to ratify this decision:
- [ROLE] — [organisation] — [stance: informed / consulted / decision-maker]
```

## Expected output
ADR document in standard format: context, options with pros/cons, decision, rationale, consequences, open questions, and review trigger condition.

## Chain next
- Update `/solution-blueprint` where the decision affects the design
- Add any risks identified during the decision to `/raid-log`

## PPTX output

After `/architecture-decision-record` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /architecture-decision-record output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — ADR: [DECISION TITLE]"
Slides:
- Slide 1: "ADR: [DECISION TITLE]" — layout: structured card (Context, Options Considered, Decision Taken, Rationale, Consequences — each in a labelled box)
  Content: full ADR document — all sections in order
Footer: "[CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 1-slide branded insert per decision. Run once per major ADR from the /solution-blueprint. Stack ADR slides into the architecture section of the engagement deck — one slide per decision.
