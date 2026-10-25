# Image Processing for Guitar Note Segmentation

A research project combining **Machine Audition**, **Image Processing**, and **Computer Vision** for segmenting guitar notes from time-frequency representations (Spectrograms, CQT, Scalograms).

## Project Structure

```text
Machine Audition/
├── data/                      # Dataset directory (ignored in git)
│   ├── raw/                   # Raw audio & annotations (e.g. GAPS dataset)
│   └── processed/             # Generated spectrograms and ground-truth segmentation masks
├── scripts/                   # Utility scripts (downloading, data validation)
│   └── download_gaps.py
├── src/                       # Core algorithm modules
│   ├── audio/                 # Audio processing & time-frequency transformation (STFT, CQT, Mel)
│   ├── image_processing/      # Image filtering, morphological operations, contour detection
│   ├── vision_models/         # Deep learning vision models (U-Net, Mask R-CNN, etc.)
│   └── evaluation/            # Evaluation metrics (IoU, Dice, Note Onset/Offset F1)
├── notebooks/                 # Jupyter notebooks for visual experiments
├── requirements.txt           # Project dependencies
└── README.md
```

## Getting Started

### 1. Installation
Clone the repository and install required dependencies:
```bash
pip install -r requirements.txt
```

### 2. Download Dataset
Download the GAPS dataset using the provided script:
```bash
python scripts/download_gaps.py
```
