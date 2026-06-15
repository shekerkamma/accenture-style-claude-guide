---
skill: /solution-blueprint
pack: Solution Delivery
vertical: manufacturing
chains-from: /ai-use-case-prioritiser, /ai-build-buy-partner, /responsible-ai-framework
chains-into: /architecture-decision-record, /integration-sequencing, /raci-design
---

# Prompt Template: Solution Blueprint — Manufacturing & Industrial

**When to use:** Translating approved manufacturing AI use cases into a delivery design that can be deployed on the shop floor, integrated with OT systems, and operated by maintenance and production teams without heavy IT dependency.

## Copy-paste prompt

```
Run /solution-blueprint for [CLIENT NAME]:

Sub-sector: [AUTOMOTIVE / AEROSPACE / PROCESS / DISCRETE / CONSUMER GOODS]
Use cases in scope (from /ai-use-case-prioritiser Wave 1):
1. [USE CASE] — safety-critical: [Y/N] — OT integration required: [Y/N]
2. [USE CASE] — safety-critical — OT integration

Business outcomes required:
- [e.g. "Reduce unplanned downtime on Lines 1–3 by 25% (currently 400 hours/year at £8k/hour)"]
- [e.g. "Reduce visual inspection false escape rate from 2.1% to <0.5%"]
- [e.g. "Improve OEE from 72% to 80% on the lighthouse plant within 12 months"]

OT / plant floor technology landscape:
- PLCs in use: [BRAND + model — e.g. "Siemens S7-300, S7-1500", "Rockwell ControlLogix", "mixed legacy"]
- SCADA / historian: [e.g. "OSIsoft PI System v3.5", "AVEVA InTouch", "Ignition SCADA"]
- MES: [e.g. "SAP ME / MII", "Siemens Opcenter", "Rockwell Plex", "custom / none"]
- Asset connectivity: [% of critical assets connected to historian / SCADA]
- OT network architecture: [OT air-gapped from IT Y/N / DMZ in place / direct IT/OT connection]
- Sensor coverage: [e.g. "Vibration sensors on 60% of motors; temperature sensors on all; no acoustic sensors"]
- ERP: [SAP S/4HANA / SAP ECC / Oracle / Microsoft Dynamics — for supply chain use cases]
- Cloud platform: [Azure / AWS / GCP / on-prem — any OT security constraint on cloud connectivity]

Constraints:
- No remote access to OT network: [Y/N — common constraint; affects cloud architecture significantly]
- Air-gapped plant: [Y/N — data extraction mechanism needed]
- Sensor gaps: [LIST any assets with insufficient sensor coverage for Wave 1 use cases]
- PLC vendor lock-in: [Y/N — e.g. "Must use Siemens toolchain; no third-party integration approved"]
- Change management: [e.g. "Plant downtime for sensor installation must be in planned maintenance windows only"]
- Plant maintenance team skill level: [BRIEF — e.g. "2 condition monitoring engineers; no ML capability"]

Internal build team: [SIZE / OT + data capability — e.g. "4 data engineers, 2 ML engineers; no OT knowledge in-house"]
Sourcing decisions (from /ai-build-buy-partner): [BRIEF — e.g. "Buy Azure IoT + Aspentech for PdM; build quality inspection in-house on Azure Custom Vision"]
```

## Expected output
OT-aware capability map (Outcome → Capability → Component, with OT data source and connectivity requirement per component), IT/OT integration architecture (edge vs cloud vs hybrid), phased delivery plan with sensor installation and OT connectivity as explicit pre-conditions, and design constraints register including OT security and plant maintenance window constraints.

## Manufacturing-specific quality checks
- Sensor coverage gaps must be listed as explicit pre-conditions — no model can work without the data it needs
- OT air-gap or network separation must drive the architecture choice (edge deployment vs secure tunnel vs data diode)
- Wave 1 must use the most connected, best-maintained assets — do not start on the worst-data plant
- Maintenance team operability: every AI output must be interpretable by the maintenance crew, not just the data science team (e.g., "bearing wear detected — replace within 14 days" not "anomaly score: 0.87")

## Chain next
- Run `/architecture-decision-record` for: cloud vs edge for OT data, PdM vendor vs in-house model, OT connectivity mechanism (MQTT / OPC-UA / data diode)
- Run `/integration-sequencing` — OT historian / SCADA integration is always the critical path

## PPTX output

After `/solution-blueprint` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /solution-blueprint output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — Solution Blueprint | Manufacturing"
Slides:
- Slide 1: "Capability Map — OT-Integrated Architecture" — layout: hierarchical table (Outcome → Capability → Component; OT data source column; Edge/Cloud flag column; Build/Buy/Partner column)
  Content: Capability Map + Component Register with OT integration method per component
- Slide 2: "Phased Delivery — Lighthouse Plant First" — layout: phase timeline (Connectivity / Baseline / Model / Deploy / Scale waves; sensor installation and OT readiness as explicit pre-conditions)
  Content: Phased Delivery Plan — include OT connectivity and sensor pre-conditions
Footer: "[FIRM NAME] | [CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 2-slide branded insert. The OT connectivity pre-conditions on Slide 2 are the COO's biggest concern — showing that the plan accounts for sensor gaps prevents the most common delivery failure in manufacturing AI.
