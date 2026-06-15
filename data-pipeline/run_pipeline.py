#!/usr/bin/env python3
"""
run_pipeline.py — orchestrator: run all fetchers → data/intel.json

Usage:
    python3 data-pipeline/run_pipeline.py
    python3 data-pipeline/run_pipeline.py --skip-market     # GitHub + EDGAR only
    python3 data-pipeline/run_pipeline.py --company IBM --github-org IBM --cik 0000051143

Env vars:
    GITHUB_TOKEN          — optional, raises rate limit 60 → 5000 req/hr
    EXA_API_KEY           — optional, enables Exa web search for market data
    FIRECRAWL_BEARER_AUTH — optional, enables Firecrawl scraping

Output: data/intel.json (merged from all fetchers)
"""
import argparse, json, os, sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "data-pipeline"))

import fetch_github
import fetch_financials
import fetch_market


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--company", default=None, help="Override company name")
    parser.add_argument("--github-org", default=None)
    parser.add_argument("--cik", default=None)
    parser.add_argument("--skip-market", action="store_true")
    parser.add_argument("--skip-financials", action="store_true")
    parser.add_argument("--out", default=str(ROOT / "data/intel.json"))
    args = parser.parse_args()

    # Patch sources if overrides given
    sources_path = ROOT / "data-pipeline/sources.json"
    sources = json.loads(sources_path.read_text())
    if args.company:
        sources["target"]["name"] = args.company
    if args.github_org:
        sources["target"]["github_org"] = args.github_org
    if args.cik:
        sources["target"]["sec_cik"] = args.cik
    sources_path.write_text(json.dumps(sources, indent=2))

    print("=" * 60)
    print(f"  INTEL PIPELINE — {sources['target']['name']}")
    print(f"  {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print("=" * 60)

    # ── Stage 1: GitHub ───────────────────────────────────────────────────────
    print("\n[1/3] GitHub intelligence")
    github_intel = fetch_github.main()

    # ── Stage 2: Financials (SEC EDGAR) ──────────────────────────────────────
    financials = {}
    if not args.skip_financials:
        print("\n[2/3] Financials (SEC EDGAR)")
        financials = fetch_financials.main()
    else:
        print("\n[2/3] Financials — skipped")

    # ── Stage 3: Market research ──────────────────────────────────────────────
    market_intel = {}
    if not args.skip_market:
        print("\n[3/3] Market research")
        market_intel = fetch_market.main()
    else:
        print("\n[3/3] Market research — skipped")

    # ── Merge ─────────────────────────────────────────────────────────────────
    print("\n[merge] building intel.json...")
    intel = {
        "meta": {
            "target": sources["target"]["name"],
            "github_org": sources["target"]["github_org"],
            "built_at": datetime.now(timezone.utc).isoformat(),
            "sources": ["github", "sec_edgar", "market_research"],
        },
        "github": github_intel,
        "financials": financials,
        "market": market_intel,
        # ── Derived summary (quick-access for builder scripts) ────────────────
        "summary": _derive_summary(github_intel, financials),
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(intel, indent=2))
    print(f"\n✓ Pipeline complete → {out}")
    _print_summary(intel["summary"])
    return intel


def _derive_summary(github: dict, financials: dict) -> dict:
    """Extract the numbers builder scripts need most."""
    s = {}

    # GitHub
    if github:
        s["github_org_repos"] = github.get("summary", {}).get("total_repos", 0)
        s["github_org_stars"] = github.get("summary", {}).get("total_stars", 0)
        kr = github.get("key_repos", {})
        for name, data in kr.items():
            slug = name.replace("-", "_")
            s[f"repo_{slug}_stars"] = data.get("stars", 0)
            s[f"repo_{slug}_pushed"] = data.get("pushed_at", "")
            releases = data.get("releases", {})
            if releases.get("count"):
                s[f"repo_{slug}_release_count"] = releases["count"]
                s[f"repo_{slug}_latest_tag"] = releases.get("latest_tag", "")
                s[f"repo_{slug}_release_span_months"] = releases.get("span_days", 0) // 30

    # Financials
    if financials:
        rev = financials.get("xbrl_financials", {}).get("revenue_usd", [])
        if rev:
            s["latest_annual_revenue_usd"] = rev[0]["value"]
            s["latest_annual_revenue_fy"] = rev[0]["fy"]
            if len(rev) >= 2:
                s["prev_annual_revenue_usd"] = rev[1]["value"]
                s["revenue_yoy_pct"] = round(
                    (rev[0]["value"] - rev[1]["value"]) / rev[1]["value"] * 100, 1)

    return s


def _print_summary(s: dict):
    print("\n── Key Numbers ──────────────────────────────────────────")
    if "latest_annual_revenue_usd" in s:
        rev = s["latest_annual_revenue_usd"]
        fy = s.get("latest_annual_revenue_fy", "")
        yoy = s.get("revenue_yoy_pct", "")
        print(f"  Revenue FY{fy}: ${rev/1e9:.1f}B  (+{yoy}% YoY)")
    if "github_org_repos" in s:
        print(f"  GitHub: {s['github_org_repos']} repos, {s.get('github_org_stars', 0):,} stars")
    for k, v in s.items():
        if "latest_tag" in k:
            repo = k.replace("repo_", "").replace("_latest_tag", "")
            pushed = s.get(k.replace("latest_tag", "pushed"), "")
            count = s.get(k.replace("latest_tag", "release_count"), "")
            months = s.get(k.replace("latest_tag", "release_span_months"), "")
            print(f"  {repo}: {v}  ({count} releases over {months}mo, last push {pushed})")
    print("─────────────────────────────────────────────────────────")


if __name__ == "__main__":
    main()
