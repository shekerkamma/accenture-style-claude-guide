---
skill: /win-strategy
pack: engagement-management
chains-from: (first skill — triggered by qualified opportunity)
chains-into: /commercial-structuring, /narrative-builder
---

# Prompt Template: Win Strategy

**When to use:** As soon as an opportunity is qualified and before the proposal is written. Do not write the proposal until the win strategy is set.

## Copy-paste prompt

```
Run /win-strategy for [CLIENT NAME]:

Opportunity: [BRIEF DESCRIPTION — e.g. "AI-assisted customer service transformation, 18-month programme"]
Estimated value: [£X / $X]
Decision timeline: [RFP due: DATE / Award expected: DATE]
Decision makers:
- [NAME / ROLE] — [stance: champion / neutral / risk] — [hot button]
- [NAME / ROLE] — [stance] — [hot button]

Intelligence gathered so far:
- Why they are buying now: [BRIEF]
- Budget situation: [APPROVED / PENDING / UNKNOWN]
- Prior relationships with our firm: [BRIEF]
- Known incumbent or competition: [LIST]
- What we know about competitor strengths: [BRIEF]
- What we know about their weaknesses as a client: [BRIEF — e.g. "Slow approvals, decision by committee"]

Our position:
- Our relevant track record: [BRIEF]
- Our team available to deploy: [BRIEF]
- Known weaknesses in our position: [BRIEF — e.g. "No reference client in this sub-sector"]

Do we want this work? Go / No-go: [GO / UNDECIDED / NO-GO]
Reason: [BRIEF]
```

## Expected output
Intelligence summary, hot button map, competitor analysis table, win themes (3–4), go/no-go recommendation with rationale, pursuit plan, and win probability assessment.

## Chain next
- Win themes → `/narrative-builder` to build the proposal story
- Commercial model → `/commercial-structuring` to price the engagement

## PPTX output

After `/win-strategy` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /win-strategy output for [CLIENT NAME]
Deck title: "[OPPORTUNITY NAME] — Win Strategy"
Slides:
- Slide 1: "Win Themes" — layout: 3–4 cards (win theme title, differentiator statement, proof point for each)
  Content: Win Themes section — each theme as a card
- Slide 2: "Competitive Position" — layout: comparison table (evaluation dimension rows × our firm + named competitors; our position column highlighted)
  Content: Competitor Analysis Table section
Footer: "INTERNAL — NOT FOR CLIENT DISTRIBUTION | [DATE]"
```

Produces a 2-slide internal pursuit pack insert. These slides go in the pursuit war room, not the client deck. Use INTERNAL footer — the competitive position must not reach the client.
