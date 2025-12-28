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

