# Epoch-Based Comparison of Extreme Rainfall Frequency

## Purpose
This analysis evaluates how the frequency of extreme rainfall events has changed across distinct historical periods (“epochs”), rather than assuming long-term stationarity.

Instead of treating precipitation extremes as rare and statistically stable, this approach explicitly compares event counts across time windows to identify frequency shifts already underway.

---

## Method Overview
Using daily precipitation data derived from PRISM:

1. Extreme rainfall events are defined using a fixed threshold (e.g., ≥ 3 inches in 24 hours).
2. Events are counted annually for each county.
3. Annual counts are aggregated into multi-year epochs (e.g., 1980–2000 vs. 2001–2021).
4. Differences and percent change in event frequency are calculated between epochs.

This approach preserves comparability while allowing frequency to evolve over time.

---

## Why Epoch Comparison Matters
Traditional return-period metrics assume that the probability of extreme events is stationary. Epoch-based comparison avoids this assumption and instead asks:

- Are extreme rainfall events becoming more frequent?
- How quickly is that change occurring?
- What does that imply for planning based on historical baselines?

This framing is particularly relevant for emergency management and infrastructure planning, where repeated exposure—not single extremes—drives risk.

---

## Outputs
- Event counts per epoch
- Percent change in extreme rainfall frequency
- Tables used as inputs to flood context and vulnerability analyses

---

## Interpretation Notes
- This analysis evaluates **frequency**, not magnitude.
- Thresholds are held constant across time to isolate temporal change.
- Results should be interpreted as indicators of increasing hazard pressure, not precise forecasts.
