---
skill: /responsible-ai-framework
pack: AI & Digital Transformation
vertical: healthcare
chains-from: /ai-use-case-prioritiser, /risk-and-mitigation
chains-into: /solution-blueprint, /raid-log
---

# Prompt Template: Responsible AI Framework — Healthcare & Life Sciences

**When to use:** Before deploying any clinical AI tool, diagnostic model, or patient-facing system. Clinical AI failures are patient safety events — govern them accordingly.

## Copy-paste prompt

```
Run /responsible-ai-framework for [CLIENT NAME]:

Sub-sector: [HOSPITAL SYSTEM / HEALTH INSURER / PHARMA / MEDTECH]
Primary regulator: [FDA / NHS England / MHRA / EMA / CMS / state health department]

Applicable regulatory obligations (check all that apply):
- [ ] FDA Software as a Medical Device (SaMD) — 510k / De Novo / PMA pathway
- [ ] EU MDR / IVDR — CE mark for diagnostic AI
- [ ] UKCA — UK conformity assessment post-Brexit
- [ ] HIPAA — US patient data privacy and AI
- [ ] UK GDPR / Data Security & Protection Toolkit — NHS
- [ ] NHS DCB0129 / DCB0160 — clinical risk management standards
- [ ] EU AI Act — Annex III high-risk (medical devices, biometric)
- [ ] 21 CFR Part 820 / ISO 13485 — quality management for medical devices
- [ ] [OTHER]

AI use cases requiring governance design:
1. [USE CASE] — diagnostic Y/N — patient-facing Y/N — autonomous decision Y/N — risk level: [High/Critical if diagnostic]
2. [USE CASE] — diagnostic Y/N — patient-facing Y/N — autonomous decision Y/N — risk level
[continue...]

Clinical governance infrastructure:
- Medical director / CMO sponsorship: [CONFIRMED / NOT YET]
- Clinical safety officer: [EXISTS / DOESN'T EXIST — required for DCB0129]
- Clinical AI committee or review board: [EXISTS / DOESN'T EXIST]
- Existing clinical AI policy: [EXISTS / DOESN'T EXIST]
- Adverse event / near-miss reporting for AI: [EXISTS / DOESN'T EXIST]

Known bias or safety concerns:
- [e.g. "Sepsis model trained on EHR data with documented demographic bias — Black patients under-scored"]
- [e.g. "Chest X-ray AI validated on US population — performance on our UK population unknown"]
- [e.g. "Readmission model uses socioeconomic features — ethical concern raised by clinical ethics board"]
```

## Expected output
HC-calibrated AI risk tier taxonomy (Low/Medium/High/Critical with clinical safety triggers), use case risk register with FDA/CE/MHRA/DCB pathway mapping, governance requirements per tier (clinical safety assessment, MRC/FDA validation, clinical ethics review, board approval, post-market surveillance plan), bias testing requirements, and adverse event monitoring cadence.

## HC-specific quality checks
- Diagnostic AI (radiology, pathology, clinical decision support) must carry explicit FDA SaMD classification or EU MDR risk class
- Any autonomous clinical decision must include a human-override mechanism and clinician override audit trail
- Bias testing must include demographic sub-group analysis (age, sex, ethnicity, deprivation) — standard in NHS/FDA guidance
- Post-market surveillance plan required for any FDA-cleared or CE-marked tool — not optional

## Chain next
- Risk tier and clinical safety requirements become hard constraints in `/solution-blueprint` design
- Safety-critical risks go immediately to `/raid-log` as P1 items

## PPTX output

After `/responsible-ai-framework` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /responsible-ai-framework output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — Responsible AI Framework | Healthcare"
Slides:
- Slide 1: "Clinical AI Risk Register" — layout: table (use case, risk tier, diagnostic Y/N, FDA/CE/MHRA classification, required governance, post-market surveillance required)
  Content: Use Case Risk Register with regulatory pathway column
- Slide 2: "Clinical AI Governance Structure" — layout: tier diagram (Low → Critical; clinical safety assessment and approval pathway per tier; adverse event escalation path)
  Content: Governance Requirements per Tier + Review Board Design sections
Footer: "[FIRM NAME] | [CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 2-slide branded insert. Present to the Clinical Ethics Board or Medical Advisory Board before any diagnostic AI procurement — Slide 1 is their checklist.
