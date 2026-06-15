---
skill: /stakeholder-cadence
pack: engagement-management
chains-from: /engagement-kickoff, /raci-design
chains-into: /progress-reporting, /stakeholder-alignment
---

# Prompt Template: Stakeholder Cadence

**When to use:** In the first week of delivery — design the architecture of meetings and forums that will govern the engagement from kickoff to closeout.

## Copy-paste prompt

```
Run /stakeholder-cadence for [CLIENT NAME]:

Engagement: [NAME]
Duration: [N months]

Stakeholders to manage:
1. [NAME / ROLE] — [organisation] — [interest: sponsor / decision-maker / impacted / informed] — [availability: weekly / monthly / quarterly]
2. [NAME / ROLE] — [organisation] — [interest] — [availability]
[continue for all stakeholders...]

Current pain points in governance (if known):
- [e.g. "Previous engagements had too many status meetings — client fatigued"]
- [e.g. "Sponsor is time-poor — needs concise 30-minute monthly touchpoints"]
- [e.g. "Working-level team meets daily but decisions get stuck without sponsor access"]

Delivery rhythm:
- Sprint / delivery cadence: [BRIEF — e.g. "2-week sprints"]
- Key milestones requiring stakeholder input: [LIST with dates]
- Decision points requiring executive approval: [LIST with dates]
```

## Expected output
Forum architecture (governance vs. collaboration forums), agenda template per forum, escalation path, stakeholder engagement plan, and cadence calendar for the first 90 days.

## Chain next
- Forum architecture feeds into the weekly `/progress-reporting` cycle
- Exec engagement model connects to `/stakeholder-alignment` for difficult moments

## PPTX output

After `/stakeholder-cadence` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /stakeholder-cadence output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — Stakeholder Cadence"
Slides:
- Slide 1: "Forum Architecture" — layout: table (forum name, purpose, frequency, participants, chair, agenda template)
  Content: Forum Architecture section — all governance and collaboration forums
Footer: "[CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 1-slide branded insert. Attach to the kick-off pack and update if forums change. A single clear table prevents meeting proliferation throughout the engagement.
