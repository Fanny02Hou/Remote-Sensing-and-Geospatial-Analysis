
## Task 3 Part A: Internal Accuracy Assessment

Random Forest internal validation was conducted using a stratified 80/20 train-test split of the ROI training samples.

- Overall Accuracy (OA): 0.9770
- Kappa coefficient: 0.9378
- OOB Accuracy: 0.9756
- Test Accuracy: 0.9770
- Macro avg F1: 0.8271
- Weighted avg F1: 0.9760
- Weighted - Macro F1 gap: 0.1488

The confusion matrix and classification report were saved to the output folder. Although the internal accuracy is high, this evaluation is based on ROI-derived samples and may overestimate real-world map accuracy. Therefore, Task 3 Part B will compare the Bare/Landslide class against the independent SWCB landslide inventory.
