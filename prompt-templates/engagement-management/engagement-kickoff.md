---
skill: /engagement-kickoff
pack: engagement-management
chains-from: /commercial-structuring, /raci-design
chains-into: /stakeholder-cadence, /progress-reporting
---

# Prompt Template: Engagement Kick-Off

**When to use:** In the week before the engagement starts — plan the kick-off meeting and the first 30 days to create momentum and establish governance from day one.

## Copy-paste prompt

```
Run /engagement-kickoff for [CLIENT NAME]:

Engagement: [NAME]
Start date: [DATE]
Kick-off meeting date: [DATE]
Duration: [N months]

Attendees (for the kick-off meeting):
- Client: [LIST names/roles]
- Consulting team: [LIST names/roles]

Scope agreed (from proposal / contract):
- Workstreams: [LIST]
- Key milestones: [LIST with dates]
- Out of scope (explicitly): [LIST]

Known risks or sensitivities at day 1:
- [e.g. "Key client SME is unavailable for 3 weeks from start"]
- [e.g. "Client is simultaneously running another transformation — bandwidth risk"]
- [e.g. "Cultural tension between IT and business — needs careful navigation"]

Governance preferences:
- Client's preferred meeting cadence: [BRIEF or UNKNOWN]
- Executive sponsor availability: [BRIEF]
- Client's preferred communication style: [e.g. "Weekly status email, no surprise escalations"]
```

## Expected output
Kick-off meeting agenda, governance cadence design, ways of working charter, 30-day action plan with owner/date, RACI summary, escalation path, and communications drumbeat.

## Chain next
- Governance design → `/stakeholder-cadence` to build out the full forum architecture
- 30-day plan → tracks via `/progress-reporting` from Week 1

## PPTX output

After `/engagement-kickoff` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /engagement-kickoff output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — Engagement Kick-Off"
Slides:
- Slide 1: "Governance & Ways of Working" — layout: two-column (Governance Cadence table left / Ways of Working charter right)
  Content: Governance Cadence Design + Ways of Working Charter sections
- Slide 2: "30-Day Action Plan" — layout: table (action, owner, due date, dependencies)
  Content: 30-Day Action Plan section — all items with owner and date
Footer: "[FIRM NAME] | [CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 2-slide kick-off pack insert. Share with all attendees on Day 1. These slides establish accountability from the first meeting.
