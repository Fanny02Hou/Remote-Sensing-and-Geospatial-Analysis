# Week 8 — ARIA v5.0: The Matai'an Three-Act Auditor

This notebook builds **ARIA v5.0**, a remote-sensing-based disaster audit workflow for the **2025 Matai’an Creek barrier-lake event** using **Sentinel-2 imagery**.

The goal is to reconstruct the event in **three acts**:

- **Act 1 (Pre-event):** forested valley, no lake  
- **Act 2 (Mid-event):** barrier lake detected before the breach  
- **Act 3 (Post-event):** drained lake, upstream landslide scar, and downstream debris-flow footprint over Guangfu  

---

## What this notebook does

- Connects to the **Planetary Computer STAC API**
- Selects **Pre / Mid / Post** Sentinel-2 scenes for the Matai’an AOI
- Streams multi-band image cubes and converts them to surface reflectance
- Computes spectral metrics such as:
  - **NIR drop**
  - **NDVI change**
  - **BSI change**
  - **post-event SWIR**
- Detects three hazard footprints:
  - **Barrier lake**
  - **Landslide source**
  - **Debris flow**
- Vectorizes the masks into polygons
- Integrates previous ARIA outputs from:
  - **W3 shelters**
  - **W7 Top-5 bottlenecks**
  - **W8 Guangfu overlay**
- Builds an **Eyewitness Impact Table**
- Produces a **Coverage Gap Map**
- Generates an **AI advisor prompt** for operational briefing

---

## Core idea

This notebook is not only about mapping hazards from satellite imagery.  
It also asks a system-level question:

> **Did the original ARIA coverage zone actually cover the real disaster footprint?**

The answer from this audit is that the earlier ARIA setup was still too focused on **Hualien City assets**, while the true downstream impact in **Guangfu** became clear only after adding the Guangfu overlay.

---

## Main outputs

- Selected **Pre / Mid / Post** Sentinel-2 scenes
- Barrier lake mask
- Landslide source mask
- Debris-flow mask
- Threshold tuning results for landslide detection
- `mataian_detections.gpkg`
- `impact_table.csv`
- `coverage_gap_map`
- AI operational briefing prompt

---

## Key takeaway

**Sentinel-2 acts as an eyewitness.**  
By combining spectral evidence with earlier ARIA infrastructure layers, this notebook shows that the Matai’an event was not just a hazard-mapping problem, but a **coverage-gap problem** in the ARIA system itself.