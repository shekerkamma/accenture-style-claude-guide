---
skill: /change-readiness-assessment
pack: solution-delivery
chains-from: /solution-blueprint, /engagement-kickoff
chains-into: /change-impact-assessment, /adoption-plan
---

# Prompt Template: Change Readiness Assessment

**When to use:** Before designing the adoption plan — understand where resistance will come from and what ADKAR stage each impacted group is at.

## Copy-paste prompt

```
Run /change-readiness-assessment for [CLIENT NAME]:

Change being implemented: [BRIEF DESCRIPTION — e.g. "Deploying AI-assisted invoice processing in Accounts Payable"]
Go-live date: [DATE]

Impacted groups:
1. [GROUP NAME] — [SIZE] people — [role/function] — [current process they will change]
2. [GROUP NAME] — [SIZE] people — [role/function] — [current process they will change]
[continue for all groups...]

Context for each group (fill what you know):
- Change communication to date: [BRIEF — e.g. "Town hall announcement 3 months ago, no follow-up"]
- Current sentiment signals: [BRIEF — e.g. "AP team concerned about job security; IT team supportive"]
- Prior change experience: [BRIEF — e.g. "Failed ERP rollout in 2023 — trust in IT is low"]
- Leadership sponsorship visibility: [BRIEF]
- Training delivered to date: [NONE / BRIEF]
- Any early adoption or pilots: [NONE / BRIEF]

Known resistance points:
- [LIST any specific objections or concerns you have already heard]
```

## Expected output
ADKAR scorecard per group (Awareness/Desire/Knowledge/Ability/Reinforcement, each 1–5), active barrier point identification, targeted interventions per barrier, readiness risk rating, and recommended sequencing.

## Chain next
- Low-scoring groups inform the `/change-impact-assessment` severity ratings
- Barrier points and interventions feed directly into the `/adoption-plan`

## PPTX output

After `/change-readiness-assessment` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /change-readiness-assessment output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — Change Readiness Assessment"
Slides:
- Slide 1: "ADKAR Readiness Scorecard" — layout: heatmap table (impacted group rows × Awareness/Desire/Knowledge/Ability/Reinforcement columns; 1–5 score with RAG shading; active barrier highlighted per group)
  Content: ADKAR Scorecard section — all groups and dimension scores
- Slide 2: "Priority Interventions" — layout: table (group, active barrier, intervention, owner, timeline)
  Content: Targeted Interventions section — top interventions ordered by barrier severity
Footer: "[FIRM NAME] | [CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 2-slide branded insert. The ADKAR heatmap is the key tool with HR and change leads — red/amber cells pinpoint exactly where adoption investment should go.
