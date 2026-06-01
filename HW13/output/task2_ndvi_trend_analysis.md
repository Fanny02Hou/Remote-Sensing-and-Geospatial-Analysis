
## Task 2 — Pixel-Level Linear Trend Analysis

本任務使用 `ee.Reducer.linearFit()` 對太魯閣研究區 2000–2026 年的年度 NDVI 影像進行像素層級線性趨勢分析。每個像素都建立一條 `NDVI = slope × time + offset` 的線性迴歸式，其中 `slope` 代表該像素每年的 NDVI 變化量。

### 1. Greening / Browning / Stable 統計結果

本次分類門檻設定為：

```text
Greening: slope > 0.001
Browning: slope < -0.001
Stable: -0.001 <= slope <= 0.001
統計結果如下：

Class	Area (km²)	Percentage
Greening	1484.15	83.64%
Browning	75.29	4.24%
Stable	215.85	12.16%

結果顯示，太魯閣研究區有 83.64% 的有效像素呈現長期 greening，只有 4.24% 呈現長期 browning，另有 12.16% 屬於相對穩定區域。這表示從 26 年尺度來看，研究區整體以植被恢復或長期變綠為主。

2. Slope Map 空間判讀

在 slope map 中，綠色區域代表 NDVI 長期增加，可能與森林自然演替、災後植被恢復或裸露地逐漸再植生有關。紅色區域則代表 NDVI 長期下降，可能與坡面崩塌、河道沖刷、裸露岩盤增加、道路或聚落周邊開發有關。

由於 browning 像素比例相對較低，這些退化區很可能不是整體性植被退化，而是集中在局部地形敏感區，例如河谷邊坡、崩塌帶、裸露地或受反覆擾動的坡面。

3. W13 6-year Sentinel-2 vs W14 26-year Landsat

W13 使用 Sentinel-2 進行約 6 年的高解析度時序分析，優點是空間解析度高，可以看見較細的災後變化，例如個別崩塌面、道路邊坡破壞或河道細部變化。然而，6 年時間窗較短，容易受到單一事件、季節差異或雲遮罩品質影響，因此不一定能代表長期趨勢。

W14 使用 Landsat 建立 26 年長期時序，雖然空間解析度較粗，但能夠分辨短期波動與長期訊號。本次結果顯示，太魯閣研究區即使受到颱風與地震等擾動，整體仍以 greening 為主。這說明若只看 W13 的短期 Sentinel-2 變化，可能會強調災後局部退化；但若放到 W14 的 26 年 Landsat 脈絡中，則可以看見生態系長期恢復與韌性的背景。

4. 小結

Task 2 的結果顯示，長期趨勢圖能夠回答「哪些區域正在長期變綠或退化」的問題。它不只是災後變化偵測，而是把每個像素的 26 年歷史壓縮成一個 slope 值，讓我們能從空間上辨識長期 greening、browning 與 stable 區域。
