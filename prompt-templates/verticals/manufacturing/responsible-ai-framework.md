---
skill: /responsible-ai-framework
pack: AI & Digital Transformation
vertical: manufacturing
chains-from: /ai-use-case-prioritiser, /risk-and-mitigation
chains-into: /solution-blueprint, /raid-log
---

# Prompt Template: Responsible AI Framework — Manufacturing & Industrial

**When to use:** Before deploying AI on the plant floor, in safety-critical processes, or in autonomous / semi-autonomous control loops. Industrial AI failures cause downtime, product liability, and safety incidents.

## Copy-paste prompt

```
Run /responsible-ai-framework for [CLIENT NAME]:

Sub-sector: [AUTOMOTIVE / AEROSPACE / PROCESS / DISCRETE / ENERGY]
Primary regulatory context:
- Safety standards applicable: [ISO 26262 (automotive) / DO-178C (aerospace) / IEC 61511 (process safety) / IEC 62061 (machinery safety) / other]
- OT/cyber standards: [IEC 62443 / NIST CSF / NIS2 Directive (EU) / other]
- Product liability regime: [EU Product Liability Directive / US / other]
- Export control: [ITAR / EAR — relevant for aerospace/defence AI]
- EU AI Act: [applicable — check Annex III: safety components of products / critical infrastructure]

AI use cases requiring governance design:
1. [USE CASE] — in safety-critical process Y/N — autonomous control loop Y/N — worker safety impact Y/N
2. [USE CASE] — safety-critical Y/N — autonomous Y/N — worker safety Y/N
[continue...]

Existing safety and quality governance:
- Functional safety programme: [EXISTS — standard / DOESN'T EXIST]
- Quality management system: [ISO 9001 / IATF 16949 (automotive) / AS9100 (aerospace) / none]
- OT cybersecurity programme: [IEC 62443 certified / IN PROGRESS / DOESN'T EXIST]
- EHS (Environment, Health & Safety) function: [EXISTS / BRIEF]
- Change management process for process changes: [EXISTS / BRIEF — MOC process?]

Known safety or liability concerns:
- [e.g. "Predictive maintenance — if model misses a failure, OEM has product liability exposure"]
- [e.g. "Visual inspection AI — if defect escapes to customer, ISO 9001 requires root cause analysis"]
- [e.g. "Autonomous scheduling — if it causes a safety incident by removing a planned maintenance window"]
```

## Expected output
Industrial AI risk tier taxonomy (Low/Medium/High/Critical with safety-criticality triggers), use case risk register with functional safety and product liability assessment, governance requirements per tier (MOC process, functional safety review, OT security sign-off, quality validation), monitoring and override requirements for control-loop AI, and product liability boundary map.

## Manufacturing-specific quality checks
- Any AI in a safety-critical control loop requires functional safety assessment (IEC 61511 / IEC 26262 equivalent) before deployment
- Visual inspection AI that replaces human quality inspection must be validated against the same statistical quality standard as the human process
- Predictive maintenance failure must trigger a defined failsafe (e.g., revert to time-based maintenance schedule) — not just an alert
- AI that changes process parameters autonomously must go through the Management of Change (MOC) process — even if the AI is "just" making recommendations

## Chain next
- Functional safety requirements become hard constraints in `/solution-blueprint` — specifically in the control loop architecture decisions
- All High/Critical risks go to `/raid-log` immediately

## PPTX output

After `/responsible-ai-framework` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /responsible-ai-framework output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — Responsible AI Framework | Manufacturing"
Slides:
- Slide 1: "Industrial AI Risk Register" — layout: table (use case, risk tier, safety-critical Y/N, functional safety standard, product liability exposure, required governance)
  Content: Use Case Risk Register with safety-criticality column
- Slide 2: "Industrial AI Governance Structure" — layout: tier diagram (Low → Critical; functional safety assessment, MOC process, OT security sign-off, and quality validation per tier)
  Content: Governance Requirements per Tier + Review Board Design sections
Footer: "[FIRM NAME] | [CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 2-slide branded insert. The safety-criticality column on Slide 1 is the artefact the EHS director and plant manager need before authorising AI on the shop floor.
