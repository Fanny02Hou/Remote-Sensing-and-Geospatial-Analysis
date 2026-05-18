# HW11 — Sentinel-2 Land Cover Classification and Landslide Validation

## Overview

This project performs post-earthquake land cover classification in the Hualien / Taroko region using Sentinel-2 multispectral imagery.  
The workflow combines:

- K-means unsupervised classification
- Random Forest supervised classification
- Google Earth Pro ROI training samples
- SWCB landslide inventory validation
- Gemini AI-generated disaster assessment report

The study focuses on evaluating post-earthquake bare land / landslide detection after the 2024 Hualien earthquake and comparing internal classification accuracy with independent external validation using official SWCB landslide polygons.

---

# Study Area

- Hualien County, Taiwan
- Xiulin / Taroko region
- Suhua Highway corridor
- Coastal and mountainous terrain

Bounding box used in this project:

```python
TAROKO_BBOX = [121.4, 24.1, 121.8, 24.25]
```

---

# Data Sources

## 1. Sentinel-2 L2A Imagery

Source:
- Microsoft Planetary Computer STAC API

Selected scene:
- `S2A_MSIL2A_20240827T022531_R046_T51QUG_20240827T053853`

Bands used:

| Band | Description |
|---|---|
| B02 | Blue |
| B03 | Green |
| B04 | Red |
| B08 | Near Infrared (NIR) |
| B11 | SWIR1 |
| B12 | SWIR2 |

Additional layer:
- SCL (Scene Classification Layer) for cloud masking

---

## 2. ROI Training Samples

Generated manually using:
- Google Earth Pro

Classes:

| ID | Class |
|---|---|
| 0 | Water |
| 1 | Forest |
| 2 | Cropland |
| 3 | Bare/Landslide |
| 4 | Built-up |

ROI polygons stored as:
```text
data/Week12_ROI.kmz
```

---

## 3. SWCB Landslide Inventory

Official landslide polygons from:
- Soil and Water Conservation Bureau (SWCB)

File:
```text
data/20240802新生崩塌地.kml
```

Used for:
- Independent external validation

---

# Project Structure

```text
HW11/
├── data/
│   ├── 20240802新生崩塌地.kml
│   └── Week12_ROI.kmz
│
├── output/
│
├── script/
│   └── HW11.ipynb
│
├── .env
├── .gitignore
└── Homework-Week12.md
```

---

# Environment Setup

## Install Required Packages

```bash
pip install planetary-computer pystac-client stackstac rasterio geopandas shapely scikit-learn matplotlib pandas numpy python-dotenv google-generativeai
```

---

# Gemini API Setup

Create a `.env` file in the project root:

```env
AI_API_KEY=your_gemini_api_key
```

The notebook automatically loads the key using:

```python
from dotenv import load_dotenv
```

---

# Workflow

# Task 1 — K-means Unsupervised Classification

## Steps

1. Connect to Microsoft Planetary Computer
2. Search Sentinel-2 post-earthquake imagery
3. Load Sentinel-2 bands using STAC streaming
4. Apply SCL cloud mask
5. Generate feature matrix
6. Perform K-means clustering (K = 5)
7. Interpret clusters manually

## Outputs

| Output | Description |
|---|---|
| `kmeans_classification.png` | Raw K-means clusters |
| `kmeans_landcover_interpreted.png` | Interpreted land cover map |
| `kmeans_cluster_mean_spectra.png` | Mean spectra plot |
| `task1_kmeans_discussion.md` | Discussion |

---

# Task 2 — Random Forest Supervised Classification

## Steps

1. Parse ROI polygons from KMZ
2. Rasterize ROI polygons to Sentinel-2 grid
3. Extract training pixels
4. Split train/test samples
5. Train Random Forest classifier
6. Predict full-scene land cover
7. Generate feature importance analysis
8. Compare K-means vs Random Forest

## Outputs

| Output | Description |
|---|---|
| `rf_classification.png` | RF classification map |
| `rf_feature_importance.png` | Feature importance chart |
| `rf_accuracy_summary.csv` | Accuracy metrics |
| `kmeans_vs_rf_comparison.png` | Comparison figure |

---

# Task 3 — Accuracy Assessment

## Part A — Internal Validation

Metrics:
- Overall Accuracy
- Kappa coefficient
- OOB accuracy
- Precision / Recall / F1-score
- Confusion matrix

### Results

| Metric | Value |
|---|---|
| Overall Accuracy | 0.9770 |
| Kappa | 0.9378 |
| OOB Accuracy | 0.9756 |

---

## Part B — External Validation with SWCB

### Method

- Rasterize SWCB landslide polygons
- Compare with RF Bare/Landslide class
- Pixel-level overlap analysis

### Metrics

| Metric | Value |
|---|---|
| Recall | 0.6096 |
| Precision | 0.0070 |
| IoU | 0.0070 |

### Key Finding

Although internal accuracy is very high, the RF Bare/Landslide class greatly overestimates official SWCB landslide areas.

This demonstrates that:
- Internal validation ≠ real-world disaster mapping performance
- Bare soil, riverbeds, roads, and disturbed surfaces can be confused with landslides

---

# Task 4 — AI-generated Disaster Report

Gemini LLM was integrated to automatically generate:
- Disaster assessment summary
- Landslide interpretation
- SWCB comparison discussion
- GIS application suggestions

Additional hallucination checks were performed:
- Numeric consistency verification
- Critical evaluation of AI-generated content

Outputs:
- `task4_llm_generated_report.md`
- `task4_llm_report_critical_evaluation.md`

---

# Main Results

## Land Cover Area Statistics

| Class | Area (ha) | Percentage |
|---|---:|---:|
| Water | 22360.92 | 35.07% |
| Forest | 27924.96 | 43.80% |
| Cropland | 3129.76 | 4.91% |
| Bare/Landslide | 10157.40 | 15.93% |
| Built-up | 182.16 | 0.29% |

---

# Key Findings

1. Forest and water dominate the study area.
2. Bare/Landslide areas are concentrated along mountainous slopes and the Suhua Highway corridor.
3. SWIR bands (B11, B12) are most important for classification.
4. Random Forest performs significantly better than K-means for complex land cover separation.
5. External validation reveals strong overprediction of landslide areas.
6. AI-generated reports are useful for summarization but still require human verification.

---

# Reflection

## 1. Understanding Supervised vs Unsupervised Classification

This project improved understanding of the differences between K-means and Random Forest classification, especially regarding spectral clustering versus labeled land-cover mapping.

## 2. Internal Accuracy Does Not Guarantee External Performance

Although Random Forest achieved very high internal accuracy, SWCB external validation revealed large disagreement, highlighting the importance of independent validation datasets.

## 3. Integrating AI into GIS Workflows

The project demonstrated how Gemini LLM can assist in generating disaster assessment reports, while also emphasizing the importance of checking AI-generated numerical and spatial interpretations.

