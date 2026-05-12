# Week 12 Pre-Lab: Image Classification & Land Cover Mapping — ARIA v8.0 Setup

**Course:** NTU Remote Sensing & Spatial Information Analysis (遙測與空間資訊之分析與應用)  
**Instructor:** Prof. Su Wen-Ray  
**Week:** 12 | **Theme:** Image Classification & Land Cover Identification（影像分類與地物辨識）  
**Time Required:** ~20 minutes

---

## Objectives

By the end of this pre-lab, you will:
- Verify your W8–W10 STAC API environment is still functional
- Install classification-specific packages (scikit-learn, if not already present)
- Understand the conceptual leap from **index thresholding** to **classification**
- Review unsupervised (K-means) and supervised (Random Forest) classification concepts
- Prepare to connect classification results with W9's confusion matrix framework

---

## Step 1: Verify Environment

### 1a. Colab or Local Environment

This week **does not require a GPU**. Traditional classifiers (K-means, Random Forest) run efficiently on CPU.（本週不需要 GPU，傳統分類器在 CPU 上即可快速執行。）

```python
# Colab users
from google.colab import drive
drive.mount('/content/drive')

# Or use your local environment (same conda/venv from W8–W10)
```

### 1b. Confirm Key Packages

```python
import pystac_client
import planetary_computer as pc
import stackstac
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
import rasterio
import geopandas as gpd

print("✓ pystac_client:", pystac_client.__version__)
print("✓ scikit-learn:", __import__('sklearn').__version__)
print("✓ All core dependencies loaded successfully")
```

If any import fails:

```bash
pip install pystac_client stackstac planetary-computer scikit-learn rasterio geopandas
```

---

## Step 2: The Conceptual Leap — Why Classification?

### What W8–W10 achieved（W8–W10 做了什麼）

In previous weeks we relied on **thresholding**（閾值法）— a single index, a single cutoff, two classes:

| Week | Method | Logic | Limitation |
|------|--------|-------|------------|
| W8 | NDVI > 0.4 → vegetation | Human picks one threshold | Only 2 classes（只能分兩類） |
| W9 | ΔNDVI > T → change | Human picks a difference threshold | Cannot tell *what* changed |
| W10 | VV < −18 dB → water | Human picks a SAR threshold | Only water / non-water |

**Core limitation:** Thresholding uses one index at a time and can only separate two classes. But the real world has many land cover types: water, forest, bare soil, built-up, cropland, landslide debris…（真實世界有很多類別）

### What W12 upgrades（W12 升級什麼）

**Classification** uses **multiple bands simultaneously** to assign each pixel to a **land cover class**:

```
Thresholding:   NDVI (one number)           → is / is not vegetation
Classification: [B2, B3, B4, B8, B11, B12] → water / forest / bare / built-up / cropland / landslide
```

**Upgrade path（升級邏輯）:**
```
W8–W10   Thresholding (human rules, one index at a time)
   ↓
W12a     Unsupervised classification (machine finds clusters: K-means)
   ↓
W12b     Supervised classification (human provides examples, machine learns rules: Random Forest)
```

---

## Step 3: Feature Space — Concept Review

### What is Feature Space?（什麼是特徵空間？）

Each pixel has multiple band values, forming a "multi-dimensional coordinate":

| Band | Physical meaning | Role in feature space |
|------|------------------|-----------------------|
| B2 (Blue) | Blue reflectance（藍光反射率） | Dimension 1 |
| B3 (Green) | Green reflectance（綠光反射率） | Dimension 2 |
| B4 (Red) | Red reflectance（紅光反射率） | Dimension 3 |
| B8 (NIR) | Near-infrared reflectance（近紅外反射率） | Dimension 4 |
| B11 (SWIR1) | Shortwave infrared（短波紅外） | Dimension 5 |
| B12 (SWIR2) | Shortwave infrared（短波紅外） | Dimension 6 |

**Key intuition:** In this 6-dimensional space, pixels of the same land cover type tend to **cluster together**（同類地物的像素會「聚在一起」）.

- Water: low NIR, low SWIR → clusters in the lower-left corner
- Vegetation: high NIR, low Red → clusters in the upper-right corner
- Bare soil: moderate values across all bands → clusters in the middle

Classification is essentially **drawing boundaries in feature space**（在特徵空間中劃分區域）.

---

## Step 4: K-means — Unsupervised Classification

### Core Concept

**Unsupervised** = no human-labeled examples required; the machine finds clusters on its own（不需要人類提供範例，機器自己找分群）.

**K-means algorithm:**
1. Randomly place K "centroids" in feature space（隨機放 K 個中心點）
2. Assign each pixel to the nearest centroid（每個像素分配到最近的中心點）
3. Recompute each cluster center as the mean of its members（重新計算每群的中心）
4. Repeat steps 2–3 until convergence（重複直到收斂）

**You decide:** K (how many clusters)

**Pros:** Fast; no training data needed  
**Cons:** Clusters may not correspond to real land cover types; K must be guessed

### Self-Test Q1

What land cover type does "Cluster 3" represent in a K-means result?

