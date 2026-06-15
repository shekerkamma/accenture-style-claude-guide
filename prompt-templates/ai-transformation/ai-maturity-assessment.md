---
skill: /ai-maturity-assessment
pack: ai-transformation
chains-from: /situation-assessment
chains-into: /ai-use-case-prioritiser, /data-readiness-assessment
---

# Prompt Template: AI Maturity Assessment

**When to use:** Start of any AI strategy engagement — before recommending investments, use cases, or operating model changes.

## Copy-paste prompt

```
Run /ai-maturity-assessment for [CLIENT NAME]:

Organisation: [NAME]
Industry: [INDUSTRY]
Size: [EMPLOYEE COUNT] employees / [ANNUAL REVENUE]
Scope: [Whole enterprise / [BUSINESS UNIT] only]

What we know about their AI today:
- Data infrastructure: [BRIEF DESCRIPTION — e.g. "cloud DW on Snowflake, data team of 8"]
- AI tools in use: [LIST — e.g. "GitHub Copilot, Azure OpenAI pilot in marketing"]
- AI team: [EXISTS / DOESN'T EXIST / size and location]
- Known AI initiatives: [LIST]
- AI governance / responsible AI policy: [EXISTS / DOESN'T EXIST]
- Culture / leadership attitude toward AI: [BRIEF — e.g. "CEO is a champion, middle management cautious"]

Assessment purpose: [e.g. "Inform the AI strategy recommendation" / "Prepare the board investment case"]
```

## Expected output
Maturity scorecard (5 dimensions × 1–4 scale), dimension deep-dives with specific evidence and blockers, peer benchmark, and 2–3 highest-leverage priority investments.

## Chain next
- Proceed to `/ai-use-case-prioritiser` to identify which use cases match the maturity level
- Run `/data-readiness-assessment` in parallel to assess data fitness

## PPTX output

After `/ai-maturity-assessment` completes, chain to `/branded-pptx-deck`:

```
/branded-pptx-deck

Source: paste the full /ai-maturity-assessment output for [CLIENT NAME]
Deck title: "[CLIENT NAME] — AI Maturity Assessment"
Slides:
- Slide 1: "AI Maturity Scorecard" — layout: scorecard matrix (5 dimension rows × 4 level columns; shade the current level per dimension)
  Content: Maturity Scorecard section — all 5 dimensions with current level and evidence
- Slide 2: "Priority Investments" — layout: 3 cards (investment title, rationale, expected maturity uplift)
  Content: Priority Investments section — top 3 recommendations
Footer: "[CLIENT NAME] | [DATE] | CONFIDENTIAL"
```

Produces a 2-slide branded insert. The scorecard matrix is the primary executive artefact — dark cells show current level, lighter cells show the gap to Leading.
