# ARIA v4.0 - Hualien Disaster Accessibility Assessment

## Project Overview

This project builds an integrated disaster accessibility assessment workflow for Hualien, Taiwan, by combining:

- road network analysis
- shelter / facility accessibility analysis
- bottleneck diagnosis based on betweenness centrality
- rainfall impact assessment using the Week 6 kriging rainfall raster
- pre-disaster and post-disaster isochrone comparison

The objective is to assess whether key facilities remain reachable under disaster conditions and to identify transportation bottlenecks, accessibility loss, and priority response strategies.

---

## Data Sources

- **Road network**: OpenStreetMap (via OSMnx)
- **Shelter / facility data**: `shelters_with_risk.geojson`
- **Terrain / facility audit data**: `terrain_risk_audit.geojson`
- **Rainfall data**: `kriging_rainfall.tif` (Week 6 kriging output)

---

## Workflow Summary

1. Load and standardize shelter / facility data
2. Select 5 key facilities for analysis
3. Download or load the road network from OpenStreetMap
4. Project the network to EPSG:3826
5. Compute edge travel time from road length and speed
6. Identify Top 5 bottleneck nodes using betweenness centrality
7. Sample rainfall from the kriging raster at road segment midpoints
8. Convert rainfall values to congestion factors
9. Compute pre-disaster and post-disaster isochrones
10. Compare accessibility changes using shrinkage ratios
11. Generate AI bonus prompt / strategy briefing support files

---

## Deliverables

- `ARIA_v4.ipynb` — complete analysis notebook
- `accessibility_impact_table.csv`
- `top5_bottleneck_nodes.csv`
- `selected_facilities.csv`
- `homework_week7_summary.md`
- `README.md`

---

## AI Diagnostic Log

### 1. OSMnx road network extraction
**Issue:** Large network extent or repeated downloads may slow down notebook execution.  
**Solution:** The workflow saves and reuses GraphML files when possible to reduce repeated OSM downloads.

### 2. Isochrone comparison
**Issue:** In the current analysis, pre-disaster and post-disaster isochrones may appear identical.  
**Solution:** This is not a coding error. It occurs because sampled rainfall values were below the congestion threshold, resulting in congestion factors of 0.0.

### 3. Gemini API invocation
**Issue:** Automatic AI generation may fail due to API key issues, quota limits, or model availability.  
**Solution:** The notebook exports an AI prompt file and a manual fallback markdown template so the AI bonus can still be completed manually.

---

## Final Summary

# ARIA v4.0 — Homework-Week7 Summary

## Project Overview
This homework develops a network-based disaster accessibility assessment workflow in Hualien, integrating road network data, shelter/facility data, and kriging rainfall results.

## Key Results
- Total road network nodes: **3421**
- Total road network edges: **9815**
- Top bottleneck node: **649286213** (centrality = **0.140247**)
- Highest-capacity selected facility: **國風國中** (capacity = **800**)
- Maximum accessibility shrinkage observed: **0.0000**

## Interpretation
- In the current analysis, sampled rainfall values from the kriging raster were all below the congestion threshold.
- Therefore, the congestion factor remained 0.0 on all road segments, and post-disaster travel time was identical to pre-disaster travel time.
- As a result, pre-disaster and post-disaster isochrone areas were the same, and all shrinkage values were 0.0.

## Selected Facilities
- **F1** — 中正國小 (花蓮縣花蓮市, risk = 中風險, capacity = 187)
- **F2** — 中原國小文中三國中預定地 (花蓮縣花蓮市, risk = 高風險, capacity = 85)
- **F3** — 忠孝國小 (花蓮縣花蓮市, risk = 中風險, capacity = 47)
- **F4** — 主權社區活動中心 (花蓮縣花蓮市, risk = 中風險, capacity = 72)
- **F5** — 國風國中 (花蓮縣花蓮市, risk = 中風險, capacity = 800)

## Output Files
- Accessibility impact table: `accessibility_impact_table.csv`
- Top 5 bottleneck nodes: `top5_bottleneck_nodes.csv`
- Selected facilities: `selected_facilities.csv`
- AI bonus prompt: `ai_bonus_prompt.txt`
- AI bonus manual template: `ai_strategy_briefing_manual_template.md`
- AI strategy briefing: `ai_strategy_briefing.md`
- AI run log: `ai_bonus_run_log.txt`

## AI Bonus Status
- AI status: **success**
- The AI-generated strategy briefing was successfully created and saved.

## Notes
- Road network CRS was standardized to **EPSG:3826**.
- Travel time was computed from road length and maxspeed, with a default speed used when necessary.
- Isochrone analysis was performed for **5-minute** and **10-minute** thresholds.
- The current workflow used the **Week 6 kriging rainfall raster** as the rainfall source.
- Top 5 bottleneck nodes were identified using **betweenness centrality**.

---

## Submission Checklist

- [ ] `ARIA_v4.ipynb`
- [ ] `accessibility_impact_table.csv`
- [ ] `top5_bottleneck_nodes.csv`
- [ ] `selected_facilities.csv`
- [ ] `README.md`

---

## Notes

- All major spatial analyses were standardized to **EPSG:3826**
- Isochrone comparison was performed for **5-minute** and **10-minute** thresholds
- The current workflow uses **betweenness centrality** for bottleneck detection
- The current rainfall source is the **Week 6 kriging raster**
- AI bonus results may be completed either automatically or manually, depending on API availability
