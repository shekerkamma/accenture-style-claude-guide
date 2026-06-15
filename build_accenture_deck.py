#!/usr/bin/env python3
"""
Accenture Strategy Analysis — 24-slide PPTX
Same 21-skill structure as the guide deck but populated with real Accenture data.
Source: FY2025 annual results, 10-K, competitive intelligence (June 2026)
"""
import sys
from pathlib import Path

PPTXKIT_DIR = Path.home() / ".claude/skills/branded-pptx-deck/scripts"
sys.path.insert(0, str(PPTXKIT_DIR))
from pptxkit import Brand, Deck, PP_ALIGN, MSO_ANCHOR, Inches, Pt, RGBColor

OUT_DIR = Path(__file__).parent
OUT_FILE = OUT_DIR / "accenture-strategy-analysis-v2-draft.pptx"
FOOTER = "Accenture Strategy Analysis  |  Sources: FY2025 10-K + GitHub:Accenture (223 repos)  |  June 2026"
TOTAL = 24

d = Deck(footer=FOOTER)
b = d.b

# ── helpers ───────────────────────────────────────────────────────────────────

def tbl(s, headers, rows, x, y, w, col_widths=None, row_h=Inches(0.32)):
    """Render a simple table with teal header row and alternating navy rows."""
    n = len(headers)
    if col_widths is None:
        col_widths = [w / n] * n
    # header row
    cx = x
    d.rect(s, x, y, w, row_h, b.TEAL)
    for i, h in enumerate(headers):
        d.text(s, h, cx + Inches(0.06), y + Inches(0.04), col_widths[i] - Inches(0.08),
               row_h - Inches(0.06), size=9.5, color=b.NAVY, bold=True, shrink=True)
        cx += col_widths[i]
    # data rows
    fills = [b.NAVY, b.NAVY_2]
    for ri, row in enumerate(rows):
        ry = y + row_h * (ri + 1)
        d.rect(s, x, ry, w, row_h, fills[ri % 2])
        cx = x
        for i, cell in enumerate(row):
            d.text(s, str(cell), cx + Inches(0.06), ry + Inches(0.04),
                   col_widths[i] - Inches(0.08), row_h - Inches(0.06),
                   size=9.5, color=b.WHITE, shrink=True)
            cx += col_widths[i]

def skill_slide(page, domain_num, domain_name, skill_name,
                action_title, exec_read, bullets, tbl_headers, tbl_rows,
                tbl_col_widths=None, bottom_note=None):
    """Accenture-populated skill slide: action title + findings + data table."""
    s = d.slide(fill=b.WHITE)
    d.rect(s, 0, 0, d.W, Inches(0.14), b.TEAL)
    d.rect(s, 0, 0, Inches(0.06), d.H, b.NAVY)

    # domain + skill chip
    chip_w = Inches(4.8)
    d.rect(s, Inches(0.65), Inches(0.22), chip_w, Inches(0.26), b.LIGHT_TEAL)
    d.text(s, f"DOMAIN {domain_num}: {domain_name.upper()}  ·  {skill_name.upper()}",
           Inches(0.72), Inches(0.26), chip_w - Inches(0.1), Inches(0.2),
           size=8.5, color=b.ACCENT, bold=True)

    # action title (the so-what for Accenture)
    d.text(s, action_title, Inches(0.65), Inches(0.55), Inches(12.3), Inches(0.8),
           size=24, color=b.NAVY, bold=True, font=b.FONT_H, shrink=True, ls=1.1)
    d.rect(s, Inches(0.65), Inches(1.38), Inches(2.0), Inches(0.04), b.TEAL)

    # ── LEFT COLUMN: exec read + bullets ──
    LX, LW = Inches(0.65), Inches(5.1)

    # exec read (italic summary)
    d.text(s, exec_read, LX, Inches(1.5), LW, Inches(0.88),
           size=11.5, color=b.MUTED, italic=True, ls=1.3, shrink=True)

    # key finding bullets
    d.text(s, "KEY FINDINGS", LX, Inches(2.42), LW, Inches(0.22),
           size=8.5, color=b.TEAL, bold=True)
    d.rect(s, LX, Inches(2.64), LW, Inches(0.03), b.LIGHT_TEAL)

    for i, bullet in enumerate(bullets):
        by = Inches(2.72) + i * Inches(0.62)
        d.rect(s, LX, by + Inches(0.08), Inches(0.06), Inches(0.06), b.TEAL, radius=0.15)
        d.text(s, bullet, LX + Inches(0.18), by, LW - Inches(0.2), Inches(0.58),
               size=11, color=b.INK, shrink=True, ls=1.2)

    if bottom_note:
        d.rect(s, LX, Inches(6.1), LW, Inches(0.56), b.SOFT, radius=0.05)
        d.text(s, bottom_note, LX + Inches(0.1), Inches(6.18), LW - Inches(0.2), Inches(0.45),
               size=9.5, color=b.MUTED, italic=True, shrink=True)

    # ── RIGHT COLUMN: data table ──
    RX, RW = Inches(6.05), Inches(6.95)
    d.text(s, "ACCENTURE OUTPUT", RX, Inches(1.5), RW, Inches(0.22),
           size=8.5, color=b.TEAL, bold=True)
    d.rect(s, RX, Inches(1.72), RW, Inches(0.03), b.TEAL)

    row_h = Inches(0.32) if len(tbl_rows) <= 5 else Inches(0.28)
    tbl(s, tbl_headers, tbl_rows, RX, Inches(1.78), RW,
        col_widths=tbl_col_widths, row_h=row_h)

    d.footer(s, page, TOTAL)
    return s


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 1 — COVER
# ─────────────────────────────────────────────────────────────────────────────
s1 = d.slide(fill=b.NAVY)
d.rect(s1, Inches(10.1), 0, Inches(3.233), d.H, b.NAVY_2)
d.rect(s1, 0, 0, Inches(0.18), d.H, b.TEAL)
d.rect(s1, 0, 0, d.W, Inches(0.12), b.TEAL)

d.text(s1, "ACCENTURE  ·  STRATEGY ANALYSIS", Inches(0.65), Inches(0.9),
       Inches(9), Inches(0.32), size=10, color=b.TEAL, bold=True)
d.text(s1, "Accenture Strategy\nAnalysis 2026",
       Inches(0.65), Inches(1.35), Inches(9.2), Inches(2.1),
       size=48, color=b.WHITE, bold=True, font=b.FONT_H, shrink=True, ls=1.1)
