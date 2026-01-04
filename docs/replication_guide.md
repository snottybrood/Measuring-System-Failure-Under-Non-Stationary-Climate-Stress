# Replication Guide  
Non-Stationary Flood Risk Framework

This guide describes how to replicate the analytical workflow used in this project.  
The emphasis is on **replicating analytic decisions and logic**, not reproducing identical software steps.

The framework is modular and can be implemented using ArcGIS Pro, QGIS, Python (GeoPandas / xarray), or equivalent GIS and data-analysis tools.

---

## 1. Overview of the Replication Workflow

The workflow consists of five core modules:

1. Historical extreme rainfall frequency analysis (PRISM)
2. Epoch-based comparison of observed frequency change
3. Future frequency projections (CORDEX or equivalent climate models)
4. Flood hazard context interpretation (e.g., FEMA flood zones, river gauges)
5. Population exposure and vulnerability analysis (census + GIS)

Each module can be replicated independently, but full interpretation relies on their integration.

---

## 2. Required Inputs

### 2.1 Climate Data

**Historical precipitation**
- Daily precipitation time series (e.g., PRISM)
- Spatial unit: county or grid subset covering the study region
- Temporal coverage sufficient to support multi-decade comparison

**Future precipitation (optional but recommended)**
- Daily precipitation output from regional climate models (e.g., CORDEX)
- Consistent units and temporal resolution with historical analysis

---

### 2.2 Spatial Data

- Census tract boundaries (ACS 5-year geometry)
- County boundaries
- Flood hazard polygons (e.g., FEMA FIRM)
- Optional: river gauge locations or riverine context layers

All spatial layers must be projected into a **common projected coordinate reference system** suitable for area calculations.

---

### 2.3 Census and Demographic Data

- ACS 5-year population tables at the census tract level
- Variables should be extracted as **counts**, not percentages

Minimum recommended variables:
- Total population
- Race / ethnicity
- Age (65+)
- Disability status
- Poverty or income indicator

---

## 3. Module Replication Steps

---

### 3.1 Historical Extreme Rainfall Frequency (PRISM)

**Objective:**  
Quantify how often extreme rainfall events occur over time.

**Key steps:**
1. Define an extreme rainfall threshold (e.g., ≥ 3 inches in 24 hours)
2. Convert daily precipitation to a binary exceedance indicator
3. Count exceedance events annually
4. Store annual event counts for later comparison

**Critical requirement:**  
The threshold definition must remain **constant across time**.

---

### 3.2 Epoch-Based Comparison

**Objective:**  
Identify changes in extreme rainfall frequency without assuming stationarity.

**Key steps:**
1. Define two or more historical time windows (“epochs”)
2. Aggregate annual event counts within each epoch
3. Calculate differences and percent change between epochs

**Interpretation note:**  
This step evaluates **frequency change**, not magnitude or intensity.

---

### 3.3 Future Frequency Analysis (CORDEX or Equivalent)

**Objective:**  
Assess how extreme rainfall frequency may change under future climate conditions.

**Key steps:**
1. Apply the same threshold logic used in historical analysis
2. Convert daily precipitation to exceedance indicators
3. Aggregate exceedances over defined future periods
4. Calculate differences between early- and late-future periods

**Important:**  
Results should be interpreted as **directional risk signals**, not deterministic forecasts.

---

### 3.4 Flood Hazard Context Integration

**Objective:**  
Provide spatial context for how frequency increases translate into flood risk.

**Key steps:**
1. Identify relevant flood hazard layers (e.g., FEMA SFHA polygons)
2. Treat hazard layers as **context**, not predictions
3. Use flood zones to locate where increased storm frequency is most likely to matter

This module does not perform hydraulic or inundation modeling.

---

### 3.5 Population Exposure & Vulnerability Analysis (GIS)

**Objective:**  
Estimate which populations are potentially exposed to flood hazard areas.

**Required logic:**  
An **areal-weighted spatial join** must be used.

**Steps:**
1. Intersect census tracts with flood hazard polygons
2. Calculate intersection area and percent overlap
3. Multiply population counts by percent overlap
4. Sum weighted values back to original tract GEOIDs
5. Aggregate tract-level exposure to county scale
6. Calculate percentages **after aggregation**

This avoids assuming uniform population distribution.

---

## 4. Required Outputs

### Intermediate Outputs (Tract Level)
- Raw population counts
- Areal-weighted exposed population estimates
- Flood area overlap metrics

### Final Outputs (County Level)
- Percent population exposed to flood hazard areas
- Demographic exposure metrics
- Tables suitable for planning and reporting

All intermediate tables should be exported to non-proprietary formats (e.g., CSV) to enable replication without specific software licenses.

---

## 5. Validation and Sensitivity Checks

Replicators are encouraged to:
- test alternate rainfall thresholds
- vary epoch boundaries
- compare results across multiple climate models
- assess sensitivity to spatial resolution

Such variations should preserve the **core analytic logic**.

---

## 6. Ethical and Responsible Replication

This framework is intended to support:
- equitable disaster preparedness
- risk-informed planning
- transparency in climate risk assessment

Replicated analyses should:
- clearly document assumptions
- avoid overstating precision
- be interpreted alongside local knowledge and expertise

---

## 7. What Replication Does *Not* Require

- Identical software tools
- Identical datasets
- Exact numerical agreement

Replication requires **conceptual fidelity**, not numerical duplication.

---

## 8. Summary

Replication of this framework depends on:
- consistent definition of extreme events
- preservation of areal-weighted exposure logic
- clear separation between hazard context and vulnerability metrics
- transparent documentation of assumptions

When these conditions are met, the framework can be adapted to new regions, datasets, and decision contexts.

---

**End of Replication Guide**