**Answer:** You don't know. K-means only gives cluster *numbers*, not names. You must manually interpret each cluster based on its spectral signature. That is what "unsupervised" means — the machine has no knowledge of real-world labels.（K-means 只給編號，不會告訴你這是水還是森林。）

---

## Step 5: Random Forest — Supervised Classification

### Core Concept

**Supervised** = human provides labeled examples (training samples), and the machine learns classification rules from them（人類提供「標記好的範例」，機器從中學習規則）.

**Random Forest algorithm:**
1. Randomly sample a subset of training data（隨機抽取子集）
2. Build a decision tree (e.g., "if NIR > 0.3 and Red < 0.1 → vegetation")
3. Repeat steps 1–2 to build many trees (100+ trees)（建立 100+ 棵樹）
4. For prediction, all trees vote; majority wins（所有樹投票，多數決）

**You prepare:** Training samples — representative pixels for each class（每個類別的像素範例）

**Pros:** Output labels correspond to real land cover classes; typically more accurate than K-means  
**Cons:** Requires human-labeled training data (labor-intensive)

### Self-Test Q2

Why is it called a "Forest"?

**Answer:** Because it consists of many decision trees (typically 100–500). Each tree is trained on a different random subset of features and samples, and the final prediction is a majority vote. "Random" refers to the randomness in both feature and sample selection.（每棵樹用不同的隨機子集訓練，最後多數決。）

---

## Step 6: Confusion Matrix — Second Encounter

### W9 vs W12 Confusion Matrix

| | W9 (Change Detection) | W12 (Image Classification) |
|---|---|---|
| Purpose | Evaluate change / no-change detection accuracy | Evaluate multi-class classification accuracy |
| Number of classes | 2 (changed / unchanged) | N (water / forest / bare / built-up…) |
| Key metrics | Producer's / User's accuracy | Same, but **per class** |
| Disaster relevance | Missed change = omission（漏報） | Landslide classified as forest = omission（崩塌地被分成森林 = 漏報） |

**Pedagogical link:** In W9 you learned the 2×2 confusion matrix. W12 upgrades it to N×N. The concepts are identical, but the information content is much richer.（W9 的 2×2 升級到 W12 的 N×N，概念一樣，資訊量更大。）

### Self-Test Q3

How large is a confusion matrix for a 5-class classification?

**Answer:** 5×5. The diagonal contains correctly classified pixels; off-diagonal cells represent misclassifications. Each row sums to the total validation samples for that class.

---

## Step 7: Self-Test — Synthesis

### Q4: Thresholding vs K-means vs Random Forest

Complete the table:

| Property | Thresholding | K-means | Random Forest |
|----------|-------------|---------|---------------|
| Requires training data? | ❌ | ❌ | ✅ |
| Requires human-defined K? | N/A | _____ | N/A |
| Uses multiple bands simultaneously? | ❌ (one index at a time) | _____ | _____ |
| Output has class names? | Yes (human-defined) | _____ | _____ |
| Number of output classes | 2 | _____ | _____ |

**Answers:** K-means requires K = ✅; multi-band = ✅; class names = ❌ (only cluster IDs); output classes = K. Random Forest: multi-band = ✅; class names = ✅ (from training data); output classes = however many classes exist in the training data.

### Q5: Feature Space Thinking

Why does classification using 6 bands (B2–B4, B8, B11–B12) typically outperform classification using only RGB (B2–B4)?

**Answer:** More dimensions = more discriminative information. The NIR and SWIR bands carry physical signals about vegetation structure and moisture content that are invisible in RGB. For example, healthy and stressed vegetation may appear similar in RGB but differ greatly in NIR.（NIR 和 SWIR 提供植被和水分的物理訊號，在 RGB 中看不到。）

---

## Step 8: Reflection Questions (Optional)

1. **How to choose K in K-means?** If the study area has 5 known land cover types, should you set K = 5? (Hint: a single land cover type may have multiple spectral sub-classes.)（同一種地物可能有多個光譜變異）

2. **Training sample quality:** If all your training samples come from the city center, will the classifier perform well in rural areas? Why or why not?（訓練樣本的空間代表性）

3. **Classification + W10 fusion:** If Random Forest identifies "landslide" pixels, and W10 SAR confirms anomalous backscatter in the same area, how does this relate to the concept of sensor fusion?（分類結果 + SAR 的交叉驗證）

---

## Checklist Before Class

- [ ] STAC API environment (pystac_client, stackstac, planetary_computer) works correctly
- [ ] scikit-learn installed (KMeans, RandomForestClassifier importable)
- [ ] Understand feature space concept (multiple bands = multi-dimensional coordinates)
- [ ] Understand K-means (unsupervised: machine clusters on its own) vs Random Forest (supervised: human provides labeled examples)
- [ ] Understand how confusion matrix upgrades from W9's 2×2 to W12's N×N
- [ ] Completed Self-Test (5 questions)
- [ ] Optional: reflected on K selection and training sample quality

**You're ready for Week 12!**

---

*Note: If you encounter any environment issues, post on NTUCool or email Prof. Su before class.*
