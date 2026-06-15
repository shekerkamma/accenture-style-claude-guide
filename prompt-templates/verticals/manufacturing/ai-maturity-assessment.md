---
skill: /ai-maturity-assessment
pack: AI & Digital Transformation
vertical: manufacturing
chains-from: /situation-assessment
chains-into: /ai-use-case-prioritiser, /data-readiness-assessment
---

# Prompt Template: AI Maturity Assessment — Manufacturing & Industrial

**When to use:** Start of any AI engagement at a discrete or process manufacturer, industrial conglomerate, or automotive/aerospace supplier — before recommending investments, use cases, or operating model changes.

## Copy-paste prompt

```
Run /ai-maturity-assessment for [CLIENT NAME]:

Organisation: [NAME]
Sub-sector: [AUTOMOTIVE / AEROSPACE & DEFENCE / PROCESS MANUFACTURING (chemicals, pharma mfg) / DISCRETE MANUFACTURING / CONSUMER GOODS / INDUSTRIAL EQUIPMENT / MINING / ENERGY & UTILITIES]
Size: [EMPLOYEE COUNT / NUMBER OF PLANTS / ANNUAL REVENUE]
Scope: [Whole enterprise / [PLANT NAME or MANUFACTURING NETWORK] / [PRODUCT LINE] only]

Operational technology context:
- Plant / shop floor systems: [e.g. "Siemens S7 PLCs", "Rockwell ControlLogix", "mixed legacy PLCs"]
- MES (Manufacturing Execution System): [e.g. "SAP ME", "Siemens Opcenter", "Rockwell Plex", "none"]
- SCADA / historian: [e.g. "GE iFIX", "Wonderware InTouch / AVEVA", "OSIsoft PI System / AVEVA PI"]
- ERP: [SAP S/4HANA / SAP ECC / Oracle / Microsoft Dynamics]
- IT/OT integration: [EXISTS / PARTIAL / NOT CONNECTED — specify if OT is air-gapped]
- IoT connectivity: [e.g. "80% of assets connected via Azure IoT Hub", "majority of floor unconnected", "MQTT broker on-prem"]

What we know about their AI today:
- Data infrastructure: [e.g. "Azure Data Lake with Databricks; PI data available but siloed"]
- AI tools in use: [e.g. "SAP AI Core for demand planning", "Azure ML for quality inspection pilot", "vendor predictive maintenance (Aspentech, SparkCognition)"]
- Known AI initiatives: [LIST — e.g. "Pilot predictive maintenance on Line 3 — running for 6 months"]
- AI governance / ethics policy: [EXISTS / DOESN'T EXIST]
- OT security posture: [BRIEF — e.g. "IEC 62443 Level 2 certification achieved; cyber-physical risk is primary concern"]
- Culture / leadership attitude: [BRIEF — e.g. "Plant managers resist data extraction; corporate IT wants centralised; tension is blocking progress"]

Assessment purpose: [e.g. "Inform the Industry 4.0 AI roadmap" / "Prepare the CapEx investment case for smart factory"]
```

## Expected output
Maturity scorecard (5 dimensions × 1–4 scale) with manufacturing-specific evidence (IT/OT integration depth, PI System coverage, MES/ERP data availability, OT security maturity, plant manager adoption), dimension deep-dives with industrial peer benchmarks, and 2–3 priority investments calibrated to the OT environment and CapEx cycle.

## Manufacturing-specific quality checks
- Data dimension must assess IT/OT integration separately from IT data maturity — the PI historian and MES are often better sources than the ERP
- Technology dimension must flag OT security (IEC 62443) as a constraint on AI deployment architecture — cloud connectivity from plant floor may be restricted
- Culture dimension must assess plant manager vs corporate IT tension — this is the most common failure mode in manufacturing AI
- Any "Leading" score in Technology must validate that OT connectivity actually exists at asset level, not just in the historian

## Chain next
- Proceed to `/ai-use-case-prioritiser` using the manufacturing use case library (predictive maintenance, quality inspection, demand forecasting, energy optimisation, supply chain)
- Run `/data-readiness-assessment` on PI System / MES data before committing to asset-level use cases

## PPTX output

After `/ai-maturity-assessment` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /ai-maturity-assessment output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — AI Maturity Assessment | Manufacturing"
Slides:
- Slide 1: "AI Maturity Scorecard" — layout: scorecard matrix (5 dimension rows × 4 level columns; shade current level per dimension; add industrial peer benchmark row at bottom)
  Content: Maturity Scorecard + Peer Benchmark sections
- Slide 2: "Priority Investments — OT-Aware Roadmap" — layout: 3 cards (investment, plant use case, IT/OT dependency, expected uplift in OEE or cost terms)
  Content: Priority Investments section — denominate value in OEE points, downtime reduction, or scrap rate
Footer: "[FIRM NAME] | [CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 2-slide branded insert. Manufacturing executives respond to OEE points and downtime minutes — denominate every investment in these terms on Slide 2.
