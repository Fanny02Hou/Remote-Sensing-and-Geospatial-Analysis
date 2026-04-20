# HW8 — ARIA v5.0: Matai’an Three-Act Auditor

## Overview
This assignment builds **ARIA v5.0** to reconstruct the 2025 **Matai’an Creek barrier-lake event** using **Sentinel-2 imagery**.  
The workflow follows a **three-act structure**:

- **Act 1 (Pre-event):** forested valley before lake formation  
- **Act 2 (Mid-event):** barrier lake present before the breach  
- **Act 3 (Post-event):** drained lake, landslide source, and downstream debris-flow footprint  

## Main Tasks
- Select **Pre / Mid / Post** Sentinel-2 scenes from Planetary Computer
- Build reusable spectral metrics:
  - NIR drop
  - SWIR post brightness
  - BSI change
  - NDVI change
- Detect three hazard layers:
  - **Barrier lake**
  - **Landslide source**
  - **Debris flow**
- Vectorize masks into polygons
- Integrate previous ARIA layers:
  - W3 shelters
  - W4 terrain risk
  - W7 top-5 bottlenecks
  - W8 Guangfu overlay
- Build an **Eyewitness Impact Table**
- Produce a **Coverage Gap Map**
- Generate an **AI advisor prompt**

## Key Results
- **Pre scene:** `S2A_MSIL2A_20250615T023141_R046_T51QUG_20250615T070417`
- **Mid scene:** `S2C_MSIL2A_20250911T022551_R046_T51QUG_20250911T055914`
- **Post scene:** `S2B_MSIL2A_20251016T022559_R046_T51QUG_20251016T042804`

### Detection Summary
- Barrier lake area: **1.022 km²**
- Landslide source area: **19.660 km²**
- Debris-flow footprint area: **1.460 km²**

### Coverage Summary
- **W3 hits:** 28
- **W7 hits:** 0
- **Guangfu hits:** 4 / 5

## Key Finding
The results show that the original ARIA setup, which focused mainly on **Hualien City assets**, did not effectively represent the actual **Guangfu disaster corridor**.  
The **Guangfu overlay** was necessary to reveal the real downstream impact pattern.

## project structure
```
HW8/
├── README.md
├── mataian_three_act_auditor.ipynb
├── output/
│   ├── 06_change_metrics_panel.png
│   ├── 07_lake_mask.png
│   ├── 08_landslide_threshold_grid.png
│   ├── 08c_landslide_mask_final.png
│   ├── 09_debris_mask.png
│   ├── 10_three_masks.png
│   ├── 12_coverage_gap_map.png
│   ├── impact_table.csv
│   ├── mataian_detections.gpkg
│   └── 13_ai_advisor_prompt.txt
└── data/
    └── (optional: cached STAC items)
```
## Gemini API setting

To use the AI advisor prompt feature, you need to set up your Google Gemini API key. You can do this by:

1. Creating a `.env` file in the project root with your API key:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```

2. Or setting the environment variable directly in your terminal:
   ```
   set GEMINI_API_KEY=your_actual_api_key_here
   ```

## Notes
This notebook uses:
- `pystac-client`
- `planetary-computer`
- `stackstac`
- `rioxarray`
- `geopandas`
- `matplotlib`

The analysis combines **remote sensing**, **vector overlay**, and **coverage-gap auditing** to evaluate whether ARIA captured the real disaster footprint.

