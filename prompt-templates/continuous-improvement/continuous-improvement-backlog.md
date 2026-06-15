---
skill: /continuous-improvement-backlog
pack: continuous-improvement
chains-from: /performance-review, /post-implementation-review
chains-into: /initiative-prioritizer, /transformation-roadmap (if major wave needed)
---

# Prompt Template: Continuous Improvement Backlog

**When to use:** Ongoing post go-live — capture, score, and sequence enhancement ideas to prevent the solution from stagnating.

## Copy-paste prompt

```
Run /continuous-improvement-backlog for [CLIENT NAME]:

Solution / capability: [NAME]
Backlog review date: [DATE]

New improvement ideas to add (from this period):
1. [IDEA] — [source: user feedback / performance review / team observation] — [brief description]
2. [IDEA] — [source] — [brief description]
[continue for all new ideas...]

Existing backlog items (if updating an existing backlog — list current items with status):
| ID | Item | Current Score | Status | Owner |
|---|---|---|---|---|
| CI-001 | [ITEM] | [SCORE] | [In Progress/Backlog/Parked] | [NAME] |
[continue...]

Scoring context:
- Business priorities this quarter: [BRIEF — e.g. "Cost reduction is the focus; growth initiatives deprioritised until Q2"]
- Capacity for improvement work: [e.g. "BAU team has ~20% bandwidth available for improvement"]
- Regulatory deadlines affecting priority: [BRIEF]

Ideas that should be parked regardless of score:
- [IDEA] — [reason: e.g. "Requires data access not available until 2027"]
```

## Expected output
Scored backlog (Score = Value + Urgency + (6-Effort) + Risk, each 1–5), Horizon 1/2/3 classification, sequenced roadmap for Horizon 1, parking lot with reasons, and review cadence recommendation.

## Chain next
- Horizon 1 items → integrate into the sprint/delivery plan
- Large Horizon 2/3 clusters → `/transformation-roadmap` to plan the next improvement wave

## PPTX output

After `/continuous-improvement-backlog` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /continuous-improvement-backlog output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — CI Backlog: [DATE]"
Slides:
- Slide 1: "Improvement Backlog" — layout: table (ID, improvement idea, horizon, composite score, owner, status) sorted by score descending
  Content: Scored Backlog section — Horizon 1 and 2 items only (Horizon 3 is parking lot, exclude)
Footer: "[FIRM NAME] | [CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 1-slide BAU governance insert. Include in the monthly performance review pack. It signals to the client that the improvement pipeline is active and managed, not stagnating.
