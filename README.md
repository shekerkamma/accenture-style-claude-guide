# Accenture-Style Claude Guide

21 consulting frameworks applied to Claude — prompt templates, branded PPTX decks, and a LinkedIn carousel, all grounded in Accenture's real FY2025 10-K and GitHub data.

## What's In Here

| File | Description |
|------|-------------|
| `accenture-style-claude-guide-draft.pptx` | 24-slide guide deck — the $39 consulting prompt guide replicated as a branded PPTX |
| `accenture-strategy-analysis-v2-draft.pptx` | 24-slide Accenture strategy analysis — 21 frameworks applied to real FY2025 data + 223 GitHub repos |
| `accenture-carousel-draft.pptx` | 22-slide LinkedIn carousel (8×8" square format) — one insight per framework |
| `accenture-carousel-content.md` | Raw carousel content — all 22 slides as markdown |
| `build_guide_deck.py` | Builder script for the 24-slide guide deck |
| `build_accenture_deck.py` | Builder script for the populated Accenture analysis deck |
| `build_carousel.py` | Builder script for the LinkedIn carousel |

## The 21 Consulting Frameworks (Prompt Templates)

Sourced from [aapersh/strategy-skills-for-claude](https://github.com/aapersh/strategy-skills-for-claude) — 21 SKILL.md files organized across 6 domains.

### Domain 1: Diagnosis & Framing
- **Situation Assessment** — fact-based baseline; used for business reviews, turnaround diagnosis, board prep
- **Growth Barriers** — identifies binding growth constraints; stalled revenue, funnel issues
- **Assumption Audit** — surfaces load-bearing strategic assumptions; pressure-tests strategy

### Domain 2: Market & Competitive Intelligence
- **Market Mapping** — sizes and segments markets; TAM/SAM/SOM, white space
- **Competitive Intel** — models likely competitor moves; market entry, pricing changes
- **Customer Segmentation** — MECE customer segments; ICP work, go-to-market focus
- **Profit Pool Analysis** — maps where profit is created and captured; channel strategy

### Domain 3: Strategic Choice & Economics
- **Strategic Options** — generates and compares options; build-buy-partner decisions
- **Business Case Builder** — evidence-backed business cases; ROI, NPV, board cases
- **Portfolio Review** — capital allocation; where to invest or exit
- **Pricing Strategy** — diagnoses pricing power; discount leakage, packaging redesign

### Domain 4: Operating Model & Execution
- **Operating Model Design** — translates strategy into capabilities and roles
- **Transformation Roadmap** — converts strategy to delivery plan; 90-day plans, workstreams
- **Initiative Prioritizer** — prioritizes by impact and feasibility; annual planning, OKRs

### Domain 5: Risk, Performance & Value Governance
- **KPI Architect** — designs KPI systems tied to strategic decisions; dashboards, OKRs
- **Risk & Mitigation** — builds strategic risk register; likelihood, impact, mitigation, owner
- **Value Realization** — tracks and captures strategic value; benefits tracking, synergy capture
- **War Gaming** — stress-tests strategy against disruptions; scenario planning

### Domain 6: Alignment & Executive Communication
- **Decision Memo** — produces executive decision memos; board memos, investment recommendations
- **Narrative Builder** — builds executive strategy narratives; Pyramid Principle, board decks
- **Stakeholder Alignment** — maps influence and pre-wire paths; board approval, change management

## Using as Claude Slash Commands (Global)

These 21 frameworks are registered as global slash commands in Claude Code. From any project:

```
/strategy-consulting              # orchestrator — pick a framework interactively
/situation-assessment             # run directly
/war-gaming                       # run directly
/business-case-builder            # run directly
# ...any of the 21 triggers
```

The prompt templates live at `~/.claude/skills/strategy-consulting/skills/`.

## What the Accenture Analysis Found (Key Outputs)

Applied all 21 frameworks to Accenture using FY2025 10-K data + GitHub intelligence:

| Finding | Data |
|---------|------|
| GenAI revenue tripled | $0.9B → $2.7B in FY2025 |
| GenAI bookings | $5.9B (nearly doubled YoY) |
| AI Refinery SDK | v1.31.3, 29 releases in 14 months, last pushed June 9 2026 |
| mcp-bench | Accenture Labs benchmark, accepted NeurIPS 2025, live HuggingFace leaderboard |
| FY2026 guidance | 2–5% growth (deceleration from 7%) |
| Operations unit risk | Only 3% growth, 10–14% margin — most at-risk business unit |

**Six strategic recommendations:**
1. Commercialize AI Refinery™ — platform licensing by Q1 FY2026
2. Launch Agentic AI service line — build on $5.9B bookings
3. Scale outcome-based pricing to 20% of deals by FY2027
4. Automate Operations margin — AI-augment delivery
5. Pre-wire the OpenAI alliance — secure SI position before Frontier Alliance deepens
6. Reframe FY2026 to investors as a managed platform pivot, not deceleration

## Build Requirements

The PPTX builder scripts require [pptxkit](https://github.com/shekerkamma/content-ideas) — the branded PPTX toolkit.

```bash
# Install dependency
pip install python-pptx

# Rebuild any deck
python3 build_guide_deck.py        # → accenture-style-claude-guide-draft.pptx
python3 build_accenture_deck.py    # → accenture-strategy-analysis-v2-draft.pptx
python3 build_carousel.py          # → accenture-carousel-draft.pptx
```

pptxkit must be on the Python path — it ships with the `branded-pptx-deck` Claude skill at `~/.claude/skills/branded-pptx-deck/scripts/pptxkit.py`.

## Sources

- Accenture FY2025 Annual Report & 10-K (September 2025)
- [github.com/Accenture](https://github.com/Accenture) — 223 public repos, June 2026 snapshot
- VMR Consulting Market Report 2026
- Avasant Strategic Consulting Update 2026
- [aapersh/strategy-skills-for-claude](https://github.com/aapersh/strategy-skills-for-claude) — 21 consulting SKILL.md prompt templates

---

*Built with Claude Code + 21 Accenture-style consulting frameworks*
