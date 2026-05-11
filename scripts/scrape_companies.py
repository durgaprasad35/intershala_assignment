#!/usr/bin/env python3
"""Simple scraper prototype to fetch company homepages and extract basic fields.

Notes:
- This is a helper. It does not bypass site rules. Use responsibly and with API keys where available.
"""
import argparse
import csv
import json
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup


def fetch_url(url, timeout=15):
    try:
        r = requests.get(url, timeout=timeout, headers={"User-Agent": "ResearchBot/1.0"})
        r.raise_for_status()
        return r.text
    except Exception as e:
        print(f"fetch error {url}: {e}")
        return None


def extract_basic(html):
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.string.strip() if soup.title else ""
    # find meta description
    desc = ""
    m = soup.find("meta", attrs={"name": "description"})
    if m and m.get("content"):
        desc = m.get("content").strip()
    return {"title": title, "description": desc}


def load_seeds(seed_file):
    path = Path(seed_file)
    if path.suffix.lower() == ".csv":
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            seeds = []
            for row in reader:
                company = (row.get("Company") or row.get("company") or row.get("name") or "").strip()
                domain = (row.get("Domain") or row.get("domain") or row.get("website") or "").strip()
                if company or domain:
                    seeds.append({"company": company, "domain": domain})
            return seeds

    seeds = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        seeds.append({"company": line, "domain": line})
    return seeds


def main(seed_file, out_json):
    seed = load_seeds(seed_file)
    results = []
    for item in seed:
        company = item.get("company", "")
        q = item.get("domain", "").strip()
        if not q:
            q = company.strip()
        if not q:
            continue
        # try as URL first
        url = q if q.startswith("http") else f"https://{q}"
        html = fetch_url(url)
        if html is None and not q.startswith("http"):
            # try http with www, or search-friendly
            for alt in [f"https://www.{q}", f"http://{q}"]:
                html = fetch_url(alt)
                if html:
                    url = alt
                    break
        data = {"company": company or q, "seed": q, "url": url if html else "", "title": "", "description": ""}
        if html:
            info = extract_basic(html)
            data.update(info)
        results.append(data)
        time.sleep(1)

    out_path = Path(out_json)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(results, indent=2))
    print(f"Wrote {out_json} with {len(results)} entries")


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument("seed_file", help="newline-separated seeds or CSV with Company/Domain columns")
    p.add_argument("out_json", help="output JSON file path")
    args = p.parse_args()
    main(args.seed_file, args.out_json)