d.rect(s1, Inches(0.65), Inches(3.55), Inches(3.0), Inches(0.07), b.TEAL)
d.text(s1, "21 consulting frameworks  ·  Applied to Accenture FY2025 data\nPowered by the Accenture-Style Claude Skills Guide",
       Inches(0.65), Inches(3.75), Inches(8.8), Inches(0.75), size=16, color=b.LIGHT_TEAL, ls=1.3)

stats = [("$69.7B", "FY2025 Revenue"), ("$2.7B", "GenAI Revenue"), ("7%", "Revenue Growth"), ("$5.9B", "GenAI Bookings")]
for i, (num, label) in enumerate(stats):
    cx = Inches(0.65) + i * Inches(2.28)
    d.rect(s1, cx, Inches(4.7), Inches(2.1), Inches(0.9), b.NAVY_2, radius=0.06)
    d.text(s1, num, cx + Inches(0.12), Inches(4.76), Inches(2.0), Inches(0.46),
           size=26, color=b.GOLD, bold=True)
    d.text(s1, label, cx + Inches(0.12), Inches(5.22), Inches(1.9), Inches(0.28),
           size=10.5, color=b.MUTED)

d.text(s1, "GITHUB SIGNALS\ngithub.com/Accenture", Inches(10.3), Inches(1.4), Inches(2.7), Inches(0.55),
       size=11, color=b.MUTED, align=PP_ALIGN.CENTER)
for i, lbl in enumerate(["223 public repos", "AI Refinery SDK v1.31", "mcp-bench NeurIPS25",
                          "AmpliGraph 2.2K stars", "Federated Learning Lab",
                          "Python-first AI stack", "Apache 2.0 licensed", "Active since 2015"]):
    d.text(s1, lbl, Inches(10.3), Inches(2.1) + i * Inches(0.5), Inches(2.7), Inches(0.38),
           size=10.5, color=b.MUTED, align=PP_ALIGN.CENTER)
d.footer(s1, 1, TOTAL, dark=True)


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 2 — EXECUTIVE OVERVIEW (replaces generic TOC)
# ─────────────────────────────────────────────────────────────────────────────
s2 = d.slide(fill=b.WHITE)
d.rect(s2, 0, 0, d.W, Inches(0.14), b.TEAL)
d.rect(s2, 0, 0, Inches(0.06), d.H, b.NAVY)
d.text(s2, "Executive Overview: Accenture FY2025 Snapshot",
       Inches(0.65), Inches(0.3), Inches(11.5), Inches(0.65),
       size=28, color=b.NAVY, bold=True, font=b.FONT_H)
d.text(s2, "The $3B AI bet is paying off — but structural headwinds require a second act",
       Inches(0.65), Inches(1.0), Inches(11.5), Inches(0.35), size=13.5, color=b.MUTED, italic=True)
d.rect(s2, Inches(0.65), Inches(1.4), Inches(2.0), Inches(0.05), b.TEAL)

# KPI grid — 4 columns
kpis = [
    ("$69.7B", "Total Revenue", "+7% YoY", b.GOLD),
    ("$2.7B", "GenAI Revenue", "Tripled FY24→FY25", b.TEAL),
    ("$80.6B", "New Bookings", "Record year", b.GOLD),
    ("77,000", "AI Practitioners", "Target: 80K", b.TEAL),
    ("$5.9B", "GenAI Bookings", "Nearly doubled", b.GOLD),
    ("14.1%", "Consulting Mkt Share", "#1 by revenue", b.TEAL),
    ("129", "Deals >$100M/qtr", "Record", b.GOLD),
    ("$10.9B", "Free Cash Flow", "FY2025", b.TEAL),
]
card_w, card_h = Inches(2.9), Inches(1.1)
for i, (num, label, note, col) in enumerate(kpis):
    row, col_i = divmod(i, 4)
    cx = Inches(0.55) + col_i * (card_w + Inches(0.12))
    cy = Inches(1.65) + row * (card_h + Inches(0.12))
    d.rect(s2, cx, cy, card_w, card_h, b.NAVY, radius=0.06)
    d.text(s2, num, cx + Inches(0.15), cy + Inches(0.1), card_w - Inches(0.3), Inches(0.5),
           size=26, color=col, bold=True)
    d.text(s2, label, cx + Inches(0.15), cy + Inches(0.6), card_w - Inches(0.3), Inches(0.26),
           size=11, color=b.WHITE)
    d.text(s2, note, cx + Inches(0.15), cy + Inches(0.84), card_w - Inches(0.3), Inches(0.2),
           size=9.5, color=b.MUTED)

d.text(s2, "FY2026 Guidance: 2–5% growth  ·  Adj. EPS +5–8%  ·  $9.3B+ to shareholders  |  GitHub: 223 repos, AI Refinery SDK v1.31.3 (active), mcp-bench @ NeurIPS 2025",
       Inches(0.65), Inches(6.6), Inches(12.1), Inches(0.3), size=10.5, color=b.MUTED)
d.footer(s2, 2, TOTAL)


# ─────────────────────────────────────────────────────────────────────────────
# SLIDES 3–23: 21 SKILL SLIDES — POPULATED WITH ACCENTURE DATA
# ─────────────────────────────────────────────────────────────────────────────

# ── SLIDE 3: Situation Assessment ────────────────────────────────────────────
skill_slide(3, 1, "Diagnosis & Framing", "Situation Assessment",
    "Accenture Enters FY2026 From Strength But Faces a Structural Transition",
    "Revenue grew 7% to $69.7B in FY2025 — the $3B GenAI bet is working. But FY2026 guidance of 2–5% reflects a deliberate pause: US federal headwinds, macro softness, and a market asking whether AI advisory fees will be commoditized.",
    [
        "GenAI revenue tripled to $2.7B; bookings of $5.9B build a 2-year forward pipeline",
        "US federal exposure creates a 1–1.5% drag on FY2026 growth — manageable but visible",
        "Premium perception gap vs MBB limits pricing power on pure strategy mandates",
        "'Reinvention partner' positioning is gaining traction: 129 deals >$100M per quarter"
    ],
    ["Area", "Evidence", "Interpretation", "Confidence"],
    [
        ["Financial", "$69.7B, +7% FY2025", "AI tailwind offsetting macro softness", "High"],
        ["AI Position", "$2.7B GenAI, tripled", "First-mover advantage holding", "High"],
        ["Market Share", "14.1% consulting", "Scale leader, premium gap vs MBB", "High"],
        ["Risk", "US federal -1–1.5% FY2026", "Near-term drag, diversifiable", "Medium"],
        ["Talent", "77K AI practitioners", "On track to 80K target", "High"],
    ],
    tbl_col_widths=[Inches(1.5), Inches(2.0), Inches(2.2), Inches(1.25)],
    bottom_note="Source: Accenture FY2025 Annual Report, 10-K (Sept 2025)"
)

