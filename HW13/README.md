# HW14 — ARIA v9.5: The Resilience Monitor

**Course:** NTU Remote Sensing & Spatial Information Analysis  
**Instructor:** Prof. Su Wen-Ray  
**Student:** Yen-Ni Hou  
**Assignment:** Week 14 Homework  
**Topic:** Landsat Multi-Decadal Trend Analysis & Resilience Assessment in Xiulin / Taroko, Taiwan

---

# Overview

This homework upgrades the ARIA framework from **v9.0** to **v9.5 — The Resilience Monitor**, extending the temporal analysis window from **6 years (Sentinel-2)** to **26 years (Landsat 5/7/8/9)**.

The objective is to investigate long-term environmental change, ecosystem resilience, and urban landscape transformation through:

- Landsat multi-mission harmonization
- Long-term vegetation trend analysis
- Pixel-level greening/browning detection
- Taoyuan pond disappearance monitoring
- Post-earthquake vegetation resilience assessment
- Cross-sensor comparison between Landsat and Sentinel-2

---

# Study Areas

## 1. Xiulin / Taroko (Hualien, Taiwan)

Primary study area for:

- NDVI long-term trend analysis
- Pixel-level greening/browning mapping
- Vegetation resilience assessment
- Multi-index dashboard analysis
- Cross-sensor comparison

### Temporal Range

| Dataset | Time Range |
|----------|------------|
| Landsat | 2000–2026 |
| Sentinel-2 | 2018–2026 |

---

## 2. Taoyuan Plateau

Secondary study area for:

- MNDWI-based water monitoring
- Pond disappearance analysis
- Urban flood resilience assessment

---

# Data Sources

## Landsat Collection 2 Level 2

| Sensor | Collection |
|----------|------------|
| Landsat 5 TM | LANDSAT/LT05/C02/T1_L2 |
| Landsat 7 ETM+ | LANDSAT/LE07/C02/T1_L2 |
| Landsat 8 OLI | LANDSAT/LC08/C02/T1_L2 |
| Landsat 9 OLI-2 | LANDSAT/LC09/C02/T1_L2 |

### Processing

- Band harmonization
- Surface reflectance scaling
- QA_PIXEL cloud masking
- Annual median composites

---

## Sentinel-2

Collection:

```text
COPERNICUS/S2_SR_HARMONIZED
```

Used for:

- Cross-sensor comparison
- Earthquake damage hotspot inspection
- True-color visualization

---

# Workflow

```text
Task 1
Landsat Harmonization
      ↓
26-Year NDVI Time Series
      ↓
Task 2
Pixel-Level Trend Analysis
      ↓
Greening / Browning Mapping
      ↓
Task 3
Taoyuan Pond Disappearance
      ↓
Water Frequency Analysis
      ↓
Task 4
Vegetation Resilience Metrics
      ↓
Recovery Ratio Assessment
      ↓
Bonus Analyses
```

---

# Task 1 — Landsat Harmonization + 26-Year NDVI Trend

## Objectives

- Harmonize Landsat 5/7/8/9 spectral bands
- Build annual NDVI time series (2000–2026)
- Detect long-term vegetation changes

## Outputs

- Annual NDVI statistics CSV
- 26-year NDVI trend plot
- Long-term trend analysis report

## Key Findings

- Overall greening trend observed
- NDVI trend:

```text
+0.00279 NDVI/year
```

- Total increase:

```text
+0.0725 NDVI
```

- 2024 earthquake impact visible but does not overturn the long-term greening trajectory

---

# Task 2 — Pixel-Level Linear Trend Analysis

## Objectives

- Perform pixel-level NDVI regression
- Identify greening and browning areas
- Compare long-term and short-term trends

## Method

```text
NDVI = slope × time + offset
```

using:

```python
ee.Reducer.linearFit()
```

## Results

| Class | Area (km²) | Percentage |
|---------|---------:|-----------:|
| Greening | 1466.90 | 82.67% |
| Browning | 83.79 | 4.72% |
| Stable | 224.60 | 12.66% |

## Outputs

- NDVI slope map
- Trend class map
- GeoTIFF export
- Trend statistics

---

# Task 3 — Taoyuan Pond Disappearance Analysis

## Objectives

- Detect historical pond loss
- Quantify urbanization impacts
- Evaluate flood resilience implications

## Indicator

### MNDWI

```text
MNDWI = (Green − SWIR1) / (Green + SWIR1)
```

Water threshold:

