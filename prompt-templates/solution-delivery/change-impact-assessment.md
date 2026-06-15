---
skill: /change-impact-assessment
pack: solution-delivery
chains-from: /change-readiness-assessment, /solution-blueprint
chains-into: /adoption-plan
---

# Prompt Template: Change Impact Assessment

**When to use:** In parallel with or after the change readiness assessment — assess the severity and breadth of change across process, technology, role, and behaviour dimensions.

## Copy-paste prompt

```
Run /change-impact-assessment for [CLIENT NAME]:

Change being implemented: [BRIEF]
Impacted groups (from /change-readiness-assessment): [LIST]

For each impacted group, describe what changes:

[GROUP 1 NAME]:
- Process changes: [BRIEF — e.g. "Approval workflow changes from email to system-generated queue"]
- Technology changes: [BRIEF — e.g. "New AI dashboard replaces 3 legacy screens"]
- Role changes: [BRIEF — e.g. "Role expands to include AI review; some tasks automated away"]
- Behaviour changes required: [BRIEF — e.g. "Must trust AI recommendations rather than manually verifying every line"]

[GROUP 2 NAME]:
- Process changes: [BRIEF]
- Technology changes: [BRIEF]
- Role changes: [BRIEF]
- Behaviour changes required: [BRIEF]

[continue for all groups...]

Known compounding factors:
- [e.g. "This change lands alongside a restructure announcement"]
- [e.g. "Training budget limited — no classroom delivery available"]
```

## Expected output
Impact severity matrix (H/M/L per dimension per group), compounding impact identification, change volume heatmap, group-level change narrative, and design implications for the adoption plan.

## Chain next
- High-severity groups and dimensions become the focus of the `/adoption-plan` activity schedule

## PPTX output

After `/change-impact-assessment` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /change-impact-assessment output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — Change Impact Assessment"
Slides:
- Slide 1: "Change Impact Matrix" — layout: heatmap table (impacted group rows × Process/Technology/Role/Behaviour columns; H/M/L cells with RAG shading)
  Content: Impact Severity Matrix section — all groups across all dimensions
- Slide 2: "High-Impact Groups — Design Implications" — layout: two-column (group + change narrative left / adoption plan implication right)
  Content: Group-Level Change Narratives + Design Implications — HIGH severity groups only
Footer: "[CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 2-slide branded insert. Filter Slide 2 to HIGH-rated groups — these drive the adoption plan activity schedule.
