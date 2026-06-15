#!/usr/bin/env python3
"""
Builder: The Ultimate Accenture-Style Guide to Claude — 24-slide PPTX
Mirrors the $39 LinkedIn guide structure: Cover + TOC + 21 skill slides + OS Backbone
"""
import sys
from pathlib import Path

SKILL_PATH = Path(__file__).parent
PPTXKIT_DIR = Path.home() / ".claude/skills/branded-pptx-deck/scripts"
sys.path.insert(0, str(PPTXKIT_DIR))

from pptxkit import Brand, Deck, PP_ALIGN, MSO_ANCHOR, Inches, Pt, RGBColor

OUT_DIR = SKILL_PATH
OUT_FILE = OUT_DIR / "accenture-style-claude-guide-draft.pptx"

FOOTER = "The Ultimate Accenture-Style Guide to Claude  |  360 AI & Transformation Prompts"
TOTAL = 24

d = Deck(footer=FOOTER)
b = d.b

# ─── helpers ─────────────────────────────────────────────────────────────────

def chip(s, label, x, y, w=Inches(2.5), color=None, text_color=None):
    color = color or b.TEAL
    text_color = text_color or b.NAVY
    d.rect(s, x, y, w, Inches(0.28), color, radius=0.08)
    d.text(s, label, x, y + Inches(0.04), w, Inches(0.24),
           size=9, color=text_color, bold=True, align=PP_ALIGN.CENTER)

def section_label(s, label, x, y, color=None):
    color = color or b.TEAL
    d.text(s, label, x, y, Inches(6), Inches(0.22),
           size=9, color=color, bold=True)

def skill_slide(page, domain_num, domain_name, skill_name, when_items,
                workflow_steps, prompt_text, output_items):
    """Render one skill slide — structured 2-column layout."""
    s = d.slide(fill=b.WHITE)
    # teal top band
    d.rect(s, 0, 0, d.W, Inches(0.14), b.TEAL)
    # left navy strip (decorative)
    d.rect(s, 0, 0, Inches(0.06), d.H, b.NAVY)

    # domain chip
    chip(s, f"DOMAIN {domain_num}: {domain_name.upper()}", Inches(0.65), Inches(0.25),
         w=Inches(4.6), color=b.LIGHT_TEAL, text_color=b.ACCENT)

    # skill title
    d.text(s, skill_name, Inches(0.65), Inches(0.58), Inches(12.1), Inches(0.75),
           size=28, color=b.NAVY, bold=True, font=b.FONT_H, shrink=True)

    # teal rule under title
    d.rect(s, Inches(0.65), Inches(1.35), Inches(2.2), Inches(0.04), b.TEAL)

    # ── LEFT COLUMN (x=0.65, w=5.2") ──
    LX = Inches(0.65)
    LW = Inches(5.2)

    # WHEN TO USE
    section_label(s, "WHEN TO USE", LX, Inches(1.48))
    d.rect(s, LX, Inches(1.72), LW, Inches(0.04), b.LIGHT_TEAL)

    when_text = "\n".join(f"•  {item}" for item in when_items)
    d.text(s, when_text, LX, Inches(1.78), LW, Inches(1.15),
           size=12, color=b.INK, ls=1.2, shrink=True)

    # WORKFLOW
    section_label(s, "WORKFLOW", LX, Inches(3.0))
    d.rect(s, LX, Inches(3.22), LW, Inches(0.04), b.LIGHT_TEAL)

    for i, step in enumerate(workflow_steps):
        step_y = Inches(3.3) + i * Inches(0.65)
        # number chip
        d.rect(s, LX, step_y, Inches(0.28), Inches(0.28), b.TEAL, radius=0.12)
        d.text(s, str(i + 1), LX, step_y + Inches(0.02), Inches(0.28), Inches(0.26),
               size=11, color=b.NAVY, bold=True, align=PP_ALIGN.CENTER)
        # step text
        d.text(s, step, LX + Inches(0.35), step_y, LW - Inches(0.38), Inches(0.58),
               size=11.5, color=b.INK, shrink=True)

    # ── RIGHT COLUMN (x=6.1, w=6.8") ──
    RX = Inches(6.1)
    RW = Inches(6.8)

    # KEY PROMPT box (navy background)
    d.rect(s, RX, Inches(1.48), RW, Inches(2.65), b.NAVY, radius=0.06)
    d.text(s, "KEY PROMPT  →  Tell Claude:", RX + Inches(0.2), Inches(1.58),
           RW - Inches(0.4), Inches(0.28), size=10, color=b.GOLD, bold=True)
    d.text(s, prompt_text, RX + Inches(0.2), Inches(1.88), RW - Inches(0.4), Inches(2.1),
           size=12.5, color=b.WHITE, ls=1.3, shrink=True)

    # OUTPUT FORMAT
    section_label(s, "OUTPUT INCLUDES", RX, Inches(4.25))
    d.rect(s, RX, Inches(4.47), RW, Inches(0.04), b.TEAL)

    # Output items in 2 columns
    mid = len(output_items) // 2 + len(output_items) % 2
    col1 = output_items[:mid]
    col2 = output_items[mid:]
    col_w = RW / 2 - Inches(0.1)

    for i, item in enumerate(col1):
        iy = Inches(4.55) + i * Inches(0.38)
        d.rect(s, RX, iy + Inches(0.08), Inches(0.06), Inches(0.06), b.TEAL, radius=0.15)
        d.text(s, item, RX + Inches(0.15), iy, col_w, Inches(0.35),
               size=11, color=b.INK, shrink=True)

    for i, item in enumerate(col2):
        iy = Inches(4.55) + i * Inches(0.38)
        cx = RX + col_w + Inches(0.2)
        d.rect(s, cx, iy + Inches(0.08), Inches(0.06), Inches(0.06), b.TEAL, radius=0.15)
        d.text(s, item, cx + Inches(0.15), iy, col_w, Inches(0.35),
               size=11, color=b.INK, shrink=True)

    d.footer(s, page, TOTAL)
    return s


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 1 — COVER
# ─────────────────────────────────────────────────────────────────────────────
s1 = d.slide(fill=b.NAVY)