```text
MNDWI > 0.1
```

## Results

| Category | Area (ha) |
|-----------|----------:|
| Lost ponds | 385.67 |
| New water | 56.18 |
| Stable water | 4476.08 |
| Net change | -329.48 |

## Validation

223 known pond locations:

| Metric | Value |
|----------|------:|
| Detected ponds | 173 |
| Detection rate | 91.53% |

## Outputs

- Water frequency map
- Pond change map
- Validation statistics
- Flood resilience discussion

---

# Task 4 — Vegetation Resilience Assessment

## Objectives

Assess ecosystem recovery after the 2024 Hualien Earthquake.

### Periods

| Period | Date |
|----------|------------|
| Baseline | 2020–2024/03 |
| Impact | 2024/04–2024/12 |
| Recovery | 2025/06–2026/03 |

---

## Recovery Ratio

```text
Recovery Ratio =
(Recovery − Impact)
/
(Baseline − Impact)
```

### Interpretation

| Value | Meaning |
|---------|---------|
| >1 | Exceeded baseline |
| =1 | Full recovery |
| 0–1 | Partial recovery |
| 0 | No recovery |
| <0 | Continued degradation |

---

## Results

| Class | Percentage |
|---------|-----------:|
| Continued degradation | 20.13% |
| Slow recovery | 37.44% |
| Recovering | 23.75% |
| Exceeded baseline | 18.68% |

## Outputs

- Recovery ratio map
- Recovery class map
- Recovery statistics
- Integration summary report

---

# Bonus 1 — Multi-Index Dashboard

## Indicators

- NDVI
- MNDWI
- NBR

## Purpose

Compare vegetation, hydrological, and disturbance signals across 26 years.

## Outputs

- Multi-panel dashboard
- Trend analysis report

---

# Bonus 2 — NDVI Time-Lapse Animation

## Objective

Visualize vegetation evolution from 2000–2026.

## Output

```text
bonus2_taroko_ndvi_26yr_timelapse.gif
```

### Key Events

- Typhoon Morakot (2009)
- Hualien Earthquake (2024)
- Post-earthquake recovery (2025–2026)

---

# Bonus 3 — Landsat × Sentinel-2 Cross-Sensor Analysis

## Objectives

- Compare annual NDVI consistency
- Evaluate multi-resolution damage detection
- Investigate earthquake hotspots

---

## Cross-Sensor Regression

```text
S2_NDVI = 0.3150 × Landsat_NDVI + 0.3283
R² = 0.1676
```

---

## Earthquake Damage Comparison

| Sensor | Resolution | Damage Area (km²) |
|----------|-----------|------------------:|
| Landsat | 30 m | 70.068 |
| Sentinel-2 | 10 m | 78.519 |

Difference:

```text
+8.451 km²
(+12.06%)
```

Sentinel-2 detects more fragmented and small-scale damage areas due to its higher spatial resolution.

---

## Hotspot Investigation

Two additional analyses were conducted:

### 1. Landsat vs Sentinel-2 ΔNDVI Comparison

- Landsat 30 m
- Sentinel-2 10 m

### 2. Sentinel-2 True Color Pre/Post Earthquake Inspection

Used to visually inspect:

- Landslide scars
- Exposed soil
- Valley disturbances
- Slope failures

---

# Main Outputs

```text
output/
│
├── Task 1
├── Task 2
├── Task 3
├── Task 4
│
├── Bonus 1
├── Bonus 2
├── Bonus 3
│
└── Markdown Reports
```

---

# Key Conclusions

1. The Taroko region exhibits a long-term greening trend despite major disturbances.
2. More than 80% of the study area shows positive NDVI trends over 26 years.
3. Taoyuan has experienced substantial pond loss, potentially reducing urban flood resilience.
4. Post-earthquake recovery is occurring, but more than half of damaged areas have not yet fully recovered.
5. Landsat provides long-term environmental context, while Sentinel-2 reveals high-resolution disturbance details.
6. Combining both sensors offers a powerful framework for ecosystem resilience monitoring.

---

# Reflection

This assignment demonstrated how long-term satellite archives can transform environmental monitoring from simple change detection into resilience assessment. By integrating Landsat's 26-year historical record with Sentinel-2's high-resolution observations, it becomes possible to understand not only where changes occur, but also whether ecosystems are recovering or degrading over time. The workflow highlights the value of combining temporal depth and spatial detail for disaster monitoring, environmental management, and future decision support.

---