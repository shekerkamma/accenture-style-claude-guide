---
skill: /integration-sequencing
pack: solution-delivery
chains-from: /solution-blueprint
chains-into: /raid-log, /stage-gate-review
---

# Prompt Template: Integration Sequencing

**When to use:** Once the solution blueprint identifies which systems must be integrated — sequence the integration work to de-risk the delivery and enable early testing.

## Copy-paste prompt

```
Run /integration-sequencing for [CLIENT NAME]:

Systems to be integrated (from /solution-blueprint):
1. [SYSTEM A] — [type: source / target / bidirectional] — [data / events being exchanged]
2. [SYSTEM B] — [type] — [data / events]
3. [SYSTEM C] — [type] — [data / events]

Integration constraints:
- API availability: [LIST any systems with limited/no APIs]
- Access restrictions: [e.g. "SAP requires OData v4; no direct DB writes"]
- Data sensitivity: [e.g. "PII must stay in EU region"]
- Throughput requirements: [BRIEF]
- Downtime constraints: [e.g. "SAP has 4-hour maintenance window Sundays"]

Timeline:
- Overall delivery timeline: [BRIEF]
- First thin thread target date: [DATE]
- Full integration target date: [DATE]

Known dependencies between integrations:
- [e.g. "System B integration cannot start until System A auth is resolved"]
```

## Expected output
Thin thread identification, P1/P2/P3 integration phases, dependency map, test gate specification per phase, rollback positions, and critical path with top risks.

## Chain next
- Add integration risks to `/raid-log`
- Use phase dates to populate `/stage-gate-review` schedule

## PPTX output

After `/integration-sequencing` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /integration-sequencing output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — Integration Sequencing"
Slides:
- Slide 1: "Integration Phases" — layout: phase table (Phase, System Pair, Data/Events Exchanged, Dependency, Test Gate, Target Date)
  Content: P1/P2/P3 Integration Phases section
- Slide 2: "Critical Path & Top Risks" — layout: table (integration, critical path flag, top risk, rollback position)
  Content: Critical Path + Risk sections
Footer: "[CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 2-slide branded insert. Use Slide 1 as the integration plan anchor in the stage gate pack for each wave.
