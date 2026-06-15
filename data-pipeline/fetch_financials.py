#!/usr/bin/env python3
"""
fetch_financials.py — pull SEC EDGAR 10-K/10-Q filings for the target company.

Usage:
    python3 data-pipeline/fetch_financials.py
    python3 data-pipeline/fetch_financials.py --cik 0001467373

Output: data/financials.json
"""
import argparse, json, re, sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
SOURCES = json.loads((ROOT / "data-pipeline/sources.json").read_text())

HEADERS = {"User-Agent": "intel-pipeline/1.0 research@example.com", "Accept": "application/json"}


def edgar(path: str) -> dict | list:
    url = f"https://data.sec.gov{path}"
    req = Request(url, headers=HEADERS)
    with urlopen(req, timeout=20) as r:
        return json.loads(r.read())


def fetch_xbrl_facts(cik: str) -> dict:
    """Pull XBRL company facts — annual revenue, income, EPS."""
    cik_padded = cik.lstrip("0").zfill(10)
    try:
        facts = edgar(f"/api/xbrl/companyfacts/CIK{cik_padded}.json")
    except HTTPError:
        return {}

    us_gaap = facts.get("facts", {}).get("us-gaap", {})

    def series(concept: str) -> list[dict]:
        vals = us_gaap.get(concept, {}).get("units", {}).get("USD", [])
        annual = [v for v in vals if v.get("form") in ("10-K", "20-F") and v.get("fp") == "FY"]
        # Deduplicate by fiscal year — keep the highest value per year (full-year total)
        by_fy: dict[str, dict] = {}
        for v in annual:
            fy = v["end"][:4]
            if fy not in by_fy or v["val"] > by_fy[fy]["val"]:
                by_fy[fy] = v
        return sorted(by_fy.values(), key=lambda v: v["end"], reverse=True)[:5]

    revenue = series("Revenues") or series("RevenueFromContractWithCustomerExcludingAssessedTax")
    net_income = series("NetIncomeLoss")
    eps_diluted = [
        v for v in us_gaap.get("EarningsPerShareDiluted", {}).get("units", {}).get("USD/shares", [])
        if v.get("form") in ("10-K", "20-F") and v.get("fp") == "FY"
    ]
    eps_diluted = sorted(eps_diluted, key=lambda v: v["end"], reverse=True)[:5]

    def fmt(series_data: list) -> list[dict]:
        return [{"fy": v["end"][:4], "value": v["val"], "filed": v.get("filed", "")}
                for v in series_data]

    return {
        "revenue_usd": fmt(revenue),
        "net_income_usd": fmt(net_income),
        "eps_diluted": [{"fy": v["end"][:4], "value": v["val"]} for v in eps_diluted],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cik", default=SOURCES["target"]["sec_cik"])
    parser.add_argument("--out", default=str(ROOT / "data/financials.json"))
    args = parser.parse_args()

    cik = args.cik.lstrip("0").zfill(10)
    print(f"[financials] fetching SEC EDGAR data for CIK {cik}...")

    # Submissions — filing index
    submissions = edgar(f"/submissions/CIK{cik}.json")
    company_name = submissions.get("name", "Unknown")
    print(f"  company: {company_name}")

    recent = submissions["filings"]["recent"]
    forms = recent["form"]
    filing_dates = recent["filingDate"]
    accessions = recent["accessionNumber"]

    def get_filings(form_type: str, n: int = 4) -> list[dict]:
        found = []
        for i, f in enumerate(forms):
            if f == form_type:
                found.append({"date": filing_dates[i], "accession": accessions[i]})
            if len(found) >= n:
                break
        return found

    filings_10k = get_filings("10-K")
    filings_10q = get_filings("10-Q", n=4)
    print(f"  10-K filings: {len(filings_10k)}, 10-Q filings: {len(filings_10q)}")

    # XBRL financials
    print(f"  fetching XBRL facts...")
    xbrl = fetch_xbrl_facts(cik)
    if xbrl.get("revenue_usd"):
        print(f"  latest revenue: ${xbrl['revenue_usd'][0]['value']:,.0f} (FY{xbrl['revenue_usd'][0]['fy']})")

    intel = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "company": company_name,
        "cik": cik,
        "filings": {
            "10-K": filings_10k,
            "10-Q": filings_10q,
        },
        "xbrl_financials": xbrl,
        "sec_filing_url": f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik}&type=10-K",
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(intel, indent=2))
    print(f"[financials] written → {out}")
    return intel


if __name__ == "__main__":
    main()
