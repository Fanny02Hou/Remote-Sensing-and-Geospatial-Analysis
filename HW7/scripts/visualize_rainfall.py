# ============================================================
# Visualize Original Rainfall Data
# ============================================================

import rasterio
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Load the rainfall raster
KRIGING_RAINFALL_PATH = Path("../data/kriging_rainfall.tif")

if KRIGING_RAINFALL_PATH.exists():
    with rasterio.open(KRIGING_RAINFALL_PATH) as src:
        print("✅ Rainfall raster opened")
        print(f"Raster CRS: {src.crs}")
        print(f"Raster bounds: {src.bounds}")
        print(f"Raster shape: {src.shape}")
        print(f"Raster nodata: {src.nodata}")
        
        # Read the data
        rainfall_data = src.read(1)
        
        # Mask nodata values
        if src.nodata is not None:
            rainfall_data = np.where(rainfall_data == src.nodata, np.nan, rainfall_data)
        
        print(f"\n--- Rainfall Statistics ---")
        print(f"Min: {np.nanmin(rainfall_data):.6f} mm/hr")
        print(f"Max: {np.nanmax(rainfall_data):.6f} mm/hr")
        print(f"Mean: {np.nanmean(rainfall_data):.6f} mm/hr")
        print(f"Std: {np.nanstd(rainfall_data):.6f} mm/hr")
        print(f"Non-null pixels: {np.sum(~np.isnan(rainfall_data))}")
        
        # Create visualization
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Plot 1: Rainfall values
        im1 = ax1.imshow(rainfall_data, cmap='Blues', aspect='auto')
        ax1.set_title('Rainfall Data (mm/hr)')
        ax1.set_xlabel('Column')
        ax1.set_ylabel('Row')
        plt.colorbar(im1, ax=ax1, label='Rainfall (mm/hr)')
        
        # Plot 2: Histogram
        valid_data = rainfall_data[~np.isnan(rainfall_data)]
        ax2.hist(valid_data, bins=50, alpha=0.7, color='blue', edgecolor='black')
        ax2.set_title('Rainfall Distribution')
        ax2.set_xlabel('Rainfall (mm/hr)')
        ax2.set_ylabel('Frequency')
        ax2.grid(True, alpha=0.3)
        
        # Add statistics text
        stats_text = f"Min: {np.nanmin(rainfall_data):.4f}\nMax: {np.nanmax(rainfall_data):.4f}\nMean: {np.nanmean(rainfall_data):.4f}"
        ax2.text(0.02, 0.98, stats_text, transform=ax2.transAxes, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        
        plt.tight_layout()
        plt.show()
        
        # Check threshold values
        print(f"\n--- Threshold Analysis ---")
        CONGESTION_BREAK_1 = 10.0
        CONGESTION_BREAK_2 = 40.0
        CONGESTION_BREAK_3 = 80.0
        
        below_10 = np.sum(valid_data < CONGESTION_BREAK_1)
        between_10_40 = np.sum((valid_data >= CONGESTION_BREAK_1) & (valid_data < CONGESTION_BREAK_2))
        between_40_80 = np.sum((valid_data >= CONGESTION_BREAK_2) & (valid_data < CONGESTION_BREAK_3))
        above_80 = np.sum(valid_data >= CONGESTION_BREAK_3)
        
        print(f"Values < {CONGESTION_BREAK_1} mm/hr (cf=0.0): {below_10} ({below_10/len(valid_data)*100:.1f}%)")
        print(f"Values {CONGESTION_BREAK_1}-{CONGESTION_BREAK_2} mm/hr (cf=0.3): {between_10_40} ({between_10_40/len(valid_data)*100:.1f}%)")
        print(f"Values {CONGESTION_BREAK_2}-{CONGESTION_BREAK_3} mm/hr (cf=0.6): {between_40_80} ({between_40_80/len(valid_data)*100:.1f}%)")
        print(f"Values >= {CONGESTION_BREAK_3} mm/hr (cf=0.9): {above_80} ({above_80/len(valid_data)*100:.1f}%)")

else:
    print(f"❌ Rainfall raster not found: {KRIGING_RAINFALL_PATH}")
