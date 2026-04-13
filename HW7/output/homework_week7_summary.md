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