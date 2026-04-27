## 7. Week 8 vs. Week 9 Comparison

### 7.1 Week 8 and Week 9 Interpretation Framework

本段比較重點不在於列舉單一受影響項目，而是比較 Week 8 與 Week 9 對災害範圍的判別方式。Week 8 主要依賴目視判讀、災害圖層疊合與情境式解釋，適合快速建立災害影響的初步認知；Week 9 則進一步加入多光譜差值指標、SCL 雲遮罩、門檻最佳化、驗證點與精度指標，因此能對 Week 8 的初步判讀進行量化確認與不確定性評估。

### 7.2 Comparison Table

| Layer | W8 Finding | W9 Validated Finding | Agreement | Notes |
| --- | --- | --- | --- | --- |
| Vegetation Impact | Week 8 主要依據目視判讀與災害圖層疊合結果，以現象式方式判斷植被或地表是否可能受到擾動。此方法可快速指出疑似受損區，但尚未透過樣本驗證或精度指標量化其可靠性。 | Week 9 以 ΔNDVI 量化植被下降，並透過驗證點進行 threshold optimization。最佳判別門檻為 delta_ndvi_post < -0.100；高信心變化區為 32.891 km²，低信心變化區為 15.961 km²。精度結果為 OA=79.6%、PA=69.0%、UA=90.9%、F1=0.784。 | 部分一致 | W8 與 W9 都指出植被或地表擾動是重要災害訊號；差異在於 W8 偏向快速目視判讀，W9 則以 ΔNDVI 門檻、驗證點與精度指標進行量化確認。 |
| Water Inundation | Week 8 主要依據水體相關圖層與目視判讀來辨識可能的淹水或堰塞湖影響。此方法適合快速掌握水體變化位置，但較容易受到雲、陰影、濕地或影像品質差異影響。 | Week 9 以 ΔNDWI 分析水體變化，並使用 SCL intersection mask 排除雲、雲影與無效像元。phantom water comparison 顯示，若未套用遮罩，raw ΔNDWI 可能產生約 21.293 km² 的潛在假水體訊號，因此 W9 對水體變化的判讀較重視資料品質控制。 | 部分一致 | W8 可快速辨識疑似水體變化，但 W9 顯示若缺乏 SCL cloud masking，水體訊號可能被 phantom water 高估；因此 W9 對水體判讀提供較嚴格的品質控制。 |
| Debris Field | Week 8 主要依據崩塌、土砂或地表裸露的目視特徵進行 debris field 判讀。此方法可快速建立災害初步範圍，但對於 debris、裸露地與其他地表擾動的區分仍較依賴人工解釋。 | Week 9 以 ΔBSI 與 NDVI-loss 輔助判讀裸露土砂與地表擾動，其中 ΔBSI Pre→Post 最大值為 0.403。然而，本次精度驗證採二元 Change / No Change，因此 W9 對 debris field 的判讀仍屬間接支持，並非獨立 debris 類別分類。 | 部分一致 | W8 的 debris field 判讀較依賴目視特徵與災害脈絡，W9 則以 ΔBSI 與 NDVI-loss 提供光譜證據。不過，W9 尚未建立獨立 debris 類別驗證，因此結果應視為輔助支持而非完全確認。 |

### 7.3 Analysis

Week 9 的量化驗證大致支持 Week 8 的目視判讀方向，特別是在植被下降、地表擾動與水體變化等主要災害訊號上；但兩者最大的差異在於，Week 8 偏向以目視判讀與圖層疊合建立快速災害認知，Week 9 則進一步以 ΔNDVI 門檻、驗證點與混淆矩陣評估結果的可靠性。

精度指標顯示 Week 9 的結果較適合用來確認已偵測到的變化區，而不適合單獨用來排除所有災害影響；UA 為 90.9%，表示被判定為變化的區域大多可信，但 PA 為 69.0%，代表仍有部分實際變化可能被漏判。

在水體判讀方面，Week 9 的 phantom water comparison 顯示若缺乏 SCL 雲與雲影遮罩，raw ΔNDWI 可能產生約 21.293 km² 的潛在假水體訊號，因此 Week 9 相較於 Week 8 更能指出水體目視判讀可能高估或不確定的位置。

整體而言，Week 9 提高了對核心災害範圍的信心，尤其是 32.891 km² 的高信心變化區；但它也使解釋更保守，低信心區、No Detection 區與 SCL 遮罩區仍需搭配後續影像、現地資料或其他感測器資料查核。