# Method Card (Plain Language)

What this method answers

This workflow is designed to answer three practical questions:

How is severe rainfall frequency changing over time?
It measures how often extreme rainfall events occur, using a consistent definition applied across historical and future periods.

Where are those changes occurring?
Results can be summarized by counties, watersheds, or other regions to identify spatial patterns in changing storm frequency.

Who is repeatedly exposed to flood risk as conditions change?
Frequency changes are interpreted alongside flood hazard context and social vulnerability indicators to highlight communities facing cumulative or repeated exposure.

What makes this approach different

It focuses on event frequency, not storm intensity or stationary return periods.

A fixed threshold is used to detect change without assuming the climate is stable.

Observed data, projections, and vulnerability indicators are kept modular and transparent, so each step can be inspected or reused independently.

This makes the workflow suitable for planning and equity analysis, not just academic modeling.

Inputs

Depending on the module being run, the workflow may use:

PRISM daily precipitation data
(observed rainfall used to establish historical frequency)

Regional climate model output (CORDEX)
(used to estimate future changes in frequency)

FEMA flood hazard layers
(to provide flood risk context, not deterministic prediction)

USGS stream gauge data
(to contextualize flooding and hydrologic response)

Census / ACS indicators
(to represent social vulnerability and exposure)

Note: This repository does not redistribute restricted datasets. Users supply or download data according to licensing rules.

Outputs

The workflow produces:

Severe rainfall frequency tables and maps

Epoch-based change summaries
(e.g., earlier vs. later historical periods)

Future frequency change estimates
(based on model output, documented assumptions)

Exposure and vulnerability overlays

Summary tables suitable for:

hazard mitigation planning

environmental justice analysis

communication with decision-makers

How results should be interpreted

Results describe changes in how often extreme rain occurs, not precise flood depths or damages.

Flood layers and stream gauges provide context, not deterministic forecasts.

Percent change values should be interpreted alongside absolute counts, especially where events are rare.

What this method is (and is not)

This method is:

A transparent, replicable way to analyze non-stationary rainfall risk

Designed for planning, comparison, and prioritization

This method is not:

A hydraulic flood model

A damage or loss estimation tool

A replacement for site-specific engineering analysis