#!/usr/bin/env python3
"""
build_market_deck.py — branded 12-slide analysis deck from live market research.

Usage:
    python3 build_market_deck.py accenture
    python3 build_market_deck.py ibm
    python3 build_market_deck.py accenture --out my-deck.pptx
"""
import argparse, json, sys
from pathlib import Path

ROOT = Path(__file__).parent
PPTXKIT = Path.home() / ".claude/skills/branded-pptx-deck/scripts"
sys.path.insert(0, str(PPTXKIT))

from pptxkit import Brand, Deck, PP_ALIGN, MSO_ANCHOR, Inches, Pt, RGBColor


def hx(s):
    s = s.lstrip("#")
    return RGBColor(int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16))


def trunc(s, n):
    s = (s or "").strip()
    return s[:n] + "…" if len(s) > n else s


# ── Market research data (from Exa, IBM/Accenture investor docs, Everest Group) ──

ACN = {
    "name": "Accenture",
    "ticker": "ACN",
    "headline": "The $70B Reinvention Machine",
    "tagline": "AI-first transformation partner · FY2025 results",
    "fy": "FY2025",
    "fy_period": "12 months ended Aug 31, 2025",

    # Financials
    "revenue": 69.7,
    "revenue_yoy": "+7%",
    "bookings": 80.6,
    "bookings_yoy": "-1%",
    "book_to_bill": "1.2x",
    "consulting_rev": 35.1,
    "managed_services_rev": 34.6,
    "consulting_growth": "+6%",
    "managed_services_growth": "+9%",
    "op_margin": "15.6%",
    "eps": "$11.44",
    "eps_growth": "+8%",
    "fcf": "$10.9B",
    "employees": "779,000",

    # AI metrics (the real story)
    "genai_bookings": 5.9,
    "genai_bookings_yoy": "nearly doubled",
    "genai_revenue": 2.7,
    "genai_revenue_yoy": "tripled",
    "ai_staff": "77,000",
    "ai_staff_prior": "40,000",
    "genai_trained": "550,000+",
    "ai_projects": "6,000+",
    "ai_investment": "$3B",
    "large_deals_100m": "129 quarterly clients >$100M (record)",
    "multi_service_deals": "80%",

    # Revenue by industry
    "by_industry": [
        ("Products",             21.2, 30, "+8%"),
        ("Health & Public Svc",  14.8, 21, "+6%"),
        ("Financial Services",   12.8, 18, "+10%"),
        ("Comms, Media & Tech",  11.5, 16, "+6%"),
        ("Resources",             9.5, 14, "+5%"),
    ],

    # Revenue by geo
    "by_geo": [
        ("Americas", 35.1, 50, "+9%"),
        ("EMEA",     24.6, 35, "+6%"),
        ("Asia Pacific", 10.0, 14, "+4%"),
    ],

    # Revenue history (from EDGAR, for trend chart)
    "rev_history": [
        ("2021", 50.5), ("2022", 61.6), ("2023", 64.1),
        ("2024", 64.9), ("2025", 69.7),
    ],

    # Competitive position
    "genai_market_share": "7%",
    "market_share_source": "IoT Analytics, Jan 2025",
    "analyst_tier": "Leader",
    "analyst_source": "Everest Group PEAK Matrix: AI & GenAI Services 2025",

    # Strategy
    "strategic_moves": [
        ("Reinvention Services Launch", "Sep 1 2025: Collapsed 5 BUs (Strategy, Technology, Operations, Song, Industry X) into one integrated 'Reinvention Services' unit — simpler sell, faster cross-service deals."),
        ("$3B GenAI First-Mover Bet", "Committed $3B to GenAI in FY2023. Result: $2.7B GenAI revenue in FY2025 (tripled YoY), $5.9B bookings. Fastest ramp of any new technology category in Accenture history."),
        ("Talent at Scale", "Grew AI & data staff from 40K to 77K in 2 years. 550,000+ employees trained in GenAI fundamentals. $1B invested in client upskilling platform + Udacity acquisition."),
        ("Ecosystem #1 Position", "No. 1 partner for all top 10 ecosystem partners (AWS, Azure, Google, SAP, Salesforce, etc.). 60% of FY25 revenue from ecosystem work, growing 9% — outpacing total revenue growth."),
    ],

    # Key risks
    "risks": [
        ("Premium Pricing Pressure", "Client feedback: Accenture priced at premium vs peers. Cost-conscious mid-market enterprises may route to Deloitte, Capgemini, or offshore players."),
        ("US Federal Headwind", "FY2026 guidance excludes 1–1.5% drag from US federal business contraction. Government consulting spend uncertainty is a notable near-term risk."),
        ("Execution at Scale", "6,000+ AI projects = massive delivery risk. Referenced clients flag project management gaps and timeline misalignment in some engagements."),
        ("Consulting vs Services Mix Shift", "Managed Services growing faster (+9%) than Consulting (+6%). Higher managed services mix may compress margins over time."),
    ],

    # Competitive comparison
    "competitors": [
        ("Accenture ◀", "$69.7B", "7%",   "Reinvention Services + AI Refinery",   "Leader"),
        ("IBM",          "$62.8B", "2%",   "watsonx + Hybrid Cloud",               "Leader"),
        ("Deloitte",     "~$65B",  "3%",   "Deloitte AI",                           "Leader"),
        ("PwC",          "~$55B",  "<1%",  "PwC AI",                                "Major Contender"),
        ("Capgemini",    "~$23B",  "<1%",  "AI Lab + partnerships",                 "Leader"),
        ("McKinsey",     "~$16B",  "<1%",  "QuantumBlack",                          "Major Contender"),
    ],
}

