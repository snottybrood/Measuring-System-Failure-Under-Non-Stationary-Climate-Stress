# Projected Changes in Extreme Rainfall Frequency (CORDEX)

## Purpose
This analysis estimates how the frequency of extreme precipitation events may change under future climate conditions using CORDEX regional climate model output.

The focus is on **event frequency**, not storm intensity or total precipitation.

---

## Data Source
- CORDEX North America regional climate simulations
- Daily precipitation output
- Selected emissions scenario (e.g., RCP8.5)
- Model: MPI-ESM-LR (WRF downscaling)

---

## Method Overview
1. Daily precipitation data are subset spatially to the study region.
2. Extreme events are defined using a fixed precipitation threshold consistent with historical analysis.
3. Binary exceedance (event / no event) is calculated for each day.
4. Event counts are summed across two future periods:
   - Early future (e.g., 2021–2050)
   - Late future (e.g., 2051–2080)
5. Differences in event frequency are calculated between periods.

---

## Consistency with Historical Analysis
Threshold definitions and frequency logic are intentionally aligned with PRISM-based historical analysis to support comparability between observed and projected changes.

---

## Outputs
- Spatial maps showing change in extreme rainfall frequency
- Difference fields highlighting areas of increasing event counts
- Inputs for downstream flood context interpretation

---

## Interpretation Notes
- Results reflect modeled frequency change, not deterministic forecasts.
- Differences should be interpreted as **directional risk signals**.
- Uncertainty varies across models and regions.

This analysis is intended to inform planning discussions, not replace ensemble-based climate assessments.
