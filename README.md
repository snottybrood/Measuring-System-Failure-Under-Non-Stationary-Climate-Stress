
## Black Lattice Method: Measuring System Failure Under Non-Stationary Climate Stress

This work focuses on **non-stationary climate conditions** — where historical assumptions no longer hold — and builds methods to measure:

Most climate risk systems are still built on a static question: where might flooding happen? That assumption is breaking. Black Lattice reframes climate risk around a more urgent reality: how often environmental stress is already pushing infrastructure, policy, and communities past their ability to recover. In a non-stationary climate, risk is not a fixed probability; it is a moving threshold of system failure.

This framework translates shifting climate signals into measurable stress and failure dynamics, exposing when traditional risk models underestimate exposure, misprice resilience, and misguide investment. It moves beyond hazard prediction toward system-level vulnerability under real-world change.

The result is a new class of climate intelligence: not just mapping risk, but revealing when systems are quietly exceeding their design limits.

## What This Repository Represents

This is a working body of systems, pipelines, and analyses that explore:

- Climate data as a **system-stress generator** (CORDEX, PRISM, NOAA)
- Spatial data infrastructures as **decision architectures**
- Environmental justice as a **distribution of system failure**
- Data pipelines that translate raw environmental signals into **policy-relevant insight**

Each project here is part of a larger question:

*What happens when reality moves faster than the systems designed to measure it?*

---

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