IBM_DATA = {
    "name": "IBM",
    "ticker": "IBM",
    "headline": "The $12.5B AI Book of Business",
    "tagline": "Hybrid cloud + enterprise AI platform · FY2024/2025 results",
    "fy": "FY2024",
    "fy_period": "12 months ended Dec 31, 2024",

    # Financials (FY2024 = calendar year 2024)
    "revenue": 62.8,
    "revenue_yoy": "+1% (+3% CC)",
    "bookings": None,
    "fcf": "$12.7B",
    "fcf_yoy": "+$1.5B",
    "op_gross_margin_expansion": "+130bps",
    "software_pct": "~45%",
    "integrated_clients": "~80%",  # buy across all 3 segments
    "employees": "~280,000",

    # Segments (FY2024)
    "segments": [
        ("Software",        27.1, 43, "+8.3% (+9% CC)",   "32.1%"),
        ("Consulting",      20.7, 33, "-0.9% (+0.6% CC)", "9.9%"),
        ("Infrastructure",  14.0, 22, "-3.9% (-2.7% CC)", "17.5%"),
        ("Financing/Other",  1.0,  2, "—",                "—"),
    ],

    # Software sub-segments
    "software_breakdown": [
        ("Hybrid Platform & Solutions", "+8.1% CC", "Red Hat +12%, Automation +15%, Data & AI +2%"),
        ("Transaction Processing",      "+9.6% CC", "IBM Z mainframe — most successful program in history"),
    ],

    # AI metrics
    "genai_book_q4_2024": 5.0,
    "genai_book_q3_2025": 9.5,
    "genai_book_q4_2025": 12.5,
    "genai_consulting_run_rate": "$3.6B annualized (Q4 2025)",
    "genai_pct_backlog": "25%",
    "consulting_genai_pct": "~15% of consulting revenue",
    "consulting_advantage_deals": "500+",
    "consultants_genai_certified": "~75,000 (~50%)",
    "redhat_openshift_arr": "$1.4B",
    "automation_q3_2025": "+22% (with HashiCorp)",

    # HashiCorp
    "hashicorp_deal": "$6.4B",
    "hashicorp_closed": "February 27, 2025",
    "hashicorp_impact": "Terraform + Vault → IBM Automation portfolio. Ansible + Terraform = end-to-end IaC. Deployment time: 45 min → 3 min.",

    # Revenue history (EDGAR)
    "rev_history": [
        ("2020", 73.6), ("2021", 57.4), ("2022", 60.5),
        ("2023", 61.9), ("2024", 62.8),
    ],

    # Strategy
    "strategic_moves": [
        ("Software-Led Portfolio Transformation", "Software is now 45% of IBM revenue (vs ~35% in 2020). Gross margin expanded 130bps to 58% in FY2024. The shift from services-heavy to software-led is the core Arvind Krishna thesis — now executing."),
        ("HashiCorp: Infrastructure IaC at Scale", "$6.4B acquisition closed Feb 2025. Terraform (+Ansible) = end-to-end infrastructure-as-code. Vault + OpenShift = secrets management for hybrid cloud. Automation segment hit +22% in Q3 2025 partly driven by HashiCorp."),
        ("watsonx: AI for Regulated Enterprise", "watsonx GenAI book grew $5B → $12.5B in 18 months. Granite models 90% more cost-efficient than frontier alternatives. Key differentiator: on-premise deployment for banking, healthcare, government — sectors where cloud-only AI (OpenAI, Google) cannot serve."),
        ("Client Zero Credibility", "IBM 'ate its own cooking': decomposed 490 internal workflows, instrumented ~70 with digital workers, claims $3.5B internal productivity gains. Revenue inflection: –3% to +5% CAGR. Used as proof point in 500+ IBM Consulting Advantage deals."),
    ],

    # Key risks
    "risks": [
        ("Consulting Growth Lag", "Consulting -0.9% FY2024 vs Accenture +6%. IBM Consulting (~38% of revenue) trails Accenture, Deloitte, McKinsey on GenAI services market share (2% vs 7%). Needs reacceleration or Software must carry more weight."),
        ("Microsoft Copilot + Azure OpenAI Scale", "Microsoft has demonstrably larger enterprise AI distribution. IBM's $12.5B GenAI book vs OpenAI ~$20B 2025 revenue. Microsoft's enterprise reach via M365 seat base gives structural advantage."),
        ("Granite vs Frontier Model Gap", "IBM Granite models are cost-efficient but capability-trailing vs GPT-5, Claude 4.x, Gemini 3.0. If enterprises shift production workloads to frontier models, IBM's 'AI for business' niche narrows."),
        ("HashiCorp Product Overlap", "Terraform vs Ansible, OpenShift vs Waypoint: significant product overlap unresolved. Partner ecosystem confused about when to use IBM Z + Terraform vs Ansible. Long-term roadmap still unclear as of June 2025."),
    ],

    # Competitive comparison
    "competitors": [
        ("IBM ◀",       "$62.8B", "2%",   "watsonx + Red Hat + HashiCorp",         "Leader"),
        ("Accenture",   "$69.7B", "7%",   "Reinvention Services + AI Refinery",    "Leader"),
        ("Microsoft",   "$245B",  "N/A",  "Azure OpenAI / M365 Copilot",           "Platform"),
        ("Deloitte",    "~$65B",  "3%",   "Deloitte AI",                           "Leader"),
        ("Capgemini",   "~$23B",  "<1%",  "AI Lab",                                "Leader"),
        ("Red Hat",     "Internal","—",   "OpenShift / RHEL AI / Ansible",         "Acquired"),
    ],

    # Competitive position
    "genai_market_share": "2%",
    "market_share_source": "IoT Analytics, Jan 2025",
    "analyst_tier": "Leader",
    "analyst_source": "Everest Group PEAK Matrix: AI & GenAI Services 2025",
}


# ── Slide builders ────────────────────────────────────────────────────────────