# right dark strip
d.rect(s1, Inches(10.2), 0, Inches(3.133), d.H, b.NAVY_2)
# teal left edge
d.rect(s1, 0, 0, Inches(0.18), d.H, b.TEAL)
# teal top accent
d.rect(s1, 0, 0, d.W, Inches(0.12), b.TEAL)

# kicker
d.text(s1, "AI FOR CONSULTANTS", Inches(0.65), Inches(0.9), Inches(8), Inches(0.35),
       size=11, color=b.TEAL, bold=True)

# main title
d.text(s1, "The Ultimate\nAccenture-Style\nGuide to Claude",
       Inches(0.65), Inches(1.45), Inches(9.3), Inches(2.9),
       size=48, color=b.WHITE, bold=True, font=b.FONT_H, shrink=True, ls=1.1)

# teal rule
d.rect(s1, Inches(0.65), Inches(4.45), Inches(3.0), Inches(0.07), b.TEAL)

# subtitle
d.text(s1, "360 AI & Digital Transformation Prompts\nThat Push Claude to Its Limits",
       Inches(0.65), Inches(4.65), Inches(8.5), Inches(0.8),
       size=18, color=b.LIGHT_TEAL, ls=1.3)

# stat chips
stats = [("21", "Strategy Skills"), ("6", "Consulting Domains"), ("360", "Copy-Paste Prompts")]
for i, (num, label) in enumerate(stats):
    cx = Inches(0.65) + i * Inches(2.9)
    d.rect(s1, cx, Inches(5.65), Inches(2.6), Inches(0.95), b.NAVY_2, radius=0.06)
    d.text(s1, num, cx + Inches(0.15), Inches(5.7), Inches(0.9), Inches(0.55),
           size=32, color=b.GOLD, bold=True)
    d.text(s1, label, cx + Inches(1.1), Inches(5.82), Inches(1.4), Inches(0.35),
           size=12, color=b.MUTED)

