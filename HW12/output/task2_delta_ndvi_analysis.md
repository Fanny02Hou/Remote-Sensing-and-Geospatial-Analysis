# Task 2 — Pre/Post Earthquake Median Composite Analysis

## 1. Three-phase ΔNDVI damage area summary

Using the threshold **ΔNDVI < -0.15**, the estimated vegetation-loss areas are:

| Change stage | Meaning | Damage area (ha) | Damage area (km²) |
|---|---|---:|---:|
| Post-EQ − Pre-EQ | Earthquake-related vegetation loss | 7740.15 | 77.4015 |
| Post-Dam − Post-EQ | Post-dam or later-stage change | 6257.68 | 62.5768 |
| Post-Dam − Pre-EQ | Total accumulated change | 6839.04 | 68.3904 |

## 2. Interpretation

The **Post-EQ − Pre-EQ** ΔNDVI map shows the immediate vegetation decrease after the 2024 Hualien earthquake.  
The estimated damaged area is **7740.15 ha**, suggesting that a considerable portion of the Xiulin / Taroko study area experienced NDVI decline after the earthquake.

The **Post-Dam − Post-EQ** map represents later-stage change after the post-earthquake period.  
Its damaged area is **6257.68 ha**, indicating that some areas continued to show NDVI decline during the later period.  
However, this stage should be interpreted carefully because the change may include effects from later disturbances, seasonal differences, vegetation recovery patterns, or cloud-mask-related compositing differences.

The **Post-Dam − Pre-EQ** map represents the total accumulated difference between the later period and the pre-earthquake baseline.  
The estimated accumulated damaged area is **6839.04 ha**, which helps evaluate whether the landscape remained below the pre-earthquake NDVI condition.

## 3. W9 two-scene change detection vs. W13 composite-based change detection

In Week 9, change detection relied mainly on two individual Sentinel-2 scenes.  
That approach is sensitive to cloud cover, cloud shadow, atmospheric differences, seasonal mismatch, and scene-specific noise.  
In contrast, Week 13 uses Google Earth Engine to build **median composites** from many images within each phase.  
This reduces the influence of individual cloudy or noisy scenes and produces a more stable representation of each period.

The three-phase W13 design is also more informative than a simple before-after comparison.  
Instead of only detecting total change, it separates the timeline into earthquake-related change, post-dam or later-stage change, and total accumulated change.  
Therefore, the W13 method is more suitable for disaster monitoring because it turns a snapshot-based comparison into a multi-stage temporal interpretation.

## 4. 中文說明

本任務使用 **ΔNDVI < -0.15** 作為植被明顯下降的判斷門檻。  
結果顯示，地震後相對震前的植被損失面積約為 **7740.15 ha**；堰塞湖後相對震後的下降面積約為 **6257.68 ha**；堰塞湖後相對震前的累積下降面積約為 **6839.04 ha**。

W9 的方法主要是兩張單景影像相減，因此容易受到雲、雲影、季節差異與單張影像品質影響。  
W13 則利用 GEE 將多張影像做 median composite，可降低單景雜訊與雲遮罩造成的不穩定性。  
此外，三期比較能將地震直接影響、後續變化與累積影響分開討論，因此更適合用於災害監測與長期環境變遷分析。
