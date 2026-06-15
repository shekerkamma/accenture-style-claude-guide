---
skill: /ai-use-case-prioritiser
pack: AI & Digital Transformation
vertical: financial-services
chains-from: /ai-maturity-assessment, /situation-assessment
chains-into: /data-readiness-assessment, /responsible-ai-framework, /solution-blueprint
---

# Prompt Template: AI Use Case Prioritiser — Financial Services

**When to use:** When a FS firm has a long list of AI use cases (often from an internal innovation programme or benchmarking study) and must narrow to a funded, regulator-ready portfolio.

## Copy-paste prompt

```
Run /ai-use-case-prioritiser for [CLIENT NAME]:

Sub-sector: [RETAIL BANKING / CIB / INSURANCE / ASSET MANAGEMENT / PAYMENTS]
AI maturity level: [1–4 from /ai-maturity-assessment, or UNKNOWN]

FS use case long list — mark any already in flight:
Credit & Lending:
- [ ] AI credit scoring (alternative data)
- [ ] Real-time affordability assessment
- [ ] Collections propensity model
- [ ] SME lending automation
- [x / ] [OTHER — add your own]

Fraud & Financial Crime:
- [ ] Real-time transaction fraud detection
- [ ] AML transaction monitoring (reduce false positives)
- [ ] KYC document extraction and verification
- [ ] Entity resolution / beneficial ownership
- [ ] [OTHER]

Customer & Distribution:
- [ ] Next best action / next best offer
- [ ] Churn propensity and retention
- [ ] Personalised pricing (home insurance, personal loans)
- [ ] AI-assisted advisor (wealth / mortgage)
- [ ] Customer service virtual agent (L1 deflection)
- [ ] [OTHER]

Operations & Risk:
- [ ] Regulatory reporting automation (COREP, FINREP, MiFID)
- [ ] Contract review and extraction (legal / compliance)
- [ ] Model monitoring and drift detection
- [ ] Back-office intelligent document processing
- [ ] [OTHER]

Trading & Markets (CIB only):
- [ ] Algorithmic trade execution
- [ ] Research summarisation (earnings, analyst reports)
- [ ] Portfolio risk scenario modelling
- [ ] [OTHER]

Constraints:
- MRM review capacity: [e.g. "MRM can onboard 4 new models per quarter"]
- Regulatory restrictions on automation: [BRIEF]
- Executive sponsor priorities: [e.g. "CFO: cost out; CCO: fraud losses; CDO: data monetisation"]
- Competitor moves: [BRIEF — e.g. "Competitor A launched AI credit scoring in Q1"]
```

## Expected output
Scored register with FS-specific scoring (Value × Feasibility × Regulatory Complexity), Wave 1/2/3 portfolio with MRM queue alignment, high-risk use cases flagged for early `/responsible-ai-framework` review, and recommended thin thread (fastest value with lowest regulatory friction).

## FS-specific quality checks
- Credit decisioning use cases must be flagged for explainability (ECOA/Equal Credit Opportunity, FCA consumer duty)
- AML/KYC use cases must note MLRO sign-off requirement
- Customer-facing AI must flag Consumer Duty / CFPB obligations
- Wave 1 should include at least one low-regulatory-friction use case for quick win

## Chain next
- Run `/responsible-ai-framework` on any High/Critical regulatory complexity use cases before committing to Wave 1
- Run `/data-readiness-assessment` on credit and AML use cases — data lineage and quality are typically the constraint

## PPTX output

After `/ai-use-case-prioritiser` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /ai-use-case-prioritiser output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — AI Use Case Portfolio | Financial Services"
Slides:
- Slide 1: "FS AI Use Case Portfolio — Value vs Regulatory Complexity" — layout: 2×2 matrix (Value on Y axis, Regulatory Complexity on X axis; use case IDs plotted; quadrants: Quick Wins / Strategic Bets / Compliance-First / High Effort)
  Content: Portfolio Map section — all scored use cases with regulatory complexity flag
- Slide 2: "Wave 1 Portfolio — Regulatory-Cleared" — layout: table (use case, domain, value score, regulatory tier: Low/Med/High, MRM queue slot, owner, timeline)
  Content: Wave 1 Portfolio section
Footer: "[FIRM NAME] | [CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 2-slide branded insert. FS boards and risk committees respond well to the regulatory complexity axis — it makes the sequencing rationale explicit and defensible.