# right strip content
d.text(s1, "CONSULTING\nFRAMEWORKS", Inches(10.4), Inches(1.5), Inches(2.7), Inches(0.7),
       size=13, color=b.MUTED, align=PP_ALIGN.CENTER)
for i, label in enumerate(["Situation Assessment", "Market Mapping", "War Gaming",
                            "Business Case", "Stakeholder Alignment", "Decision Memo",
                            "Narrative Builder", "KPI Architect"]):
    d.text(s1, label, Inches(10.4), Inches(2.4) + i * Inches(0.52), Inches(2.7), Inches(0.42),
           size=11, color=b.MUTED, align=PP_ALIGN.CENTER)

d.footer(s1, 1, TOTAL, dark=True)


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 2 — TABLE OF CONTENTS
# ─────────────────────────────────────────────────────────────────────────────
s2 = d.slide(fill=b.WHITE)
d.rect(s2, 0, 0, d.W, Inches(0.14), b.TEAL)
d.rect(s2, 0, 0, Inches(0.06), d.H, b.NAVY)

d.text(s2, "What's Inside", Inches(0.65), Inches(0.3), Inches(10), Inches(0.65),
       size=30, color=b.NAVY, bold=True, font=b.FONT_H)
d.text(s2, "21 strategy skills  ·  6 consulting domains  ·  1 reusable transformation OS",
       Inches(0.65), Inches(1.0), Inches(11), Inches(0.35), size=13, color=b.MUTED)
d.rect(s2, Inches(0.65), Inches(1.38), Inches(1.8), Inches(0.05), b.TEAL)

DOMAINS = [
    ("01", "Diagnosis & Framing", ["Situation Assessment", "Growth Barriers", "Assumption Audit"]),
    ("02", "Market & Competitive Intel", ["Market Mapping", "Competitive Intel",
                                          "Customer Segmentation", "Profit Pool Analysis"]),
    ("03", "Strategic Choice & Economics", ["Strategic Options", "Business Case Builder",
                                            "Portfolio Review", "Pricing Strategy"]),
    ("04", "Operating Model & Execution", ["Operating Model Design", "Transformation Roadmap",
                                           "Initiative Prioritizer"]),
    ("05", "Risk, Performance & Value", ["KPI Architect", "Risk & Mitigation",
                                         "Value Realization", "War Gaming"]),
    ("06", "Alignment & Exec Communication", ["Decision Memo", "Narrative Builder",
                                              "Stakeholder Alignment"]),
]

cols = [DOMAINS[:3], DOMAINS[3:]]
for ci, col in enumerate(cols):
    cx = Inches(0.65) + ci * Inches(6.5)
    cy = Inches(1.55)
    for domain_num, domain_name, skills in col:
        # domain header
        d.rect(s2, cx, cy, Inches(6.0), Inches(0.32), b.NAVY, radius=0.04)
        d.text(s2, f"  {domain_num}  {domain_name}", cx, cy + Inches(0.04),
               Inches(6.0), Inches(0.28), size=11.5, color=b.TEAL, bold=True)
        cy += Inches(0.36)
        for skill in skills:
            d.rect(s2, cx + Inches(0.15), cy + Inches(0.07), Inches(0.06), Inches(0.06),
                   b.TEAL, radius=0.15)
            d.text(s2, skill, cx + Inches(0.32), cy, Inches(5.5), Inches(0.32),
                   size=12, color=b.INK)
            cy += Inches(0.33)
        cy += Inches(0.15)

d.footer(s2, 2, TOTAL)


# ─────────────────────────────────────────────────────────────────────────────
# SLIDES 3–23: 21 SKILL SLIDES
# ─────────────────────────────────────────────────────────────────────────────

