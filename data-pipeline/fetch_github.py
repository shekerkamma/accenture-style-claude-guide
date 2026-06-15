#!/usr/bin/env python3
"""
fetch_github.py — pull live GitHub org intelligence for a target company.

Usage:
    python3 data-pipeline/fetch_github.py                  # uses sources.json
    python3 data-pipeline/fetch_github.py --org Accenture  # override org
    python3 data-pipeline/fetch_github.py --token ghp_xxx  # authenticated (5000 req/hr)

Output: data/github_intel.json
"""
import argparse, base64, json, os, sys, time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

SOURCES = json.loads((ROOT / "data-pipeline/sources.json").read_text())
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")

def gh(path: str, token: str = "") -> dict | list:
    url = f"https://api.github.com{path}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "intel-pipeline/1.0",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = Request(url, headers=headers)
    try:
        with urlopen(req, timeout=15) as r:
            return json.loads(r.read())
    except HTTPError as e:
        if e.code == 404:
            return {}
        if e.code == 403:
            print(f"  [rate-limited] {path} — add --token for 5000 req/hr")
            return {}
        raise


def fetch_org_repos(org: str, token: str) -> list[dict]:
    repos, page = [], 1
    while True:
        batch = gh(f"/orgs/{org}/repos?per_page=100&sort=stars&page={page}", token)
        if not batch:
            break
        repos.extend(batch)
        page += 1
        if len(batch) < 100:
            break
        time.sleep(0.5)
    return repos


def fetch_repo_detail(org: str, name: str, token: str, fetch_readme: bool = False) -> dict:
    r = gh(f"/repos/{org}/{name}", token)
    if not r:
        return {}
    detail = {
        "name": r["name"],
        "description": r.get("description", ""),
        "stars": r["stargazers_count"],
        "forks": r["forks_count"],
        "open_issues": r["open_issues_count"],
        "language": r.get("language", ""),
        "license": (r.get("license") or {}).get("spdx_id", ""),
        "pushed_at": r["pushed_at"][:10],
        "created_at": r["created_at"][:10],
        "homepage": r.get("homepage", ""),
        "topics": r.get("topics", []),
        "archived": r.get("archived", False),
    }

    # releases
    releases = gh(f"/repos/{org}/{name}/releases?per_page=100", token)
    if isinstance(releases, list) and releases:
        detail["releases"] = {
            "count": len(releases),
            "latest_tag": releases[0]["tag_name"],
            "latest_date": releases[0]["published_at"][:10],
            "oldest_date": releases[-1]["published_at"][:10],
            "span_days": (
                datetime.fromisoformat(releases[0]["published_at"][:10])
                - datetime.fromisoformat(releases[-1]["published_at"][:10])
            ).days,
        }
    else:
        detail["releases"] = {"count": 0}

    # contributors
    contribs = gh(f"/repos/{org}/{name}/contributors?per_page=10", token)
    detail["contributor_count"] = len(contribs) if isinstance(contribs, list) else 0

    # readme excerpt
    if fetch_readme:
        readme_data = gh(f"/repos/{org}/{name}/readme", token)
        if readme_data and "content" in readme_data:
            try:
                content = base64.b64decode(readme_data["content"]).decode("utf-8")
                detail["readme_excerpt"] = content[:2000]
            except Exception:
                pass

    return detail


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--org", default=SOURCES["target"]["github_org"])
    parser.add_argument("--token", default=GITHUB_TOKEN)
    parser.add_argument("--out", default=str(ROOT / "data/github_intel.json"))
    args = parser.parse_args()

    token = args.token
    org = args.org
    cfg = SOURCES["github"]

    print(f"[github] fetching {org} org data...")

    # Rate limit check
    rl = gh("/rate_limit", token)
    remaining = rl.get("rate", {}).get("remaining", "?")
    print(f"  API rate limit: {remaining} requests remaining")

    # All org repos
    print(f"  fetching all repos (paginated)...")
    all_repos = fetch_org_repos(org, token)
    print(f"  found {len(all_repos)} repos")

    total_stars = sum(r["stargazers_count"] for r in all_repos)
    langs: dict[str, int] = {}
    for r in all_repos:
        l = r.get("language") or "Other"
        langs[l] = langs.get(l, 0) + 1
    top_repos = sorted(all_repos, key=lambda r: r["stargazers_count"], reverse=True)[:10]

    # Key repo deep dives
    print(f"  fetching key repo details: {cfg['key_repos']}")
    key_repo_data = {}
    for name in cfg["key_repos"]:
        print(f"    {name}...")
        fetch_readme = name in cfg.get("fetch_readme_for", [])
        detail = fetch_repo_detail(org, name, token, fetch_readme)
        if detail:
            key_repo_data[name] = detail
        time.sleep(0.3)

    intel = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "org": org,
        "summary": {
            "total_repos": len(all_repos),
            "total_stars": total_stars,
            "language_breakdown": dict(sorted(langs.items(), key=lambda x: -x[1])[:10]),
        },
        "top_repos_by_stars": [
            {"name": r["name"], "stars": r["stargazers_count"],
             "description": r.get("description", ""), "pushed_at": r["pushed_at"][:10]}
            for r in top_repos
        ],
        "key_repos": key_repo_data,
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(intel, indent=2))
    print(f"[github] written → {out}")
    return intel


if __name__ == "__main__":
    main()
