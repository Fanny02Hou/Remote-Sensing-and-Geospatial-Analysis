# Week 14 Pre-Lab: GEE Advanced — Long-term Trends & Climate Resilience — ARIA v9.5 Setup

**Course:** NTU Remote Sensing & Spatial Information Analysis (遙測與空間資訊之分析與應用)  
**Instructor:** Prof. Su Wen-Ray  
**Week:** 14 | **Theme:** GEE Advanced — Landsat Multi-Decadal Trend Analysis & Resilience（GEE 進階 — Landsat 長期趨勢與韌性分析）  
**Time Required:** ~20 minutes

---

## Objectives

By the end of this pre-lab, you will:
- Understand the upgrade from W13 (Sentinel-2, 6 years) to W14 (Landsat, 20+ years)
- Review Landsat mission history and band naming conventions
- Understand why long-term trend analysis requires multi-sensor harmonization
- Review the concepts of linear regression and resilience in vegetation monitoring
- Confirm your GEE environment is ready (should already be set up from W13)

---

## Step 1: Verify GEE Environment (from W13)

You should already have a working GEE setup from Week 13. Run this quick check:

```python
import ee
import geemap

ee.Initialize(project='your-project-id')

# Quick test
point = ee.Geometry.Point([121.5, 24.1])
elev = ee.Image('USGS/SRTMGL1_003').sample(point, 30).first().get('elevation').getInfo()
print(f"✓ GEE connected — elevation: {elev} m")
```

If this fails, revisit Week 13 Pre-lab Step 2 for authentication instructions.

---

## Step 2: The Upgrade — From 6 Years to 20+ Years

### W13 vs W14 Comparison

| | W13 (Sentinel-2) | W14 (Landsat) |
|---|---|---|
| Time span | 2020–2026 (6 years) | 2000–2026 (26 years) |
| Resolution | 10 m | 30 m |
| Revisit | 5 days | 8–16 days |
| Best for | High-detail recent changes | Long-term decadal trends |
| Key question | "What happened after the earthquake?" | "What has been happening for 20 years?" |

### Why Landsat?（為什麼用 Landsat？）

Sentinel-2 launched in 2015 — only ~10 years of data. To answer questions like "Has this riverbank been eroding for decades?" or "Is this forest recovering from a typhoon 15 years ago?", we need the **Landsat archive**, which provides continuous global coverage since 1984.

W14 uses **Landsat 5 (2000–2012)**, **Landsat 7 (2000–present)**, **Landsat 8 (2013–present)**, and **Landsat 9 (2021–present)** — harmonized into a single time series.

**Upgrade logic（升級邏輯）:**
```
W13:  S2 time series (6 yrs)  → "What changed after the earthquake?"
W14:  Landsat time series (26 yrs) → "What has been changing for TWO DECADES?"
      + Taoyuan pond disappearance analysis (MNDWI)
      + Resilience metrics (recovery rate after disturbance)
```

---

## Step 3: Landsat Band Mapping — The Harmonization Challenge

Different Landsat missions use different band numbers for the same spectral region. This is the key technical challenge for multi-decadal analysis.

### Band Mapping Table

| Spectral Region | L5 TM | L7 ETM+ | L8 OLI | L9 OLI-2 | Use |
|----------------|-------|---------|--------|----------|-----|
| Blue | SR_B1 | SR_B1 | SR_B2 | SR_B2 | Atmospheric scattering |
| Green | SR_B2 | SR_B2 | SR_B3 | SR_B3 | Vegetation vigor |
| Red | SR_B3 | SR_B3 | SR_B4 | SR_B4 | Chlorophyll absorption |
| NIR | SR_B4 | SR_B4 | SR_B5 | SR_B5 | Vegetation structure |
| SWIR1 | SR_B5 | SR_B5 | SR_B6 | SR_B6 | Moisture content |
| SWIR2 | SR_B7 | SR_B7 | SR_B7 | SR_B7 | Geology/minerals |

### Key Indices

| Index | Formula | Detects |
|-------|---------|---------|
| **NDVI** | (NIR − Red) / (NIR + Red) | Vegetation health |
| **MNDWI** | (Green − SWIR1) / (Green + SWIR1) | Water bodies |
| **NBR** | (NIR − SWIR2) / (NIR + SWIR2) | Burn severity |

