---
skill: /ai-use-case-prioritiser
pack: AI & Digital Transformation
vertical: healthcare
chains-from: /ai-maturity-assessment, /situation-assessment
chains-into: /data-readiness-assessment, /responsible-ai-framework, /solution-blueprint
---

# Prompt Template: AI Use Case Prioritiser — Healthcare & Life Sciences

**When to use:** When a health system, insurer, or pharma firm has a long list of AI opportunities and must select a funded, clinically governed, regulatory-ready portfolio.

## Copy-paste prompt

```
Run /ai-use-case-prioritiser for [CLIENT NAME]:

Sub-sector: [HOSPITAL SYSTEM / HEALTH INSURER / PHARMA / BIOTECH / MEDTECH]
AI maturity level: [1–4 from /ai-maturity-assessment, or UNKNOWN]

HC use case long list — mark any already in flight:
Clinical Decision Support:
- [ ] Sepsis early warning
- [ ] Deterioration prediction (NEWS2 / EWS enhancement)
- [ ] Readmission risk prediction
- [ ] Medication error / drug interaction alert
- [ ] Differential diagnosis support (LLM-assisted)
- [ ] [OTHER]

Radiology & Pathology (Diagnostics):
- [ ] Radiology triage (chest X-ray, CT pulmonary embolism)
- [ ] Pathology slide analysis (digital pathology AI)
- [ ] Screening programme augmentation (mammography, diabetic retinopathy)
- [ ] Radiologist workflow prioritisation
- [ ] [OTHER]

Operations & Administration:
- [ ] No-show / DNA prediction
- [ ] Theatre / OR scheduling optimisation
- [ ] Bed management and discharge planning
- [ ] Prior authorisation automation (health insurer)
- [ ] Medical coding and CDI (clinical documentation improvement)
- [ ] Claims fraud detection (health insurer)
- [ ] [OTHER]

Drug Discovery & Clinical Trials (Pharma / Biotech):
- [ ] Target identification and validation
- [ ] Clinical trial patient matching
- [ ] Adverse event detection in real-world data
- [ ] Regulatory submission drafting (AI-assisted)
- [ ] [OTHER]

Workforce & Patient Experience:
- [ ] Clinical staff scheduling optimisation
- [ ] Patient self-service (symptom checker, appointment booking)
- [ ] Remote patient monitoring AI
- [ ] Patient-facing AI triage
- [ ] [OTHER]

Constraints:
- Clinical governance pathway: [e.g. "All clinical AI requires CMO approval + clinical safety officer sign-off"]
- FDA/CE mark requirement: [e.g. "Any diagnostic AI must be FDA 510k cleared before go-live"]
- EHR integration complexity: [e.g. "Epic-certified apps only; custom integrations require 6-month approval"]
- Clinician adoption risk: [BRIEF — e.g. "Radiologists very resistant to AI after prior failed rollout"]
- Executive sponsor priorities: [e.g. "CEO: reduce length of stay; CMO: reduce diagnostic error; CFO: revenue cycle"]
```

## Expected output
Scored register with HC-specific scoring (Clinical Value × Operational Feasibility × Regulatory Complexity × Clinician Adoption Risk), Wave 1/2/3 portfolio with FDA/CE mark pathway per use case, high-regulatory-risk use cases flagged for early `/responsible-ai-framework`, and recommended thin thread (fastest clinical validation with lowest patient safety risk).

## HC-specific quality checks
- Any use case affecting diagnostic decisions must carry an FDA SaMD / CE mark pathway assessment
- Clinician adoption risk must be scored separately — even high-value use cases fail without adoption
- Wave 1 should include at least one operational/administrative use case (lower clinical risk) if clinical maturity is low
- Drug discovery use cases (pharma) are typically Wave 2+ due to data and validation complexity

## Chain next
- Run `/responsible-ai-framework` on all diagnostic and clinical decision support use cases
- Run `/data-readiness-assessment` — FHIR API maturity and EHR data quality are the most common blockers

## PPTX output

After `/ai-use-case-prioritiser` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /ai-use-case-prioritiser output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — AI Use Case Portfolio | Healthcare"
Slides:
- Slide 1: "HC AI Portfolio — Clinical Value vs Regulatory Complexity" — layout: 2×2 matrix (Clinical Value Y, Regulatory Complexity X; use case IDs plotted; quadrants: Operational AI / Clinical AI / Research / Admin Automation)
  Content: Portfolio Map section
- Slide 2: "Wave 1 Portfolio — Governed for Clinical Safety" — layout: table (use case, domain, clinical value score, regulatory pathway, FDA/CE status, CMO approval needed Y/N, owner)
  Content: Wave 1 Portfolio section with regulatory pathway column
Footer: "[FIRM NAME] | [CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 2-slide branded insert. The regulatory pathway column on Slide 2 is the artefact clinical boards need — it shows the path to deployment, not just the business case.
