# Deep-Profiling Project: Submission Summary

**Date:** 11 May 2026  
**Project:** Federer Criteria Profiling for Mid-Market Indian Tech Manufacturers  
**Status:** ✅ COMPLETE

---

## Project Overview

This project identifies and scores 25 high-potential mid-market Indian technical manufacturers against a **6-criteria Federer model** (Founder-led, Differentiated, Engineering-driven, technical Decision-maker, in Evolving/Emerging sectors, with Evidence of growth). The focus is on specialty biotech, diagnostics, and defence/electronics manufacturers in the Hyderabad cluster.

---

## Deliverables

### 1. **25-Company Shortlist with Federer Scoring**
**File:** [`outputs/research_shortlist.csv`](outputs/research_shortlist.csv)

- **25 companies** evaluated across all 6 Federer criteria
- **21 columns** including:
  - Company basics (name, website, city, segment)
  - 6 criterion scores (C1–C6, each Weak/Moderate/Strong with evidence)
  - Federer Score (0–100)
  - Verdict (Strong fit / Fit / Borderline / Not ICP)
  - Personalization hook (one-line why it's interesting)

**Key Results:**
- **Tier 1 (90+):** 6 companies (Bharat Biotech, Ananth, Indian Immunologicals, Biological E, Cyient DLM, MTAR)
- **Tier 2 (80–89):** 6 companies (Molbio, Virchow, Data Patterns, Avantel, Lazuline, Anthea)
- **Tier 3 (50–79):** 10 companies (Borderline/provisional, including Alkali Metals, Aizant, smaller biotech plays)
- **Tier 4 (<55):** 3 companies (Deliberate rejections: Shantha=acquired, Hetero=too large, Sai Life=service-only)

**Hyderabad Density:** 11 of 25 (44%) have primary ops/R&D in Hyderabad

---

### 2. **Methodology & Scoring Framework**
**File:** [`methodology.md`](methodology.md)

Documents:
- **6 Federer Criteria** with definition and how to assess each
- **Evidence-collection approach** (web scraping, LinkedIn research, company briefs)
- **Scoring scale:** Weak (0–30) / Moderate (31–70) / Strong (71–100)
- **City & segment choice:** Hyderabad (densest cluster) + specialty biotech/diagnostics/defence
- **Data sources:** Provided company list + unicorn dataset + web research

**Updates in this phase:**
- Shifted from generic "technical manufacturing" to focused biotech/diagnostics/defence segments
- Integrated user-provided company list as priority input
- Documented caveats (provisional entries flagged for second-pass verification)

---

### 3. **README & Usage Guide**
**File:** [`outputs/README_SHORTLIST.md`](outputs/README_SHORTLIST.md)

Explains:
- CSV column definitions (21 columns)
- Scoring bands & verdict categories (Tier 1–4)
- Top 6 recommendations (all scoring 90+)
- Hyderabad clustering insight
- Data quality caveats (provisional entries, decision-maker bios to verify)
- Next steps (phone verification, revenue confirmation, M&A tracking)

---

### 4. **Web Scraping & Enrichment Scripts**
**File:** [`scripts/scrape_companies.py`](scripts/scrape_companies.py)

Automated tool to:
- Load a seed CSV of company names and domains
- Fetch homepage titles and descriptions via `fetch_webpage`
- Output enriched JSON with metadata
- **Fix:** Auto-creates output directory (`out_path.parent.mkdir(parents=True, exist_ok=True)`)

**Usage:**
```bash
python3 scripts/scrape_companies.py data/unicorn_seed_candidates.csv outputs/enriched.json
```

---

### 5. **Seed Data**
**File:** [`data/unicorn_seed_candidates.csv`](data/unicorn_seed_candidates.csv)

25 Indian biotech, diagnostics, and defence companies with domains. Used as input to scraper and as foundation for manual deep profiling.

---

## Evidence Levels & Transparency

### **High-Confidence Companies (Tier 1–2: 80+)**
- **Evidence:** Multi-source (company website, news, investor updates, regulatory filings)
- **Examples:** Bharat Biotech (patented HIMAX, WHO-prequalified), Ananth (SPADEX assembly), MTAR (ISRO/NADCAP)
- **Status:** Ready for immediate outreach

### **Borderline/Provisional Companies (Tier 3: 50–79)**
- **Evidence:** Partial or unverified (weak website, user brief, need phone confirmation)
- **Examples:** Pariksha Biotech, Huwel Lifesciences, Bionline Diagnostics
- **Status:** Marked for second-pass verification (phone/LinkedIn outreach)

### **Deliberately Rejected (Tier 4: <55)**
- **Reason:** Fail Federer fit (acquired, too large, service-only, group-owned)
- **Examples:** Shantha Biotechnics (acquired by Sanofi), Hetero (>$1B, not founder-led), Sai Life Sciences (CDMO/CRO service-only)
- **Status:** Demonstrate filtering rigor; excluded from shortlist

---

## How to Use This Shortlist

1. **Immediate Outreach (Tier 1–2):** 12 companies scoring 80+ — strongest evidence, founder-driven, differentiated
2. **Second-Pass Verification (Tier 3):** Phone calls or LinkedIn messages to confirm smaller companies; many will likely upgrade upon direct conversation
3. **Reference Rejections (Tier 4):** Use as negative examples to refine ICP for future profiling exercises
4. **Hyderabad Clustering:** If in-person visits planned, these 11 Hyderabad companies can be visited in one concentrated trip

---

## Methodology Highlights

### **The 6 Federer Criteria**

| Criterion | What It Tests | Evidence Examples |
|-----------|---------------|--------------------|
| **C1: Manufacturer** | In-house production capability | Own facilities, certifications (ISO, FDA, GMP, AS9100D), supply chain control |
| **C2: India-based** | Founder/operational presence | HQ registration, team location, tax filings, founder residency |
| **C3: Differentiated** | Unique product/tech vs. generics | Patents, proprietary platform, market position, first-mover advantage |
| **C4: Technical DM** | Founder/CTO technical depth | Educational background, R&D investment, hands-on involvement in product |
| **C5: Growing sector** | Tailwinds & demand signals | Regulatory approval trends, market adoption, investor interest, TAM growth |
| **C6: Growth signals** | Recent expansion/momentum | New facilities, funding rounds, new certifications, major contracts, partnerships |

### **Scoring Scale**
- **Weak (0–30):** Limited or no evidence; criteria not clearly met
- **Moderate (31–70):** Partial or mixed evidence; criteria partially met
- **Strong (71–100):** Clear, multi-source evidence; criteria strongly met

**Federer Score = Average of 6 criteria** (with optional weight adjustment for critical factors)

---

## Project Repository

**Location:** `/Users/rishi/projects/dp_project/`  
**Remote:** `https://github.com/durgaprasad35/intershala_assignment.git`  
**Branch:** `main`  

**Committed Files:**
- ✅ `outputs/research_shortlist.csv` — Final 25-company shortlist
- ✅ `outputs/README_SHORTLIST.md` — Usage guide & caveats
- ✅ `methodology.md` — Scoring framework & criteria
- ✅ `scripts/scrape_companies.py` — Web scraping tool
- ✅ `data/unicorn_seed_candidates.csv` — Seed data
- ✅ `.gitignore` — Updated to preserve key outputs

**Latest Commit:** `feat: Complete 25-company Federer shortlist with deep profiling` (12fda19)

---

## Next Steps (Optional Post-Submission)

1. **Phone Verification:** Reach out to Tier 3 companies (Pariksha, Huwel, Bionline, etc.) to confirm business model, decision-maker names, and revenue
2. **Founder Interview Loop:** For Tier 1–2 companies, schedule 20-min calls to validate growth signals and technical depth
3. **Market Update Tracking:** Monitor LinkedIn, Crunchbase, and investor updates for M&A, funding, or pivots that change ICP fit
4. **Scale-Up Dataset:** Use this 25-company model to extend to 100–200 companies using automated scoring

---

## Contact & Questions

For questions about methodology, scoring, or company inclusion/exclusion, refer to:
- **Scoring logic:** See `methodology.md` (6 Federer criteria section)
- **Evidence gaps:** See `outputs/README_SHORTLIST.md` (Data Quality & Caveats)
- **Company details:** See `outputs/research_shortlist.csv` (all 6 criteria + evidence columns)

---

**Project Status:** ✅ SUBMISSION READY

All deliverables complete, code pushed to GitHub, and ready for review.