> **Key concept:** We write a **harmonization function** that renames bands from each Landsat mission to a common set (`Blue`, `Green`, `Red`, `NIR`, `SWIR1`, `SWIR2`). This lets us compute NDVI and MNDWI consistently across all 26 years.（我們寫一個波段統一函數，把不同 Landsat 任務的波段名稱對應到統一名稱，就能跨 26 年一致計算 NDVI 和 MNDWI。）

---

## Step 4: GEE Landsat Collections

### Collection IDs in GEE

| Mission | GEE Collection ID | Years | Notes |
|---------|-------------------|-------|-------|
| Landsat 5 | `LANDSAT/LT05/C02/T1_L2` | 1984–2012 | TM sensor |
| Landsat 7 | `LANDSAT/LE07/C02/T1_L2` | 1999–present | ETM+, SLC failure after 2003 |
| Landsat 8 | `LANDSAT/LC08/C02/T1_L2` | 2013–present | OLI sensor |
| Landsat 9 | `LANDSAT/LC09/C02/T1_L2` | 2021–present | OLI-2 sensor |

### Cloud Masking with QA_PIXEL

Unlike Sentinel-2's SCL band, Landsat uses a **QA_PIXEL** bitmask for cloud masking:

```python
def mask_landsat_clouds(image):
    qa = image.select('QA_PIXEL')
    # Bit 3 = cloud, Bit 4 = cloud shadow
    cloud_mask = qa.bitwiseAnd(1 << 3).eq(0)
    shadow_mask = qa.bitwiseAnd(1 << 4).eq(0)
    return image.updateMask(cloud_mask.And(shadow_mask))
```

### Landsat 7 SLC-off Issue（Landsat 7 條紋問題）

In May 2003, Landsat 7's Scan Line Corrector (SLC) failed, causing **stripe artifacts** in all subsequent images. These appear as wedge-shaped gaps of missing data. GEE automatically masks these pixels, but it means Landsat 7 images after 2003 have reduced spatial coverage. When computing composites (median), the gaps are filled by other images in the stack.（2003 年後的 Landsat 7 影像有條紋缺失，但中位數合成可以自動填補。）

### Self-Test Q1

Why do we need to harmonize band names across Landsat missions before computing a 20-year NDVI time series?

**Answer:** Different Landsat missions use different band numbering for the same spectral region (e.g., NIR is B4 in L5/L7 but B5 in L8/L9). Without harmonization, computing `normalizedDifference(['B4', 'B3'])` would calculate NDVI correctly for L5/L7 but produce a wrong index for L8/L9.（因為不同 Landsat 的 NIR 波段編號不同，不統一名稱會算錯指標。）

---

## Step 5: Linear Trend & Resilience Concepts

### Pixel-Level Linear Regression

In W13 (D8), we briefly used `ee.Reducer.linearFit()` on the Sentinel-2 NDVI series. In W14, we apply this to the **full 26-year Landsat series** — the slope reveals which areas are **greening** (positive trend) vs **browning** (negative trend) over two decades.

```
NDVI(t) = slope × t + offset
```

- **slope > 0** → long-term greening (vegetation recovery, reforestation)
- **slope < 0** → long-term browning (degradation, urbanization, repeated disturbance)
- **slope ≈ 0** → stable vegetation

### Resilience（韌性）

**Resilience** is the ability of an ecosystem to recover from disturbance. After an earthquake or typhoon:
- **High resilience:** NDVI drops sharply but recovers to near-baseline within 1–2 years
- **Low resilience:** NDVI drops and stays low, or continues declining
- **Non-recovery:** Permanent land cover change (landslide scar becomes bare rock)

W14 introduces metrics to quantify resilience:
- **Recovery rate:** How fast does NDVI return to baseline after a disturbance?
- **Recovery ratio:** Post-disturbance NDVI / pre-disturbance NDVI
- **Time to recovery:** Number of years to reach 90% of baseline NDVI

### Taoyuan Pond Disappearance（桃園埤塘消失）

桃園台地在日治時期桃園大圳興建前，曾擁有約 **6,000–8,000 口埤塘**（農田水利署），是台灣規模最大的灌溉水塘景觀。隨著都市化發展，大量埤塘被填平，目前僅存約 3,000 口。Using **MNDWI** (Modified Normalized Difference Water Index) time series, we can track pond presence year by year.

- MNDWI > 0.1 → water (pond surface)
- MNDWI < 0 → land (filled pond or non-water)

By computing annual MNDWI composites and detecting where water appeared or disappeared, we map **pond disappearance** over 26 years — quantifying the scale of urbanization pressure and its impact on urban flood resilience.

### Self-Test Q2

