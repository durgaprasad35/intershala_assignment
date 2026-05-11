# 25-Company Deep-Profile Shortlist: Federer Scoring Results

## Overview

**File:** `research_shortlist.csv`  
**Total Companies:** 25  
**Scope:** Hyderabad-focused (with broader Indian presence); specialty biotech, diagnostics, and defence/electronics manufacturing  
**Methodology:** 6-criteria Federer model with evidence-based scoring  
**Date Generated:** 2025  

---

## CSV Column Definitions

| Column | Description |
|--------|-------------|
| **Company name** | Full legal name of company |
| **Website** | Primary domain or relevant web property |
| **City/Location** | Primary operational hub (Hyderabad = dense cluster focus) |
| **Segment** | Sector focus (Specialty Biotech, Diagnostics, Defence Electronics, etc.) |
| **Product description** | Core product/capability in 1–2 sentences |
| **Revenue band estimate** | Estimated annual turnover (INR crores or USD range) |
| **Decision-maker** | Name;Title;Background (where available; marked "TBV" if to be verified) |
| **C1 - Manufacturer** | Score (Weak/Moderate/Strong) + evidence snippet |
| **C2 - India-based** | Score (Weak/Moderate/Strong) + evidence snippet |
| **C3 - Differentiated** | Score (Weak/Moderate/Strong) + evidence snippet (unique tech, patents, market position) |
| **C4 - Technical DM** | Score (Weak/Moderate/Strong) + evidence snippet (founder background, technical depth) |
| **C5 - Growing sector** | Score (Weak/Moderate/Strong) + evidence snippet (sector tailwinds, demand signals) |
| **C6 - Growth signals** | Score (Weak/Moderate/Strong) + evidence snippet (recent expansions, funding, certifications, new contracts) |
| **Federer Score** | Overall 0–100 numeric score |
| **Verdict** | Fit category (see below) |
| **Personalization hook** | One-line why this company is interesting for your use case |

---

## Scoring Bands & Verdict Categories

### **Tier 1: Strong Fit (90+)**
- **6 companies** scored 90–100
- Criteria: Clear evidence across all 6 dimensions; strong web presence; recent growth signals
- Examples: Bharat Biotech (100), Ananth Technologies (100), Indian Immunologicals (98)
- **Verdict:** "Strong fit"

### **Tier 2: Good Fit (80–89)**
- **6 companies** scored 80–89
- Criteria: 5–6 criteria met; some minor evidence gaps (e.g., decision-maker bio TBV)
- Examples: Molbio Diagnostics (90), Virchow Biotech (82), Data Patterns India (82)
- **Verdict:** "Fit"

### **Tier 3: Borderline (50–79)**
- **10 companies** scored 50–79
- Criteria: 3–5 criteria met; provisional or off-segment; web presence weak or needs verification
- Subcategories:
  - **Borderline - Provisional:** Small biotech plays with unverified websites; included pending second-pass confirmation (e.g., Pariksha Biotech, Huwel Lifesciences, ABR Organics)
  - **Borderline - Service-Heavy:** Technical capability present but >50% revenue from services, not products (e.g., Aizant, Sai Life Sciences)
  - **Borderline - Off-Segment:** Manufacturing excellence but outside core biotech/diagnostics (e.g., Alkali Metals, Sai Deepa Rock Drills)
- **Verdict:** Displayed as "Borderline - [reason]"

### **Tier 4: Not ICP (18–55)**
- **3 companies** scored ≤55 and explicitly excluded
- Reason: Fail on key Federer criteria (acquired, too large, group-owned, service-only)
- Examples:
  - **Shantha Biotechnics (18):** Acquired by Sanofi; lost founder-driven status
  - **Hetero (55):** Too large (>$1B), not founder-led, generic pharma
  - **Sai Life Sciences (35):** CDMO/CRO service-only; no differentiated product
- **Verdict:** "Not ICP - [specific reason]"