# ── SLIDE 4: Growth Barriers ──────────────────────────────────────────────────
skill_slide(4, 1, "Diagnosis & Framing", "Growth Barriers",
    "Growth Is Decelerating From 7% to 2–5% — Three Binding Constraints Identified",
    "FY2026 guidance of 2–5% vs FY2025's 7% reflects external constraints rather than capability failure. The binding constraint is not AI demand (bookings are strong) but federal budget freezes, macro spend compression, and an emerging pricing floor on traditional T&M work.",
    [
        "US federal freeze: $3–5B exposure, 1–1.5% revenue headwind in FY2026",
        "T&M pricing pressure: boutique AI firms offering comparable work at 40–60% of day rates",
        "Client budget reallocation from transformation to AI ROI verification (pause-and-measure phase)",
        "GenAI bookings ($5.9B) signal demand but 12–18 month conversion lag suppresses near-term revenue"
    ],
    ["Growth Driver", "FY2025 Status", "FY2026 Risk", "Constraint Type"],
    [
        ["GenAI advisory", "$2.7B, +200%", "Sustaining", "Opportunity"],
        ["Technology impl.", "~$30B, +6%", "Moderate", "Competition"],
        ["US Federal", "~$4B, stable", "Freeze risk", "External"],
        ["Operations", "~$15B, +3%", "AI displacement", "Structural"],
        ["Strategy (pure)", "~$8B, flat", "MBB pricing gap", "Structural"],
    ],
    tbl_col_widths=[Inches(1.8), Inches(1.6), Inches(1.8), Inches(1.75)],
    bottom_note="Binding constraint: external headwinds + pricing floor on traditional work — not capability"
)

# ── SLIDE 5: Assumption Audit ─────────────────────────────────────────────────
skill_slide(5, 1, "Diagnosis & Framing", "Assumption Audit",
    "Three Load-Bearing Assumptions Underpin Accenture's 'Reinvention Partner' Strategy",
    "The $3B GenAI bet rests on assumptions that are proving out — but two remain inadequately tested as of FY2026: whether AI advisory is defensible against OpenAI direct-to-enterprise, and whether outcome-based pricing can scale.",
    [
        "PROVEN: GenAI demand is real — $5.9B in bookings and tripled revenue validate the market",
        "AT RISK: Defensibility vs OpenAI's Feb 2026 Frontier Alliance embeds AI vendors inside client teams",
        "UNPROVEN: Outcome-based pricing at scale — still <10% of Accenture contracts",
        "CRITICAL: The 77K practitioner advantage is temporary — MBB and boutiques are closing the gap"
    ],
    ["Assumption", "Importance", "Evidence Strength", "Risk Level"],
    [
        ["GenAI demand sustains at scale", "Critical", "Strong (bookings)", "Low"],
        ["$3B investment creates IP moat", "Critical", "Moderate (GenWizard)", "Medium"],
        ["OpenAI stays a partner not rival", "High", "Weak (Frontier Alliance)", "High"],
        ["Outcome pricing scales beyond pilots", "High", "Weak (<10% deals)", "High"],
        ["MBB can't build delivery at scale", "Medium", "Weakening (BCG X)", "Medium"],
    ],
    tbl_col_widths=[Inches(2.4), Inches(1.3), Inches(1.8), Inches(1.45)],
    bottom_note="Recommended test: pilot 3 outcome-based GenAI contracts by Q1 FY2026 with defined ROI gates"
)

# ── SLIDE 6: Market Mapping ───────────────────────────────────────────────────
skill_slide(6, 2, "Market & Competitive Intel", "Market Mapping",
    "The $350B Consulting Market Is Bifurcating — GenAI Advisory Is the Only High-Growth Segment",
    "The global management consulting market hit $350B+ in 2025. Traditional implementation and operations are growing 3–5%; GenAI advisory is the outlier at 60%+ growth. Accenture has a 14.1% share overall and is best-positioned in the highest-growth segment.",
    [
        "Total market: $350B+ (2025), GenAI advisory fastest-growing at $15B → $150B by 2030",
        "Accenture's strongest position: tech transformation ($120B segment, #1 by revenue)",
        "White space: mid-market AI transformation — MBB too expensive, boutiques too narrow",
        "Threat zone: pure strategy advisory ($40B) — MBB holds structural premium, Accenture under-indexed"
    ],
    ["Segment", "Size (2025)", "Growth", "Accenture Position", "Attractiveness"],
    [
        ["GenAI advisory", "$15B", "60%+", "First mover, $2.7B", "Very High"],
        ["Tech transformation", "$120B", "10–12%", "#1 by revenue", "High"],
        ["Strategy (pure)", "$40B", "5%", "Weak vs MBB", "Medium"],
        ["Managed services/ops", "$80B", "3–4%", "Strong, margin risk", "Medium"],
        ["Industry X (engineering)", "$30B", "8%", "Differentiated", "High"],
    ],
    tbl_col_widths=[Inches(1.8), Inches(1.1), Inches(0.85), Inches(1.7), Inches(1.5)],
)

# ── SLIDE 7: Competitive Intel ────────────────────────────────────────────────
skill_slide(7, 2, "Market & Competitive Intel", "Competitive Intel",
    "McKinsey and BCG Are Building Tech Delivery Arms — Accenture's Moat Is Narrowing",
    "The competitive dynamic is converging: MBB is building implementation capability (BCG X, McKinsey digital), while OpenAI's Feb 2026 Frontier Alliance embeds AI vendors directly inside client teams. Accenture must widen the IP and outcomes gap before these moves mature.",
    [
        "BCG X (tech build arm) + QuantumBlack signal MBB closing the strategy-to-delivery gap",
        "OpenAI Frontier Alliance (Feb 2026) could disintermediate advisory at the AI strategy level",
        "IBM and Capgemini undercutting on AI delivery with proprietary toolkits at lower cost",
        "Accenture advantage: mcp-bench (NeurIPS 2025) — Accenture Labs OWNS the agentic AI evaluation standard; no competitor has published comparable research"
    ],
    ["Competitor", "Current Move", "Likely Next Move", "Accenture Counter"],
    [
        ["McKinsey", "QuantumBlack tech arm", "Acquire AI integrator", "AI Refinery platform depth"],
        ["BCG", "BCG X scaling", "Compete on GenAI delivery", "77K practitioners + SDK"],
        ["OpenAI", "Frontier Alliance Feb 2026", "Direct enterprise contracts", "Own integration layer"],
        ["IBM", "WatsonX toolkit pricing", "Undercut on AI delivery", "mcp-bench standards lead"],
        ["Capgemini", "AI automation toolkits", "Mid-market at 50% cost", "Outcome pricing + IP"],
    ],
    tbl_col_widths=[Inches(1.4), Inches(1.8), Inches(1.9), Inches(1.85)],
    bottom_note="mcp-bench leaderboard: gpt-5 #1 (0.749), claude-sonnet-4 #5 (0.681)  |  Accenture Labs owns the benchmark — github.com/Accenture/mcp-bench"
)

