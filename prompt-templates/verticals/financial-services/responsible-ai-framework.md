---
skill: /responsible-ai-framework
pack: AI & Digital Transformation
vertical: financial-services
chains-from: /ai-use-case-prioritiser, /risk-and-mitigation
chains-into: /solution-blueprint, /raid-log
---

# Prompt Template: Responsible AI Framework — Financial Services

**When to use:** Before any customer-facing or automated-decisioning AI deployment in a regulated FS firm. Run this before the regulator asks — not after.

## Copy-paste prompt

```
Run /responsible-ai-framework for [CLIENT NAME]:

Sub-sector: [RETAIL BANKING / CIB / INSURANCE / ASSET MANAGEMENT / PAYMENTS]
Primary regulator: [FCA / PRA / ECB / OCC / Federal Reserve / FINRA / MAS / APRA / dual-regulated]

Applicable regulatory obligations (check all that apply):
- [ ] SR 11-7 (Fed/OCC Model Risk Management guidance) — US
- [ ] SS1/23 (PRA model risk management) — UK
- [ ] EBA model risk guidelines — EU
- [ ] EU AI Act — Article 5 prohibited / Annex III high-risk classification
- [ ] FCA Consumer Duty — fair outcomes, explainability obligations
- [ ] ECOA / Fair Lending — algorithmic bias in credit decisions — US
- [ ] GDPR Article 22 — automated individual decision-making rights — EU/UK
- [ ] DORA — digital operational resilience — EU
- [ ] [OTHER]

AI use cases requiring governance design (from /ai-use-case-prioritiser):
1. [USE CASE] — automated decision Y/N — customer-facing Y/N — uses protected characteristics Y/N
2. [USE CASE] — automated decision Y/N — customer-facing Y/N — protected characteristics Y/N
[continue...]

Existing governance infrastructure:
- Model Risk Management function: [EXISTS — size/maturity / DOESN'T EXIST]
- Model inventory and validation process: [EXISTS / PARTIAL / DOESN'T EXIST]
- Ethics board or AI review committee: [EXISTS / DOESN'T EXIST]
- Existing AI / data ethics policy: [EXISTS / DOESN'T EXIST / BRIEF]
- CISO / Chief Risk Officer engagement: [BRIEF]

High-risk scenarios known:
- [e.g. "Credit scoring model uses postcode — potential proxy for protected characteristic"]
- [e.g. "AML model has 30% false positive rate — disproportionate impact on specific demographics"]
```

## Expected output
FS-calibrated AI risk tier taxonomy (Low/Medium/High/Critical with FS regulatory triggers), use case risk register with SR 11-7 / SS1/23 / EU AI Act mapping, governance requirements per tier (MRM validation, legal review, regulatory notification, board approval), model monitoring cadence, and regulatory notification assessment.

## FS-specific quality checks
- Credit decisions must include algorithmic bias testing requirement and ECOA / Consumer Duty explainability standard
- High-risk tier must require pre-deployment MRM validation, not just post-deployment monitoring
- Any use case touching GDPR Article 22 must include human review right mechanism
- DORA classification must be assessed for AI systems deemed critical digital infrastructure

## Chain next
- Use risk tier classifications as hard constraints in `/solution-blueprint` design
- Add High/Critical use case risks directly to `/raid-log` as mandatory mitigations

## PPTX output

After `/responsible-ai-framework` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /responsible-ai-framework output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — Responsible AI Framework | Financial Services"
Slides:
- Slide 1: "AI Risk Register — Regulatory Mapping" — layout: table (use case, risk tier, automated decision Y/N, SR 11-7/SS1/23/EU AI Act classification, required governance action)
  Content: Use Case Risk Register section — all in-scope use cases with regulatory mapping
- Slide 2: "AI Governance Structure" — layout: governance tier diagram (Low → Critical tiers; review body, validation requirement, and regulatory notification for each tier)
  Content: Governance Requirements per Tier + Review Board Design sections
Footer: "[FIRM NAME] | [CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 2-slide branded insert. Slide 1 is the primary artefact for the Chief Risk Officer and board risk committee — it shows each use case is mapped to the right regulatory framework.
