---
skill: /commercial-structuring
pack: engagement-management
chains-from: /win-strategy
chains-into: /business-case-builder (client ROI), /engagement-kickoff
---

# Prompt Template: Commercial Structuring

**When to use:** After the win strategy is set and before the proposal is costed — design the fee model, build the resource plan, and run the margin scenarios.

## Copy-paste prompt

```
Run /commercial-structuring for [CLIENT NAME]:

Opportunity: [BRIEF]
Duration: [N months]
Win themes (from /win-strategy): [LIST]

Scope summary:
- Workstreams: [LIST]
- Key deliverables: [LIST]
- Number of client sites / locations: [N]
- Travel expectation: [BRIEF]

Resource plan (best estimate):
- [ROLE] — [# FTE] — [start phase] — [end phase]
- [ROLE] — [# FTE] — [start phase] — [end phase]
[continue...]

Commercial constraints:
- Client budget ceiling (if known): [£X or UNKNOWN]
- Client preferred commercial model: [T&M / Fixed / Outcome / Retainer / UNKNOWN]
- Our firm's target margin for this type of work: [%]
- Discounting tolerance: [BRIEF — e.g. "Up to 10% with approval"]
- Payment terms preference: [BRIEF]

Strategic factors:
- Is this a beachhead / loss-leader opportunity? [Y/N] — [reason]
- Is there a volume / long-term relationship angle? [BRIEF]
```

## Expected output
Commercial model options (3), resource plan, P&L at three scenarios (base/stretch/downside), negotiation brief with walk-away price, client value proposition framing, and recommended commercial model.

## Chain next
- Client value case → `/business-case-builder` for client-facing ROI
- Agreed commercial structure informs the `/engagement-kickoff` ways of working

## PPTX output

After `/commercial-structuring` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /commercial-structuring output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — Commercial Structuring"
Slides:
- Slide 1: "Commercial Model Options" — layout: 3-column comparison table (model name, structure, total value, margin %, recommended flag)
  Content: Commercial Model Options section — all 3 options with recommended highlighted
- Slide 2: "Negotiation Brief" — layout: table (item, our target, acceptable range, walk-away, rationale)
  Content: Negotiation Brief section
Footer: "INTERNAL — NOT FOR CLIENT DISTRIBUTION | [DATE]"
```

Produces a 2-slide internal commercial pack. Mark footer as INTERNAL — the negotiation brief must never reach the client.
