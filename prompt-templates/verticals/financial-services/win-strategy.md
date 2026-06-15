---
skill: /win-strategy
pack: Engagement Management
vertical: financial-services
chains-from: (first skill — triggered by qualified opportunity)
chains-into: /commercial-structuring, /narrative-builder
---

# Prompt Template: Win Strategy — Financial Services

**When to use:** Pursuing an AI or digital transformation opportunity at a bank, insurer, or asset manager. FS deals have longer cycles, stronger incumbents, and regulatory approval as a hidden gate.

## Copy-paste prompt

```
Run /win-strategy for [CLIENT NAME]:

Sub-sector: [RETAIL BANKING / CIB / INSURANCE / ASSET MANAGEMENT / PAYMENTS / FINTECH]
Opportunity: [BRIEF — e.g. "AI-assisted credit decisioning transformation, 18-month programme"]
Estimated value: [£X / $X]
Decision timeline: [RFP due: DATE / Award expected: DATE / Regulatory approval needed: Y/N]

FS-specific decision makers:
- [NAME / ROLE] — [stance: champion / neutral / risk] — [hot button]
- Chief Risk Officer / CRO — [stance] — [concern: typically model risk, regulatory exposure]
- Chief Data Officer / CDO — [stance] — [concern: typically data quality, platform consolidation]
- [Board Risk Committee — approval needed: Y/N]

Intelligence on their regulatory posture:
- Recent regulatory actions or findings: [BRIEF — e.g. "FCA supervisory letter on model risk Q4 2025"]
- Regulator relationship: [COOPERATIVE / UNDER SCRUTINY / REMEDIATION]
- How they describe AI risk appetite: [BRIEF — e.g. "Stated 'AI-cautious but outcome-driven' in annual report"]

Incumbent and competitive landscape:
- Current incumbent: [VENDOR / CONSULTING FIRM] — [how long / what they deliver]
- Known competitors for this opportunity: [LIST]
- Competitor FS track record: [BRIEF — e.g. "Competitor A has 3 Tier 1 bank references in credit AI"]
- Our FS track record: [BRIEF — e.g. "Led HSBC AML transformation 2024; reference available"]

Our position:
- FS-specific differentiators: [BRIEF — e.g. "Only firm with active SR 11-7 compliance delivery at scale"]
- Weaknesses in our position: [BRIEF — e.g. "No public reference in insurance; one CIB deal but under NDA"]
- Regulatory relationships that could help: [BRIEF]

Go / No-go: [GO / UNDECIDED / NO-GO]
Reason: [BRIEF]
```

## Expected output
FS-calibrated intelligence summary (including regulatory posture and CRO stance), hot button map with FS-specific angles (regulatory safety, model risk reduction, cost-to-comply), competitor analysis table with FS track record column, win themes addressing FS decision triggers (not just capability), pursuit plan with regulatory approval gate built in.

## FS-specific quality checks
- Win themes must address the CRO's model risk concern, not just business value
- Competitor analysis must include FS reference client count, not just general capabilities
- If regulator approval is needed, pursuit plan must include timeline buffer for that gate
- "Regulatory safe" and "regulator-tested delivery" are often more powerful win themes in FS than "fastest delivery"

## Chain next
- Win themes → `/narrative-builder` to build the proposal narrative with FS regulatory story
- Commercial model → `/commercial-structuring` — FS deals often require risk-sharing or milestone-based pricing to get CRO comfort

## PPTX output

After `/win-strategy` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /win-strategy output for [CLIENT NAME]
Deck title: "[OPPORTUNITY NAME] — Win Strategy | Financial Services"
Slides:
- Slide 1: "Win Themes — FS Edition" — layout: 3–4 cards (win theme title, FS-specific differentiator, proof point with named FS reference where possible)
  Content: Win Themes section — include regulatory angle on each card
- Slide 2: "Competitive Position in FS" — layout: comparison table (evaluation dimension rows × our firm + named competitors; FS reference count row highlighted)
  Content: Competitor Analysis Table with FS track record column
Footer: "INTERNAL — [FIRM NAME] — NOT FOR CLIENT DISTRIBUTION | [DATE]"
```

Produces a 2-slide internal pursuit pack. The FS reference count is the single most-asked question in FS RFP evaluation — make it visible in the competitive position slide.
