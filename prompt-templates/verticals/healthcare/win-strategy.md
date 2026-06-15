---
skill: /win-strategy
pack: Engagement Management
vertical: healthcare
chains-from: (first skill — triggered by qualified opportunity)
chains-into: /commercial-structuring, /narrative-builder
---

# Prompt Template: Win Strategy — Healthcare & Life Sciences

**When to use:** Pursuing an AI or digital health transformation at a hospital system, health insurer, or pharma/biotech company. HC deals are won on clinical credibility and trust, not just technical capability.

## Copy-paste prompt

```
Run /win-strategy for [CLIENT NAME]:

Sub-sector: [HOSPITAL SYSTEM / HEALTH INSURER / PHARMA / BIOTECH / MEDTECH]
Opportunity: [BRIEF — e.g. "Clinical AI strategy and deployment programme, radiology and care management, 24 months"]
Estimated value: [£X / $X]
Decision timeline: [RFP due: DATE / Award expected: DATE / Board approval cycle: BRIEF]

HC-specific decision makers:
- [NAME / ROLE] — [stance] — [hot button]
- Chief Medical Officer / CMO — [stance] — [concern: typically clinical safety, clinician workflow disruption, liability]
- Chief Nursing Officer / CNO — [stance] — [concern: typically frontline adoption, nurse workload]
- Chief Information Officer / CIO — [stance] — [concern: typically EHR integration, Epic/Cerner compatibility]
- [Clinical Ethics Board / IRB — approval needed: Y/N]
- [Board / NHS Trust Board — sign-off needed: Y/N]

Clinical credibility signals we have (or lack):
- Named clinical AI deployments we can reference: [LIST — include use case, organisation, outcomes if shareable]
- Clinical partners or physician champions we can leverage: [BRIEF]
- Peer-reviewed publications or NHS/FDA validation studies: [LIST or NONE]
- Known weaknesses: [BRIEF — e.g. "No reference in community health; all our wins are acute"]

Competitive landscape:
- Known competitors: [LIST — include their HC AI track record]
- Incumbent provider: [NAME / what they deliver / how long]
- Client's prior AI experience: [BRIEF — e.g. "Failed Epic AI rollout in 2023 — left clinical staff distrustful"]

Go / No-go: [GO / UNDECIDED / NO-GO]
Reason: [BRIEF]
```

## Expected output
HC-calibrated intelligence summary (including CMO stance and clinical safety posture), hot button map with HC angles (patient safety first, clinician adoption, Epic integration, NHS compliance), competitor analysis with clinical reference count, win themes addressing clinical credibility and outcomes evidence (not just technology), pursuit plan with clinical governance gate built in.

## HC-specific quality checks
- Win themes must address the CMO's clinical safety concern — "AI that clinicians trust" is often stronger than "AI that's accurate"
- If the client had a prior AI failure, win themes must directly address that trust deficit
- Clinical reference clients (by name or anonymised use case) are the most powerful win differentiator in HC
- Commercial model must account for clinical validation period — milestone payments tied to clinical sign-off, not technical go-live

## Chain next
- Win themes → `/narrative-builder` — lead with patient outcomes, not technology features
- Commercial model → `/commercial-structuring` — consider outcomes-based pricing tied to clinical metrics

## PPTX output

After `/win-strategy` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /win-strategy output for [CLIENT NAME]
Deck title: "[OPPORTUNITY NAME] — Win Strategy | Healthcare"
Slides:
- Slide 1: "Win Themes — Clinical Credibility Edition" — layout: 3–4 cards (win theme, clinical differentiator, outcomes evidence with named or anonymised HC reference)
  Content: Win Themes section — emphasise clinical outcomes and named references
- Slide 2: "Competitive Position in HC AI" — layout: comparison table (dimension rows × our firm + competitors; clinical reference count and use case match rows highlighted)
  Content: Competitor Analysis Table with HC track record column
Footer: "INTERNAL — [FIRM NAME] — NOT FOR CLIENT DISTRIBUTION | [DATE]"
```

Produces a 2-slide internal pursuit pack. Clinical reference clients are the single most-asked question in HC RFPs — make it the first row of the competitive position slide.
