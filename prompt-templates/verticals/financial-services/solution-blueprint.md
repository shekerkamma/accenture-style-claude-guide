---
skill: /solution-blueprint
pack: Solution Delivery
vertical: financial-services
chains-from: /ai-use-case-prioritiser, /ai-build-buy-partner, /responsible-ai-framework
chains-into: /architecture-decision-record, /integration-sequencing, /raci-design
---

# Prompt Template: Solution Blueprint — Financial Services

**When to use:** Translating approved FS AI use cases into a delivery design that will survive MRM validation, regulatory review, and core banking integration constraints.

## Copy-paste prompt

```
Run /solution-blueprint for [CLIENT NAME]:

Sub-sector: [RETAIL BANKING / CIB / INSURANCE / ASSET MANAGEMENT / PAYMENTS]
Use cases in scope (from /ai-use-case-prioritiser Wave 1):
1. [USE CASE] — risk tier: [Low/Med/High/Critical from /responsible-ai-framework]
2. [USE CASE] — risk tier: [Low/Med/High/Critical]

Business outcomes required:
- [e.g. "Reduce credit decision time from 3 days to 4 hours for SME loans <£500k"]
- [e.g. "Reduce AML false positive rate from 85% to <60% without increasing false negatives"]

FS technology landscape:
- Core banking system: [NAME + version — e.g. "Temenos T24 on-prem", "FIS Horizon", "SAP S/4HANA Banking"]
- Core banking migration status: [STABLE / MIGRATION PLANNED — timeline]
- Loan origination / policy system: [NAME — e.g. "Salesforce FSC", "nCino", "bespoke"]
- Data warehouse / lake: [NAME — e.g. "Azure Synapse + Databricks", "Snowflake on AWS", "legacy Teradata"]
- Cloud platform: [Azure / AWS / GCP / HYBRID — any approved cloud policy]
- Existing ML platform: [e.g. "Azure ML", "SAS Viya", "Databricks MLflow", "none"]
- API gateway / integration layer: [NAME — e.g. "MuleSoft", "Azure APIM", "direct DB reads (flagged as risk)"]

Constraints:
- No direct database writes to core banking: [Y/N — common FS constraint]
- All models must be registered in model inventory: [Y/N]
- MRM validation required before production: [Y/N — typical for High/Critical tier]
- Data residency: [EU only / US / APAC / no restriction]
- Vendor approval process: [BRIEF — e.g. "Third-party risk assessment adds 8–12 weeks"]
- Real-time vs batch requirement: [BRIEF — e.g. "Fraud must be real-time <200ms; credit can be near-real-time"]
- Human-in-the-loop requirement: [BRIEF — e.g. "Mandatory for decisions >£50k per regulatory guidance"]

Internal build team: [SIZE / SKILLS — e.g. "5 data scientists, 3 ML engineers, no MLOps"]
Sourcing decisions (from /ai-build-buy-partner): [BRIEF]
```

## Expected output
FS-aware capability map (Outcome → Capability → Component, with MRM validation gate as explicit component), component register with model risk classification per component, phased delivery plan with MRM validation as a milestone (not an afterthought), integration approach for core banking (API-first, no direct DB writes), and design constraints register including regulatory constraints.

## FS-specific quality checks
- Model components must each have an explicit MRM classification (in-scope / out-of-scope) and validation plan
- No direct database writes to core banking — all state changes via approved APIs or batch file
- Thin thread (Wave 1) must be demonstrable in a regulatory sandbox or UAT environment before production
- Real-time use cases (fraud) must have latency budgets and fallback logic in the design

## Chain next
- Run `/architecture-decision-record` for: model hosting (cloud vs on-prem), core banking integration pattern, vendor model vs internal model
- Run `/integration-sequencing` — core banking integration is almost always the critical path in FS

## PPTX output

After `/solution-blueprint` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /solution-blueprint output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — Solution Blueprint | Financial Services"
Slides:
- Slide 1: "Capability Map — FS Architecture" — layout: hierarchical table (Outcome → Capability → Component; MRM classification column; Build/Buy/Partner column)
  Content: Capability Map + Component Register sections with MRM flag per component
- Slide 2: "Phased Delivery — MRM Gated" — layout: phase timeline (Wave 1/2/3; MRM validation milestone shown as gate between develop and deploy for each model component)
  Content: Phased Delivery Plan section — include MRM validation as explicit milestone
Footer: "[FIRM NAME] | [CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 2-slide branded insert. The MRM-gated timeline is the artefact that gets the CRO comfortable — it shows model risk is controlled, not rushed.
