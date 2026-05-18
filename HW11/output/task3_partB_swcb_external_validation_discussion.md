
## Task 3 Part B: Independent Validation with SWCB Landslide Inventory

本研究使用 SWCB 官方新生崩塌地資料作為獨立外部驗證資料，將 Random Forest 分類結果中的 Bare/Landslide 類別與 SWCB 崩塌地範圍進行 pixel-level 比對。結果顯示，Recall 為 0.6096，代表 SWCB 官方崩塌地中約有 61.0% 被 RF Bare/Landslide 類別偵測到。然而，Precision 僅為 0.0070，IoU 為 0.0070，顯示 RF 模型判為 Bare/Landslide 的範圍遠大於 SWCB 官方崩塌地範圍，產生大量 FP。具體而言，RF Bare/Landslide 面積約為 10157.40 ha，而 SWCB rasterized landslide 面積約為 131.84 ha，兩者面積差距非常明顯。

IoU 不可能達到 1.0 的原因包括三個面向。第一，Sentinel-2 影像日期與 SWCB 官方判釋日期可能存在時間差，崩塌地在地震後可能受到降雨、植生恢復、二次崩塌或人為整治影響而改變。第二，Sentinel-2 本次使用 20 m 解析度，而 SWCB 多半依據較高解析度影像或人工判釋資料建立，因此小型崩塌或狹長崩塌邊界在 Sentinel-2 grid 中容易被混合像素平滑化。第三，RF 的 Bare/Landslide 類別定義較廣，可能同時包含道路、河床、裸露土壤、採石地、海岸砂地或亮色人工地表，但 SWCB 資料只代表官方判釋的崩塌地，因此兩者並非完全相同的地物定義。

從 overlay 圖來看，FN 主要可能出現在雲遮罩附近、陰影明顯的山谷、面積較小的崩塌地，或光譜上仍具有植被覆蓋的崩塌區。這些區域可能因為像素混合、陰影降低反射率，或與森林、裸地、農地光譜相近而未被 RF 正確辨識。相反地，大量 FP 表示 RF 將許多非官方崩塌地的裸露或高反射區也判為 Bare/Landslide，這反映出監督式分類雖然在內部測試集上有高 accuracy，但若訓練樣本未能充分代表「官方崩塌地」的嚴格定義，外部驗證結果仍可能明顯下降。

因此，內部測試準確率 0.9770 與 OOB accuracy 0.9756 雖然很高，但這主要反映模型對 ROI 樣本的分類能力；SWCB 外部驗證則更能評估模型在真實災害判釋任務中的可用性。本結果顯示，RF 分類圖可作為災後裸露地與潛在崩塌熱區的初步篩選資料，但若要作為正式崩塌地圖，仍需要進一步改善 ROI 樣本設計、細分 Bare 與 Landslide 類別，並結合 DEM、坡度、地形陰影或更高解析度影像進行修正。
