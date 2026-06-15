---
skill: /ai-maturity-assessment
pack: AI & Digital Transformation
vertical: financial-services
chains-from: /situation-assessment
chains-into: /ai-use-case-prioritiser, /data-readiness-assessment
---

# Prompt Template: AI Maturity Assessment — Financial Services

**When to use:** Start of any AI strategy engagement at a bank, insurer, asset manager, or capital markets firm — before recommending investments, use cases, or operating model changes.

## Copy-paste prompt

```
Run /ai-maturity-assessment for [CLIENT NAME]:

Organisation: [NAME]
Sub-sector: [RETAIL BANKING / CORPORATE & INVESTMENT BANKING / INSURANCE / ASSET MANAGEMENT / PAYMENTS / FINTECH]
Size: [EMPLOYEE COUNT] employees / [AUM or TOTAL ASSETS or ANNUAL REVENUE]
Scope: [Whole enterprise / [BUSINESS LINE] only — e.g. "Retail credit decisioning only"]

Regulatory context:
- Primary regulator: [FCA / PRA / ECB / OCC / Fed / FINRA / MAS / APRA]
- Applicable AI/model risk guidance: [SR 11-7 / SS1/23 / EBA model risk / EU AI Act / other]
- Model Risk Management function: [EXISTS / DOESN'T EXIST / BRIEF — e.g. "MRM team of 12, all models registered"]
- Regulatory AI restrictions: [e.g. "No fully automated credit decisions >£25k; human-in-loop required"]

What we know about their AI today:
- Core banking / policy system: [e.g. "Temenos T24", "Finacle", "FIS Profile", "COBOL mainframe — migration planned 2027"]
- Data infrastructure: [e.g. "Azure Data Lake, Snowflake DW; data lineage partially documented"]
- AI/ML tools in use: [e.g. "SAS for credit scoring, Azure ML for fraud, vendor LLM for KYC"]
- Existing models in production: [NUMBER / brief — e.g. "47 registered models; 12 are AI/ML"]
- AI governance / responsible AI policy: [EXISTS / DOESN'T EXIST / BRIEF]
- Data access and sharing constraints: [e.g. "PII locked to EU; no cross-border data transfers for retail"]
- Culture / leadership attitude: [BRIEF — e.g. "CFO is driving cost reduction via AI; Chief Risk Officer cautious on model risk"]

Assessment purpose: [e.g. "Inform the AI investment roadmap for FY26" / "Prepare the board risk committee paper"]
```

## Expected output
Maturity scorecard (5 dimensions × 1–4 scale) with FS-specific evidence (model count, MRM maturity, data lineage coverage, regulatory posture), dimension deep-dives with sector benchmarks (peer bank comparison), and 2–3 priority investments calibrated to the regulatory environment.

## FS-specific quality checks
- Data dimension must reference core banking system age and data migration status
- Governance dimension must assess MRM function maturity separately from AI ethics governance
- Technology dimension must flag vendor model risk (SAS, FICO, vendor LLMs) as distinct from internal model risk
- Any "Leading" score in Governance must be validated against SR 11-7 or SS1/23 compliance evidence

## Chain next
- Proceed to `/ai-use-case-prioritiser` using the FS use case library (credit, fraud, KYC/AML, trading, customer service)
- Run `/responsible-ai-framework` early — FS regulators require documented AI governance before deployment

## PPTX output

After `/ai-maturity-assessment` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /ai-maturity-assessment output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — AI Maturity Assessment | Financial Services"
Slides:
- Slide 1: "AI Maturity Scorecard" — layout: scorecard matrix (5 dimension rows × 4 level columns; shade current level per dimension; add FS peer benchmark row at bottom)
  Content: Maturity Scorecard + Peer Benchmark sections
- Slide 2: "Priority Investments — Regulatory-Calibrated" — layout: 3 cards (investment, rationale, regulatory alignment, expected maturity uplift)
  Content: Priority Investments section — ranked by value AND regulatory feasibility
Footer: "[FIRM NAME] | [CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 2-slide branded insert. FS boards want to see the peer benchmark row — what Tier 1 banks are at — before approving the investment level.
