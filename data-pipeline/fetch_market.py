#!/usr/bin/env python3
"""
fetch_market.py — pull market research data for the target company.

Priority order (uses first available):
  1. Exa API   — FIRECRAWL_BEARER_AUTH in env (skips; Exa key = EXA_API_KEY)
  2. Firecrawl — FIRECRAWL_BEARER_AUTH in env
  3. stdlib    — urllib direct scrape of newsroom / investor pages

Usage:
    python3 data-pipeline/fetch_market.py
    EXA_API_KEY=... python3 data-pipeline/fetch_market.py   # richer results

Output: data/market_intel.json
"""
import argparse, json, os, re, sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
SOURCES = json.loads((ROOT / "data-pipeline/sources.json").read_text())

EXA_KEY = os.getenv("EXA_API_KEY", "")
FIRECRAWL_KEY = os.getenv("FIRECRAWL_BEARER_AUTH", "")


# ── Exa HTTP client ───────────────────────────────────────────────────────────

def exa_search(query: str, n: int = 5) -> list[dict]:
    if not EXA_KEY:
        return []
    payload = json.dumps({"query": query, "numResults": n,
                          "contents": {"text": {"maxCharacters": 3000}}}).encode()
    req = Request("https://api.exa.ai/search",
                  data=payload,
                  headers={"Content-Type": "application/json", "x-api-key": EXA_KEY})
    try:
        with urlopen(req, timeout=20) as r:
            results = json.loads(r.read()).get("results", [])
            return [{"url": x.get("url"), "title": x.get("title"),
                     "published": x.get("publishedDate", "")[:10],
                     "text": x.get("text", "")[:2000]} for x in results]
    except Exception as e:
        print(f"  [exa] search failed: {e}")
        return []


# ── Firecrawl client ──────────────────────────────────────────────────────────

def firecrawl_scrape(url: str) -> str:
    if not FIRECRAWL_KEY:
        return ""
    payload = json.dumps({"url": url, "formats": ["markdown"]}).encode()
    req = Request("https://api.firecrawl.dev/v1/scrape",
                  data=payload,
                  headers={"Content-Type": "application/json",
                            "Authorization": f"Bearer {FIRECRAWL_KEY}"})
    try:
        with urlopen(req, timeout=30) as r:
            data = json.loads(r.read())
            return data.get("data", {}).get("markdown", "")[:3000]
    except Exception as e:
        print(f"  [firecrawl] scrape failed for {url}: {e}")
        return ""


# ── stdlib fallback ───────────────────────────────────────────────────────────

def stdlib_fetch(url: str, max_chars: int = 4000) -> str:
    headers = {"User-Agent": "intel-pipeline/1.0", "Accept": "text/html,application/json"}
    req = Request(url, headers=headers)
    try:
        with urlopen(req, timeout=15) as r:
            raw = r.read().decode("utf-8", errors="replace")
            # Strip HTML tags crudely
            text = re.sub(r"<[^>]+>", " ", raw)
            text = re.sub(r"\s+", " ", text).strip()
            return text[:max_chars]
    except (HTTPError, URLError) as e:
        print(f"  [stdlib] fetch failed for {url}: {e}")
        return ""


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--company", default=SOURCES["target"]["name"])
    parser.add_argument("--out", default=str(ROOT / "data/market_intel.json"))
    args = parser.parse_args()

    company = args.company
    cfg = SOURCES["market_research"]

    backend = "exa" if EXA_KEY else "firecrawl" if FIRECRAWL_KEY else "stdlib"
    print(f"[market] fetching market data for '{company}' using backend: {backend}")

    sections: dict = {}

    if EXA_KEY:
        for tmpl in cfg["exa_queries"]:
            query = tmpl.replace("{company}", company)
            print(f"  exa: {query[:60]}...")
            results = exa_search(query, n=4)
            key = re.sub(r"[^a-z0-9_]", "_", query[:40].lower())
            sections[key] = results

    elif FIRECRAWL_KEY:
        urls = cfg.get("firecrawl_urls", [])
        for url in urls:
            print(f"  firecrawl: {url}")
            sections[url] = firecrawl_scrape(url)

    else:
        # stdlib: scrape public investor/newsroom pages
        pages = {
            "newsroom": SOURCES["target"].get("newsroom_url", ""),
            "investor": SOURCES["target"].get("investor_url", ""),
        }
        for name, url in pages.items():
            if url:
                print(f"  stdlib: {url}")
                sections[name] = stdlib_fetch(url)

    intel = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "company": company,
        "backend": backend,
        "sections": sections,
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(intel, indent=2))
    print(f"[market] written → {out}")
    return intel


if __name__ == "__main__":
    main()
