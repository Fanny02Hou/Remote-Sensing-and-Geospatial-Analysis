# Task 4 — Integration Summary Report

## a. Data scale comparison

This Week 13 workflow processed **291 Sentinel-2 images** and **146 Sentinel-1 images** over the Xiulin / Taroko study area.  
If these datasets were downloaded and processed locally, the estimated data volume would be approximately **327.1 GB**, assuming about 800 MB per Sentinel-2 image and 700 MB per Sentinel-1 GRD image.  
At an approximate download speed of 50 Mbps, downloading alone could take around **14.9 hours**, before considering local storage, preprocessing, cloud masking, compositing, and raster calculation time.  
Using Google Earth Engine avoids this bottleneck because filtering, compositing, NDVI calculation, SAR processing, and export are executed on Google’s cloud servers.

## b. Key findings

The monthly NDVI time series showed temporal variability across 2020–2026.  
The mean NDVI before the earthquake was **0.4851**, while the post-earthquake mean was **0.4815**, indicating that the AOI-wide average NDVI changed only slightly.  
However, the spatial ΔNDVI maps revealed stronger localized vegetation loss.  
Using **ΔNDVI < -0.15**, the estimated vegetation-loss area was **7740.15 ha** for the earthquake phase, **6257.68 ha** for the post-dam or later-stage phase, and **6839.04 ha** for total accumulated change.  
The SAR analysis showed that mean VV changed from **-9.3416 dB** before the earthquake to **-9.4871 dB** afterward, with a small overall difference of **-0.1455 dB**.  
Although the AOI-wide SAR mean was stable, the ΔVV map captured local backscatter changes.  
By combining **ΔNDVI < -0.15** and **|ΔVV| > 2 dB**, the high-confidence change area was estimated as **537.37 ha** (**5.3737 km²**), suggesting that optical and SAR evidence overlap in selected disturbance zones.

## c. Cross-week integration

Compared with **W8 single-scene NDVI**, the GEE time-series workflow improves interpretation by showing multi-year temporal context instead of one snapshot.  
This helps distinguish event-related change from seasonal vegetation variation and image-specific noise.  
Compared with **W9 two-scene change detection**, median composites are more robust because they combine many images within each phase and reduce the influence of clouds, cloud shadows, and abnormal single-scene conditions.  
Compared with **W10 single-scene SAR**, the GEE SAR workflow extends the analysis into a multi-year VV backscatter time series and allows pre/post-earthquake ΔVV mapping.  
If the exported GeoTIFFs were used in **W12 Random Forest classification**, post-earthquake NDVI, ΔNDVI, and ΔVV could serve as additional predictor layers.  
They would likely help the classifier separate stable vegetation, disturbed slopes, exposed surfaces, and possible landslide-affected areas more effectively than spectral bands alone.

## d. Limitations

GEE is powerful for large-scale preprocessing and time-series analysis, but it is not suitable for every workflow.  
It cannot easily run arbitrary local Python libraries, highly customized machine-learning pipelines, detailed raster editing, or full InSAR processing requiring Sentinel-1 SLC phase data.  
For tasks requiring `rasterio`, `scikit-learn`, custom deep learning, local sample editing, manual QGIS inspection, or non-GEE datasets from external STAC catalogs, the W8–W12 local approach is still preferable.  
Therefore, the best workflow is complementary: use GEE for cloud-scale filtering, compositing, and export, then use local Python or QGIS for customized modeling, validation, visualization, and final interpretation.

## 中文摘要

本週作業共處理 **291 張 Sentinel-2 影像**與 **146 張 Sentinel-1 影像**。若全部下載到本機，資料量約為 **327.1 GB**，以 50 Mbps 網速估計，光下載就可能需要約 **14.9 小時**。GEE 的優勢在於可直接於雲端完成大量影像篩選、雲遮罩、NDVI 計算、SAR 分析與 GeoTIFF 匯出。

結果顯示，整體平均 NDVI 在地震前後變化不大，但 ΔNDVI 空間圖揭示局部植被下降。以 **ΔNDVI < -0.15** 判斷，地震階段植被損失面積約為 **7740.15 ha**，後續階段約為 **6257.68 ha**，累積變化約為 **6839.04 ha**。SAR 分析中，平均 VV 變化僅 **-0.1455 dB**，但 ΔVV map 仍能呈現局部散射變化。結合 NDVI 與 SAR 後，高信度變化區約為 **537.37 ha**。整體而言，W13 的 GEE 流程能將 W8 的單景 NDVI、W9 的兩期變遷偵測、W10 的 SAR 概念與 W12 的分類資料整合成雲端多時相分析流程。