def kpi_chip(d, s, cx, cy, cw, ch, val, label, sub="", val_color=None):
    b = d.b
    val_color = val_color or b.TEAL
    d.rect(s, cx, cy, cw, ch, b.WHITE, radius=0.07)
    d.rect(s, cx, cy, Inches(0.1), ch, b.TEAL, radius=0.0)
    d.text(s, val,   cx + Inches(0.2), cy + Inches(0.1),  cw - Inches(0.3), Inches(0.65),
           size=30, color=val_color, bold=True, shrink=True)
    d.text(s, label, cx + Inches(0.2), cy + Inches(0.78), cw - Inches(0.3), Inches(0.32),
           size=11, color=b.TEAL, bold=True)
    if sub:
        d.text(s, sub, cx + Inches(0.2), cy + Inches(1.1),  cw - Inches(0.3), Inches(0.28),
               size=9, color=b.MUTED)


def slide_cover(d, data):
    s = d.slide(fill=d.b.NAVY)
    b = d.b
    W, H = d.W, d.H

    d.rect(s, 0, 0, Inches(0.4), H, b.TEAL)
    d.rect(s, 0, H - Inches(0.55), W, Inches(0.55), b.NAVY_2)

    d.text(s, data["name"].upper(), Inches(0.65), Inches(0.75), Inches(10), Inches(1.2),
           size=60, color=b.WHITE, bold=True)
    d.text(s, data["headline"],  Inches(0.65), Inches(2.0), Inches(10.5), Inches(0.6),
           size=22, color=b.TEAL, bold=True, shrink=True)
    d.text(s, data["tagline"],   Inches(0.65), Inches(2.65), Inches(10.5), Inches(0.4),
           size=13, color=b.MUTED)

    # Divider
    d.rect(s, Inches(0.65), Inches(3.15), Inches(11.5), Inches(0.04), b.NAVY_2)

    # KPI row
    if data["name"] == "Accenture":
        chips = [
            (f"${data['revenue']}B",       "FY2025 Revenue",      data["revenue_yoy"] + " YoY"),
            (data["genai_bookings_yoy"],    "GenAI Bookings YoY",  f"${data['genai_bookings']}B in FY2025"),
            (data["genai_market_share"],    "GenAI Market Share",  data["market_share_source"]),
            (data["ai_staff"],              "AI & Data Staff",     f"from {data['ai_staff_prior']} two years prior"),
        ]
    else:
        chips = [
            (f"${data['revenue']}B",             "FY2024 Revenue",       data["revenue_yoy"] + " YoY"),
            (f"${data['genai_book_q4_2025']}B+", "GenAI Book (Q4 2025)", "from $5B a year ago"),
            (data["software_pct"],                "Software Revenue",     "highest-margin segment"),
            (data["hashicorp_deal"],              "HashiCorp Acquired",   data["hashicorp_closed"]),
        ]

    cw = Inches(2.9)
    cx = Inches(0.65)
    for val, label, sub in chips:
        kpi_chip(d, s, cx, Inches(3.35), cw, Inches(1.6), val, label, sub)
        cx += cw + Inches(0.15)

    d.text(s, f"June 2026 · Sources: {data['fy_period']} earnings, Everest Group, IoT Analytics",
           Inches(0.65), H - Inches(0.45), Inches(11), Inches(0.33), size=9, color=b.MUTED)


def slide_at_a_glance(d, data, page, total):
    s = d.slide(fill=d.b.SOFT)
    b = d.b
    d.header(s, "At a Glance", f"{data['name']} · {data['fy']} Key Metrics")

    if data["name"] == "Accenture":
        tiles = [
            (f"${data['revenue']}B",            "Total Revenue",           f"{data['revenue_yoy']} in both USD & local currency"),
            (f"${data['bookings']}B",            "New Bookings",            f"Book-to-bill {data['book_to_bill']} · {data['bookings_yoy']} YoY"),
            (f"${data['genai_bookings']}B",      "GenAI Bookings",          data["genai_bookings_yoy"] + " year-over-year"),
            (f"${data['genai_revenue']}B",       "GenAI Revenue",           data["genai_revenue_yoy"] + " year-over-year"),
            (data["ai_staff"],                   "AI & Data Professionals", f"up from {data['ai_staff_prior']} two years ago"),
            (data["op_margin"],                  "Adjusted Operating Margin","60–80bps expansion over FY24"),
            (data["multi_service_deals"],        "Large Deals: Multi-Service","nearly all large deals span multiple service lines"),
            (data["genai_market_share"],         "GenAI Services Market Share","vs Deloitte 3%, IBM 2%  (IoT Analytics)"),
        ]
    else:
        tiles = [
            (f"${data['revenue']}B",             "FY2024 Revenue",         data["revenue_yoy"]),
            (f"${data['genai_book_q4_2025']}B+", "GenAI Book (Q4 2025)",   "inception-to-date since Q3 2023"),
            (data["software_pct"],               "Software Mix",            "highest-margin segment · 32% gross margin"),
            (data["fcf"],                        "Free Cash Flow (FY2024)", f"{data['fcf_yoy']} vs prior year"),
            (data["integrated_clients"],         "Revenue: Multi-Segment", "clients buying Software + Consulting + Infra"),
            (data["redhat_openshift_arr"],       "OpenShift ARR",           "up 13x since Red Hat acquisition"),
            (data["hashicorp_deal"],             "HashiCorp Acquisition",   data["hashicorp_closed"]),
            (data["genai_market_share"],         "GenAI Services Share",    data["market_share_source"]),
        ]

    tw = Inches(5.9)
    th = Inches(1.55)
    gap = Inches(0.22)
    left = Inches(0.4)
    right = left + tw + gap

    positions = [(left, Inches(1.5)), (right, Inches(1.5)),
                 (left, Inches(3.1)), (right, Inches(3.1)),
                 (left, Inches(4.7)), (right, Inches(4.7))]

    for i, ((tx, ty), (val, label, sub)) in enumerate(zip(positions, tiles[:6])):
        d.rect(s, tx, ty, tw, th, b.WHITE, radius=0.06)
        d.rect(s, tx, ty, Inches(0.1), th, b.TEAL, radius=0.0)
        d.text(s, val,   tx + Inches(0.2), ty + Inches(0.08), tw - Inches(0.3), Inches(0.72),
               size=30, color=b.INK, bold=True, shrink=True)
        d.text(s, label, tx + Inches(0.2), ty + Inches(0.83), tw - Inches(0.3), Inches(0.3),
               size=11, color=b.TEAL, bold=True)
        d.text(s, sub,   tx + Inches(0.2), ty + Inches(1.16), tw - Inches(0.3), Inches(0.3),
               size=9, color=b.MUTED, shrink=True)

    d.footer(s, page, total)


