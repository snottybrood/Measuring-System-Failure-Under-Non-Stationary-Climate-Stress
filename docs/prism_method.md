PRISM Observed Extreme Rainfall Frequency — Method Overview

# PRISM Observed Extreme Rainfall Frequency  
## Method Overview (Module 1: Observed Reality)

This module documents a transparent, replicable method for assessing **how the frequency of severe rainfall has already changed**, using observed precipitation data from the PRISM Climate Group.

The purpose of this module is not to predict future flooding, but to establish a clear, inspectable baseline of **what is already happening** in the historical record.

---

## 1. What Question Does This Method Answer?

This workflow answers a simple but consequential question:

**Are extreme rainfall events occurring more frequently than they did in the past?**

Rather than asking how large individual storms are, the method focuses on **how often severe rainfall occurs**, because frequency changes directly affect flood risk, recovery time, and cumulative exposure.

---

## 2. Why Focus on Frequency (Not Intensity)?

Many climate analyses emphasize storm intensity or modeled return periods. This method instead focuses on **event frequency**, for three reasons:

- Flood risk increases when storms happen more often, even if intensity stays constant.
- Infrastructure and communities are stressed by reduced recovery time between events.
- Frequency can be measured directly from observations without fitting probabilistic models.

This approach avoids assuming that historical stationarity still holds.

---

## 3. Data Source: PRISM Precipitation

Observed daily precipitation data are sourced from the **PRISM Climate Group**, which provides gridded climate observations based on station data, topography, and interpolation methods.

This module does **not** redistribute PRISM data.  
Users are responsible for downloading and using PRISM data in accordance with PRISM data use policies.

---

## 4. Defining an “Extreme” Rainfall Event

An extreme rainfall event is defined using a **fixed daily precipitation threshold**:

- **≥ 3.0 inches (76.2 mm) in 24 hours**

This threshold is applied **consistently across all years** in the analysis.

Using a fixed threshold ensures that changes in frequency reflect changes in observed rainfall behavior, not changes in definitions or statistical fitting.

Users may adjust the threshold for local context, but comparisons should always use a single fixed value.

---

## 5. Event Identification and Annual Counts

Daily precipitation time series are processed as follows:

1. Each day is classified as either:
   - an extreme event (threshold exceeded), or
   - a non-event
2. Extreme events are counted **annually**
3. The result is a time series of **annual extreme rainfall frequency**

No smoothing, trend fitting, or return-period modeling is applied at this stage.

---

## 6. Epoch-Based Comparison (Non-Stationary Framing)

To evaluate change over time without assuming stationarity, annual event counts are grouped into **multi-year historical windows (“epochs”)**, such as:

- 1980–2000  
- 2001–2021  

For each epoch, total extreme-event counts are calculated and compared.

Change is expressed as:
- absolute difference in event counts
- percent change relative to the earlier epoch

This approach mirrors the logic used in the original thesis analysis and avoids imposing parametric trend assumptions.

---

## 7. What This Method Does *Not* Do

This module does **not**:

- predict future rainfall or flooding
- model inundation extent
- fit statistical return periods
- claim causality for individual events
- account for river hydraulics or land-use change

Those questions are addressed in later modules using different data and methods.

---

## 8. Why This Module Comes First

Before discussing projections or impacts, it is essential to establish whether the observed climate signal itself has changed.

This module provides that foundation by making the observed frequency signal:
- transparent
- replicable
- open to scrutiny

If the observed signal cannot be agreed upon, downstream risk conversations lack a shared empirical basis.

---

## 9. Replication and Adaptation

This workflow can be replicated for other regions by:

1. Downloading PRISM daily precipitation data for the region of interest
2. Applying the same fixed extreme-event threshold
3. Aggregating events annually
4. Comparing event frequency across historical epochs

Sample data and runnable notebooks are provided in this repository to support replication and testing.

---

## 10. Ethical Use Note

This analysis is intended to support:
- risk-informed planning
- emergency management preparedness
- environmental justice and equity analysis

It should not be used to:
- deny assistance
- downplay lived experience
- replace local knowledge or engagement

Observed data is a starting point for conversation, not the final word.
