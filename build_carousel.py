#!/usr/bin/env python3
"""
Accenture LinkedIn Carousel — 22 slides, 1:1 square format (8×8 inches)
Condensed insight-per-slide format for LinkedIn carousel delivery.
"""
import sys
from pathlib import Path

PPTXKIT_DIR = Path.home() / ".claude/skills/branded-pptx-deck/scripts"
sys.path.insert(0, str(PPTXKIT_DIR))
from pptxkit import Brand, Deck, PP_ALIGN, MSO_ANCHOR, Inches, Pt, RGBColor
from pptx import Presentation
from pptx.util import Inches as PInches, Emu

OUT_DIR = Path(__file__).parent
OUT_FILE = OUT_DIR / "accenture-carousel-draft.pptx"

# ── Square deck (8" × 8") ─────────────────────────────────────────────────────
d = Deck(footer="")
d.prs.slide_width = Inches(8)
d.prs.slide_height = Inches(8)
d.W = Inches(8)
d.H = Inches(8)
d.M = Inches(0.4)
d.CW = d.W - d.M * 2
b = d.b

TOTAL = 22

def cs(s, title, stat_num, stat_label, bullets, domain_tag, slide_num,
       dark=False, accent_color=None):
    """Standard carousel skill slide."""
    ac = accent_color or b.TEAL
    bg = b.NAVY if dark else b.WHITE
    tc = b.WHITE if dark else b.NAVY
    mc = b.LIGHT_TEAL if dark else b.MUTED

    d.rect(s, 0, 0, d.W, d.H, bg)
    # top band
    d.rect(s, 0, 0, d.W, Inches(0.1), ac)
    # left spine
    d.rect(s, 0, 0, Inches(0.06), d.H, ac)

    # domain tag chip
    d.rect(s, Inches(0.4), Inches(0.22), Inches(4.2), Inches(0.26), b.NAVY_2 if not dark else b.NAVY_2)
    d.text(s, f"DOMAIN: {domain_tag.upper()}", Inches(0.5), Inches(0.26),
           Inches(4.0), Inches(0.2), size=8, color=ac, bold=True)

    # slide counter
    d.text(s, f"{slide_num}/{TOTAL}", Inches(6.8), Inches(0.26), Inches(0.8), Inches(0.22),
           size=9, color=mc, bold=True, align=PP_ALIGN.RIGHT)

    # title
    d.text(s, title, Inches(0.4), Inches(0.6), Inches(7.2), Inches(1.6),
           size=22, color=tc, bold=True, font=b.FONT_H, shrink=True, ls=1.15)

    # teal rule
    d.rect(s, Inches(0.4), Inches(2.28), Inches(1.5), Inches(0.04), ac)

    # stat box
    d.rect(s, Inches(0.4), Inches(2.42), Inches(7.2), Inches(0.88), b.NAVY if not dark else b.NAVY_2, radius=0.06)
    d.text(s, stat_num, Inches(0.55), Inches(2.5), Inches(2.5), Inches(0.65),
           size=28, color=b.GOLD, bold=True)
    d.text(s, stat_label, Inches(3.1), Inches(2.58), Inches(4.3), Inches(0.55),
           size=12.5, color=b.WHITE, ls=1.2, shrink=True)

    # bullets
    for i, bullet in enumerate(bullets):
        by = Inches(3.48) + i * Inches(1.2)
        d.rect(s, Inches(0.4), by + Inches(0.08), Inches(0.06), Inches(0.06), ac, radius=0.15)
        d.text(s, bullet, Inches(0.58), by, Inches(7.0), Inches(1.1),
               size=13, color=tc, ls=1.25, shrink=True)

    # footer strip
    d.rect(s, 0, Inches(7.7), d.W, Inches(0.3), b.NAVY_2 if not dark else b.NAVY)
    d.text(s, "Accenture Strategy Analysis 2026  ·  Applied via Accenture-Style Claude Skills",
           Inches(0.25), Inches(7.74), Inches(7.5), Inches(0.22),
           size=7.5, color=b.MUTED, align=PP_ALIGN.CENTER)


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 1 — COVER
# ─────────────────────────────────────────────────────────────────────────────
s = d.slide(fill=b.NAVY)
d.rect(s, 0, 0, d.W, Inches(0.12), b.TEAL)
d.rect(s, 0, 0, Inches(0.1), d.H, b.TEAL)
d.rect(s, 0, d.H - Inches(0.08), d.W, Inches(0.08), b.TEAL)

