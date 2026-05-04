# Week 10: SAR & Sensor Fusion — All-Weather Monitoring

**Course:** NTU Remote Sensing & Spatial Information Analysis (遙測與空間資訊之分析與應用)  
**Instructor:** Prof. Su Wen-Ray  
**Week:** 10 | **Theme:** All-Weather Monitoring & Sensor Fusion  
**Date:** 2026 Spring

## 📋 Overview

This exercise focuses on **Synthetic Aperture Radar (SAR) data processing** and **sensor fusion** techniques for all-weather disaster monitoring. Students will learn to combine SAR data with optical imagery to achieve reliable flood detection, especially during adverse weather conditions when optical sensors are limited by cloud cover.

## 🎯 Learning Objectives

By completing this exercise, you will:

- ✅ Understand SAR physics and radar backscatter mechanisms
- ✅ Process Sentinel-1 SAR data using STAC API streaming
- ✅ Perform SAR water detection using thresholding and morphological processing
- ✅ Implement sensor fusion between SAR and optical data
- ✅ Create confidence maps for flood detection
- ✅ Analyze landslide dam (堰塞湖) formation and evolution

## 📁 Project Structure

```
Exercise10/
├── README.md                    # This file
├── prelab_w10.md               # Pre-lab preparation guide
├── data/                       # Data directory (empty for streaming)
├── output/                     # Generated analysis results
│   ├── W10_L1_sar_flood.png
│   ├── W10_L2_confidence_map.png
│   ├── W10_optical_vs_sar.png
│   ├── W10_sar_before_after.png
│   └── threshold_test.png
└── script/
    ├── prelab_w10.ipynb        # Pre-lab setup notebook
    └── Week10-Student.ipynb    # Main exercise notebook
```

## 🛠️ Prerequisites

### Required Python Packages
```bash
pip install pystac_client stackstac scikit-learn rasterio rioxarray
pip install numpy matplotlib scipy xarray planetary-computer
```

### Environment Setup
- Activate your Week 8/9 virtual environment
- Verify all packages are installed (see prelab guide)
- Ensure Week 9 optical results are accessible for homework

## 📚 Key Concepts

### SAR Physics
- **Active Remote Sensing**: Satellite emits and measures microwave pulses
- **Backscatter Mechanisms**: 
  - Specular reflection (water): < -20 dB
  - Volume scattering (vegetation): -8 to -3 dB
  - Double-bounce (buildings): > 0 dB
- **All-Weather Capability**: Works through clouds, rain, and at night

### Sensor Fusion Logic
- **High Confidence**: Both optical and SAR indicate water
- **Medium Confidence**: Only one sensor indicates water
- **Low Confidence**: Sensors disagree (requires expert interpretation)

## 🚀 Getting Started

### 1. Pre-Lab Preparation
1. Read `prelab_w10.md` thoroughly
2. Complete the dB conversion self-test
3. Review SAR vs. Optical comparison table
4. Verify Week 9 optical outputs are ready

### 2. Lab Exercise
1. Open `script/Week10-Student.ipynb`
2. Execute cells sequentially
3. Follow the guided analysis pipeline
4. Generate required outputs in the `output/` directory

### 3. Homework Assignment
1. Use your Week 9 optical results
2. Apply sensor fusion techniques
3. Analyze Typhoon Fenghuang case (Hualien)
4. Submit confidence maps and analysis

## 📊 Data Sources

### Primary Data
- **Sentinel-1 SAR**: C-band, 10m resolution, RTC processed
- **Sentinel-2 Optical**: Multi-spectral, 10m resolution
- **Copernicus DEM**: 30m global elevation model

### Access Methods
- **STAC API**: Real-time streaming from Microsoft Planetary Computer
- **Pre-processed**: Homework uses prepared GeoTIFF files

## 🔍 Analysis Pipeline

### SAR Water Detection
1. **Data Acquisition**: Stream Sentinel-1 RTC data via STAC
2. **Preprocessing**: Convert linear to dB scale
3. **Thresholding**: Apply water detection threshold (-14 dB)
4. **Morphological Processing**: Remove noise with opening operation
5. **Validation**: Compare with optical water masks

### Sensor Fusion
1. **Data Alignment**: Ensure spatial and temporal consistency
2. **Confidence Mapping**: Create multi-level confidence maps
3. **Change Detection**: Identify flood extent changes
4. **Validation**: Cross-validate with ground truth data

## 📈 Expected Outputs

### Lab Results
- SAR water detection maps
- Before/after flood comparison
- Optical vs. SAR comparison plots
- Threshold optimization analysis

### Homework Results
- Sensor fusion confidence maps
- Typhoon Fenghuang flood analysis
- Quantitative accuracy assessment
- Interpretation report

## 🎓 Learning Outcomes

Upon completion, students will be able to:

- Process SAR data from raw to analysis-ready products
- Implement robust water detection algorithms
- Perform multi-sensor data fusion
- Design all-weather disaster monitoring systems
- Critically evaluate sensor limitations and uncertainties

## 🔧 Technical Notes

### SAR Processing Considerations
- **Orbit Direction**: Use consistent ascending/descending orbits
- **Speckle Filtering**: Apply median filter to reduce noise
- **Threshold Selection**: Optimize for specific environmental conditions
- **Geometric Consistency**: Maintain same viewing geometry for time series

### Common Issues & Solutions
- **Data Access**: Use retry mechanisms for STAC API calls
- **Memory Management**: Process large datasets in chunks
- **Coordinate Systems**: Ensure consistent CRS across datasets
- **Quality Control**: Validate results with multiple methods

## 📖 References

- European Space Agency. (2023). *Sentinel-1 User Guide*
- Copernicus. (2023). *Sentinel-2 MSI User Guide*
- Microsoft. (2023). *Planetary Computer STAC API Documentation*
- ARIA Project. (2023). *SAR Flood Detection Guidelines*

## 🤝 Support

- **Course Forum**: NTUCool discussion board
- **Email**: Prof. Su Wen-Ray
- **Office Hours**: As announced in class

---

**Note:** This exercise builds upon concepts and skills developed in Weeks 8-9. Ensure you have completed those exercises before proceeding.

**Last Updated:** April 2026