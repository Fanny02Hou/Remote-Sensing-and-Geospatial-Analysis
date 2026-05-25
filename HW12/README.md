# HW12 — Multi-temporal Remote Sensing Change Detection and Disaster Monitoring using Google Earth Engine

## Project Overview

This homework develops a **multi-temporal remote sensing analysis workflow using Google Earth Engine (GEE)** to investigate environmental changes associated with the **2024 Hualien Earthquake** and subsequent landscape evolution in the **Xiulin / Taroko region, Taiwan**.

The workflow integrates **Sentinel-2 optical imagery**, **Sentinel-1 SAR imagery**, and **time-series analysis** to perform vegetation monitoring, change detection, composite analysis, and disaster interpretation across multiple temporal stages.

Compared with traditional local processing approaches, this workflow demonstrates how cloud-based geospatial computation can efficiently process long-term Earth observation datasets and generate reproducible outputs for environmental monitoring.

---

# Study Area

**Location:** Xiulin Township / Taroko National Park, Hualien, Taiwan

**AOI Bounding Box**

```text
[121.3453, 24.0460, 121.8515, 24.3577]
```

---

# Study Period

| Dataset | Time Range |
|---|---|
| Sentinel-2 | 2020-01-01 → 2026-03-31 |
| Sentinel-1 | 2022-01-01 → 2026-03-31 |

Important events:

| Event | Date |
|---|---|
| 2024 Hualien Earthquake | 2024-04-03 |
| Post-Earthquake Composite | 2024-04-01 → 2024-09-30 |
| Post-Dam Composite | 2025-10-01 → 2026-03-31 |

---

# Objectives

This homework aims to:

- Build a complete Google Earth Engine workflow
- Analyze long-term vegetation dynamics
- Detect earthquake-related environmental change
- Compare optical and SAR observations
- Generate exportable GeoTIFF products
- Create temporal visualization products

---

# Workflow Summary

## Task 1 — Sentinel-2 NDVI Time Series Analysis

### Completed Tasks

- Connected Google Earth Engine Python API
- Built Sentinel-2 ImageCollection
- Applied SCL cloud masking
- Computed NDVI:

\[
NDVI=\frac{NIR-Red}{NIR+Red}
\]

- Generated monthly median composites
- Built NDVI time-series visualization
- Compared:
  - Pre-earthquake period
  - Post-earthquake period
  - Post-dam period
- Generated automated interpretation report

### Outputs

```text
task1_monthly_ndvi_timeseries.png
task1_ndvi_analysis.md
task1_sentinel2_metadata.csv
```

---

## Task 2 — Multi-phase Composite Change Detection

### Completed Tasks

Constructed three-phase NDVI composites:

1. Pre-EQ
2. Post-EQ
3. Post-Dam

Calculated:

```text
ΔNDVI EQ
= Post-EQ − Pre-EQ
```

```text
ΔNDVI Dam
= Post-Dam − Post-EQ
```

```text
ΔNDVI Total
= Post-Dam − Pre-EQ
```

### Additional Analysis

- Damage mask extraction
- Threshold analysis

```text
ΔNDVI < −0.15
```

- Static change visualization
- W9 vs W13 methodological comparison

### Outputs

```text
task2_delta_ndvi_static_maps_red_blue.png
task2_delta_ndvi_analysis.md
task2_delta_ndvi_damage_area.csv
```

---

## Task 3 — Sentinel-1 SAR Change Analysis

### Completed Tasks

- Loaded Sentinel-1 GRD VV imagery
- Generated SAR time series
- Computed VV statistics
- Built VV composites
- Calculated:

```text
ΔVV
= Post-EQ − Pre-EQ
```

### Optical–SAR Integration

Defined high-confidence change:

```text
ΔNDVI < −0.15
AND
|ΔVV| > 2 dB
```

Estimated:

```text
High-confidence change area
≈ 537 ha
```

### Outputs

```text
task3_sentinel1_vv_timeseries.png
task3_delta_vv_map.png
task3_ndvi_sar_high_confidence_change_map.png
task3_sentinel1_sar_analysis.md
```

---

## Task 4 — GeoTIFF Export

### Completed Tasks

Exported:

- Post-earthquake NDVI
- Earthquake ΔNDVI
- Total ΔNDVI

Export settings:

```text
Scale: 10 m
CRS: EPSG:32651
Format: GeoTIFF
```

### Outputs

```text
taroko_post_eq_ndvi_2024.tif
taroko_delta_ndvi_eq_2024.tif
taroko_delta_ndvi_total_2026.tif
```

---

# Bonus 1 — InSAR Interpretation Exercise

Completed interpretation of:

**2016 Kumamoto Earthquake Interferogram**

Topics covered:

- Satellite information
- Fringe interpretation
- LOS displacement estimation
- Deformation direction
- Comparison between InSAR and SAR amplitude analysis

---

# Bonus 2 — NDVI Time-Lapse Animation

### Completed Tasks

Generated:

- Semi-annual NDVI median composites
- Frame annotation
- Event labeling
- GIF animation

Produced:

```text
taroko_ndvi_timelapse.gif
```

Animation period:

```text
2020 → 2026
```

### Outputs

```text
bonus2/
├── frames/
├── taroko_ndvi_timelapse.gif
├── bonus2_frame_metadata.csv
└── bonus2_timelapse_description.md
```

---

# Key Findings

- Long-term NDVI variability reflects seasonal and disturbance effects.
- Earthquake-related vegetation loss exists but becomes clearer through spatial analysis than AOI-wide averages.
- SAR backscatter changes complement NDVI observations and reduce false detections.
- Multi-temporal composites improve robustness compared with single-scene analysis.
- GEE enables scalable analysis that would require substantial local storage and processing time.

---

# Technologies

```text
Python
Google Earth Engine
Sentinel-1 GRD
Sentinel-2 SR
NumPy
Pandas
Matplotlib
PIL
ImageIO
GeoTIFF
Jupyter Notebook
```

---

# Repository Structure

```text
HW12/
├── data/
├── output/
│   ├── task1/
│   ├── task2/
│   ├── task3/
│   ├── task4/
│   └── bonus2/
├── script/
│   └── HW12.ipynb
└── Homework-Week13.md
```

---
