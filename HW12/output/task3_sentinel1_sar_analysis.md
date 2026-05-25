
# Task 3 — Sentinel-1 SAR Time Series Analysis

## 1. Sentinel-1 VV time series

This task used **146 Sentinel-1 GRD VV images** from **2022-01-01 to 2026-03-31** over the Xiulin / Taroko study area.  
The mean VV backscatter before the 2024 Hualien earthquake was **-9.3416 dB**, while the mean VV after the earthquake was **-9.4871 dB**.  
The overall post-earthquake change was therefore **-0.1455 dB**, suggesting that the AOI-wide average SAR backscatter changed only slightly after the earthquake.

## 2. ΔVV map interpretation

The ΔVV map was calculated as:

```text
ΔVV = Post-EQ VV − Pre-EQ VV
The mean ΔVV from the composite map was -0.0059 dB, with values ranging from -6.5092 dB to 10.5123 dB.
Positive ΔVV values may indicate increased surface roughness, exposed soil, landslide scars, or stronger radar scattering.
Negative ΔVV values may indicate smoother surfaces, moisture changes, geometric effects, or reduced backscatter.

## 3. NDVI/SAR cross-reference

To identify high-confidence change areas, this task combined optical and SAR evidence:
ΔNDVI < -0.15
AND
|ΔVV| > 2.0 dB
The resulting high-confidence change area was 537.37 ha (5.3737 km²).
These areas are more reliable candidates for disaster-related surface change because they show both vegetation loss in Sentinel-2 NDVI and significant backscatter change in Sentinel-1 SAR.

4. 中文說明

本任務使用 146 張 Sentinel-1 GRD VV 影像，分析秀林 / 太魯閣研究區在 2022–2026 年間的 SAR 後向散射變化。
地震前平均 VV 約為 -9.3416 dB，地震後平均 VV 約為 -9.4871 dB，整體變化為 -0.1455 dB。
這代表若只看整個 AOI 的平均 SAR 訊號，地震後變化並不劇烈，但空間上的 ΔVV map 仍可顯示局部地表散射變化。

透過交叉比對 ΔNDVI < -0.15 與 |ΔVV| > 2.0 dB，可找出同時具有植被下降與 SAR 散射變化的高信度變化區。
本次估計的高信度變化面積為 537.37 ha，顯示多源資料結合能比單獨使用 NDVI 或 SAR 更有助於篩選可能的災害變化區。
