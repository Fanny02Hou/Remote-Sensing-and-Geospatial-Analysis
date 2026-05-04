# Week 10 Homework: ARIA v7.0 — All-Weather Flood Detection System

## 作業目的

本次作業旨在建立 **ARIA v7.0 全天候稽查系統**，解決光學遙測在颱風期間雲層遮蔽的局限性。透過整合合成孔徑雷達 (SAR) 與光學感測器資料，實現不受天氣影響的洪水偵測能力，並結合地形分析與 AI 策略簡報，提供決策支援資訊。

**案例研究：** 花蓮地區，颱風鳳凰 (Typhoon Fung-wong) 期間的洪水監測

## 完成任務內容

### ✅ Task 1: SAR 全天候洪水偵測 (25%)
- **SAR 資料載入與處理：** 成功載入 Sentinel-1 GRD 資料，應用中值濾波 (5×5 kernel) 降低斑點雜訊
- **閾值分割：** 使用 -14.0 dB 閾值進行水體提取，並應用形態學開運算與連通元件過濾清理假水體
- **面積計算：** 精確計算洪水覆蓋面積，輸出統計資訊與視覺化成果
- **輸出：** 2×2 子圖展示原始 SAR、濾波後 SAR、二值洪水遮罩及疊加圖

### ✅ Task 2: 感測器融合 — 多源確信度地圖 (30%)
- **融合邏輯實現：** 建立四級確信度分類系統
  - **高確信度 (High Confidence)：** 光學 NDWI + SAR 雙重證據
  - **SAR 僅雲層區 (SAR Only Cloudy)：** SAR 穿透雲層偵測
  - **光學僅 (Optical Only)：** 僅光學偵測，需人工檢核
  - **無偵測 (No Detection)：** 無水體證據
- **網格對齊：** 使用 `reproject_mask_to_match` 函數確保 SAR 與光學資料空間一致性
- **面積統計：** 計算各確信度級別的面積，輸出詳細統計表格

### ✅ Task 3: 地形分析 — DEM 與坡度評估 (20%)
- **坡度資料處理：** 載入並對齊 DEM 衍生坡度圖至 SAR 網格
- **地形過濾：** 應用 25° 坡度閾值排除陡坡上不可能的洪水偵測
- **形態學清理：** 針對 DEM 不適用地區，使用連通元件過濾替代地形校正
- **前後對比：** 量化地形過濾移除的假陽性像素數量與面積

### ✅ Task 4: AI 策略簡報 + ARIA v7.0 報告 (25%)

#### Part A: AI 策略簡報 (15%)
- **關鍵指標整理：** 提取高確信度洪水面積、SAR 僅雲層區面積、假陽性移除面積等核心指標
- **LLM 互動：** 使用 Gemini API 生成花蓮縣緊急管理策略簡報
- **反思分析：** 評估 AI 簡報的準確性與局限性，強調決策支援而非最終撤離邊界

#### Part B: ARIA v7.0 演進報告 (10%)
- **W9 vs W10 比較：** 量化展示光學僅偵測與融合偵測的差異
- **改進分析：** 突顯 SAR 在雲層覆蓋區的補強能力與確信度分級的精細化

## 環境設定 (.env 配置)

### 必要參數設定

```bash
# 基本資料夾設定
DATA_DIR=data
OUTPUT_DIR=output

# 研究範圍 (花蓮地區)
BBOX_WEST=121.28
BBOX_SOUTH=23.56
BBOX_EAST=121.52
BBOX_NORTH=23.76

# 投影與解析度設定
TARGET_EPSG=32651
TARGET_RESOLUTION=10.0

# Sentinel-2 光學設定
S2_COLLECTION=sentinel-2-l2a
S2_PRE_START=2025-11-01
S2_PRE_END=2025-11-10
S2_POST_START=2025-11-13
S2_POST_END=2025-11-15
S2_MAX_CLOUD=100
S2_GREEN_BAND=B03
S2_NIR_BAND=B08
S2_SCL_BAND=SCL
NDWI_THRESHOLD=0.0
SCL_CLEAR_CLASSES=2,4,5,6,7,11

# Sentinel-1 SAR 設定
S1_COLLECTION=sentinel-1-rtc
S1_PRE_START=2025-11-01
S1_PRE_END=2025-11-10
S1_POST_START=2025-11-13
S1_POST_END=2025-11-15
SAR_POLARIZATION=vv
SAR_ORBIT_MODE=auto_same
REQUIRE_SAME_RELATIVE_ORBIT=true
PREFERRED_ORBIT=auto
SAR_THRESHOLD=-14.0
MEDIAN_FILTER_SIZE=5
APPLY_MORPHOLOGY=true
MORPH_KERNEL_SIZE=3
MIN_WATER_AREA_HA=0.5
MIN_WATER_PIXELS=50

# DEM 地形設定
DEM_COLLECTION=cop-dem-glo-30
COMPUTE_DEM_SLOPE=true
APPLY_DEM_SLOPE_FILTER=false
SLOPE_THRESHOLD=25.0

# 融合設定
REFERENCE_GRID=post_sar
FUSION_MODE=change_based

# STAC API 設定
STAC_API=https://planetarycomputer.microsoft.com/api/stac/v1

# AI API 設定 (擇一設定)
AI_API_KEY=your_gemini_api_key_here
# 或
# GEMINI_API_KEY=your_gemini_api_key_here
# 或
# GOOGLE_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.0-flash
```
### 重要注意事項
 
1. **API 金鑰安全：** `.env` 檔案包含敏感資訊，**切勿提交至 GitHub**
2. **閾值調整：** 
   - `NDWI_THRESHOLD=0.0` 適合濁水災害情境
   - `SAR_THRESHOLD=-14.0` 為花蓮案例最佳值 (一般 ARIA 預設 -18 dB)
3. **地形過濾：** `APPLY_DEM_SLOPE_FILTER=false` 因災後地形可能改變，改用形態學清理
4. **執行順序：** 請依 Cell 1→Cell 2→...→Cell 11 順序執行，確保變數依賴關係正確
 
## 技術特色
 
- **全天候能力：** SAR 穿透雲層，解決光學遙測天氣限制
- **多源融合：** 整合光學、SAR、DEM 三種資料來源
- **確信度分級：** 四級分類系統提供決策支援層級資訊
- **AI 增強：** 結合大型語言模型生成策略簡報
- **地形審計：** 排除陡坡假陽性，提升物理合理性
 
## 執行環境需求

```bash
# 核心套件
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.5.0
rasterio>=1.3.0
rioxarray>=0.11.0
xarray>=0.20.0
scipy>=1.7.0

# 遙測與 STAC
pystac-client>=0.7.0
planetary-computer>=0.5.0
stackstac>=0.4.0

# AI 互動
google-generativeai>=0.3.0
python-dotenv>=0.19.0
```

## 執行步驟

1. 設定 `.env` 檔案
2. 執行 Jupyter Notebook Cell 1-11
3. 檢視輸出結果與報告

## 本作業成功實現了從光學僅偵測到全天候融合系統的技術躍遷，為災害應急管理提供了更可靠的遙測決策支援工具。