def slide_revenue_segments(d, data, page, total):
    s = d.slide(fill=d.b.WHITE)
    b = d.b
    d.header(s, "Revenue Breakdown", "Segment & industry mix driving growth")

    if data["name"] == "Accenture":
        # Left: by type of work
        d.rect(s, Inches(0.4), Inches(1.5), Inches(5.8), Inches(5.0), b.SOFT, radius=0.06)
        d.text(s, "BY TYPE OF WORK", Inches(0.6), Inches(1.65), Inches(5.4), Inches(0.35),
               size=11, color=b.TEAL, bold=True)

        work_items = [
            ("Consulting",       35.1, "+6%",  "Strategy, Technology, Song, Industry X"),
            ("Managed Services", 34.6, "+9%",  "Operations, BPO, application management"),
        ]
        for i, (name, rev, gr, desc) in enumerate(work_items):
            wy = Inches(2.15) + i * Inches(2.0)
            bw = Inches(4.0) * (rev / 70)
            d.rect(s, Inches(0.6), wy + Inches(0.5), bw, Inches(0.55), b.TEAL if i == 0 else hx("#00907A"), radius=0.04)
            d.text(s, name,  Inches(0.6), wy,                Inches(3.5), Inches(0.4), size=13, color=b.INK, bold=True)
            d.text(s, f"${rev}B · {gr} YoY", Inches(0.6), wy + Inches(0.45), Inches(2.5), Inches(0.4), size=10, color=b.WHITE, bold=True)
            d.text(s, desc,  Inches(0.6), wy + Inches(1.1),  Inches(5.2), Inches(0.4), size=9.5, color=b.MUTED)

        # Right: by industry
        d.rect(s, Inches(6.4), Inches(1.5), Inches(6.5), Inches(5.0), b.SOFT, radius=0.06)
        d.text(s, "BY INDUSTRY GROUP", Inches(6.6), Inches(1.65), Inches(6.1), Inches(0.35),
               size=11, color=b.TEAL, bold=True)

        bar_colors = [b.TEAL, hx("#009B82"), hx("#007B68"), hx("#005F50"), hx("#004038")]
        for i, (industry, rev, pct, gr) in enumerate(data["by_industry"]):
            iy = Inches(2.1) + i * Inches(0.85)
            bw = Inches(4.8) * (rev / 22)
            d.text(s, industry, Inches(6.6), iy, Inches(3.0), Inches(0.38), size=10.5, color=b.INK, bold=True)
            d.rect(s, Inches(6.6), iy + Inches(0.42), bw, Inches(0.28), bar_colors[i], radius=0.03)
            d.text(s, f"${rev}B ({pct}) · {gr}", Inches(6.6), iy + Inches(0.75), Inches(5.0), Inches(0.28),
                   size=9, color=b.MUTED)

    else:  # IBM
        # Segment table
        d.rect(s, Inches(0.4), Inches(1.5), Inches(12.3), Inches(0.5), b.NAVY, radius=0.0)
        headers = ["Segment", "FY2024 Revenue", "% of Total", "Growth (CC)", "Gross Margin"]
        col_ws = [Inches(2.8), Inches(2.4), Inches(1.8), Inches(2.8), Inches(2.5)]
        cx = Inches(0.5)
        for h, w in zip(headers, col_ws):
            d.text(s, h, cx, Inches(1.6), w, Inches(0.35), size=10, color=b.WHITE, bold=True)
            cx += w

        for ri, (seg, rev, pct, gr, margin) in enumerate(data["segments"]):
            ry = Inches(2.05) + ri * Inches(0.75)
            row_fill = b.LIGHT_TEAL if ri == 0 else (b.SOFT if ri % 2 == 0 else b.WHITE)
            d.rect(s, Inches(0.4), ry, Inches(12.3), Inches(0.72), row_fill, radius=0.0)
            cells = [seg, f"${rev}B", f"{pct}%", gr, margin]
            cx = Inches(0.5)
            for ci, (cell, w) in enumerate(zip(cells, col_ws)):
                is_bold = (ci == 0) or (ci == 3 and "+" in cell)
                color = b.TEAL if (ci == 3 and "+" in cell) else b.INK
                d.text(s, cell, cx, ry + Inches(0.12), w, Inches(0.48),
                       size=11, color=color, bold=is_bold)
                cx += w

        # Key insight below table
        d.rect(s, Inches(0.4), Inches(5.15), Inches(12.3), Inches(0.95), b.NAVY_2, radius=0.06)
        d.text(s, "KEY INSIGHT: IBM's transformation thesis — Software (45% of revenue, 32% margin) carries growth while Consulting recovers. "
               "Infrastructure declining ~3% is \"in line with product cycle\" expectations. "
               "Red Hat (Software) is the acquisition that changed IBM's trajectory.",
               Inches(0.6), Inches(5.25), Inches(12.0), Inches(0.75),
               size=10.5, color=b.WHITE, shrink=True)

    d.footer(s, page, total)


