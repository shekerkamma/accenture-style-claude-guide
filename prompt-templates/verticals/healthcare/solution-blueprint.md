---
skill: /solution-blueprint
pack: Solution Delivery
vertical: healthcare
chains-from: /ai-use-case-prioritiser, /ai-build-buy-partner, /responsible-ai-framework
chains-into: /architecture-decision-record, /integration-sequencing, /raci-design
---

# Prompt Template: Solution Blueprint — Healthcare & Life Sciences

**When to use:** Translating approved clinical AI use cases into a delivery design that can be integrated with the EHR, governed through clinical safety processes, and deployed without disrupting clinical workflows.

## Copy-paste prompt

```
Run /solution-blueprint for [CLIENT NAME]:

Sub-sector: [HOSPITAL SYSTEM / HEALTH INSURER / PHARMA / MEDTECH]
Use cases in scope (from /ai-use-case-prioritiser Wave 1):
1. [USE CASE] — clinical risk tier: [Low/Med/High/Critical] — FDA/CE required: [Y/N]
2. [USE CASE] — clinical risk tier — FDA/CE required

Business outcomes required:
- [e.g. "Reduce unplanned readmissions within 30 days by 15%"]
- [e.g. "Increase radiology throughput by 20% without adding radiologist headcount"]

Healthcare technology landscape:
- EHR system: [NAME + version — e.g. "Epic Hyperspace 2024", "Cerner Millennium", "InterSystems TrakCare"]
- EHR integration mechanism: [Epic App Orchard / SMART on FHIR / HL7 v2 / direct Epic API / CDS Hooks / other]
- FHIR API availability: [R4 / STU3 / NOT AVAILABLE]
- PACS / imaging system (if radiology use case): [NAME — e.g. "Sectra IDS7", "Intelerad IntelePACS"]
- Data warehouse / analytics platform: [e.g. "Epic Clarity / Caboodle", "Azure Health Data Services", "Databricks on Azure"]
- Cloud platform: [Azure / AWS / GCP / on-prem — any NHS DSP Toolkit / HIPAA BAA constraints]
- Existing AI tools: [LIST — e.g. "Epic Predictive Risk scoring (HAF)", "Aidoc for radiology triage"]

Constraints:
- EHR vendor certification required: [Y/N — e.g. "Epic App Orchard certification adds 3–6 months"]
- FHIR API approved for use: [Y/N]
- Patient data de-identification required for model training: [Y/N + method]
- Clinical validation study required before go-live: [Y/N — standard for clinical AI in NHS/FDA context]
- Human-in-the-loop requirement: [Y/N + description from /responsible-ai-framework]
- Clinician workflow change: [BRIEF — e.g. "Must surface in existing Epic workflow — no new screen"]
- IT change freeze periods: [BRIEF — e.g. "No deployments October–January (winter pressures)"]

Internal build team: [SIZE / clinical informatics capability]
Sourcing decisions (from /ai-build-buy-partner): [BRIEF — e.g. "Buy FDA-cleared radiology AI; Build care management model in-house"]
```

## Expected output
Clinical-aware capability map (Outcome → Capability → Component, with FDA/CE classification and clinical validation gate as explicit components), EHR integration architecture (FHIR-first vs HL7 vs Epic native), phased delivery plan with clinical validation study as a milestone, and design constraints register including patient safety and EHR certification constraints.

## HC-specific quality checks
- Clinical AI components must each have an explicit FDA SaMD / CE mark classification and pre-deployment validation requirement
- EHR integration must use approved mechanism (FHIR R4 / Epic App Orchard / CDS Hooks) — direct DB access is a hard no in Epic environments
- Thin thread must include a clinical pilot with real patient data and CMO sign-off before wider rollout
- Winter pressure / IT change freeze periods must be respected in the delivery timeline

## Chain next
- Run `/architecture-decision-record` for: buy vs build (FDA-cleared vs in-house model), EHR integration pattern (FHIR vs HL7 vs Epic native), model hosting (cloud vs on-prem for patient data)
- Run `/integration-sequencing` — EHR integration is the critical path in almost every HC AI deployment

## PPTX output

After `/solution-blueprint` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /solution-blueprint output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — Solution Blueprint | Healthcare"
Slides:
- Slide 1: "Capability Map — EHR-Integrated Architecture" — layout: hierarchical table (Outcome → Capability → Component; FDA/CE status column; EHR integration method column; Build/Buy/Partner column)
  Content: Capability Map + Component Register with clinical governance flag per component
- Slide 2: "Phased Delivery — Clinical Validation Gated" — layout: phase timeline (Waves with clinical validation study, CMO sign-off, and Epic certification as explicit milestones)
  Content: Phased Delivery Plan — include all clinical governance gates
Footer: "[FIRM NAME] | [CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 2-slide branded insert. The clinical validation gate in the timeline is the artefact the CMO and Board need — it shows patient safety is the delivery principle, not speed.