d.text(s, "ACCENTURE  ·  STRATEGY ANALYSIS", Inches(0.45), Inches(0.5),
       Inches(7.2), Inches(0.3), size=9.5, color=b.TEAL, bold=True)
d.text(s, "We ran 21 consulting frameworks on Accenture itself.",
       Inches(0.45), Inches(1.0), Inches(7.1), Inches(1.1),
       size=30, color=b.WHITE, bold=True, font=b.FONT_H, shrink=True, ls=1.1)
d.text(s, "Here's what we found.",
       Inches(0.45), Inches(2.2), Inches(7.1), Inches(0.65),
       size=30, color=b.GOLD, bold=True, font=b.FONT_H)
d.rect(s, Inches(0.45), Inches(3.0), Inches(2.0), Inches(0.06), b.TEAL)
d.text(s, "360 AI strategy prompts · Applied to $69.7B FY2025 data\n+ 223 GitHub repos · June 2026",
       Inches(0.45), Inches(3.2), Inches(7.0), Inches(0.8),
       size=14, color=b.LIGHT_TEAL, ls=1.3)

for i, (num, lbl) in enumerate([("$69.7B", "Revenue"), ("$2.7B", "GenAI Rev"), ("7%", "Growth"), ("$5.9B", "Bookings")]):
    cx = Inches(0.35) + i * Inches(1.85)
    d.rect(s, cx, Inches(4.3), Inches(1.7), Inches(0.85), b.NAVY_2, radius=0.06)
    d.text(s, num, cx + Inches(0.1), Inches(4.38), Inches(1.5), Inches(0.45),
           size=22, color=b.GOLD, bold=True)
    d.text(s, lbl, cx + Inches(0.1), Inches(4.8), Inches(1.5), Inches(0.24),
           size=10, color=b.MUTED)

d.text(s, "Swipe to see the full analysis →",
       Inches(0.45), Inches(5.45), Inches(7.0), Inches(0.36),
       size=14, color=b.TEAL, bold=True)

d.rect(s, 0, Inches(7.7), d.W, Inches(0.3), b.NAVY_2)
d.text(s, "Sources: Accenture FY2025 10-K · github.com/Accenture · VMR 2026 · Avasant 2026",
       Inches(0.25), Inches(7.74), Inches(7.5), Inches(0.22),
       size=7.5, color=b.MUTED, align=PP_ALIGN.CENTER)

# ── SLIDES 2–21: 20 SKILL / INSIGHT SLIDES ───────────────────────────────────