# ── SLIDE 8: Customer Segmentation ───────────────────────────────────────────
skill_slide(8, 2, "Market & Competitive Intel", "Customer Segmentation",
    "Fortune 100 Is Accenture's Core — Mid-Market and Growth Regions Are the Upside",
    "91 of the Fortune 100 are Accenture clients — the enterprise base is defended. The growth opportunity is in the Fortune 500 mid-tier (under-penetrated for GenAI), growth markets (APAC/LatAm at 17% revenue), and the government segment (stabilize before re-growing).",
    [
        "Fortune 100 (91 clients): defend and deepen with AI — largest bookings per client",
        "Fortune 500 mid-tier: highest GenAI curiosity, least AI deployment — biggest expansion runway",
        "US Federal (~$4B): stabilize FY2026, protect relationship through budget uncertainty",
        "APAC/LatAm (17% revenue): fastest-growing; underweight vs market share potential"
    ],
    ["Segment", "Revenue Scale", "AI Penetration", "FY2026 Priority", "Action"],
    [
        ["Fortune 100", "~$35B+", "High", "Defend & deepen", "Expand GenAI scope"],
        ["Fortune 500 mid-tier", "~$20B", "Low", "Grow aggressively", "GenAI starter packs"],
        ["US Federal gov't", "~$4B", "Medium", "Stabilize", "Continuity assurance"],
        ["APAC / LatAm", "~$12B", "Low", "Accelerate", "Local GenAI delivery"],
        ["Mid-market (<$1B rev)", "Emerging", "Very low", "Test & learn", "Productized AI"],
    ],
    tbl_col_widths=[Inches(1.7), Inches(1.3), Inches(1.2), Inches(1.4), Inches(1.35)],
)

# ── SLIDE 9: Profit Pool Analysis ────────────────────────────────────────────
skill_slide(9, 2, "Market & Competitive Intel", "Profit Pool Analysis",
    "GenAI Advisory Captures 2× the Margin of Traditional Implementation — Follow the Profit",
    "The profit pool is shifting. GenAI advisory and pure strategy consulting carry 20–25% margins while traditional IT implementation runs 13–16%. Accenture's $2.7B GenAI revenue is disproportionately profitable — and the platform model (GenWizard) promises even higher margins at scale.",
    [
        "GenAI advisory: ~$2.7B revenue at est. 22–25% margin — the most attractive pool",
        "Strategy & Consulting: ~$18B at 18–22% margin — high-value but MBB-contested",
        "Technology implementation: ~$30B but 13–16% margin — volume play, AI automation needed",
        "Operations/managed services: margin compression risk as AI automates routine work"
    ],
    ["Service Pool", "Est. Revenue", "Est. Margin", "Profit Pool", "Trend"],
    [
        ["GenAI advisory", "$2.7B", "22–25%", "~$650M", "Growing fast"],
        ["Strategy & Consulting", "~$18B", "18–22%", "~$3.5B", "Stable"],
        ["Technology impl.", "~$30B", "13–16%", "~$4.2B", "Margin pressure"],
        ["Operations/managed", "~$15B", "10–14%", "~$1.8B", "AI threat"],
        ["Industry X / Song", "~$4B", "15–18%", "~$680M", "Growing"],
    ],
    tbl_col_widths=[Inches(1.75), Inches(1.2), Inches(1.15), Inches(1.2), Inches(1.65)],
    bottom_note="Strategic implication: allocate growth investment to GenAI advisory; automate Operations to protect margin"
)

# ── SLIDE 10: Strategic Options ───────────────────────────────────────────────
skill_slide(10, 3, "Strategic Choice & Economics", "Strategic Options",
    "AI Refinery Platform Is the Moat — GitHub Evidence Confirms the IP Strategy Is Real",
    "GitHub data confirms Accenture's platform bet is tangible: AI Refinery SDK (v1.31.3, 29 releases, last pushed June 2026) is a production-grade multi-agent platform with its own Distiller Framework, LLM-agnostic inference, and Responsible AI module. This is not vaporware — it is shippable IP.",
    [
        "AI Refinery SDK (github.com/Accenture/airefinery-sdk): multi-agent platform, Apache 2.0, 29 releases in 14 months",
        "Distiller Framework: orchestrates specialist agents for complex enterprise workflows — directly competes with BCG X",
        "mcp-bench (NeurIPS 2025): Accenture Labs published the MCP tool-use benchmark used by the entire industry",
        "Option B (AI Refinery + delivery scale) is NOW defensible — not aspirational"
    ],
    ["Option", "Core Bet", "GitHub Evidence", "Verdict"],
    [
        ["A: AI-Native Advisor", "Beat MBB on AI strategy", "mcp-bench research lead", "Complement"],
        ["B: AI Refinery Platform", "Multi-agent IP + delivery scale", "SDK v1.31, 29 releases, active", "RECOMMENDED"],
        ["C: Pure Impl. Scale", "Cost leadership", "No platform evidence", "Reject"],
    ],
    tbl_col_widths=[Inches(1.8), Inches(2.2), Inches(2.0), Inches(0.95)],
    bottom_note="AI Refinery homepage: sdk.airefinery.accenture.com  |  Source: github.com/Accenture/airefinery-sdk"
)

