---
skill: /ai-use-case-prioritiser
pack: ai-transformation
chains-from: /ai-maturity-assessment, /strategic-options
chains-into: /data-readiness-assessment, /solution-blueprint
---

# Prompt Template: AI Use Case Prioritiser

**When to use:** When a long list of AI use cases must be narrowed to a funded, sequenced portfolio — typically after a discovery workshop or benchmarking exercise.

## Copy-paste prompt

```
Run /ai-use-case-prioritiser for [CLIENT NAME]:

Long list of candidate use cases ([N] total):
1. [USE CASE] — [DOMAIN] — [BRIEF DESCRIPTION]
2. [USE CASE] — [DOMAIN] — [BRIEF DESCRIPTION]
[... continue for all use cases]

Organisation context:
- AI maturity level: [1–4 from /ai-maturity-assessment, or UNKNOWN]
- Strategic priorities for this year: [LIST — e.g. "cost reduction, customer retention, speed to market"]
- Executive hot buttons: [e.g. "CFO wants cost out; CTO wants platform modernisation"]
- Known constraints: [e.g. "budget cap £2M, must show ROI within 12 months, GDPR sensitivity in customer data"]
- Competitor AI moves: [BRIEF — e.g. "Competitor A just launched AI pricing engine"]

Scoring guidance:
- Prioritise use cases that can show value within 90 days for Wave 1
- Flag any use cases with data readiness concerns
```

## Expected output
Scored register (Value × Feasibility), 2×2 portfolio map with IDs in each quadrant, Wave 1/2/3 portfolio with owners, parking lot with reasons, portfolio balance check, and recommended first mobilisation.

## Chain next
- Run `/data-readiness-assessment` on Wave 1 use cases to confirm data is ready
- Pass Wave 1 into `/solution-blueprint` to design the delivery

## PPTX output

After `/ai-use-case-prioritiser` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /ai-use-case-prioritiser output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — AI Use Case Portfolio"
Slides:
- Slide 1: "Use Case Portfolio — Value vs Feasibility" — layout: 2×2 matrix with use case IDs plotted in each quadrant (Quick Wins / Strategic Bets / Low Priority / Foundation)
  Content: Portfolio Map section — use case IDs and positions by quadrant
- Slide 2: "Wave 1 Portfolio" — layout: table (use case, domain, value score, feasibility score, Wave, owner, timeline)
  Content: Wave 1 Portfolio section — funded and sequenced use cases
Footer: "[FIRM NAME] | [CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 2-slide branded insert. The 2×2 is the key strategic conversation starter — clients immediately debate which quadrant to prioritise.
