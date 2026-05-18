
## Task 2: K-means vs Random Forest Comparison

K-means 與 Random Forest 的主要差異在於是否使用訓練樣本。K-means 僅根據六個 Sentinel-2 波段的光譜相似性進行分群，因此 cluster 本身沒有固定地物意義，必須透過平均光譜與影像判讀進行人工解釋。相較之下，Random Forest 使用 Google Earth Pro ROI 訓練樣本建立分類規則，因此輸出結果能直接對應到 Water、Forest、Cropland、Bare/Landslide 與 Built-up 五個土地覆蓋類別。

從空間分布來看，兩者皆能大致分辨海洋水體與山區森林，但 K-means 對於裸地、農地與建物等光譜較相近的類別較容易產生混淆。Random Forest 因為使用了人工標記樣本，因此能更明確地將崩塌地、農地與建物分成不同類別。不過，Random Forest 的結果仍受訓練樣本品質影響，若 ROI 樣本不夠代表研究區完整變異，分類結果可能會出現局部誤判或過度分類。

本研究中，Random Forest 的測試集準確率為 0.9770，OOB accuracy 為 0.9756，顯示監督式分類在訓練樣本設計良好的情況下具有穩定表現。然而，這些內部精度仍須搭配 Task 3 的 SWCB 崩塌地外部驗證，以確認模型對災後裸地／崩塌類別的實際判釋能力。
