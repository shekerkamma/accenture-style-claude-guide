---
skill: /post-implementation-review
pack: solution-delivery
chains-from: /benefits-register, /hypercare-plan
chains-into: /continuous-improvement-backlog, /performance-review, /operating-rhythm-design
---

# Prompt Template: Post-Implementation Review

**When to use:** 90 days after go-live — compare actual performance against the business case and identify what needs to change to fully realise the benefits.

## Copy-paste prompt

```
Run /post-implementation-review for [CLIENT NAME]:

Project: [PROJECT NAME]
Go-live date: [DATE]
Review date: [DATE] (should be ~90 days post go-live)

Benefits actuals vs business case:
[For each benefit from the /benefits-register:]
1. [BENEFIT NAME]
   - Business case target (90-day): [VALUE]
   - Actual (90-day): [VALUE]
   - Variance: [% above/below target]
   - Reason for variance: [BRIEF, if known]

2. [BENEFIT NAME]
   [same structure...]

Adoption status:
- Active users vs target: [N actual / N target]
- Key adoption barriers still present: [LIST]

Issues encountered post go-live:
- [ISSUE] — [impact] — [status: resolved / ongoing]

Team and stakeholder feedback:
- [BRIEF summary of feedback from end users, management, sponsor]

What we would do differently:
- [LIST — from the delivery team's perspective]
```

## Expected output
90-day actuals vs business case table, variance analysis with five-why root cause for underperforming benefits, forward actions register (with owners and dates), and revised forecast to full benefit realisation.

## Chain next
- Enhancement opportunities → `/continuous-improvement-backlog`
- Benefits tracking cadence → `/performance-review` (quarterly)
- BAU governance → `/operating-rhythm-design`

## PPTX output

After `/post-implementation-review` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /post-implementation-review output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — Post-Implementation Review (90 days)"
Slides:
- Slide 1: "90-Day Actuals vs Business Case" — layout: table (benefit, business case target, 90-day actual, variance %, RAG, root cause summary)
  Content: Benefits Actuals vs Business Case section — all benefits
- Slide 2: "Lessons Learned & Forward Actions" — layout: two-column (What Worked / What to Change) above actions table (action, owner, due date, status)
  Content: Variance Analysis root causes + Forward Actions Register sections
Footer: "[FIRM NAME] | [CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 2-slide branded insert. This is the primary sponsor artefact at 90 days — Slide 1 demonstrates investment return, Slide 2 shows team accountability.