SLIDES = [
    # (title, stat_num, stat_label, [bullets], domain_tag, dark)
    ("Accenture enters FY2026 from strength — but a structural transition is underway",
     "$2.7B", "GenAI revenue tripled year-over-year in FY2025",
     ["The $3B AI bet is paying off — GenAI revenue tripled and bookings hit $5.9B",
      "FY2026 guidance decelerates to 2–5%: US federal freeze + T&M pricing pressure",
      "129 deals >$100M per quarter sets a record — enterprise trust is holding"],
     "Diagnosis & Framing", False),

    ("Growth is decelerating to 2–5% — three binding constraints identified",
     "1–1.5%", "FY2026 revenue drag from US federal budget freeze alone",
     ["US federal freeze ($3–5B exposure) is the most immediate and quantifiable drag",
      "Boutique AI firms undercutting Accenture at 40–60% of T&M day rates",
      "$5.9B GenAI bookings signal demand — but 12–18 month lag suppresses near-term rev"],
     "Diagnosis & Framing", True),

    ("Three assumptions underpin 'Reinvention' — one is proven, two are at risk",
     "<10%", "Of Accenture contracts are outcome-based — critical assumption UNPROVEN",
     ["PROVEN: GenAI demand is real — $5.9B in bookings validates the market",
      "AT RISK: OpenAI Frontier Alliance (Feb 2026) embeds AI vendors inside client teams",
      "UNPROVEN: Outcome-based pricing at scale — still <10% of deals today"],
     "Diagnosis & Framing", False),

    ("The $350B consulting market is bifurcating — GenAI advisory is the only high-growth segment",
     "$150B", "GenAI advisory market projected by 2030 — from $15B today (60%+ CAGR)",
     ["Accenture is #1 by revenue in tech transformation, the $120B core segment",
      "Strategy advisory ($40B) still dominated by MBB — Accenture is under-indexed",
      "White space: mid-market AI transformation — MBB too costly, boutiques too narrow"],
     "Market & Competitive Intel", True),

    ("Accenture Labs published the benchmark their competitors will be judged by",
     "486⭐", "mcp-bench on GitHub — NeurIPS 2025, live HuggingFace leaderboard",
     ["MBB (BCG X, McKinsey QuantumBlack) are closing the strategy-to-delivery gap",
      "OpenAI Frontier Alliance: AI vendors embedded inside Fortune 100 client teams",
      "Accenture counter: mcp-bench owns the evaluation standard for agentic AI"],
     "Market & Competitive Intel", False),

    ("91 of the Fortune 100 are clients — the growth upside is in the Fortune 500 mid-tier",
     "91/100", "Fortune 100 companies are current Accenture clients",
     ["Fortune 100: defend and deepen — expand GenAI scope, 129 deals >$100M per quarter",
      "Fortune 500 mid-tier: highest GenAI curiosity, lowest AI deployment — biggest runway",
      "APAC/LatAm at 17% of revenue: fastest-growing, underweight vs market potential"],
     "Market & Competitive Intel", True),

    ("GenAI advisory captures 2× the margin of traditional implementation",
     "22–25%", "Estimated margin on GenAI advisory vs. 13–16% for traditional implementation",
     ["GenAI advisory ($2.7B): the most attractive profit pool in the Accenture portfolio",
      "Operations/managed services (~$15B): margin compression risk as AI automates routine work",
      "Platform IP (AI Refinery SDK): potential 60%+ margins at licensing scale"],
     "Market & Competitive Intel", False),

    ("AI Refinery SDK is the moat — GitHub proves it's real, not a slide-deck promise",
     "v1.31.3", "AI Refinery SDK — last pushed June 9, 2026. 29 releases in 14 months.",
     ["github.com/Accenture/airefinery-sdk: production multi-agent platform, Apache 2.0",
      "Distiller Framework orchestrates specialist AI agents — competes with BCG X",
      "This is Option B (platform + delivery scale) confirmed as live, not aspirational"],
     "Strategic Choice & Economics", True),

    ("The $3B AI bet has a sub-18-month payback — and the GitHub IP adds uncounted value",
     "5 streams", "Of IP value: AI Refinery, mcp-bench, AmpliGraph, Federated Learning, ADM",
     ["Financial ROI: $2.7B GenAI revenue in FY2025 against $3B 3-year investment",
      "Research: mcp-bench (NeurIPS 2025) + AmpliGraph (2,237 stars) = citation leverage",
      "Platform licensing (AI Refinery): potential 60%+ margins, zero marginal cost"],
     "Strategic Choice & Economics", False),

    ("Technology and GenAI advisory are INVEST — Operations needs AI automation to survive",
     "3%", "Operations growth rate — with only 10–14% margin. Most at-risk business unit.",
     ["Technology (~$30B): INVEST — AI delivery augmentation improves margin and speed",
      "Song (~$4B): GROW — 12% growth, AI-creative convergence creates differentiation",
      "Operations (~$15B): FIX — AI automation is the only path to margin defense"],
     "Strategic Choice & Economics", True),

    ("T&M pricing is Accenture's biggest margin risk — outcome-based must scale to 20%+",
     "<10% → 20%", "Current vs. target outcome-based contract mix by FY2027",
     ["T&M risk: GenAI doubles delivery speed → clients will renegotiate day rates downward",
      "Opportunity: capture 15–25% of the 15–30% cost reduction AI creates for clients",
      "Bridge: 'Reinvention packs' (fixed-scope, outcome-defined) as the pricing transition"],
     "Strategic Choice & Economics", False),

    ("AI Refinery's Distiller Framework IS the target operating architecture",
     "LLM-agnostic", "AI Refinery Inference API — connect GPT-5, Claude, Gemini — no vendor lock-in",
     ["Distiller Framework: multi-agent orchestrator — parallel execution with context passing",
      "Responsible AI module: built-in policy/safety rules per query — Fortune 100 governance-ready",
      "ADM (Application Delivery Method): 12-phase lifecycle, 11 specialist agent roles"],
     "Operating Model & Execution", True),

    ("GitHub commit history proves Phase 3 is LIVE — not just a strategy slide",
     "June 9, 2026", "Date of last AI Refinery SDK commit — 6 days before this analysis",
     ["Phase 1 (FY2023–24): $3B committed, 47M training hours — COMPLETE",
      "Phase 2 (FY2025): $2.7B GenAI revenue, 77K AI practitioners — DELIVERED",
      "Phase 3 (FY2026): AI Refinery v1.31.3 pushed June 9 — LIVE and shipping"],
     "Operating Model & Execution", False),

    ("Agentic AI and AI Refinery commercialization are the vital few — everything else waits",
     "47,000+", "GenAI client projects identified — Accenture must now prioritize ruthlessly",
     ["P1: Agentic AI service line (High/High) — build on $5.9B bookings, launch Q1 FY2026",
      "P2: AI Refinery platform commercialization — 29 releases, ready to ship externally",
      "KILL: Traditional headcount-led outsourcing growth — commoditized, margin-dilutive"],
     "Operating Model & Execution", True),

    ("Accenture needs a new KPI system built around AI outcomes — not headcount and billability",
     "Target: $8B+", "GenAI bookings in FY2026 — the new #1 leading performance indicator",
     ["Replace: gross headcount growth — wrong proxy for value in the AI-augmented era",
      "New leading KPI: GenAI booking velocity + outcome-based deal % (target 20%)",
      "New driver KPI: AI-augmented revenue per consultant (not hours billed)"],
     "Risk, Performance & Value", False),

    ("OpenAI disintermediation and GenAI commoditization are the two existential risks",
     "Feb 2026", "OpenAI Frontier Alliance launched — AI vendors now embedded in client teams",
     ["CRITICAL: OpenAI direct enterprise — advisory layer disintermediated at the model level",
      "HIGH: GenAI commodity pricing — boutiques offering comparable work at 50% of day rates",
      "Mitigation: own the integration layer + accelerate AI Refinery IP moat NOW"],
     "Risk, Performance & Value", True),

    ("The $3B AI investment generated $2.7B in year-2 revenue — ahead of plan",
     "$0.9B → $2.7B", "GenAI revenue FY2024 to FY2025 — tripled in a single year",
     ["FY2026 target: $5B+ GenAI revenue based on $5.9B bookings forward pipeline",
      "Next value stream: AI Refinery platform licensing — recurring IP revenue at scale",
      "Value at risk: ~$10B in future GenAI revenue if OpenAI disintermediation accelerates"],
     "Risk, Performance & Value", False),

    ("Two scenarios could break Accenture's strategy — both need pre-committed responses today",
     "18–24 months", "First-mover window before MBB tech arms and OpenAI commoditize advisory",
     ["Scenario 1 (CRITICAL): OpenAI direct enterprise — own the integration layer, ship IP",
      "Scenario 2 (HIGH): GenAI ROI recession — pivot immediately to cost-reduction use cases",
      "Early signal to watch: BCG X headcount growth rate + GenAI deal cancellation rate"],
     "Risk, Performance & Value", True),

    ("Recommendation: commercialize AI Refinery before the first-mover window closes",
     "Q1 FY2026", "Board decision deadline for AI Refinery licensing + agentic AI service line",
     ["Evidence: AI Refinery v1.31.3 is production-ready — 29 releases, Apache 2.0",
      "Evidence: $5.9B GenAI bookings + $2.7B revenue confirm demand is real and growing",
      "Risk of inaction: BCG X and OpenAI move faster; Accenture loses the IP premium"],
     "Alignment & Exec Comms", False),

    ("The investor narrative: 'We bet on AI first — now we're building the moat'",
     "SCQA", "Situation → Complication → Question → Answer — the full story arc",
     ["SITUATION: $69.7B, GenAI tripled — FY2025 was the proof year for the $3B bet",
      "COMPLICATION: FY2026 decelerates — managed platform pivot, not a warning sign",
      "ACTION: Platform commercialization + agentic AI approved Q1 = the moat-building phase"],
     "Alignment & Exec Comms", True),
]

