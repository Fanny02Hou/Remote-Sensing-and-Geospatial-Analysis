
## Bonus 3 — Landsat × Sentinel-2 Cross-Sensor Analysis

本 Bonus 比較 Landsat 30 m 與 Sentinel-2 10 m 在太魯閣研究區的年度 NDVI 與地震前後 ΔNDVI 受損偵測結果。

### 1. Cross-sensor annual NDVI comparison

2018–2026 年的跨感測器比較顯示，Sentinel-2 年均 NDVI 系統性低於 Landsat。平均偏差為 **-0.0608 NDVI**，表示 Sentinel-2 的年度平均 NDVI 約比 Landsat 低 0.058。Scatter plot 的 R² 為 **0.039**，代表兩個感測器在年度平均 NDVI 上的線性一致性不高。

這個結果可能與山區複雜地形、陰影、雲遮罩、觀測日期差異、空間解析度差異與混合像素效應有關。Landsat 30 m 像素較容易混合森林、裸地、道路、河道與陰影；Sentinel-2 10 m 解析度較高，能保留更多局部異質性，因此兩者的年度平均值不一定會完全一致。

### 2. Multi-resolution earthquake damage comparison

本研究使用 `ΔNDVI < -0.15` 作為地震後植被受損門檻。結果顯示，Landsat 偵測到的受損面積為 **70.068 km²**，Sentinel-2 偵測到的受損面積為 **78.519 km²**。Sentinel-2 比 Landsat 多偵測 **8.451 km²**，約增加 **12.06%**。

這表示 Sentinel-2 的 10 m 解析度能捕捉較細小或狹長的受損區，例如道路邊坡、窄河谷、局部崩塌面與破碎化裸露地。相對地，Landsat 30 m 較適合掌握區域尺度的整體受損趨勢，但可能低估小尺度或空間破碎的災害影響。

### 3. Methodological reflection

若研究目標是建立長期背景、觀察 20 年以上的 greening/browning 趨勢，Landsat 較適合，因為它具有長時間序列與穩定的歷史觀測紀錄。若研究目標是災後細節判讀、崩塌面邊界、道路中斷或局部裸露地變化，Sentinel-2 較適合，因為其 10 m 空間解析度較高。

最理想的作法是兩者整合：先用 Landsat 建立長期趨勢與歷史脈絡，再用 Sentinel-2 對近期災害熱區進行高解析度檢視。這樣可以同時回答「這個區域長期是否異常」與「災後細節在哪裡」兩種問題。