# ── SLIDE 11: Business Case Builder ──────────────────────────────────────────
skill_slide(11, 3, "Strategic Choice & Economics", "Business Case Builder",
    "The $3B AI Bet Has a Sub-18-Month Payback — GitHub IP Adds Uncounted Strategic Value",
    "Beyond the financial ROI, GitHub evidence adds a second value stream: AI Refinery SDK (29 releases in 14 months, Apache 2.0) and mcp-bench (NeurIPS 2025, live leaderboard) represent defensible IP assets that no competitor can simply purchase. The platform case is stronger than financials alone show.",
    [
        "Financial ROI: $2.7B GenAI revenue in FY2025 against $3B 3-year investment — payback in <18 months",
        "IP value (GitHub): AI Refinery SDK v1.31.3 — production multi-agent platform, 29 releases, active development",
        "Research value: mcp-bench (NeurIPS 2025) — Accenture Labs sets the industry benchmark for agentic AI evaluation",
        "Hidden asset: 223 public repos, AmpliGraph (2,237 stars), Federated Learning Lab — deep bench of reusable IP"
    ],
    ["Value Stream", "Asset", "Evidence", "FY2027 Potential"],
    [
        ["GenAI Services", "Delivery + practitioners", "FY2025: $2.7B revenue", "$5B+ revenue"],
        ["Platform IP", "AI Refinery SDK", "v1.31.3, 29 releases, June 2026", "$100M+ licensing"],
        ["Research Leadership", "mcp-bench framework", "NeurIPS 2025, live leaderboard", "Talent + brand"],
        ["Knowledge Graph AI", "AmpliGraph (2.2K stars)", "Most-starred ML repo", "Client data products"],
        ["Federated Learning", "Labs-FL project", "Privacy-preserving AI research", "Regulated sectors"],
    ],
    tbl_col_widths=[Inches(1.6), Inches(1.65), Inches(2.1), Inches(1.6)],
    bottom_note="Source: github.com/Accenture  |  AI Refinery: sdk.airefinery.accenture.com  |  mcp-bench: arXiv:2508.20453"
)

# ── SLIDE 12: Portfolio Review ────────────────────────────────────────────────
skill_slide(12, 3, "Strategic Choice & Economics", "Portfolio Review",
    "Technology and GenAI Advisory Are Invest; Operations Needs AI Automation to Survive",
    "Accenture's five service units have diverging trajectories. Technology and GenAI advisory are the growth engines. Song is a sleeper with 12% growth. Operations faces the most disruptive AI threat to its margin base and must be redesigned, not grown headcount-first.",
    [
        "Technology (~$30B): Invest — AI delivery augmentation improves margin and speed",
        "Strategy & Consulting (~$18B): Invest selectively — GenAI advisory is the high-margin wedge",
        "Song (~$4B): Grow — AI-creative convergence makes this differentiated, not a cost center",
        "Operations (~$15B): Fix — AI automation is the only path to margin defense; reduce headcount dependency"
    ],
    ["Business Unit", "Est. Revenue", "Growth", "Margin", "Recommendation"],
    [
        ["Technology", "~$30B", "8%", "13–16%", "INVEST (AI-powered)"],
        ["Strategy & Consulting", "~$18B", "6%", "18–22%", "INVEST (GenAI advisory)"],
        ["Operations", "~$15B", "3%", "10–14%", "FIX (AI automate)"],
        ["Song", "~$4B", "12%", "15–18%", "GROW (AI-creative)"],
        ["Industry X", "~$4B", "8%", "15–18%", "GROW (industrial AI)"],
    ],
    tbl_col_widths=[Inches(1.75), Inches(1.2), Inches(0.8), Inches(1.0), Inches(2.2)],
)

# ── SLIDE 13: Pricing Strategy ────────────────────────────────────────────────
skill_slide(13, 3, "Strategic Choice & Economics", "Pricing Strategy",
    "T&M Pricing Is Accenture's Biggest Margin Risk — Outcome-Based Must Scale to 20%+ of Deals",
    "Time-and-materials pricing exposes Accenture to AI-driven day-rate compression as GenAI increases delivery speed. The strategic move is outcome-based pricing — where Accenture captures a share of the value created, not hours spent. Currently <10% of contracts; target must be 20%+ by FY2027.",
    [
        "T&M risk: as GenAI 2× delivery speed, clients will renegotiate day rates downward",
        "Outcome pricing opportunity: AI-enabled transformations generate 15–30% cost reduction for clients — Accenture can capture 15–25% of that value",
        "Packaging: 'Reinvention packs' (fixed-scope, outcome-defined) are the bridge from T&M to outcomes",
        "Segment logic: Fortune 100 CFOs prefer outcome deals; mid-market needs fixed-price simplicity"
    ],
    ["Pricing Model", "Current Mix", "FY2027 Target", "Margin Impact"],
    [
        ["Time & Materials", "~75%", "55%", "Declining (AI compress)"],
        ["Fixed-scope packs", "~15%", "25%", "Stable, predictable"],
        ["Outcome-based", "<10%", "20%", "High (value share)"],
        ["Platform licensing", "<1%", "5%+", "Very high (60%+ margin)"],
    ],
    tbl_col_widths=[Inches(1.8), Inches(1.4), Inches(1.6), Inches(2.15)],
    bottom_note="Pilot design: 3 outcome-based GenAI deals in FS and healthcare by Q2 FY2026 with ROI-share terms"
)

# ── SLIDE 14: Operating Model Design ──────────────────────────────────────────
skill_slide(14, 4, "Operating Model & Execution", "Operating Model Design",
    "AI Refinery's Distiller Framework IS the Target Operating Architecture",
    "GitHub confirms the target operating model is already in code: AI Refinery SDK's Distiller Framework orchestrates specialist AI agents across enterprise workflows with LLM-agnostic inference, a Responsible AI module, and Knowledge Extraction API. The platform replaces manual delivery orchestration at scale.",
    [
        "Distiller Framework: multi-agent orchestrator — agents handle different tasks in parallel, with context passing",
        "LLM-agnostic inference API: connect any model (GPT-5, Claude, Gemini) — no vendor lock-in at the agent layer",
        "Responsible AI module: built-in policy/safety rules applied to every query — required for Fortune 100 governance",
        "ADM (Application Delivery Method): 12-phase lifecycle, 11 specialist agent roles — formal delivery framework"
    ],
    ["Model Element", "Current State", "AI Refinery Target", "GitHub Evidence"],
    [
        ["Team structure", "Practice silos", "AI agent pods (Distiller)", "airefinery-sdk v1.31"],
        ["Delivery tools", "Manual + legacy tools", "LLM-agnostic inference API", "29 SDK releases"],
        ["Governance", "Billability KPIs", "RAI module + outcome metrics", "RAI module built-in"],
        ["Knowledge work", "Human analysts", "Knowledge Extraction API", "Docs/tables/figures"],
        ["Billing model", "T&M dominant", "Outcome + platform licensing", "Apache 2.0 = commercializable"],
    ],
    tbl_col_widths=[Inches(1.65), Inches(1.65), Inches(1.9), Inches(1.75)],
    bottom_note="AI Refinery Distiller Framework: github.com/Accenture/airefinery-sdk  |  Homepage: sdk.airefinery.accenture.com"
)