SKILLS = [
    # (domain_num, domain_name, skill_name, when_items, workflow_steps, prompt_text, output_items)

    # DOMAIN 1
    (1, "Diagnosis & Framing",
     "Situation Assessment",
     ["Business reviews & strategy planning",
      "Turnaround or performance diagnosis",
      "Board prep & investor briefings"],
     ["Frame the assessment question and decision context",
      "Build a MECE view across performance, market, customers & operations",
      "Separate confirmed facts from hypotheses; surface implications"],
     '"Run a situation assessment for [company/function]. Analyze [areas: financial, market, customer, ops]. Use McKinsey-style framing. Separate facts from interpretations. End with strategic implications and open questions."',
     ["Executive Read (1 paragraph)", "Fact Base table",
      "Momentum Signals", "Strategic Issues list", "Open Questions"]),

    (1, "Diagnosis & Framing",
     "Growth Barriers",
     ["Stalled growth or revenue plateau",
      "Funnel or conversion issues",
      "Retention problems or market expansion blockers"],
     ["Define the growth target, baseline, and gap",
      "Build a driver tree for growth; gather signals across acquisition, conversion, retention",
      "Distinguish symptoms from root causes; recommend the binding constraint"],
     '"Diagnose the growth barriers for [company/product]. Build a growth driver tree. Identify where momentum breaks. Separate root causes from symptoms. Recommend the binding constraint and top 3 actions."',
     ["Growth Gap statement", "Driver Tree (MECE)",
      "Barrier Assessment table", "Binding Constraint", "Recommended Actions"]),

    (1, "Diagnosis & Framing",
     "Assumption Audit",
     ["Before board reviews & major investments",
      "Strategy pressure tests & acquisition cases",
      "Launch decisions that rest on unverified beliefs"],
     ["Extract explicit and implicit assumptions across 6 categories",
      "Score each assumption by importance and evidence strength",
      "Convert weak load-bearing assumptions into specific validation tests"],
     '"Audit the assumptions behind [strategy/plan]. Extract explicit and implicit assumptions. Score by importance and evidence strength. Identify load-bearing assumptions. Convert weak ones into a test plan with owners and decision triggers."',
     ["Strategy Under Test", "Assumption Register (scored)",
      "Load-Bearing Assumptions", "Test Plan", "Recommendation"]),

    # DOMAIN 2
    (2, "Market & Competitive Intel",
     "Market Mapping",
     ["Market entry, expansion & category creation",
      "TAM/SAM/SOM sizing for investors or strategy",
      "White space identification & where-to-play choices"],
     ["Define the market boundary and decision question",
      "Build top-down and bottom-up sizing logic; segment MECE by needs/economics",
      "Identify attractive spaces, contested spaces, and white space"],
     '"Map the [market] for [company/context]. Size it top-down and bottom-up. Segment by [dimension: needs/channel/geography/use case]. Identify white space and where-to-play options. Include attractiveness drivers."',
     ["Market Definition", "Size Estimate (2 methods)",
      "Segment Map table", "White Space", "Where-To-Play Options"]),

    (2, "Market & Competitive Intel",
     "Competitive Intel",
     ["Market entry or product launch planning",
      "Pricing changes or channel conflicts",
      "M&A threats and share-defense planning"],
     ["Map competitors' goals, assets, constraints, and economics",
      "Infer likely moves under base, aggressive, and defensive scenarios",
      "Recommend pre-emptive or reactive moves with early signals"],
     '"Model likely competitive moves by [competitor list] in response to [our move/market shift]. Map their incentives, capabilities, and constraints. Build base and aggressive scenarios. Recommend our response playbook with early warning signals."',
     ["Competitor Map table", "Likely Moves by scenario",
      "Response Plan", "Strategic Implication", "Early Warning Signals"]),

    (2, "Market & Competitive Intel",
     "Customer Segmentation",
     ["ICP definition & go-to-market focus",
      "Retention strategy & pricing segmentation",
      "Product roadmap or account coverage decisions"],
     ["Define the decision the segmentation must support",
      "Build MECE segments based on needs, economics, and behavior",
      "Score segments by attractiveness and right to win; recommend priority"],
     '"Create customer segments for [company/product] to support [decision: targeting/pricing/retention]. Build MECE segments based on [data/signals]. Score by size, growth, profitability, and fit. Recommend priority segments with implications."',
     ["Segmentation Objective", "Segment Definitions table",
      "Segment Prioritization scoring", "Strategic Implications"]),

    (2, "Market & Competitive Intel",
     "Profit Pool Analysis",
     ["Market entry and where-to-play decisions",
      "Product portfolio and channel strategy",
      "Understanding where margin actually sits"],
     ["Map revenue and margin by activity, segment, product, or channel",
      "Identify profit concentration, leakage points, and structural drivers",
      "Assess who captures value and why; recommend strategic implications"],
     '"Analyze the profit pool in [market/value chain/product set]. Map revenue and margin by [dimension]. Identify where profit concentrates, where it leaks, and the structural reasons. Recommend strategic implications for [company]."',
     ["Scope definition", "Profit Pool Map table",
      "Value Capture by player", "Strategic Implications", "Where-to-play recommendation"]),

    # DOMAIN 3
    (3, "Strategic Choice & Economics",
     "Strategic Options",
     ["Choosing a growth path or market entry strategy",
      "Build-buy-partner decisions",
      "Avoiding false binaries in executive strategy debates"],
     ["Generate 3-5 mutually distinct, viable strategic options",
      "Define decision criteria; assess each option on attractiveness, feasibility, and risk",
      "Identify hybrids; recommend best path with trade-offs visible"],
     '"Generate strategic options for [decision]. Create 3-5 meaningfully distinct paths. Evaluate each on [criteria: attractiveness/feasibility/risk/economics/fit]. Show trade-offs and what must be true for each. Recommend the best path with rationale."',
     ["Decision framing", "Options table (upside/trade-off/what-must-be-true)",
      "Evaluation matrix", "Recommendation", "Next Tests"]),

    (3, "Strategic Choice & Economics",
     "Business Case Builder",
     ["Investment decisions, M&A screening, product bets",
      "ROI, payback, and NPV analysis for board approval",
      "Pricing moves and transformation program funding"],
     ["Identify value drivers, cost drivers, timing, and risks",
      "Build base, downside, and upside cases with visible assumptions",
      "Calculate ROI/NPV/payback; recommend proceed, test, or redesign"],
     '"Build a business case for [initiative/investment]. Model value drivers, costs, and timing. Create base, downside, and upside scenarios. Calculate [ROI/payback/NPV]. Surface load-bearing assumptions with sensitivity analysis. Recommend proceed or redesign."',
     ["Decision statement", "Economics Summary (3 scenarios)",
      "Value Drivers table", "Cost & Investment", "Risks", "Recommendation"]),

    (3, "Strategic Choice & Economics",
     "Portfolio Review",
     ["Capital allocation and resource reallocation decisions",
      "Product or market portfolio rationalization",
      "Annual planning: where to invest, hold, fix, or exit"],
     ["Define the portfolio and evaluation criteria",
      "Score each element on attractiveness, performance, fit, and right to win",
      "Identify invest/maintain/fix/exit candidates; recommend allocation moves"],
     '"Review the portfolio of [businesses/products/markets/initiatives] for [company]. Score each on attractiveness, performance, strategic fit, and right to win. Identify invest, maintain, fix, harvest, and exit candidates. Recommend resource reallocation moves."',
     ["Portfolio Scope", "Evaluation Matrix (scored)",
      "Allocation Moves table", "Decisions Required", "Trade-offs"]),

    (3, "Strategic Choice & Economics",
     "Pricing Strategy",
     ["Price increase readiness or discount leakage",
      "Packaging redesign and monetization optimization",
      "Understanding willingness to pay by segment"],
     ["Diagnose leakage across list price, discounting, mix, and packaging",
      "Assess willingness to pay by segment and competitive alternatives",
      "Generate pricing moves with risks; design a pilot or rollout sequence"],
     '"Develop a pricing strategy for [product/service/segment]. Diagnose leakage across [list price/discounting/mix/packaging]. Assess willingness to pay by segment. Generate pricing moves with risks. Include a pilot design and rollout sequence."',
     ["Pricing Objective", "Diagnosis table",
      "Segment Price Logic", "Recommended Moves", "Risks & Tests", "Pilot design"]),

    # DOMAIN 4
    (4, "Operating Model & Execution",
     "Operating Model Design",
     ["Transformations and new business unit setup",
      "Functional redesigns and scale-up challenges",
      "Aligning org structure to a new strategy"],
     ["Identify required capabilities from the strategy",
      "Diagnose current model gaps; design target roles, decision rights, and governance",
      "Recommend implementation phases with transition risks"],
     '"Design the target operating model for [company/function] to execute [strategy]. Identify required capabilities. Map current gaps. Design target roles, decision rights, governance, processes, and metrics. Show transition risks and first moves."',
     ["Strategic Requirement", "Capability Model (gap analysis)",
      "Target Model elements", "Decision Rights table", "Transition Plan"]),

    (4, "Operating Model & Execution",
     "Transformation Roadmap",
     ["Strategy → execution: turning a plan into a delivery roadmap",
      "Cost programs, digital transformations, post-merger integration",
      "PMO setup and governance design"],
     ["Identify workstreams and capabilities required",
      "Sequence phases by value, dependency, and readiness; assign owners and milestones",
      "Build the first 90-day plan with decision gates and governance"],
     '"Build a transformation roadmap for [company/program] to achieve [outcome] by [date]. Identify workstreams. Sequence by dependency and value. Assign owners, milestones, and governance. Include a first 90-day plan and decision gates."',
     ["Target Outcome", "Workstreams table",
      "Roadmap (phased)", "First 90 Days", "Governance rhythm"]),

    (4, "Operating Model & Execution",
     "Initiative Prioritizer",
     ["Too many projects competing for limited resources",
      "Annual planning and OKR focus-setting",
      "Transformation portfolio rationalization"],
     ["Inventory initiatives and score by impact, feasibility, urgency, and fit",
      "Identify dependencies and sequencing constraints",
      "Select the vital few; build the priority roadmap and kill list"],
     '"Prioritize the following initiatives for [company/team]: [list]. Score each on impact, feasibility, urgency, and strategic fit. Identify dependencies. Recommend the vital few with a phased roadmap. Include a kill list with rationale and revisit triggers."',
     ["Criteria & weights", "Initiative Assessment (scored)",
      "Priority Roadmap", "Kill List with rationale", "Dependencies"]),

    # DOMAIN 5
    (5, "Risk, Performance & Value",
     "KPI Architect",
     ["Metrics are noisy, backward-looking, or disconnected from decisions",
      "Building dashboards for strategy execution or transformation governance",
      "OKR design and operating review cadence"],
     ["Start from decisions leaders need to make; build the value driver tree",
      "Separate outcome, driver, and activity metrics; remove vanity metrics",
      "Assign owners, thresholds, and review cadence"],
     '"Design a KPI system for [objective/team/function]. Start from the decisions [leaders] must make. Build a driver tree. Separate outcome, driver, and activity metrics. Remove vanity metrics. Assign owners and thresholds. Include a review cadence."',
     ["Strategic Objective", "KPI System table (with decision link)",
      "Driver Tree", "Metrics To Remove", "Review Cadence"]),

    (5, "Risk, Performance & Value",
     "Risk & Mitigation",
     ["Strategy or initiative approval requiring a serious risk view",
      "Board materials, launch planning, transformation governance",
      "Investment decisions with material downside risks"],
     ["Identify risks across 7 categories: market, customer, competitor, financial, operational, regulatory, organizational",
      "Score likelihood and impact; define mitigations, triggers, and owners",
      "Recommend go, no-go, redesign, or gated approval with residual risk"],
     '"Build a strategic risk register for [strategy/initiative]. Identify risks across market, customer, competitive, financial, operational, regulatory, and org categories. Score likelihood and impact. Define mitigations, triggers, and owners. Recommend go/no-go."',
     ["Strategy Under Review", "Risk Register (scored)",
      "Highest-Risk Assumptions", "Contingency Moves", "Go/No-Go recommendation"]),

    (5, "Risk, Performance & Value",
     "Value Realization",
     ["Ensuring promised transformation value is actually captured",
      "Benefits tracking for acquisitions and synergy programs",
      "Post-launch governance for major initiatives"],
     ["Define the value ambition and benefit categories",
      "Assign owners and measurement methods; set baselines, targets, and timing",
      "Define governance, escalation, and proof standards"],
     '"Build a value realization plan for [initiative/transformation/acquisition]. Define benefit categories. Set baselines and targets. Assign owners and proof standards. Include governance cadence and escalation triggers. Identify risks to capture."',
     ["Value Ambition", "Value Ledger table",
      "Governance cadence", "Risks To Capture", "Proof Standards"]),

    (5, "Risk, Performance & Value",
     "War Gaming",
     ["Before committing to a strategy that rivals could disrupt",
      "Competitive response planning and scenario stress-testing",
      "Regulatory, market shift, or execution failure scenarios"],
     ["Identify scenario dimensions: competitor, customer, market, regulatory, operational",
      "Build base, adverse, and aggressive scenarios; assess impact on economics",
      "Identify early warning signals; recommend defensive and offensive responses"],
     '"War-game the following strategy: [strategy summary]. Build base, adverse, and aggressive scenarios across [competitor/market/regulatory/operational] dimensions. Identify vulnerabilities and early warning signals. Produce a response playbook with owners."',
     ["Strategy Under Test", "Scenarios table (5 dimensions)",
      "Vulnerabilities analysis", "Response Playbook", "Early Warning Signals"]),

    # DOMAIN 6
    (6, "Alignment & Exec Communication",
     "Decision Memo",
     ["Written recommendation for board or executive approval",
      "Investment recommendation or strategy approval memo",
      "Any decision where a deck would be overkill"],
     ["Extract the recommendation and strongest supporting evidence",
      "Summarize alternatives considered and why they lost",
      "State risks, mitigations, economics, and next steps; write answer-first"],
     '"Write a decision memo for [audience] recommending [action]. Lead with the recommendation. Include: decision required, context and urgency, options considered with trade-offs, evidence, risks and mitigations, and immediate next steps after approval."',
     ["Recommendation (answer-first)", "Decision Required",
      "Context & Urgency", "Options Considered", "Evidence", "Risks", "Next Steps"]),

    (6, "Alignment & Exec Communication",
     "Narrative Builder",
     ["Strategy story that must land quickly with executives or boards",
      "Board deck storyline and headline sequencing",
      "Any recommendation that needs Pyramid Principle structure"],
     ["Choose the story pattern: Pyramid, SCQA, options, transformation, or roadmap",
      "Build a headline sequence that tells the story by itself",
      "Prepare hostile questions and answers for the most likely objections"],
     '"Build an executive narrative for [audience] recommending [action/strategy]. Use [Pyramid Principle / SCQA]. Lead with the answer. Create a headline sequence that tells the story independently. Prepare answers to the top 5 hostile questions a skeptical executive will ask."',
     ["Audience & Decision", "Core Message (1 sentence)",
      "Storyline (headline per page)", "Pyramid Logic", "Hostile Q&A"]),

    (6, "Alignment & Exec Communication",
     "Stakeholder Alignment",
     ["Executive buy-in for a strategy or transformation",
      "Board approval and pre-wiring campaigns",
      "Change management for programs with significant resistance"],
     ["Identify stakeholders and map their influence relationships",
      "Map each person's interests, likely concerns, and decision criteria",
      "Build a pre-wire engagement plan sequenced before the formal meeting"],
     '"Map stakeholder alignment for [decision/program]. Identify who must say yes and who influences them. Map each stakeholder\'s interests, concerns, and decision criteria. Assess support level. Build a pre-wire plan with actions, owners, timing, and desired outcomes."',
     ["Decision Path", "Stakeholder Map (influence/stance/message)",
      "Resistance Points", "Pre-Wire Plan", "Objections & Responses"]),
]

