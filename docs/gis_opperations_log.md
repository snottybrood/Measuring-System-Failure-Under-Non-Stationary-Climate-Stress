GIS Operations Log

Census, Flood Hazard, and Exposure Analysis (ArcGIS Pro)

This document records the exact spatial logic and variable-level transformations used to integrate U.S. Census population data with FEMA flood hazard layers for exposure and vulnerability analysis.

The goal is replicability of analytic decisions, not replication of ArcGIS interface steps.

All operations were performed in ArcGIS Pro, but the logic is platform-agnostic and can be reproduced in other GIS environments.

1. Purpose of GIS Operations

The GIS workflow answers the question:

Which populations are repeatedly exposed to flood risk under increasing storm frequency, and how is that exposure distributed across demographic vulnerability indicators?

GIS is used to:

align census population counts with flood hazard polygons

avoid treating population as evenly distributed across space

aggregate exposure metrics to county scale for emergency management and planning relevance

2. Spatial Inputs
2.1 Administrative Boundaries
Census Tracts

Source: U.S. Census Bureau (ACS 5-year)
Geometry unit of analysis: census tract polygons

Key identifier fields:

GEOID (11-digit census tract identifier)

STATEFP

COUNTYFP

TRACTCE

Census tracts serve as the base unit for population variables.

Counties

Purpose: aggregation and reporting unit

County identifiers:

STATEFP

COUNTYFP

COUNTY_NAME

Counties were selected based on high Social Vulnerability Index (SVI) designation and relevance for hazard mitigation planning.

2.2 Flood Hazard Data
FEMA Flood Hazard Areas

Source: Effective FEMA Flood Insurance Rate Map (FIRM) polygons

Key attributes:

FLD_ZONE (e.g., AE, A)

SFHA_FLAG (100-year flood hazard indicator)

Flood hazard zones are used as exposure context, not deterministic inundation boundaries.

3. Tabular Inputs (Census Variables)

Population variables were extracted at the census tract level as raw counts.

All variables are treated as counts, not densities, prior to spatial operations.

Core population fields:

POP_TOTAL

POP_WHITE

POP_BLACK

POP_NATIVE

POP_ASIAN

POP_HISPANIC

Age / disability:

POP_ELDERLY_65UP

POP_DISABLED

Socioeconomic:

POP_BELOW_POVERTY

These variables originate from ACS tables (e.g., B01001, B02001, C18108, C17002) and are standardized into the field names above before spatial processing.

4. Coordinate Reference System & Geometry Preparation

All spatial layers were projected into a common projected coordinate system suitable for area calculations.

Geometry preparation steps:

Invalid geometries repaired

Multipart census tract geometries dissolved by GEOID

One polygon record retained per census tract

Additional geometry fields created:

TRACT_AREA_SQM — total tract area (square meters)

5. Core Spatial Operation: Areal-Weighted Flood Exposure Join
5.1 Rationale

Census population variables represent people, while flood hazard layers represent space.

A direct spatial join would incorrectly assume uniform population distribution within tracts.

To avoid this assumption, an areal-weighted spatial join was applied.

5.2 Areal-Weighted Join Logic

Operation:
Census tract polygons were intersected with FEMA flood hazard polygons.

Steps:

Census tracts intersected with flood hazard polygons

Intersection geometries created for each tract–flood overlap

Intersection area calculated:

FLOOD_INTERSECT_AREA_SQM

Percent overlap calculated as:

FLOOD_AREA_PCT = FLOOD_INTERSECT_AREA_SQM / TRACT_AREA_SQM


Population variables multiplied by FLOOD_AREA_PCT to create areal-weighted exposure estimates

Example:

EXP_POP_TOTAL = POP_TOTAL * FLOOD_AREA_PCT


Weighted values summed back to original census tract GEOID

This produces tract-level estimates of population exposed to flood hazard areas without assuming uniform spatial distribution.

6. Aggregation to County Scale

Areal-weighted tract-level exposure values were aggregated to the county level.

Aggregation rules:

Weighted population fields summed by COUNTYFP

Raw population totals summed separately

Percentages calculated after aggregation, not before

No interpolation beyond areal weighting applied

County-level derived fields:

COUNTY_POP_TOTAL

COUNTY_EXP_POP_TOTAL

PCT_POP_EXPOSED = COUNTY_EXP_POP_TOTAL / COUNTY_POP_TOTAL

Equivalent calculations applied for each demographic subgroup.

County-level aggregation was chosen because:

counties align with emergency management and hazard mitigation planning

counties match funding and reporting frameworks

county-scale results support comparability across jurisdictions

7. Output Products
7.1 Intermediate Outputs (Tract Level)

Exported table includes:

GEOID

TRACT_AREA_SQM

FLOOD_INTERSECT_AREA_SQM

FLOOD_AREA_PCT

Raw population fields (POP_*)

Areal-weighted exposure fields (EXP_POP_*)

FLD_ZONE

These tables are exported to CSV to enable replication without ArcGIS.

7.2 Final Outputs (County Level)

County-level exposure tables include:

Percent population in flood hazard zones

Demographic exposure metrics

SVI context fields where applicable (SVI_RANK, SVI_THEME)

Spatial layers are also produced for mapping and visualization.

8. Interpretation Notes & Limitations

Flood hazard zones provide context, not event-specific predictions

Exposure estimates reflect potential repeated risk, not inundation depth

Areal weighting is a conservative approximation and may under- or over-estimate exposure in heterogeneous tracts

Results should be interpreted alongside storm frequency analysis and river gauge context

9. Replication Notes

This workflow can be replicated using:

QGIS (intersection + field calculations)

Python (GeoPandas overlay + area-weighted aggregation)

Key requirements for replication:

preserve areal-weighted logic

preserve aggregation order

maintain separation between hazard context and population vulnerability

10. Ethical Use Statement

This analysis is intended to support:

equitable disaster preparedness

risk-informed planning

identification of communities facing cumulative hazard exposure

It should not be used to:

deny assistance

stigmatize communities

replace local knowledge or community engagement

End of GIS Operations Log