def slide_ai_platform(d, data, page, total):
    s = d.slide(fill=d.b.NAVY)
    b = d.b

    d.rect(s, 0, 0, d.W, Inches(1.25), b.NAVY_2)
    d.text(s, "AI PLATFORM & STRATEGY",    Inches(0.5), Inches(0.12), Inches(11), Inches(0.45),
           size=13, color=b.TEAL, bold=True)
    d.text(s, f"How {data['name']} is monetizing the AI wave",
           Inches(0.5), Inches(0.62), Inches(11), Inches(0.5), size=18, color=b.WHITE)

    if data["name"] == "Accenture":
        metrics = [
            ("$2.7B",   "GenAI Revenue",    "tripled YoY"),
            ("$5.9B",   "GenAI Bookings",   "nearly doubled YoY"),
            ("77,000",  "AI Staff",          "from 40K 2 years ago"),
            ("6,000+",  "AI Projects",       "delivered in FY2025"),
        ]
        insight = ("The $3B Bet Is Paying Off",
                   "Accenture's FY2023 decision to commit $3B to GenAI is the clearest first-mover bet in consulting. "
                   "FY2025 results validate the thesis: $2.7B revenue (tripled), $5.9B bookings (nearly doubled), 7% GenAI market share. "
                   "No competitor has matched this scale of AI revenue to date. The model: train talent first, ship client solutions second, monetize at scale third. "
                   "CEO Julie Sweet: 'We are reinventing what we sell, how we deliver, how we partner.'")
    else:
        metrics = [
            ("$12.5B+", "GenAI Book (Q4'25)", "from $5B a year ago"),
            ("+22%",    "Automation Growth",   "Q3 2025 incl. HashiCorp"),
            ("$1.4B",   "OpenShift ARR",        "13x since Red Hat acqn"),
            ("93%",     "Fortune 500 on IBM HC","hybrid cloud penetration"),
        ]
        insight = ("The 'AI for Regulated Enterprise' Niche",
                   "IBM is not competing with OpenAI or Google on frontier models. Its thesis: regulated enterprises "
                   "(banking, healthcare, government, defense) cannot send data to public cloud AI. "
                   "IBM's Granite models are 90% more cost-efficient than frontier alternatives and can run on-premise. "
                   "watsonx GenAI book grew from $5B to $12.5B in 12 months — 150% growth. "
                   "The IBM 'Client Zero' story (490 workflows, $3.5B savings, -3% to +5% revenue) is the proof point for 500+ consulting deals.")

    # KPI chips row
    cw = Inches(2.9)
    cx = Inches(0.45)
    for val, label, sub in metrics:
        d.rect(s, cx, Inches(1.4), cw, Inches(1.3), b.NAVY, radius=0.08)
        d.text(s, val,   cx + Inches(0.15), Inches(1.5),  cw - Inches(0.3), Inches(0.6),
               size=28, color=b.TEAL, bold=True)
        d.text(s, label, cx + Inches(0.15), Inches(2.13), cw - Inches(0.3), Inches(0.32),
               size=11, color=b.WHITE, bold=True)
        d.text(s, sub,   cx + Inches(0.15), Inches(2.48), cw - Inches(0.3), Inches(0.25),
               size=9, color=b.MUTED)
        cx += cw + Inches(0.19)

    # Insight box
    title, body = insight
    d.rect(s, Inches(0.45), Inches(2.95), Inches(12.2), Inches(3.5), b.NAVY_2, radius=0.08)
    d.rect(s, Inches(0.45), Inches(2.95), Inches(12.2), Inches(0.06), b.TEAL, radius=0.0)
    d.text(s, title, Inches(0.65), Inches(3.05), Inches(11.8), Inches(0.5),
           size=15, color=b.TEAL, bold=True)
    d.text(s, body,  Inches(0.65), Inches(3.65), Inches(11.8), Inches(2.6),
           size=11.5, color=b.WHITE, shrink=True)

    d.footer(s, page, total, dark=True)


def slide_strategic_moves(d, data, page, total):
    s = d.slide(fill=d.b.SOFT)
    b = d.b
    d.header(s, "Strategic Moves", "What's changed and why it matters")

    moves = data["strategic_moves"]

    cw = Inches(5.9)
    ch = Inches(2.15)
    gap = Inches(0.25)
    col0 = Inches(0.4)

    nums = ["①", "②", "③", "④"]

    for i, (title, body) in enumerate(moves):
        col = i % 2
        row = i // 2
        bx = col0 + col * (cw + gap)
        by = Inches(1.5) + row * (ch + gap)

        d.rect(s, bx, by, cw, ch, b.WHITE, radius=0.07)
        d.rect(s, bx, by, cw, Inches(0.07), b.TEAL, radius=0.0)
        d.text(s, nums[i], bx + Inches(0.15), by + Inches(0.1),  Inches(0.5), Inches(0.5),
               size=20, color=b.TEAL, bold=True)
        d.text(s, title,   bx + Inches(0.65), by + Inches(0.1),  cw - Inches(0.8), Inches(0.5),
               size=12, color=b.INK, bold=True, shrink=True)
        d.text(s, body,    bx + Inches(0.15), by + Inches(0.68), cw - Inches(0.3), Inches(1.35),
               size=9.5, color=b.MUTED, shrink=True)

    d.footer(s, page, total)


