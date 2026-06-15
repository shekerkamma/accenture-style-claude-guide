---
skill: /win-strategy
pack: Engagement Management
vertical: manufacturing
chains-from: (first skill — triggered by qualified opportunity)
chains-into: /commercial-structuring, /narrative-builder
---

# Prompt Template: Win Strategy — Manufacturing & Industrial

**When to use:** Pursuing an Industry 4.0, AI, or digital manufacturing opportunity at a discrete or process manufacturer. Manufacturing deals are won on OT credibility, lighthouse references, and the ability to work with plant teams — not just strategy slides.

## Copy-paste prompt

```
Run /win-strategy for [CLIENT NAME]:

Sub-sector: [AUTOMOTIVE / AEROSPACE / PROCESS / DISCRETE / CONSUMER GOODS / INDUSTRIAL EQUIPMENT]
Opportunity: [BRIEF — e.g. "AI-driven predictive maintenance and quality inspection programme, 5 plants, 30 months"]
Estimated value: [£X / $X]
Decision timeline: [RFP due: DATE / Award expected: DATE / CapEx approval cycle: BRIEF]

Manufacturing-specific decision makers:
- [NAME / ROLE] — [stance] — [hot button]
- Chief Operating Officer / COO — [stance] — [concern: typically OEE, downtime, CapEx ROI]
- VP Manufacturing / VP Operations — [stance] — [concern: typically plant disruption, crew resistance]
- CIO / Head of Digital — [stance] — [concern: typically OT security, IT/OT architecture, ERP integration]
- Plant Managers (if separate) — [stance] — [concern: typically "not invented here", change burden]
- [CapEx Committee — approval threshold and timeline]

Industrial credibility signals we have (or lack):
- Named manufacturing AI deployments we can reference: [LIST — sub-sector, use case, OEE or cost outcome]
- OT vendors we have proven integrations with: [e.g. "Siemens MindSphere", "AVEVA PI", "OSIsoft PI", "Rockwell FactoryTalk"]
- Lighthouse plant methodology: [Y/N — do we have a proven fast-to-value, plant-first approach]
- Weaknesses: [BRIEF — e.g. "Strong in process; no discrete automotive references"]

Competitive landscape:
- Known competitors: [LIST — include their manufacturing AI / OT track record]
- Incumbent provider: [NAME / what they deliver]
- Likely OT vendor play: [BRIEF — e.g. "Siemens and Rockwell will each push their own AI platforms"]
- SI / OT integrator competition: [BRIEF]

Go / No-go: [GO / UNDECIDED / NO-GO]
Reason: [BRIEF]
```

## Expected output
Manufacturing-calibrated intelligence summary (including COO OEE ambition and plant manager stance), hot button map with industrial angles (OEE uplift, downtime reduction, scrap reduction, safety improvement), competitor analysis with manufacturing reference count and OT vendor alignment, win themes anchored in proven plant outcomes (not theoretical ROI), pursuit plan with CapEx approval gate built in.

## Manufacturing-specific quality checks
- Win themes must quantify OEE or cost impact in the first line — manufacturing executives do not read past abstract value statements
- Competitor analysis must include OT platform partnership row — who owns the Siemens / Rockwell / Honeywell relationship matters enormously
- If client has a CapEx approval cycle, pursuit plan must include timeline for that gate and pre-CapEx approval activities
- "Lighthouse plant fast, then scale" is almost always the strongest manufacturing win theme — if we have a reference for it, use it

## Chain next
- Win themes → `/narrative-builder` — lead with OEE outcome from reference client, not with technology platform
- Commercial model → `/commercial-structuring` — consider outcome-based pricing tied to OEE improvement or downtime reduction

## PPTX output

After `/win-strategy` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /win-strategy output for [CLIENT NAME]
Deck title: "[OPPORTUNITY NAME] — Win Strategy | Manufacturing"
Slides:
- Slide 1: "Win Themes — Industrial Outcomes Edition" — layout: 3–4 cards (win theme, OEE or cost outcome claim, named or anonymised manufacturing reference, OT platform credibility)
  Content: Win Themes section — denominate every theme in OEE, cost, or throughput terms
- Slide 2: "Competitive Position in Manufacturing AI" — layout: comparison table (dimension rows × our firm + competitors; OT platform partnerships and manufacturing reference rows highlighted)
  Content: Competitor Analysis Table with manufacturing track record and OT platform alignment
Footer: "INTERNAL — [FIRM NAME] — NOT FOR CLIENT DISTRIBUTION | [DATE]"
```

Produces a 2-slide internal pursuit pack. OEE outcomes and OT platform partnerships are the two columns COOs look at first in any competitive comparison — make both visible.