# ── SLIDE 15: Transformation Roadmap ──────────────────────────────────────────
skill_slide(15, 4, "Operating Model & Execution", "Transformation Roadmap",
    "GitHub Commit History Proves Phase 3 Is Live — AI Refinery SDK Last Pushed June 9, 2026",
    "GitHub is a real-time signal of where Accenture's transformation actually is. AI Refinery SDK pushed June 9, 2026 (6 days ago) with version 1.31.3 — Phase 3 is not a plan, it is in production. mcp-bench accepted to NeurIPS 2025 confirms the agentic AI research pipeline feeding Phase 4.",
    [
        "Phase 3 evidence: airefinery-sdk v1.31.3 pushed June 9, 2026 — active production development",
        "Phase 3 evidence: 29 SDK releases in 14 months (April 2025 to June 2026) = monthly release cadence",
        "Phase 4 signal: mcp-bench (NeurIPS 2025) evaluates tool-using LLM agents — agentic AI research pipeline is running",
        "Phase 4 signal: mcp-bench leaderboard is live on HuggingFace — Accenture owns the evaluation standard"
    ],
    ["Phase", "Timing", "GitHub Evidence", "Status"],
    [
        ["1 — INVEST", "FY2023–24", "AmpliGraph, early AI repos published", "COMPLETE"],
        ["2 — SCALE", "FY2025", "77K practitioners, 23 acquisitions", "DELIVERED"],
        ["3 — PLATFORM", "FY2026", "AI Refinery v1.31.3, June 9 2026", "LIVE"],
        ["4 — AGENTIC", "FY2026–27", "mcp-bench NeurIPS 2025, HF leaderboard", "IN RESEARCH"],
    ],
    tbl_col_widths=[Inches(1.5), Inches(1.1), Inches(2.85), Inches(1.5)],
    bottom_note="AI Refinery last commit: June 9, 2026  |  mcp-bench arXiv:2508.20453, NeurIPS 2025 Workshop"
)

# ── SLIDE 16: Initiative Prioritizer ──────────────────────────────────────────
skill_slide(16, 4, "Operating Model & Execution", "Initiative Prioritizer",
    "Agentic AI and GenWizard Commercialization Are the Vital Few — Federal Recovery Is a Watch Item",
    "Accenture's leadership has identified 47,000+ GenAI client projects. Prioritizing internal investments requires ruthless focus: agentic AI service lines and GenWizard IP commercialization offer the highest impact-to-feasibility ratio. US federal recovery is real but timeline-uncertain.",
    [
        "P1: Agentic AI service line (HIGH impact / HIGH feasibility) — build on $5.9B bookings momentum",
        "P2: GenWizard platform commercialization (HIGH / MEDIUM) — converts internal tool to IP revenue",
        "P3: Outcome-based pricing scale (HIGH / MEDIUM) — requires contract governance redesign",
        "Kill: Traditional headcount-led outsourcing growth — commoditized, margin-dilutive"
    ],
    ["Initiative", "Impact", "Feasibility", "Priority", "FY2026 Decision"],
    [
        ["Agentic AI service line", "Very High", "High", "P1 — Fund fully", "Launch Q1"],
        ["GenWizard commercialize", "High", "Medium", "P2 — Accelerate", "Pilot by Q2"],
        ["Outcome pricing scale", "High", "Medium", "P3 — Redesign", "Governance by Q1"],
        ["US federal recovery", "Medium", "Low", "Watch", "Track quarterly"],
        ["Trad. outsourcing growth", "Low", "High", "KILL", "Redirect resources"],
    ],
    tbl_col_widths=[Inches(1.9), Inches(0.95), Inches(1.0), Inches(1.5), Inches(1.6)],
)

# ── SLIDE 17: KPI Architect ───────────────────────────────────────────────────
skill_slide(17, 5, "Risk, Performance & Value", "KPI Architect",
    "Accenture Needs a New KPI System Built Around AI Outcomes, Not Just Revenue and Billability",
    "FY2025 results were strong by traditional metrics. FY2026 requires a KPI system that leads with AI-transformation effectiveness: GenAI revenue and bookings velocity, outcome-based deal penetration, practitioner AI utilization, and client ROI — not just T&M billing rates.",
    [
        "Current system is backward-looking: revenue, EPS, billability — misses AI transformation quality",
        "New leading indicators: GenAI booking velocity, AI practitioner utilization, outcome deal conversion rate",
        "Remove: raw headcount as a growth proxy — it signals scale, not value creation in the AI era",
        "Review cadence: monthly GenAI pipeline review; quarterly outcome deal governance"
    ],
    ["KPI", "Type", "FY2025 Baseline", "FY2026 Target", "Owner"],
    [
        ["GenAI revenue", "Outcome (lagging)", "$2.7B", "$5B+", "CEO/CFO"],
        ["GenAI bookings", "Leading", "$5.9B", "$8B+", "Sales"],
        ["AI practitioner utilization", "Driver", "~77K active", "80K + 70% AI use", "CHRO"],
        ["Outcome-based deal %", "Driver", "<10%", "20%", "Practice leads"],
        ["Client AI ROI verified", "Outcome", "Not tracked", "Track in 50 deals", "Delivery"],
    ],
    tbl_col_widths=[Inches(1.9), Inches(1.3), Inches(1.3), Inches(1.2), Inches(1.25)],
    bottom_note="Vanity metric to sunset: gross headcount growth — replace with AI-augmented revenue per consultant"
)

# ── SLIDE 18: Risk & Mitigation ───────────────────────────────────────────────
skill_slide(18, 5, "Risk, Performance & Value", "Risk & Mitigation",
    "OpenAI Disintermediation and GenAI Commoditization Are the Two Existential Risks",
    "Accenture's risk register has two category-level threats: OpenAI's Feb 2026 Frontier Alliance embedding AI vendors inside client teams (disintermediation), and the possibility that GenAI advisory becomes a commodity before Accenture builds its IP moat. US federal is manageable; talent cost is chronic.",
    [
        "CRITICAL: OpenAI Frontier Alliance — AI vendors embedded in clients may bypass advisory layer",
        "HIGH: GenAI commoditization — boutiques at 50% day rates erode pricing floor faster than expected",
        "MEDIUM: US federal budget freeze — 1–1.5% FY2026 drag; diversifiable but not eliminable near-term",
        "CHRONIC: Talent cost inflation — 779K employees, 77K AI specialists facing comp pressure"
    ],
    ["Risk", "Likelihood", "Impact", "Mitigation", "Owner"],
    [
        ["OpenAI disintermediation", "Medium-High", "Critical", "Deepen OpenAI alliance; IP lock-in", "CEO"],
        ["GenAI commodity pricing", "High", "High", "Outcome pricing + GenWizard IP", "Strategy"],
        ["US federal freeze", "High", "Medium", "Diversify to commercial accounts", "Federal lead"],
        ["MBB tech capability", "High", "High", "Accelerate delivery platform IP", "CTO"],
        ["Talent cost inflation", "High", "Medium", "AI augmentation ratio; offshore", "CHRO"],
    ],
    tbl_col_widths=[Inches(1.85), Inches(1.15), Inches(0.9), Inches(1.85), Inches(1.2)],
)

