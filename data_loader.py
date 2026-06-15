"""
data_loader.py — shared access layer for builder scripts.

Usage:
    from data_loader import load_intel, get
    intel = load_intel()
    revenue = get(intel, "summary.latest_annual_revenue_usd", default=69_700_000_000)
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent
DATA_FILE = ROOT / "data/intel.json"

# ── Hardcoded fallbacks (used when data/intel.json is absent or stale) ────────
# Run `python3 data-pipeline/run_pipeline.py` to refresh.
FALLBACKS = {
    "meta.target": "Accenture",
    "meta.github_org": "Accenture",
    # GitHub
    "summary.github_org_repos": 223,
    "summary.github_org_stars": 10027,
    "summary.repo_airefinery_sdk_stars": 54,
    "summary.repo_airefinery_sdk_pushed": "2026-06-09",
    "summary.repo_airefinery_sdk_release_count": 30,
    "summary.repo_airefinery_sdk_latest_tag": "1.31.4",
    "summary.repo_airefinery_sdk_release_span_months": 12,
    "summary.repo_mcp_bench_stars": 486,
    "summary.repo_mcp_bench_pushed": "2025-10-07",
    "summary.repo_AmpliGraph_stars": 2237,
    # Financials (Accenture FY2025 10-K)
    "summary.latest_annual_revenue_usd": 69_672_977_000,
    "summary.latest_annual_revenue_fy": "2025",
    "summary.prev_annual_revenue_usd": 64_896_464_000,
    "summary.revenue_yoy_pct": 7.4,
    # Supplemental (not in XBRL, sourced from earnings release)
    "supplemental.genai_revenue_usd": 2_700_000_000,
    "supplemental.genai_bookings_usd": 5_900_000_000,
    "supplemental.total_bookings_usd": 80_600_000_000,
    "supplemental.ai_practitioners": 77_000,
    "supplemental.fortune_100_clients": 91,
    "supplemental.quarterly_bookings_over_100m": 129,
    "supplemental.fy26_guidance_growth_low": 2.0,
    "supplemental.fy26_guidance_growth_high": 5.0,
    "supplemental.adjusted_eps_fy25": 12.93,
    "supplemental.free_cash_flow_usd": 10_900_000_000,
    # Q1 FY26 (Dec 2025)
    "supplemental.q1fy26_revenue_usd": 18_700_000_000,
    "supplemental.q1fy26_bookings_usd": 20_900_000_000,
    "supplemental.q1fy26_advanced_ai_bookings_usd": 2_200_000_000,
    "supplemental.q1fy26_advanced_ai_revenue_usd": 1_100_000_000,
    "supplemental.q1fy26_advanced_ai_clients": 1300,
    "supplemental.q1fy26_deployed_agents": 3000,
    # Market research
    "market_research.ai_consulting_market_2026_usd": 13_800_000_000,
    "market_research.ai_consulting_market_2033_usd": 73_100_000_000,
    "market_research.ai_consulting_cagr_pct": 27.1,
    "market_research.total_ai_spending_2026_usd": 2_520_000_000_000,
    "market_research.us_consulting_market_2026_usd": 411_700_000_000,
    "market_research.ai_tam_by_2029_usd": 70_000_000_000,
    # Competitor signals
    "competitors.bcg_revenue_2025_usd": 14_400_000_000,
    "competitors.bcg_ai_revenue_share_pct": 40,
    "competitors.bcg_x_headcount": 3000,
    "competitors.boutique_growth_premium_pct": 38,
}


def load_intel() -> dict:
    """Load intel.json if available; merge with fallbacks for missing keys."""
    if DATA_FILE.exists():
        try:
            live = json.loads(DATA_FILE.read_text())
            # Merge supplemental fallbacks that live data doesn't populate
            if "supplemental" not in live:
                live["supplemental"] = {}
            for k, v in FALLBACKS.items():
                if k.startswith("supplemental."):
                    sub_k = k.split(".", 1)[1]
                    live["supplemental"].setdefault(sub_k, v)
            if "market_research" not in live.get("market", {}):
                live.setdefault("market_research_fallback", {})
                for k, v in FALLBACKS.items():
                    if k.startswith("market_research."):
                        live["market_research_fallback"][k.split(".", 1)[1]] = v
            return live
        except Exception as e:
            print(f"[data_loader] warning: could not parse intel.json ({e}), using fallbacks")

    # No data file — return fallback dict structured for get()
    return {"_fallback_only": True, **{k: v for k, v in FALLBACKS.items()}}


def get(intel: dict, path: str, default=None):
    """
    Dot-path accessor with fallback.
    get(intel, "summary.github_org_repos")
    get(intel, "supplemental.genai_revenue_usd")
    """
    # Try live data via nested path
    parts = path.split(".")
    node = intel
    for p in parts:
        if isinstance(node, dict) and p in node:
            node = node[p]
        else:
            node = None
            break
    if node is not None:
        return node

    # Fallback to FALLBACKS dict
    return FALLBACKS.get(path, default)


def fmt_b(n: float | int, decimals: int = 1) -> str:
    """Format a USD value as $XB or $XM."""
    if n >= 1e9:
        return f"${n / 1e9:.{decimals}f}B"
    if n >= 1e6:
        return f"${n / 1e6:.{decimals}f}M"
    return f"${n:,.0f}"


def fmt_pct(n: float, sign: bool = True) -> str:
    prefix = "+" if sign and n > 0 else ""
    return f"{prefix}{n:.1f}%"
