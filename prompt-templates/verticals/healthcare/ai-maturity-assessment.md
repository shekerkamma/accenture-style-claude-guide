---
skill: /ai-maturity-assessment
pack: AI & Digital Transformation
vertical: healthcare
chains-from: /situation-assessment
chains-into: /ai-use-case-prioritiser, /data-readiness-assessment
---

# Prompt Template: AI Maturity Assessment — Healthcare & Life Sciences

**When to use:** Start of any AI engagement at a hospital system, health insurer, pharma/biotech firm, or medtech company — before recommending investments, use cases, or operating model changes.

## Copy-paste prompt

```
Run /ai-maturity-assessment for [CLIENT NAME]:

Organisation: [NAME]
Sub-sector: [HOSPITAL SYSTEM / HEALTH INSURER / PHARMA / BIOTECH / MEDTECH / HEALTH TECH / PRIMARY CARE / PATHOLOGY / RADIOLOGY]
Size: [EMPLOYEE COUNT / NUMBER OF BEDS / ANNUAL REVENUE]
Scope: [Whole enterprise / [CLINICAL SERVICE LINE or BUSINESS UNIT] only]

Regulatory and accreditation context:
- Primary regulator: [FDA / CMS / NHS England / MHRA / EMA / TGA / other]
- Clinical AI regulation: [FDA SaMD classification / CE mark (EU MDR) / UKCA / other]
- Data privacy: [HIPAA / GDPR / UK GDPR / state law / other]
- Accreditation body: [Joint Commission / CQC / ISO 13485 / other]

What we know about their AI today:
- EHR / EMR system: [e.g. "Epic on AWS", "Cerner", "InterSystems HealthShare", "multiple legacy systems"]
- PACS / imaging platform: [e.g. "Sectra", "GE Healthcare", "Intelerad"] — for clinical imaging use cases
- Data platform: [e.g. "Epic Cosmos", "Azure Health Data Services / FHIR API", "on-prem SQL warehouse"]
- AI tools in use: [e.g. "Epic AI modules", "vendor radiology AI (Aidoc / Annalise)", "Azure ML for care management"]
- Clinical AI models in production: [NUMBER / brief — e.g. "3 FDA-cleared radiology tools; 1 in-house readmission model"]
- Clinical governance: [e.g. "Medical AI committee exists", "CMO approval required for clinical decision support"]
- Data sharing constraints: [e.g. "No patient data to cloud without BAA; de-identification required for model training"]
- Culture / clinical leadership attitude: [BRIEF — e.g. "CMO cautious — cites AI bias in dermatology literature; CTO is a champion"]

Assessment purpose: [e.g. "Inform the digital health AI strategy" / "Prepare the board investment case for clinical AI"]
```

## Expected output
Maturity scorecard (5 dimensions × 1–4 scale) with healthcare-specific evidence (EHR integration depth, clinical governance maturity, FHIR API availability, FDA/CE mark posture, data de-identification capability), dimension deep-dives with health sector benchmarks, and 2–3 priority investments calibrated to clinical governance and regulatory constraints.

## HC-specific quality checks
- Data dimension must assess FHIR API maturity and interoperability — this is the core enabler for most clinical AI
- Governance dimension must assess clinical governance separately from data governance (CMO/medical director sign-off pathway)
- Technology dimension must distinguish FDA-cleared tools (external) from in-house models with different validation requirements
- Any "Leading" score in Governance must be validated against clinical AI committee existence and documented review process

## Chain next
- Proceed to `/ai-use-case-prioritiser` using the HC use case library (radiology, clinical decision support, care management, revenue cycle, drug discovery)
- Run `/responsible-ai-framework` early — clinical AI requires regulatory classification before deployment

## PPTX output

After `/ai-maturity-assessment` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /ai-maturity-assessment output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — AI Maturity Assessment | Healthcare"
Slides:
- Slide 1: "AI Maturity Scorecard" — layout: scorecard matrix (5 dimension rows × 4 level columns; shade current level per dimension; add healthcare peer benchmark row at bottom)
  Content: Maturity Scorecard + Peer Benchmark sections
- Slide 2: "Priority Investments — Clinically Governed" — layout: 3 cards (investment, clinical use case, regulatory pathway, expected maturity uplift)
  Content: Priority Investments section — ranked by value AND clinical governance readiness
Footer: "[FIRM NAME] | [CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 2-slide branded insert. Clinical boards want to see the regulatory pathway alongside the value case — show FDA/CE mark status for each investment.