# ── SLIDE 19: Value Realization ────────────────────────────────────────────────
skill_slide(19, 5, "Risk, Performance & Value", "Value Realization",
    "Accenture's $3B AI Investment Has Generated $2.7B in Year-2 Revenue — Value Is Materializing",
    "The FY2025 annual report confirms the $3B GenAI investment is delivering. GenAI revenue tripled. Bookings nearly doubled. The value realization challenge shifts from 'did it work?' to 'can we sustain and scale it?' — requiring a formal value ledger tied to GenWizard commercialization and agentic AI.",
    [
        "Year-2 GenAI revenue: $2.7B (tripled from FY2024 ~$0.9B) — payback materializing ahead of plan",
        "Forward value pipeline: $5.9B GenAI bookings signal $5B+ FY2026 revenue achievable",
        "Value at risk: ~$10B in future GenAI revenue if OpenAI disintermediation accelerates",
        "Next value capture: GenWizard platform licensing — shift to recurring IP revenue"
    ],
    ["Benefit", "FY2024 Baseline", "FY2025 Actual", "FY2026 Target", "Proof Standard"],
    [
        ["GenAI Revenue", "~$0.9B", "$2.7B", "$5B+", "Q4 earnings"],
        ["GenAI Bookings", "~$3B", "$5.9B", "$8B+", "Quarterly filing"],
        ["AI Practitioners", "~40K", "77K", "80K", "HR headcount"],
        ["Outcome-based deals", "<5%", "<10%", "20%", "Contract audit"],
        ["GenWizard licensing", "$0", "Pilot", "$100M+", "Revenue line"],
    ],
    tbl_col_widths=[Inches(1.7), Inches(1.3), Inches(1.2), Inches(1.15), Inches(1.6)],
)

# ── SLIDE 20: War Gaming ──────────────────────────────────────────────────────
skill_slide(20, 5, "Risk, Performance & Value", "War Gaming",
    "Two Scenarios Could Break Accenture's Strategy — Both Require Pre-Committed Responses Now",
    "War-gaming Accenture's 'Reinvention partner' strategy surfaces two high-severity scenarios: (1) OpenAI direct-to-enterprise at scale collapses advisory margin, (2) a GenAI ROI recession freezes client budgets. Both require pre-committed response plays that activate on specific early signals.",
    [
        "Scenario 1 (CRITICAL): OpenAI enterprise direct — margin collapses on advisory; response: accelerate IP moat",
        "Scenario 2 (HIGH): GenAI ROI recession — clients pause transformation spend; response: shift to cost-reduction use cases",
        "Scenario 3 (MEDIUM): MBB delivery capability — BCG X / McKinsey close implementation gap; response: pricing power and scale",
        "Early warning: monitor BCG X headcount, OpenAI enterprise contract announcements, GenAI deal cancellation rate"
    ],
    ["Scenario", "Trigger", "Severity", "Response Play"],
    [
        ["OpenAI direct enterprise", "3+ Fortune 100 bypass advisory", "Critical", "Own the integration layer; IP moat"],
        ["GenAI ROI recession", "Client ROI misses in 2 quarters", "High", "Pivot to cost-reduction cases"],
        ["MBB delivery close", "BCG X >5K staff", "High", "Price on outcomes, not hours"],
        ["AI regulation tightening", "EU AI Act enforcement surge", "Medium", "Compliance-as-service offering"],
        ["Boutique price war", "50% T&M undercutting at scale", "Medium", "Productize + platform pricing"],
    ],
    tbl_col_widths=[Inches(1.85), Inches(1.85), Inches(0.95), Inches(2.3)],
)

# ── SLIDE 21: Decision Memo ────────────────────────────────────────────────────
skill_slide(21, 6, "Alignment & Exec Communication", "Decision Memo",
    "Recommendation: Accelerate Platform Commercialization Before the First-Mover Window Closes",
    "The Board must approve GenWizard external licensing and the agentic AI service line in Q1 FY2026. The GenAI first-mover window is 18–24 months — after which MBB tech arms and OpenAI partnerships will commoditize the advisory layer. This is the defining FY2026 strategic bet.",
    [
        "Decision required: Approve GenWizard licensing pilot + agentic AI service line — Q1 FY2026",
        "Evidence: $2.7B GenAI revenue (+200%), $5.9B bookings, 77K practitioners — platform is ready",
        "Alternatives considered: (A) continue services-only model — rejected, margin compression inevitable; (B) wait for clearer demand — rejected, window closing",
        "Risk of inaction: OpenAI and BCG X move faster; Accenture loses the IP differentiation that justifies premiums"
    ],
    ["Decision Element", "Detail"],
    [
        ["Recommendation", "Approve GenWizard licensing + agentic AI service line"],
        ["Decision required", "Board: Q1 FY2026 budget allocation and governance"],
        ["Investment ask", "$500M incremental (GenWizard platform + agentic line)"],
        ["Expected return", "$1B+ incremental revenue by FY2027; 25%+ margin"],
        ["Option rejected", "Services-only: inevitable margin compression"],
        ["Key risk", "OpenAI disintermediation if delayed >12 months"],
    ],
    tbl_col_widths=[Inches(2.0), Inches(4.95)],
)

# ── SLIDE 22: Narrative Builder ───────────────────────────────────────────────
skill_slide(22, 6, "Alignment & Exec Communication", "Narrative Builder",
    "The Accenture Investor Narrative: 'We Bet on AI First — Now We're Building the Moat'",
    "Accenture's investor story must move from 'we invested in GenAI and it worked' to 'here's why no one can replicate it.' The SCQA narrative arc makes the case for platform commercialization as the structural defense — and explains why FY2026 deceleration is deliberate, not a warning sign.",
    [
        "SITUATION: $69.7B revenue, 7% growth, GenAI tripled — FY2025 was the proof year",
        "COMPLICATION: FY2026 guidance 2–5% signals deceleration; MBB building delivery capability; OpenAI threatening advisory layer",
        "QUESTION: Can Accenture sustain a premium position as GenAI advisory commoditizes?",
        "ANSWER + ACTION: Yes — but only by shifting to IP platform model before the 18-month window closes"
    ],
    ["Story Beat", "Headline", "Audience Response"],
    [
        ["Situation", "We delivered: $69.7B, AI tripled", "'Impressive — prove it sustains'"],
        ["Complication", "FY2026 headwinds are real but manageable", "'OK, what's the plan?'"],
        ["Insight", "The moat isn't scale — it's GenWizard + 77K", "'That's defensible if true'"],
        ["Answer", "Platform commercialization is the next chapter", "'Show me the economics'"],
        ["Action", "Approve GenWizard + agentic AI by Q1", "'What's the investment?'"],
    ],
    tbl_col_widths=[Inches(1.3), Inches(2.5), Inches(3.15)],
    bottom_note="Hostile Q: 'OpenAI will do this cheaper.' Answer: 'We deliver the outcome guarantee, not just the model.'"
)

