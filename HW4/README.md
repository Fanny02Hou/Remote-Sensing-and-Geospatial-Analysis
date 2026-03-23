# AI 診斷日誌

## 1. Zonal Stats 回傳 NaN（CRS 未對齊或像素未覆蓋）

**問題描述**：執行區域統計時，結果回傳 NaN 值，無法正確計算統計資訊。

**解決方案**：
- **CRS 對齊檢查**：使用 `dem.rio.crs` 和 `gdf.crs` 確認 DEM 與向量圖層的坐標系統一致，若不同則使用 `gdf = gdf.to_crs(dem.rio.crs)` 進行轉換
- **空間覆蓋驗證**：透過 `gdf.total_bounds` 與 `dem.rio.bounds()` 比較邊界，確保向量圖層完全落在 DEM 範圍內
- **像素對齊處理**：使用 `dem.rio.reproject_match()` 確保像素網格與向量圖層完美對齊，避免因偏移造成的 NaN 值

## 2. DEM 太大導致 Colab 記憶體不足（需先裁切）

**問題描述**：處理大型 DEM 檔案時，出現記憶體不足錯誤，導致程式中斷。

**解決方案**：
- **範圍裁切**：使用 `dem.rio.clip_box()` 根據研究區域邊界裁切 DEM，大幅減少資料量
- **解析度降採樣**：若記憶體仍然不足，使用 `dem.rio.reproject()` 降低解析度（如從 20m 降到 40m）
- **分塊處理**：對於超大檔案，採用 `xarray.open_mfdataset()` 分塊讀取，避免一次性載入全部資料

## 3. 坡度計算結果不合理（gradient 的 spacing 參數需與解析度匹配）

**問題描述**：計算坡度時，結果數值異常（如過大或過小），與實際地形不符。

**解決方案**：
- **解析度參數設定**：使用 `np.gradient(dem, spacing=20)` 時，spacing 參數必須與 DEM 的實際空間解析度（20 公尺）一致
- **單位轉換**：gradient 回傳的是弧度，需使用 `np.degrees(np.arctan(slope))` 轉換為坡度角度
- **邊界處理**：在計算前使用 `dem.fillna(dem.mean())` 填補邊緣的 NaN 值，確保梯度計算的連續性