for i, (title, stat_num, stat_label, bullets, domain, dark) in enumerate(SLIDES):
    s = d.slide(fill=b.NAVY if dark else b.WHITE)
    cs(s, title, stat_num, stat_label, bullets, domain, i + 2, dark=dark)

# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 22 — SIX RECOMMENDATIONS (CTA)
# ─────────────────────────────────────────────────────────────────────────────
s = d.slide(fill=b.NAVY)
d.rect(s, 0, 0, d.W, Inches(0.1), b.TEAL)
d.rect(s, 0, 0, Inches(0.08), d.H, b.TEAL)
d.rect(s, 0, d.H - Inches(0.08), d.W, Inches(0.08), b.TEAL)

d.text(s, "SIX MOVES THAT DEFINE FY2026–27", Inches(0.4), Inches(0.25),
       Inches(7.2), Inches(0.3), size=10, color=b.TEAL, bold=True)
d.text(s, "The Accenture\nStrategy Playbook",
       Inches(0.4), Inches(0.65), Inches(7.2), Inches(1.0),
       size=28, color=b.WHITE, bold=True, font=b.FONT_H, shrink=True, ls=1.1)

RECS = [
    ("01", "Commercialize AI Refinery™", "Platform licensing by Q1 FY2026"),
    ("02", "Launch Agentic AI line", "Build on $5.9B bookings"),
    ("03", "Scale outcome pricing", "Target 20% of deals by FY2027"),
    ("04", "Automate Operations", "AI-augment to defend margin"),
    ("05", "Pre-wire OpenAI alliance", "Secure SI position before deepening"),
    ("06", "Platform story to investors", "Reframe FY2026 as managed pivot"),
]