# ── SLIDE 23: Stakeholder Alignment ───────────────────────────────────────────
skill_slide(23, 6, "Alignment & Exec Communication", "Stakeholder Alignment",
    "Four Stakeholder Groups Must Believe Different Things for the Platform Strategy to Win",
    "Accenture's platform pivot requires alignment across Board, enterprise clients, the internal workforce, and investors — each with distinct concerns. Pre-wiring must happen before the Q1 FY2026 board presentation, with sequenced engagement starting with the CFO and two anchor clients.",
    [
        "Board: needs ROI evidence on $3B bet (provided) + credible path for GenWizard licensing",
        "Enterprise clients (Fortune 100): need outcome guarantees not technology promises",
        "779K employees: need clear upskilling path and job security narrative in AI-augmented model",
        "Investors: need FY2026 deceleration explained as 'managed pause' not structural decline"
    ],
    ["Stakeholder", "Current Stance", "What They Need", "Pre-Wire Action"],
    [
        ["Board", "Supportive", "GenWizard ROI proof", "CFO briefing + pilot data"],
        ["Fortune 100 clients", "Interested, cautious", "Outcome guarantees", "3 reference deals"],
        ["Employees (779K)", "Anxious", "Clear upskilling path", "All-hands + AI training"],
        ["Investors", "Watchful", "FY2026 growth recovery story", "IR roadshow narrative"],
        ["US federal clients", "Uncertain", "Continuity commitment", "1:1 agency briefings"],
    ],
    tbl_col_widths=[Inches(1.55), Inches(1.35), Inches(1.7), Inches(2.35)],
)

# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 24 — STRATEGIC RECOMMENDATIONS SUMMARY (replaces generic OS slide)
# ─────────────────────────────────────────────────────────────────────────────
s24 = d.slide(fill=b.NAVY)
d.rect(s24, 0, 0, Inches(0.18), d.H, b.TEAL)
d.rect(s24, 0, 0, d.W, Inches(0.12), b.TEAL)

d.text(s24, "ACCENTURE  ·  STRATEGIC RECOMMENDATIONS", Inches(0.65), Inches(0.26),
       Inches(11), Inches(0.3), size=10, color=b.TEAL, bold=True)
d.text(s24, "Six Moves That Define the FY2026–27 Strategy",
       Inches(0.65), Inches(0.64), Inches(11), Inches(0.6),
       size=30, color=b.WHITE, bold=True, font=b.FONT_H, shrink=True)
d.text(s24, "Applied via 21 Accenture-Style Claude consulting frameworks on live FY2025 data",
       Inches(0.65), Inches(1.28), Inches(11), Inches(0.3), size=12, color=b.LIGHT_TEAL)
d.rect(s24, Inches(0.65), Inches(1.65), Inches(2.5), Inches(0.05), b.TEAL)

RECS = [
    ("01", "Commercialize\nGenWizard IP",
     "Launch external licensing by Q1 FY2026 before MBB replicates the platform", "Platform"),
    ("02", "Launch Agentic AI\nService Line",
     "Build on $5.9B bookings momentum; first offering by Q1, 3 POCs in FS and health", "Growth"),
    ("03", "Scale Outcome-Based\nPricing to 20%",
     "Move from T&M to value-share contracts before AI compresses day rates structurally", "Margin"),
    ("04", "Automate Operations\nto Protect Margin",
     "AI-augmented delivery in Operations reduces headcount intensity; defend 10-14% margin", "Defend"),
    ("05", "Pre-Wire the\nOpenAI Alliance",
     "Deepen alliance to ensure Accenture remains preferred SI as OpenAI scales enterprise", "Risk"),
    ("06", "Tell a Platform Story\nto Investors",
     "Reframe FY2026 deceleration as 'managed platform pivot'; Q1 IR roadshow narrative", "Comms"),
]

card_w, card_gap = Inches(1.95), Inches(0.17)
sx = Inches(0.58)
for i, (num, title, desc, tag) in enumerate(RECS):
    cx = sx + i * (card_w + card_gap)
    d.rect(s24, cx, Inches(2.0), card_w, Inches(4.1), b.NAVY_2, radius=0.06)
    d.rect(s24, cx, Inches(2.0), card_w, Inches(0.08), b.TEAL, radius=0.04)
    d.text(s24, num, cx + Inches(0.12), Inches(2.15), card_w - Inches(0.2), Inches(0.28),
           size=10.5, color=b.TEAL, bold=True)
    d.text(s24, title, cx + Inches(0.12), Inches(2.46), card_w - Inches(0.2), Inches(0.7),
           size=13.5, color=b.WHITE, bold=True, font=b.FONT_H, shrink=True, ls=1.1)
    d.text(s24, desc, cx + Inches(0.12), Inches(3.22), card_w - Inches(0.2), Inches(1.55),
           size=10.5, color=b.LIGHT_TEAL, ls=1.3, shrink=True)
    # tag chip
    d.rect(s24, cx + Inches(0.12), Inches(5.38), card_w - Inches(0.24), Inches(0.25),
           b.ACCENT, radius=0.08)
    d.text(s24, tag, cx + Inches(0.12), Inches(5.4), card_w - Inches(0.24), Inches(0.22),
           size=9, color=b.WHITE, bold=True, align=PP_ALIGN.CENTER)

d.rect(s24, Inches(0.58), Inches(6.38), d.W - Inches(1.16), Inches(0.62), b.TEAL, radius=0.06)
d.text(s24, "Data sources: Accenture FY2025 Annual Report & 10-K (Sept 2025)  ·  VMR Consulting Market Report 2026  ·  Avasant Market Update 2026  ·  Applied via 21 Accenture-Style Claude Skills",
       Inches(0.75), Inches(6.5), d.W - Inches(1.5), Inches(0.36),
       size=9.5, color=b.NAVY, bold=False, align=PP_ALIGN.CENTER, shrink=True)
d.footer(s24, 24, TOTAL, dark=True)


# ─────────────────────────────────────────────────────────────────────────────
d.save(OUT_FILE)
print(f"\nDeck: {OUT_FILE}")