def slide_competitive_landscape(d, data, page, total):
    s = d.slide(fill=d.b.WHITE)
    b = d.b
    d.header(s, "Competitive Landscape", "AI consulting & enterprise technology market")

    comps = data["competitors"]

    # Market context box
    if data["name"] == "Accenture":
        mkt_text = ("AI Consulting Market Context: Valued at $14B in 2024, projected to reach $630B+ by 2028. "
                    "Tier 1 players (Accenture, IBM, Deloitte, Capgemini) hold 50–55% share. "
                    "Accenture leads GenAI services with 7% share — first-mover advantage from $3B investment.")
    else:
        mkt_text = ("IBM's Competitive Niche: Not competing on market share in GenAI services (2% vs Accenture 7%). "
                    "Competing on infrastructure + platform: 93% of Fortune 500 on IBM hybrid cloud. "
                    "Regulated industries (banking, healthcare, government) = IBM's defensible moat.")

    d.rect(s, Inches(0.4), Inches(1.5), Inches(12.3), Inches(0.75), b.LIGHT_TEAL, radius=0.06)
    d.text(s, mkt_text, Inches(0.6), Inches(1.58), Inches(12.0), Inches(0.62),
           size=10, color=b.INK, shrink=True)

    # Table
    headers = ["Company", "Revenue", "GenAI Mkt Share", "AI Platform", "Analyst Tier"]
    col_ws = [Inches(2.2), Inches(1.6), Inches(2.0), Inches(3.8), Inches(2.3)]

    d.rect(s, Inches(0.4), Inches(2.4), sum(col_ws) + Inches(0.3), Inches(0.52), b.NAVY)
    cx = Inches(0.5)
    for h, w in zip(headers, col_ws):
        d.text(s, h, cx, Inches(2.5), w - Inches(0.05), Inches(0.35),
               size=10, color=b.WHITE, bold=True)
        cx += w

    for ri, row_data in enumerate(comps):
        ry = Inches(2.95) + ri * Inches(0.64)
        is_focal = row_data[0].endswith("◀")
        row_fill = b.LIGHT_TEAL if is_focal else (b.SOFT if ri % 2 == 0 else b.WHITE)
        d.rect(s, Inches(0.4), ry, sum(col_ws) + Inches(0.3), Inches(0.62), row_fill, radius=0.0)
        cx = Inches(0.5)
        for ci, (cell, w) in enumerate(zip(row_data, col_ws)):
            color = b.TEAL if (is_focal and ci == 0) else b.INK
            d.text(s, cell, cx, ry + Inches(0.1), w - Inches(0.08), Inches(0.45),
                   size=10, color=color, bold=(is_focal and ci == 0), shrink=True)
            cx += w

    d.footer(s, page, total)


def slide_key_risks(d, data, page, total):
    s = d.slide(fill=d.b.WHITE)
    b = d.b
    d.header(s, "Key Risks & Headwinds", "What could derail the thesis")

    risks = data["risks"]
    risk_icons = ["!", "⚠", "~", "?"]
    risk_colors = [b.CORAL, b.GOLD, hx("#E05A6B"), b.MUTED]

    cw = Inches(5.9)
    ch = Inches(2.15)
    gap = Inches(0.25)
    col0 = Inches(0.4)

    for i, (title, body) in enumerate(risks):
        col = i % 2
        row = i // 2
        bx = col0 + col * (cw + gap)
        by = Inches(1.5) + row * (ch + gap)
        rc = risk_colors[i % len(risk_colors)]

        d.rect(s, bx, by, cw, ch, b.SOFT, radius=0.07)
        d.rect(s, bx, by, Inches(0.4), ch, rc, radius=0.0)
        d.rect(s, bx, by, cw, Inches(0.06), rc, radius=0.0)

        d.text(s, title, bx + Inches(0.55), by + Inches(0.1),  cw - Inches(0.7), Inches(0.5),
               size=12, color=b.INK, bold=True, shrink=True)
        d.text(s, body,  bx + Inches(0.55), by + Inches(0.68), cw - Inches(0.7), Inches(1.35),
               size=10, color=b.MUTED, shrink=True)

    d.footer(s, page, total)


def slide_revenue_trend(d, data, page, total):
    s = d.slide(fill=d.b.WHITE)
    b = d.b
    d.header(s, "Revenue Trend", "5-year trajectory from SEC EDGAR XBRL")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fys = [r[0] for r in data["rev_history"]]
        vals = [r[1] for r in data["rev_history"]]
        bar_colors = [b.HX_TEAL if i == len(vals) - 1 else b.HX_NAVY for i in range(len(vals))]

        fig, ax = plt.subplots(figsize=(10, 4))
        bars = ax.bar(fys, vals, color=bar_colors, width=0.55)
        for bar, v in zip(bars, vals):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.4,
                    f"${v:.1f}B", ha="center", va="bottom", fontsize=11, fontweight="bold")
        ax.set_ylabel("Revenue ($B)", fontsize=11)
        ax.set_facecolor("#FFFFFF")
        fig.patch.set_facecolor("#FFFFFF")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.yaxis.grid(True, linestyle="--", alpha=0.35)
        ax.set_axisbelow(True)
        ax.tick_params(axis="both", labelsize=11)
        plt.tight_layout()

        chart_path = ROOT / f"data/{data['name'].lower()}/rev_trend.png"
        chart_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(chart_path, dpi=150, bbox_inches="tight")
        plt.close()
        d.picture_centered(s, chart_path, top=Inches(1.5), width=Inches(10.5), max_bottom=Inches(6.3))
    except ImportError:
        rows = [f"{fy}: ${v}B" for fy, v in data["rev_history"]]
        d.text(s, "\n".join(rows), Inches(1), Inches(1.8), Inches(10), Inches(4.5),
               size=20, color=b.INK)

    # Annotation
    name = data["name"]
    if name == "Accenture":
        note = "Accenture added ~$20B in revenue since 2021 (+38%). FY2025 inflection driven by GenAI bookings ramp."
    else:
        note = "IBM revenue stabilized after Kyndryl (2021) and Watson Health (2022) divestitures. Software-led growth resuming."
    d.rect(s, Inches(0.5), Inches(6.0), Inches(12.3), Inches(0.45), b.LIGHT_TEAL, radius=0.04)
    d.text(s, note, Inches(0.65), Inches(6.05), Inches(12.0), Inches(0.38),
           size=10, color=b.INK, shrink=True)

    d.footer(s, page, total)