A pixel in a Taoyuan pond shows: MNDWI = 0.5 in 2005, MNDWI = 0.3 in 2015, MNDWI = −0.2 in 2025. Another pixel on a hillside in Taroko shows: NDVI = 0.8 in 2005, NDVI = 0.2 (post-typhoon) in 2015, NDVI = 0.75 in 2025. Which pixel shows resilience? Which shows permanent change?

**Answer:** The hillside pixel shows resilience — it dropped to 0.2 after a typhoon but recovered to 0.75. The Taoyuan pond pixel shows permanent change — MNDWI went from positive (water) to negative (land), meaning the pond was filled for development. This is irreversible urbanization, not a natural disturbance-recovery cycle.（山坡像素展現韌性（恢復到 0.75）；桃園埤塘像素是永久變化（被填平蓋房）。）

---

## Step 6: Cross-Week Integration Preview

### The Space-Time Framework

| Week | Dimension | Technique | Resolution |
|------|-----------|-----------|-----------|
| W6 | **Spatial** interpolation | Kriging | Continuous surface from point data |
| W13 | **Temporal** analysis (6 yr) | GEE S2 time series | High spatial (10m), short time |
| W14 | **Temporal** analysis (26 yr) | GEE Landsat time series | Medium spatial (30m), long time |

> **W6 Kriging** fills spatial gaps (between rain gauges → continuous rainfall surface).  
> **W14 GEE** fills temporal gaps (between snapshots → continuous trend over decades).  
> Together, they provide a **complete space-time picture** of environmental change.  
> （W6 填補空間空隙，W14 填補時間空隙——合在一起就是完整的時空圖像。）

### Self-Test Q3

In W13, we computed monthly NDVI statistics for 2020–2026 (6 years). If we extend this to 2000–2026 (26 years) using Landsat, what new patterns might become visible that were hidden in the 6-year window?

**Answer:** Multi-decadal patterns such as: long-term urbanization trends, repeated typhoon damage and recovery cycles, gradual pond disappearance in Taoyuan, and whether the 2024 earthquake's impact is unprecedented or part of a recurring pattern. A 6-year window might show the earthquake as a singular event, while a 26-year window shows it in the context of the region's disturbance history.（26 年的窗口能揭示都市化趨勢、颱風反覆破壞與恢復的循環、桃園埤塘漸進消失，以及 2024 地震是否是前所未有的事件。）

---

## 延伸閱讀

以下參考資料可幫助你更深入了解本週主題的應用場景：

1. **呂明倫（2024）— 使用深度學習演算法進行 Sentinel-2 影像之土地利用和土地覆蓋分類**  
   航測及遙測學刊，29(4): 231–240。DOI: 10.6574/JPRS.202412_29(4).0003  
   → 以南投埔里鎮為研究區，用 CNN 對 Sentinel-2 做 9 類 LULC 分類（OA 89%），並與 Random Forest 比較。研究區與本週 NCDR 豪雨報告的災區重疊，可看到同一區域從災害分析到土地分類的不同遙測應用面向。連結 W9 混淆矩陣、W12 影像分類的概念。

2. **NCDR（2020）— 108 年度豪雨事件災情彙整與勘災報告**  
   → 2019 年台灣五場重大豪雨事件的災情紀錄，含氣象分析、農損統計（0812 事件農損 1.7 億元）、Sentinel-2 崩塌前後比對（圖 5.28）。研究區涵蓋南投、嘉義等地，可對照本週的 Landsat 長期趨勢分析。（檔案：`108年度豪雨事件災情彙整與勘災報告.pdf`）

---

## Checklist Before Class

- [ ] GEE environment still works (`ee.Initialize()` succeeds)
- [ ] Understand the upgrade from W13 (S2, 6 yr) to W14 (Landsat, 26 yr)
- [ ] Know the Landsat band mapping (L5/L7 vs L8/L9 band numbers)
- [ ] Understand QA_PIXEL cloud masking for Landsat
- [ ] Know the Landsat 7 SLC-off issue and how compositing mitigates it
- [ ] Understand NDVI linear trend interpretation (greening vs browning)
- [ ] Understand resilience concepts (recovery rate, recovery ratio)
- [ ] Understand MNDWI for water body / pond disappearance detection
- [ ] Completed Self-Test (3 questions)

**You're ready for Week 14!**

---

*Note: Week 14 builds directly on your W13 GEE skills. The same authentication and environment setup applies — no new software is needed. If your W13 setup still works, you're good to go.*
