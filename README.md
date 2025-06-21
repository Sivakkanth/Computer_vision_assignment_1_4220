# Computer_vision_assignment_1_4220 - EC7212

**Registration Number**: EG/2020/4220
**Date**: 2025-06-16
**Course**: EC7212 – Computer Vision and Image Processing
**Assignment**: Take Home Assignment 1

---

> **Note**: Make sure `image1.jpg` is present inside the `image/` directory for all scripts to run correctly.

---

## Assignment Questions & Descriptions

### Question 1: Reduce Intensity Levels
Reduce the number of grayscale intensity levels in an image to powers of 2 (e.g., 2, 4, 8...).  
A trackbar is used to dynamically adjust the intensity level and view the result.

Script: `question_1.py`  
Libraries: `OpenCV`, `NumPy`

---

### Question 2: Spatial Averaging (Blurring)
Apply spatial averaging filters with kernel sizes:
- 3×3
- 10×10
- 20×20

Used to smooth the image using simple average filtering.

Script: `question_2.py`  
Libraries: `OpenCV`, `NumPy`

---

### Question 3: Rotate Image (Without Cropping)
Rotate an image by:
- 45 degrees
- 90 degrees

The canvas is adjusted so that no part of the image is lost during rotation.

Script: `question_3.py`  
Libraries: `OpenCV`, `NumPy`

---

### Question 4: Block-wise Downsampling
Reduce spatial resolution by averaging **non-overlapping** blocks of:
- 3×3
- 5×5
- 7×7

Each block is replaced with its mean color, simulating resolution reduction.

Script: `question_4.py`  
Libraries: `OpenCV`, `NumPy`

---

## How to Run

### 1. Install Dependencies

pip install opencv-python numpy