for i, (num, title, desc) in enumerate(RECS):
    row, col_i = divmod(i, 2)
    cx = Inches(0.35) + col_i * Inches(3.75)
    cy = Inches(1.85) + row * Inches(1.68)
    d.rect(s, cx, cy, Inches(3.5), Inches(1.52), b.NAVY_2, radius=0.06)
    d.rect(s, cx, cy, Inches(3.5), Inches(0.07), b.TEAL, radius=0.04)
    d.text(s, num, cx + Inches(0.12), cy + Inches(0.12), Inches(0.5), Inches(0.25),
           size=9.5, color=b.TEAL, bold=True)
    d.text(s, title, cx + Inches(0.12), cy + Inches(0.4), Inches(3.2), Inches(0.55),
           size=14, color=b.WHITE, bold=True, font=b.FONT_H, shrink=True)
    d.text(s, desc, cx + Inches(0.12), cy + Inches(0.98), Inches(3.2), Inches(0.46),
           size=11, color=b.LIGHT_TEAL, shrink=True)

d.rect(s, Inches(0.35), Inches(7.05), Inches(7.3), Inches(0.52), b.TEAL, radius=0.06)
d.text(s, "Save this · Follow for more AI strategy · Comment which framework you'd use first",
       Inches(0.5), Inches(7.14), Inches(7.0), Inches(0.3),
       size=11, color=b.NAVY, bold=True, align=PP_ALIGN.CENTER)

d.rect(s, 0, Inches(7.7), d.W, Inches(0.3), b.NAVY_2)
d.text(s, "22/22  ·  Accenture Strategy Analysis 2026  ·  github.com/Accenture  ·  FY2025 10-K",
       Inches(0.25), Inches(7.74), Inches(7.5), Inches(0.22),
       size=7.5, color=b.MUTED, align=PP_ALIGN.CENTER)

# ─────────────────────────────────────────────────────────────────────────────
d.save(OUT_FILE)
print(f"\nCarousel: {OUT_FILE}  ({TOTAL} slides)")