---

## Key Findings

### **Top Recommendations (Federer 90+)**

1. **Bharat Biotech** (100) — Patented HIMAX platform, 4 manufacturing sites, WHO-prequalified vaccines globally
2. **Ananth Technologies** (100) — 30+ years, assembled SPADEX satellite, ISRO/defence contracts, founder-driven
3. **Indian Immunologicals** (98) — 150+ registered products, 1st Indian tissue-culture rabies vaccine, deep rural footprint
4. **Biological E** (95) — First Indian private vaccine company, 7 WHO-prequalified products, 2B+ doses supplied
5. **Cyient DLM** (93) — Thales/Boeing contracts, AS9100D certified, new precision manufacturing facility
6. **MTAR Technologies** (92) — 30 years with ISRO, AS9100D/NADCAP certified, space/defence focus

### **Hyderabad Density:**
- **11 of 25** companies have primary operations or R&D in Hyderabad (44%)
- Includes: Bharat Biotech, Biological E, Indian Immunologicals, Ananth, Cyient DLM, Data Patterns, Molbio, Alkali Metals, Avantel, and others
- **Justification:** Hyderabad is India's densest cluster for vaccine manufacturing, diagnostics, and defence electronics

### **Provisional & Borderline Entries:**
- **10 companies (40%)** flagged as "Borderline" or "Provisional" due to:
  - Minimal web presence (e.g., Pariksha Biotech, Huwel Lifesciences)
  - Service-heavy business model (Aizant, Sai Life Sciences)
  - Off-segment but technically strong (Alkali Metals, Sai Deepa Rock Drills)
- **Recommendation:** Conduct second-pass phone/LinkedIn verification for these; some may upgrade to "Fit" tier

---

## Data Quality & Caveats

### **Evidence Collection Method:**
- **Primary:** `fetch_webpage` tool to extract company homepages, facilities descriptions, and news items
- **Secondary:** Terminal `curl` with browser user-agents for sites blocking automated access
- **Fallback:** User-provided company briefs and assignment context (for companies with minimal web presence)

### **Known Gaps:**
- **Decision-maker bios:** ~10 companies marked "TBV" (to be verified); executive names/backgrounds require LinkedIn or direct outreach verification
- **Revenue estimates:** Band-based (INR crores or USD range); exact 2024–2025 figures not available for all companies
- **Small biotech validation:** Smaller companies (Pariksha, Huwel, Chrogene) have unverified or non-responsive websites; marked "Borderline - Provisional"

### **Strengths:**
- Clear separation of high-confidence (Tier 1–2) from provisional entries
- Deliberate inclusion of "fail cases" (Shantha, Hetero, Sai Life) demonstrates filtering rigor
- Multi-source evidence for major companies (Bharat Biotech, Ananth, MTAR, etc.)

---

## How to Use This Shortlist

1. **Immediate Outreach (Tier 1–2):** Start with 12 companies scoring 80+ — these have strongest evidence and founder-driven focus
2. **Second-Pass Verification (Tier 3):** Assign phone calls or LinkedIn outreach to verify smaller Tier 3 companies; many will likely upgrade upon direct conversation
3. **Rejected Cases (Tier 4):** Use as negative examples; document why (acquired, service-heavy, too large) to refine ICP definition for future exercises
4. **Hyderabad Clustering:** If logistics/visits are planned, these 11 Hyderabad-based companies can be visited/interviewed in concentrated trip

---

## Next Steps

- [ ] Phone/LinkedIn verification of decision-makers for Tier 3 companies
- [ ] Confirm revenue bands via investor updates or founder interviews
- [ ] Document any founder pivots or recent M&A that changes ICP fit
- [ ] Prepare 2–3 personalized outreach messages per Tier 1 company

---

**Project Repository:** `dp_project/`  
**Output File:** `outputs/research_shortlist.csv`  
**Methodology File:** `methodology.md`  
