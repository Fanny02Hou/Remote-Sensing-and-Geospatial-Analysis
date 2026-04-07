# Week 7 Pre-lab: OSMnx & Network Analysis Environment

> Please complete the following steps **before class** to ensure your environment is ready.
> Estimated time: 15–20 minutes

---

## Step 1: Install New Packages

```bash
# Activate your virtual environment first!
# macOS / Linux:
source gis-env/bin/activate
# Windows:
gis-env\Scripts\activate

# Install OSMnx (road networks) and NetworkX (graph algorithms)
pip install osmnx networkx

# Install rasterio (needed for Raster-to-Network integration with Week 6 Kriging output)
pip install rasterio
```

Verify installation:

```python
import osmnx as ox
import networkx as nx
import rasterio
from shapely.geometry import Point, Polygon
print(f"OSMnx version: {ox.__version__}")
print(f"NetworkX version: {nx.__version__}")
print(f"Rasterio version: {rasterio.__version__}")
print("✅ All packages ready for Week 7!")
```

> **注意**：OSMnx 會自動安裝 `geopandas`, `shapely`, `requests` 等相依套件。`rasterio` 是獨立安裝，用於讀取 Week 6 的 Kriging GeoTIFF 並將降雨量映射到路段權重。如果之前的環境正常，通常只需要安裝 `osmnx` 和 `rasterio`。

---

## Step 2: Test OSMnx — Fetch a Small Road Network

```python
import osmnx as ox

# Fetch a small road network around NTU (台大)
G = ox.graph_from_address("National Taiwan University, Taipei", dist=500, network_type='drive')

# Basic info
print(f"Nodes (路口): {G.number_of_nodes()}")
print(f"Edges (路段): {G.number_of_edges()}")

# Project to meters (EPSG:3826)
G_proj = ox.project_graph(G, to_crs='EPSG:3826')
print(f"CRS: {G_proj.graph['crs']}")
print("✅ OSMnx road network fetching works!")
```

> **Troubleshooting**: If you get a timeout error, it may be due to network issues. OSMnx fetches data from OpenStreetMap's Overpass API, which occasionally has slow responses. Try again after a few minutes.

---

## Step 3: Test NetworkX — Basic Graph Operations

```python
import networkx as nx

# Betweenness centrality — finds "bottleneck" nodes
centrality = nx.betweenness_centrality(G, weight='length')

# Top 3 most important intersections
top_nodes = sorted(centrality, key=centrality.get, reverse=True)[:3]
for node in top_nodes:
    print(f"  Node {node}: centrality = {centrality[node]:.4f}")

print("✅ NetworkX graph algorithms work!")
```

---

## Step 4: Update Your `.env` File

Add Week 7 settings to your project's `.env`:

```
# Week 7 additions — 路網分析
NETWORK_DIST=5000
ISOCHRONE_MINUTES=5,10,15

# 塞車係數門檻（降雨 mm → 壅塞因子）
# <10mm → cf=0, 10-40mm → cf=0.3, 40-80mm → cf=0.6, >80mm → cf=0.9
CONGESTION_METHOD=threshold
CONGESTION_BREAK_1=10
CONGESTION_BREAK_2=40
CONGESTION_BREAK_3=80

# AI Advisor (Week 7 Cell [16], optional)
GOOGLE_API_KEY=your-gemini-api-key-here

# Keep previous settings
CWA_API_KEY=CWA-XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
APP_MODE=SIMULATION
SIMULATION_DATA=data/scenarios/fungwong_202511.json
PROJECT_CRS=3826
TARGET_COUNTY=花蓮縣
SLOPE_THRESHOLD=30
```

> **⚠️ 塞車係數說明**：課堂使用 threshold 方法，將時雨量分為四級（正常/略慢/嚴重遲滯/幾乎不通）。這些門檻值 10/40/80 mm 對應到台灣氣象署的降雨強度分級。

---

## Step 5: Prepare Week 6 Outputs

This week builds on your Week 6 Kriging results. Make sure you have:

- **`kriging_rainfall.tif`** — Kriging interpolated rainfall (EPSG:3826)
- **`kriging_variance.tif`** — Kriging variance / sigma map (EPSG:3826)

These GeoTIFF files will be used to assign **dynamic road weights** based on predicted rainfall intensity — even in areas without rain stations.

> **If you don't have these files**: You can still complete Week 7 using simulated weights. The teacher will demonstrate how to use Kriging raster output for road weighting, but the core network analysis logic works independently.

---

## Step 6 (Optional): Review Key Concepts

Make sure you are comfortable with:

- **Graph Theory Basics**: Nodes (vertices), edges, directed vs. undirected graphs
- **Shortest Path**: Dijkstra's algorithm concept (no need to implement from scratch)
- **Isochrone（等時線）**: From one point, how far can you travel in X minutes? (Think of it as the real-world alternative to buffer zones)
- **Betweenness Centrality**: Which nodes sit on the most shortest paths? (Bottleneck identification)
- **Dynamic Weighting**: How rainfall/flooding changes travel time on road segments
- **GraphML Format**: XML-based graph file format — we'll use `ox.save_graphml()` / `ox.load_graphml()` to persist road networks
- **GeoPandas CRS**: `.to_crs()` and why EPSG:3826 (meters) is essential for distance calculations
- **Week 5-6 ARIA outputs**: Shelter risk levels, rainfall data, Kriging GeoTIFF results

---

## Troubleshooting

**Q: `osmnx` import fails with "No module named 'osmnx'"?**
A: Make sure you activated your virtual environment. Try: `pip install --upgrade osmnx`

**Q: `ox.graph_from_address()` returns an error?**
A: Check your internet connection. OSMnx requires live access to OpenStreetMap. If behind a firewall, ask your network administrator to allow access to `overpass-api.de`.

**Q: Graph has 0 nodes?**
A: The search area might be too small or the `network_type` doesn't match available roads. Try increasing `dist` or using `network_type='all'`.

**Q: `ox.project_graph()` gives CRS warning?**
A: This is normal if OSMnx auto-detects a different local CRS. You can force it: `ox.project_graph(G, to_crs='EPSG:3826')`

**Q: `rasterio` installation fails on Windows?**
A: Try `pip install rasterio --no-binary rasterio` or use conda: `conda install -c conda-forge rasterio`. If still failing, you can still complete the core network analysis without rasterio — the Raster-to-Network integration (Cell [14]) is an advanced topic.

**Q: 什麼是塞車係數（congestion factor）？**
A: 課堂上會用 `rain_to_congestion()` 函數將降雨量轉為 0~0.9 的係數。公式：`travel_time_adj = length / (speed × (1 - cf))`。cf=0 表示正常，cf=0.9 表示幾乎不通。門檻值 10/40/80mm 已寫在 `.env` 中。