for i, skill_data in enumerate(SKILLS):
    skill_slide(i + 3, *skill_data)  # pages 3–23


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 24 — THE REUSABLE CONSULTING OS
# ─────────────────────────────────────────────────────────────────────────────
s24 = d.slide(fill=b.NAVY)
d.rect(s24, 0, 0, Inches(0.18), d.H, b.TEAL)
d.rect(s24, 0, 0, d.W, Inches(0.12), b.TEAL)

d.text(s24, "THE REUSABLE CONSULTING OS", Inches(0.65), Inches(0.28), Inches(11), Inches(0.35),
       size=11, color=b.TEAL, bold=True)
d.text(s24, "The Accenture-Style Engagement Backbone",
       Inches(0.65), Inches(0.68), Inches(10), Inches(0.65),
       size=32, color=b.WHITE, bold=True, font=b.FONT_H, shrink=True)
d.text(s24, "Apply this 6-stage OS to every transformation, strategy engagement, or digital program.",
       Inches(0.65), Inches(1.38), Inches(11), Inches(0.35), size=13, color=b.LIGHT_TEAL)
d.rect(s24, Inches(0.65), Inches(1.8), Inches(2.5), Inches(0.05), b.TEAL)

STAGES = [
    ("01", "ASSESS", "Situation assessment, assumption audit, growth barriers", "Slides 3–5"),
    ("02", "DESIGN", "Market mapping, segmentation, strategic options, profit pool", "Slides 6–11"),
    ("03", "TRANSFORM", "Operating model design, transformation roadmap, business case", "Slides 12–14"),
    ("04", "IMPLEMENT", "Initiative prioritizer, KPI architect, value realization", "Slides 15–17"),
    ("05", "GOVERN", "Risk & mitigation, war gaming, KPI review cadence", "Slides 16–18"),
    ("06", "COMMUNICATE", "Decision memo, narrative builder, stakeholder alignment", "Slides 21–23"),
]