def slide_strategic_themes(d, data, page, total):
    s = d.slide(fill=d.b.SOFT)
    b = d.b
    d.header(s, "Strategic Themes", "Signal synthesis from market intelligence")

    if data["name"] == "Accenture":
        themes = [
            ("AI Revenue Is Real, Not Narrative",
             "$2.7B GenAI revenue (tripled) + $5.9B bookings (nearly doubled) in FY2025. This is not PoC pipeline — it's delivered revenue. The $3B multi-year investment made in FY2023 is the highest-conviction AI bet by any consulting firm to date.",
             "$2.7B revenue · tripled YoY"),
            ("Reinvention Services = Simpler Cross-Sell",
             "Collapsing 5 BUs into one 'Reinvention Services' unit (Sep 2025) reduces internal friction and speeds multi-service deal closure. 80% of large deals already multi-service. This org move is a revenue acceleration lever, not just a restructure.",
             "80% of large deals are multi-service"),
            ("Talent Scale Is The Moat",
             "77,000 AI & data professionals + 550,000 GenAI-trained employees = Accenture can staff enterprise AI rollouts that no competitor can match at scale. The talent gap is the #1 barrier enterprises face — Accenture's core competency addresses it directly.",
             "77K AI staff · 550K trained"),
            ("Ecosystem Partnerships Drive Scale",
             "No. 1 partner for all top 10 tech ecosystem companies. 60% of revenue from ecosystem work (+9% YoY, outpacing total growth). This makes Accenture the implementation layer for every major tech platform — a structural advantage competitors can't easily replicate.",
             "60% ecosystem revenue · +9% YoY"),
        ]
    else:
        themes = [
            ("Software Is Now The Growth Engine",
             "Software at 45% of revenue with 32% gross margin — the highest-margin segment and the fastest growing (+9% CC). Red Hat is the acquisition thesis validated: OpenShift ARR at $1.4B (13x since acquisition). IBM's 'software-led, integrated enterprise' model is now reality, not aspiration.",
             "45% software mix · +9% CC growth"),
            ("watsonx GenAI Book: $5B → $12.5B in 12 Months",
             "$12.5B GenAI book of business (Q4 2025) from $5B a year prior = 150% growth. 25% of the $32B revenue backlog is GenAI. Annualized GenAI consulting run rate: $3.6B. IBM is not winning on market share vs Accenture — but it's winning in regulated enterprise where cloud-only AI cannot go.",
             "$12.5B book · +150% YoY"),
            ("HashiCorp Makes IBM The Infrastructure IaC Platform",
             "$6.4B HashiCorp (closed Feb 2025) adds Terraform + Vault to IBM's stack. Terraform + Ansible + Red Hat = end-to-end infrastructure-as-code. Automation segment hit +22% in Q3 2025. Deployment time cuts from 45 min to 3 min = CFO-level ROI story.",
             "$6.4B acquisition · +22% Automation"),
            ("Consulting Must Reaccelerate Or Thesis Breaks",
             "IBM Consulting was -0.9% in FY2024 (vs Accenture +6%). Returned to growth in H2 2025 (+2%). If Consulting cannot sustain mid-single-digit growth, total revenue caps at +5%. The 'Client Zero' story and Consulting Advantage platform are IBM's mechanisms for reacceleration.",
             "Consulting -0.9% FY24 → needs +5%+"),
        ]

    cw = Inches(5.9)
    ch = Inches(2.2)
    gap = Inches(0.25)
    col0 = Inches(0.4)

    for i, (title, body, stat) in enumerate(themes):
        col = i % 2
        row = i // 2
        bx = col0 + col * (cw + gap)
        by = Inches(1.5) + row * (ch + gap)

        d.rect(s, bx, by, cw, ch, b.WHITE, radius=0.07)
        d.rect(s, bx, by, Inches(0.1), ch, b.TEAL, radius=0.0)
        d.text(s, title, bx + Inches(0.2), by + Inches(0.1),  cw - Inches(0.3), Inches(0.5),
               size=12, color=b.INK, bold=True, shrink=True)
        d.text(s, body,  bx + Inches(0.2), by + Inches(0.65), cw - Inches(0.3), Inches(1.15),
               size=9.5, color=b.MUTED, shrink=True)
        d.rect(s, bx + Inches(0.2), by + Inches(1.85), cw - Inches(0.4), Inches(0.28), b.LIGHT_TEAL, radius=0.03)
        d.text(s, stat,  bx + Inches(0.3), by + Inches(1.87), cw - Inches(0.5), Inches(0.24),
               size=9, color=b.TEAL, bold=True)

    d.footer(s, page, total)


