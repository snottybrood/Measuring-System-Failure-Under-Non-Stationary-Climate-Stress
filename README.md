# nonstationary-flood-risk-framework
Replicable workflow linking severe rainfall frequency, flood risk context, and social vulnerability for hazard and equity analysis.
# Severe Storm Frequency → Flood Risk → Vulnerability (Replicable Method)

This repository contains a replicable workflow to quantify how the **frequency of severe rainfall events** is changing over time, where those changes occur, and how they intersect with **social vulnerability** indicators relevant to flood impacts.

It is designed for:
- **Emergency management / hazard mitigation planning** (repeat-impact identification, planning prioritization)
- **Environmental justice analysis** (disproportionate exposure, cumulative harm)
- **Researchers** working on non-stationary extremes and applied risk assessment

## What the workflow produces
For a given region (e.g., counties/watersheds), the workflow can generate:
- Severe rainfall event frequency (historical baseline)
- Frequency change between time intervals (e.g., 1980–2000 vs 2001–2021)
- Expected future frequency through mid-century (method documented in `docs/assumptions-limitations.md`)
- Flood probability context using stream gauge information (illustrative)
- Exposure + vulnerability overlays using census-derived indicators
- Maps and summary tables for decision support

## Key idea (plain language)
Flood impacts worsen when extreme rain becomes **more frequent**, especially where communities have limited recovery capacity.
This workflow connects:
**changing storm frequency → flood risk context → who is repeatedly exposed**.

## Quickstart (runs with sample data)
1. Create environment:
   - Conda:
     ```bash
     conda env create -f environment.yml
     conda activate severe-storm-risk
     ```
   - Or pip:
     ```bash
     pip install -r requirements.txt
     ```

2. Run the sample pipeline:
   ```bash
   bash workflows/run_all.sh --sample

View outputs:

outputs/tables/summary_demo.csv

outputs/maps/ (PNG/GeoPackage demo outputs)

Using real data (PRISM / Census / FEMA / USGS)

See docs/data_dictionary.md and docs/method-card.md.

Note: this repository does not redistribute restricted or large datasets.
Scripts are provided to download and preprocess data where licensing allows.

Assumptions and limitations

This is a risk and exposure workflow, not a deterministic flood hydraulic model.

"Return periods" are treated as non-stationary where appropriate.
See docs/assumptions-limitations.md.

Citation

If you use or adapt this workflow, please cite:
[Your Name] ([Year]). Severe Storm Frequency → Flood Risk → Vulnerability: Replicable Workflow. GitHub repository.
(See CITATION.cff for BibTeX.)

Contact / collaboration

Issues and pull requests welcome. If you're replicating this in a new region, open an issue with:

region and spatial units

storm threshold definition

time intervals of interest


---

## 4) License + citation (do this right)

### License
- If you want maximum reuse: **MIT License**
- If you want reuse but require sharing improvements: **GPL-3.0**
- If you want broad use while protecting name/branding: still MIT, plus a simple disclaimer in README

### Citation
Add a `CITATION.cff` so others can cite you correctly (journals love this).
Include:
- your name
- title
- year
- version
- DOI if you later archive it on Zenodo

---

## 5) What to publish vs what to keep private

### Publish
- full method code
- synthetic/demo data
- county-level outputs that are not sensitive
- clear assumptions and limitations
- replication instructions

### Do NOT publish (unless you explicitly decide)
- anything that could expose personal addresses or vulnerable individuals
- sensitive facility locations (if included)
- any restricted/licensed datasets directly
- anything tied to ongoing workplace/housing legal matters

Public repo should be **cleanly about the method**, not your entire life context.

---

## 6) Your release workflow for Jan 1–Jan 26 (ties to your countdown)

Do it in 3 tiers:

### Tier 1 (Jan 1): “Release 0.1 — Replication-ready sample”
- repo public
- sample pipeline runs
- method-card + glossary included
- outputs generated

### Tier 2 (Jan 8–15): “Release 0.2 — Real-data adapters”
- PRISM download/prep scripts
- Census ingestion scripts
- FEMA flood zone ingestion scripts
- USGS gauge context script

### Tier 3 (Jan 20–26): “Release 1.0 — NCEAS-ready”
- stable API
- documented configs
- reproducibility badges (GitHub Actions)
- Zenodo DOI (optional but powerful)

---

## If you want, I can generate the actual starter files
If you tell me whether you prefer:
- **conda** or **pip**
- and whether your workflow is currently **mostly notebooks** or **a Python script pipeline**

…I’ll draft:
- `environment.yml` / `requirements.txt`
- a `run_all.sh`
- a `config.yaml` pattern
- and a minimal `src/` skeleton that matches your method steps

You can drop your existing code into it instead of reinventing anything.
::contentReference[oaicite:0]{index=0}