card_w = Inches(1.95)
card_gap = Inches(0.18)
start_x = Inches(0.55)

for i, (num, stage, desc, slides) in enumerate(STAGES):
    cx = start_x + i * (card_w + card_gap)
    # card background
    d.rect(s24, cx, Inches(2.05), card_w, Inches(4.3), b.NAVY_2, radius=0.06)
    # teal top accent on card
    d.rect(s24, cx, Inches(2.05), card_w, Inches(0.08), b.TEAL, radius=0.04)
    # number
    d.text(s24, num, cx + Inches(0.12), Inches(2.2), card_w - Inches(0.24), Inches(0.35),
           size=11, color=b.TEAL, bold=True)
    # stage name
    d.text(s24, stage, cx + Inches(0.12), Inches(2.58), card_w - Inches(0.24), Inches(0.45),
           size=16, color=b.WHITE, bold=True, font=b.FONT_H, shrink=True)
    # description
    d.text(s24, desc, cx + Inches(0.12), Inches(3.12), card_w - Inches(0.24), Inches(1.8),
           size=11, color=b.LIGHT_TEAL, ls=1.3, shrink=True)
    # slide reference
    d.rect(s24, cx + Inches(0.12), Inches(5.6), card_w - Inches(0.24), Inches(0.28),
           b.NAVY, radius=0.06)
    d.text(s24, slides, cx + Inches(0.12), Inches(5.62), card_w - Inches(0.24), Inches(0.26),
           size=9.5, color=b.TEAL, bold=True, align=PP_ALIGN.CENTER)

    # arrow between cards (except last)
    if i < 5:
        ax = cx + card_w + Inches(0.04)
        d.text(s24, "→", ax, Inches(3.7), Inches(0.14), Inches(0.35),
               size=16, color=b.TEAL, bold=True, align=PP_ALIGN.CENTER)

# bottom CTA
d.rect(s24, Inches(0.55), Inches(6.45), d.W - Inches(1.1), Inches(0.65), b.TEAL, radius=0.06)
d.text(s24, "Copy any skill prompt  ·  Run it in Claude  ·  Customize the output template  ·  Deliver client-ready work",
       Inches(0.7), Inches(6.55), d.W - Inches(1.4), Inches(0.4),
       size=13, color=b.NAVY, bold=True, align=PP_ALIGN.CENTER)

d.footer(s24, 24, TOTAL, dark=True)


# ─────────────────────────────────────────────────────────────────────────────
# SAVE
# ─────────────────────────────────────────────────────────────────────────────
d.save(OUT_FILE)
print(f"\nDeck: {OUT_FILE}")