def slide_recommendations(d, data, page, total):
    s = d.slide(fill=d.b.NAVY)
    b = d.b

    d.rect(s, 0, 0, d.W, Inches(1.3), b.TEAL)
    d.text(s, "RECOMMENDATIONS", Inches(0.5), Inches(0.15), Inches(11), Inches(0.5),
           size=13, color=b.NAVY, bold=True)
    d.text(s, f"Strategic actions for teams tracking {data['name']}",
           Inches(0.5), Inches(0.65), Inches(11), Inches(0.5), size=16, color=b.NAVY)

    if data["name"] == "Accenture":
        recs = [
            ("WATCH", b.GOLD,
             "Monitor Reinvention Services deal velocity",
             "Q1 FY2026 earnings (Dec 2025): first full quarter under the new integrated BU. Watch whether large deal close rates accelerate. A rise in average deal size signals the org change is working."),
            ("COMPETE", b.CORAL,
             "Target their mid-market gap",
             "Everest Group specifically flags Accenture's limited mid-market presence as a limitation. Competitors can take mid-market AI transformation mandates that Accenture is structurally less suited to serve cost-effectively."),
            ("PARTNER", b.TEAL,
             "Engage the ecosystem partnership model",
             "60% of Accenture revenue flows through its top 10 ecosystem partners. For tech vendors wanting enterprise AI adoption, Accenture is the most efficient implementation channel — but partnership terms favor Accenture's scale."),
            ("TRACK", b.ACCENT,
             "Watch GenAI bookings trajectory vs revenue",
             "$5.9B GenAI bookings vs $2.7B GenAI revenue = 2.2x book-to-bill on AI alone. This implies a large revenue ramp still ahead in FY2026/27 as bookings convert to revenue. Watch for deceleration signals."),
        ]
    else:
        recs = [
            ("WATCH", b.GOLD,
             "Track Consulting return to growth",
             "IBM Consulting was -0.9% in FY2024, returned to +2% in H2 2025. If it cannot sustain +5%+ in FY2026, the software-led thesis faces a 38%-of-revenue deadweight problem. Watch Q1 2026 earnings."),
            ("COMPETE", b.CORAL,
             "Counter watsonx in regulated industries",
             "IBM's on-premise AI moat is in banking, healthcare, government. Competitors must choose: match IBM's hybrid capability (expensive) or concede regulated industries and focus on cloud-native enterprises."),
            ("PARTNER", b.TEAL,
             "Evaluate HashiCorp Terraform integration opportunities",
             "HashiCorp just shifted strategy from SaaS-first to hybrid cloud. Partners can build practices around Terraform + Ansible + OpenShift. The IBM channel stamp adds credibility for GSI partnerships."),
            ("TRACK", b.ACCENT,
             "Watch Granite model adoption vs frontier AI",
             "If enterprises choose GPT-5 / Claude 4 over Granite for production AI workloads, IBM's 'AI for business' niche shrinks. Q2/Q3 2026 will show whether the GenAI book converts to revenue at the claimed scale."),
        ]

    for i, (tag, tag_color, title, body) in enumerate(recs):
        by = Inches(1.45) + i * Inches(1.25)
        d.rect(s, Inches(0.4), by, Inches(0.95), Inches(1.1), tag_color, radius=0.07)
        d.text(s, tag, Inches(0.4), by + Inches(0.28), Inches(0.95), Inches(0.5),
               size=9.5, color=b.WHITE, bold=True, align=PP_ALIGN.CENTER)
        d.text(s, title, Inches(1.5), by,              Inches(11.2), Inches(0.48),
               size=13, color=b.WHITE, bold=True, shrink=True)
        d.text(s, body,  Inches(1.5), by + Inches(0.5), Inches(11.2), Inches(0.7),
               size=10.5, color=b.MUTED, shrink=True)

    d.footer(s, page, total, dark=True)


def slide_sources(d, data, page, total):
    s = d.slide(fill=d.b.SOFT)
    b = d.b
    d.header(s, "Sources & Methodology", "All data is primary-sourced or analyst-verified")

    sources = [
        ("Earnings Release",
         f"{data['name']} official earnings press release · {data['fy_period']}",
         "newsroom.accenture.com / newsroom.ibm.com"),
        ("SEC EDGAR",
         f"10-K annual filing · XBRL company facts · Revenue trend 5-year history",
         "data.sec.gov/api/xbrl"),
        ("Investor Letter / Annual Report",
         f"{data['name']} {data['fy']} Annual Report + Letter to Shareholders",
         "accenture.com / ibm.com/downloads"),
        ("Everest Group",
         "AI & Generative AI Services PEAK Matrix Assessment 2025 · Leader/Contender ratings",
         "everestgrp.com"),
        ("IoT Analytics",
         "GenAI Services Market Share Report, January 2025",
         "iot-analytics.com"),
        ("Exa Research",
         "Web research via Exa API · CRN, CIO Dive, Next Platform, Techaisle, SiliconAngle, theCUBE",
         "api.exa.ai · June 2026"),
    ]

    for i, (src, detail, url) in enumerate(sources):
        by = Inches(1.55) + i * Inches(0.82)
        d.rect(s, Inches(0.4), by, Inches(12.3), Inches(0.75), b.WHITE, radius=0.06)
        d.rect(s, Inches(0.4), by, Inches(0.1), Inches(0.75), b.TEAL, radius=0.0)
        d.text(s, src,    Inches(0.65), by + Inches(0.05), Inches(3.2), Inches(0.35),
               size=11, color=b.INK, bold=True)
        d.text(s, detail, Inches(0.65), by + Inches(0.42), Inches(9.5), Inches(0.28),
               size=9.5, color=b.MUTED, shrink=True)
        d.text(s, url,    Inches(10.2), by + Inches(0.22), Inches(2.4), Inches(0.3),
               size=9, color=b.TEAL)

    d.footer(s, page, total)


# ── Orchestrator ──────────────────────────────────────────────────────────────

def build_deck(company: str, out: str | None = None):
    data = ACN if company == "accenture" else IBM_DATA
    out_path = out or str(ROOT / f"{company}-market-brief-draft.pptx")
    footer_str = f"{data['name']} Market Intelligence Brief · June 2026 · Sources: Earnings, Everest Group, IoT Analytics, Exa"

    d = Deck(footer=footer_str)
    TOTAL = 10

    slide_cover(d, data)
    slide_at_a_glance(d, data, 2, TOTAL)
    slide_revenue_trend(d, data, 3, TOTAL)
    slide_revenue_segments(d, data, 4, TOTAL)
    slide_ai_platform(d, data, 5, TOTAL)
    slide_strategic_moves(d, data, 6, TOTAL)
    slide_competitive_landscape(d, data, 7, TOTAL)
    slide_key_risks(d, data, 8, TOTAL)
    slide_strategic_themes(d, data, 9, TOTAL)
    slide_recommendations(d, data, 10, TOTAL)

    d.save(out_path)
    print(f"\n✓ {data['name']} market brief → {out_path}  ({d.n} slides)")
    return out_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("company", help="accenture | ibm")
    parser.add_argument("--out", default=None)
    args = parser.parse_args()
    build_deck(args.company.lower(), args.out)


if __name__ == "__main__":
    main()
