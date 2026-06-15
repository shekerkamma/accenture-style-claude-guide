---
skill: /stage-gate-review
pack: solution-delivery
chains-from: /integration-sequencing, /raid-log
chains-into: /progress-reporting, /post-implementation-review
---

# Prompt Template: Stage Gate Review

**When to use:** At the end of each defined delivery phase — assess whether the work meets the exit criteria to advance, and what conditions or blockers exist.

## Copy-paste prompt

```
Run /stage-gate-review for [CLIENT NAME]:

Gate: [GATE NAME — e.g. "Alpha", "Beta", "Go-Live", "Post-hypercare"]
Review date: [YYYY-MM-DD]
Reviewing team: [LIST key attendees]

Exit criteria for this gate (from delivery plan):
1. [CRITERION] — [Met / Partially Met / Not Met] — [evidence]
2. [CRITERION] — [Met / Partially Met / Not Met] — [evidence]
3. [CRITERION] — ...

Current status summary:
- What is complete: [BRIEF]
- What is outstanding: [LIST]
- Open RAID items affecting this gate: [LIST IDs or brief descriptions]
- Quality / test results: [BRIEF — e.g. "UAT: 94% pass rate, 2 P1 defects open"]

Stakeholder positions:
- [SPONSOR / ROLE] — [supportive / neutral / concerned] — [concern if any]
```

## Expected output
Gate verdict (Go / Go with Conditions / No-Go), exit criteria scorecard, mandatory conditions if conditional go, lessons captured, and updated delivery plan with next gate.

## Chain next
- Conditions from a conditional Go → open items in `/raid-log`
- Post go-live gate → initiate `/hypercare-plan`

## PPTX output

After `/stage-gate-review` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /stage-gate-review output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — Stage Gate: [GATE NAME]"
Slides:
- Slide 1: "Gate [NAME] Verdict" — layout: scorecard (criterion rows, Met/Partial/Not Met columns, RAG, evidence; verdict banner at top: GO / CONDITIONAL GO / NO-GO)
  Content: Exit Criteria Scorecard + Gate Verdict sections
- Slide 2: "Conditions & Next Steps" — layout: table (condition, owner, due date, resolution plan) — include only for Conditional Go or No-Go verdicts
  Content: Mandatory Conditions + Updated Delivery Plan sections
Footer: "[FIRM NAME] | [CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 1–2-slide branded insert. Slide 2 only needed when the verdict is Conditional Go or No-Go.
