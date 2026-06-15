---
skill: /data-readiness-assessment
pack: ai-transformation
chains-from: /ai-maturity-assessment, /ai-use-case-prioritiser
chains-into: /solution-blueprint, /transformation-roadmap
---

# Prompt Template: Data Readiness Assessment

**When to use:** Before committing to AI use cases or before a data platform investment decision. Run once the Wave 1 use case list is known.

## Copy-paste prompt

```
Run /data-readiness-assessment for [CLIENT NAME]:

Use cases to assess (from /ai-use-case-prioritiser Wave 1):
1. [USE CASE 1]
2. [USE CASE 2]
3. [USE CASE 3]

Data landscape:
- Core systems: [LIST — e.g. "SAP S/4HANA, Salesforce, legacy Oracle DW"]
- Data warehouse / lake: [EXISTS / DESCRIPTION]
- Data governance maturity: [BRIEF]
- Known data quality issues: [LIST]
- Data access controls: [BRIEF — e.g. "PII locked in EU, cross-BU access restricted"]

For each use case, we need to know:
- What data is required
- Whether it is available, clean, and accessible
- What remediation is needed and how long it will take
```

## Expected output
Readiness scorecard per use case (Availability / Quality / Access / Lineage / Governance), verdict (Ready / Conditionally Ready / Blocked), critical gaps register, remediation roadmap, and platform implications.

## Chain next
- Use verdicts to confirm or adjust the `/ai-use-case-prioritiser` Wave 1 list
- Pass Blocked use cases to Wave 2 with data remediation as a pre-condition

## PPTX output

After `/data-readiness-assessment` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /data-readiness-assessment output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — Data Readiness Assessment"
Slides:
- Slide 1: "Data Readiness by Use Case" — layout: heatmap table (use case rows × Availability/Quality/Access/Lineage/Governance columns, RAG cells)
  Content: Readiness Scorecard section — all use cases and dimensions
- Slide 2: "Data Remediation Roadmap" — layout: table (use case, gap description, remediation action, owner, target date)
  Content: Remediation Roadmap section — Blocked and Conditionally Ready use cases only
Footer: "[FIRM NAME] | [CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 2-slide branded insert. Slide 2 covers only Blocked and Conditionally Ready use cases — Ready use cases need no action.
