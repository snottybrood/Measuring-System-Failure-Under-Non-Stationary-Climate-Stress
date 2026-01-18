Non-Stationary Flood Risk Framework

A replicable workflow linking severe rainfall frequency, flood risk context, and social vulnerability for hazard and equity analysis.

Overview

This repository provides a transparent, reproducible workflow for quantifying how the frequency of severe rainfall events is changing over time, where those changes are occurring, and how they intersect with social vulnerability relevant to flood impacts.

Rather than relying on stationary return periods, the framework focuses on observed and projected changes in event frequency, preserving empirical clarity while supporting applied risk analysis.

Who this is for

This workflow is designed for:

Emergency management & hazard mitigation
(repeat-impact identification, prioritization, planning support)

Environmental justice analysis
(disproportionate exposure, cumulative and repeated harm)

Researchers & practitioners
working on non-stationary extremes, climate impacts, and applied risk assessment

Core idea

Flood impacts intensify when extreme rainfall becomes more frequent, especially in places with limited recovery capacity.

This framework explicitly links:

Changing storm frequency → flood risk context → repeated exposure of vulnerable communities

What the workflow produces

For a given region (e.g., county, watershed, or gridded domain), the workflow can generate:

Observed severe rainfall frequency (PRISM-based baseline)

Frequency change across historical epochs
(e.g., early vs. late observed periods)

Projected future frequency change using CORDEX regional climate model output
(frequency only; no return-period fitting)

Flood probability context using stream gauge–derived indicators (illustrative)

Exposure and vulnerability overlays using census-derived metrics

Tables and maps suitable for analysis, reporting, and decision support

Repository structure
nonstationary-flood-risk-framework/
├── notebooks/
│   ├── 00_overview.ipynb
│   ├── 01_prism_precip_ingest.ipynb
│   ├── 02_prism_extremes_analysis.ipynb
│   ├── 03_epoch_comparison.ipynb
│   ├── 04_cordex_future_frequency.ipynb
│   ├── 05_exposure_vulnerability.ipynb
│   └── 06_flood_probability_context.ipynb
├── data/
│   ├── raw/        # user-provided datasets (not redistributed)
│   └── sample/     # lightweight demo inputs
├── outputs/
│   ├── tables/
│   └── maps/
├── docs/
│   ├── method-card.md
│   ├── data_dictionary.md
│   └── assumptions-limitations.md
├── environment.yml
├── requirements.txt
└── CITATION.cff

Quickstart (runs with sample data)
1. Create the environment

Conda

conda env create -f environment.yml
conda activate severe-storm-risk


or pip

pip install -r requirements.txt

2. Run the notebooks

Start with:

notebooks/00_overview.ipynb


Then proceed sequentially through the numbered notebooks.
Each notebook writes outputs to outputs/ and includes explicit continuity notes for downstream steps.

Sample data in data/sample/ allows the full workflow to run without downloading restricted datasets.

Using real data (PRISM, CORDEX, Census, USGS)

This repository does not redistribute restricted or large datasets.

Scripts and notebooks are provided to ingest and preprocess data where licensing permits.

See:

docs/data_dictionary.md

docs/method-card.md

docs/assumptions-limitations.md

Assumptions and limitations

This is a risk and exposure framework, not a deterministic hydraulic flood model.

Extreme rainfall is analyzed using fixed thresholds and event frequency, not stationary return periods.

Flood probability metrics are contextual, not predictive.

Details are documented in docs/assumptions-limitations.md.

Citation

Cartographic and visualization approaches build on long-standing Python geospatial practices.
Basemap documentation informed projection explanations; implementation uses Cartopy.

If you use or adapt this work, please cite:

Bates Norris, Zed. (2026). Non-Stationary Flood Risk Framework. GitHub repository.
See CITATION.cff for BibTeX.

Contact & collaboration

Issues and pull requests are welcome.

If you are replicating this framework in a new region, please include:

Region and spatial unit(s)

Extreme rainfall threshold definition

Time windows of interest