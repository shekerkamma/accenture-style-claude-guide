---
skill: /raid-log
pack: solution-delivery
chains-from: /solution-blueprint, /integration-sequencing, /responsible-ai-framework
chains-into: /stage-gate-review, /delivery-risk-assessment, /progress-reporting
---

# Prompt Template: RAID Log

**When to use:** At project kick-off to establish the log, then updated weekly. Pass new risks from any other skill into this log.

## Copy-paste prompt

```
Run /raid-log for [CLIENT NAME]:

Project: [PROJECT NAME]
Phase: [INITIATION / PLANNING / DELIVERY / HYPERCARE]
Log date: [YYYY-MM-DD]

Populate the RAID log from the following sources:

Risks identified (from workshops, prior skills, or known context):
- [RISK 1] — [probability H/M/L] — [impact H/M/L] — [owner] — [proposed mitigation]
- [RISK 2] — ...

Assumptions we are operating under:
- [ASSUMPTION 1] — [if false, consequence is...] — [how we will validate]
- [ASSUMPTION 2] — ...

Issues currently open (things that have already materialised):
- [ISSUE 1] — [raised: DATE] — [impact] — [owner] — [current status]

Dependencies on external parties:
- [DEPENDENCY 1] — [depends on: WHO/WHAT] — [needed by: DATE] — [status]
- [DEPENDENCY 2] — ...
```

## Expected output
Structured RAID log with RAG status per item, P×I risk scores (1–5 scale), mandatory mitigation flag for scores ≥12, owner column, and weekly review cadence.

## Chain next
- Items scoring High go into `/delivery-risk-assessment` for deeper analysis
- Open risks and issues feed the `/progress-reporting` dashboard weekly

## PPTX output

After `/raid-log` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /raid-log output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — RAID Summary"
Slides:
- Slide 1: "RAID Summary — [DATE]" — layout: 4-quadrant grid (Risks / Assumptions / Issues / Dependencies; top 3 HIGH-rated items per quadrant with RAG dot)
  Content: all four RAID sections — top 3 items per quadrant by severity
Footer: "[FIRM NAME] | [CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 1-slide branded insert for every progress reporting pack. Refresh weekly. The 4-quadrant layout gives steering committees a complete delivery health picture at a glance.
