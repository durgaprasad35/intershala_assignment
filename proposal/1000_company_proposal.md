# 1000-Company Scale-Up Proposal — DeepThought ICP

Summary

Goal: Build a vetted list of 1000 Federer-profile companies across India in 1 month, using automated data pipelines and staged human verification to keep quality high.

Sources for initial universe
- LinkedIn Sales Navigator queries (location + segment keywords)
- MCA / Tofler company lists for revenue and ownership
- Industry directories (IndiaMART, TradeIndia) filtered for manufacturers
- Export registries and customs (DGFT export data) for exporters
- Trade association membership lists (CHEMEXCIL, Indian Chemical Council)

Automation and qualification flow
1. Bulk acquisition: run parallel LinkedIn & directory queries, harvest company names/domains.
2. Auto-enrichment: for each company, fetch website, LinkedIn page, MCA summary via APIs or scraping, and run regex/heuristics to tag evidence (plant, R&D, patents, certifications).
3. Rule-based scoring: auto-assign Weak/Moderate/Strong for each criterion using presence signals (e.g., presence of "plant", "manufacturing", certification codes, founder education keywords).
4. Human QC: triage borderline and top candidates (top 25% by score) with manual verification by a researcher.

Quality control
- Use conservative heuristics to avoid false positives (e.g., require explicit mention of a manufacturing plant on website for C1 strong).
- Random sampling: daily manual checks of 5% of auto-passed companies.
- Track provenance for every data point (URL + quote snippet).

Weekly plan
- Week 1: Build pipelines, obtain access (LinkedIn/Databases), run initial queries to collect 10k candidate names. Build enrichment scripts.
- Week 2: Auto-enrich top 5k candidates, run scoring, produce shortlist of ~1500. Start human QC on top 500.
- Week 3: Complete QC for top 1500 -> finalize 1000. Start detailed profiling for top 200 (evidence capture).
- Week 4: Final verification, create CSV + outreach-ready notes for top 100, hand over to sales ops.

Expected yields
- Raw to candidate: 10k harvested
- After enrichment + rules: 1,500 qualified
- After manual QC: 1,000 final ICP-qualified

Tooling and resource needs
- Licences: LinkedIn Sales Navigator, API credits for data enrichment (Clearbit/FullContact), access to MCA/Tofler.
- Team: 2 researchers + 1 automation engineer + overseer (you).
- Infrastructure: basic AWS instance for scraping and DB, or use managed data platform.
