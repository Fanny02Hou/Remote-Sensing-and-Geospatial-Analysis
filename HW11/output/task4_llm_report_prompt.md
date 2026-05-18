
你是花蓮縣災害應變中心的 GIS 分析師。根據以下災後土地覆蓋分類結果，
撰寫一份「災後土地覆蓋分析報告」（中文，300–500 字）。

研究區：秀林鄉／太魯閣周邊，包含山區、蘇花公路沿線與近海區域
災害事件：2024 年 4 月 3 日花蓮地震
資料來源：Sentinel-2 L2A 多光譜影像
影像日期：2024-08-27T02:25:31.024000Z
分類方法：Random Forest，使用 B02、B03、B04、B08、B11、B12 六個波段
分類類別：Water、Forest、Cropland、Bare/Landslide、Built-up

內部精度評估：
- Overall Accuracy: 0.9770
- Kappa: 0.9378
- Test Accuracy: 0.9770
- OOB Accuracy: 0.9756

SWCB 官方崩塌地外部驗證：
- Recall: 0.6096
- Precision: 0.0070
- IoU: 0.0070
- SWCB rasterized landslide area: 131.84 ha
- RF Bare/Landslide area: 10157.40 ha

各類別面積統計：
 class_id     class_name class_name_zh  pixels  area_ha  area_km2  percentage
        0          Water            水體  559023 22360.92  223.6092       35.07
        1         Forest            森林  698124 27924.96  279.2496       43.80
        2       Cropland            農地   78244  3129.76   31.2976        4.91
        3 Bare/Landslide         裸地/崩塌  253935 10157.40  101.5740       15.93
        4       Built-up            建物    4554   182.16    1.8216        0.29

報告需包含：
1. 災後土地覆蓋概況。
2. 崩塌／裸地面積估計及其空間分布。
3. 與 SWCB 官方判釋結果的比對，以及不確定性說明。
4. 這張分類圖如何支援後續避難所評估或路網可達性分析。
5. 不可以捏造沒有提供的數字；所有面積與精度必須依照上方資料描述。
