**DCT Image Compression**

A Python application that demonstrates image compression using the "Discrete Cosine Transform (DCT)", the same fundamental technique used in JPEG image compression. The application allows users to upload an image, apply DCT-based compression, and compare the original image with the reconstructed compressed image.

**Project Overview**

Digital images can be represented in the frequency domain using the Discrete Cosine Transform. By retaining only the most significant frequency coefficients and discarding less important ones, image data can be compressed while preserving much of the visual quality.

This project applies DCT compression to both grayscale and color images and reconstructs the image using the Inverse Discrete Cosine Transform (IDCT).

## Features

* Upload images through a graphical interface.
* Supports JPG, JPEG, PNG, BMP, TIFF, and TIF formats.
* Performs two-dimensional DCT transformation.
* Removes low-magnitude frequency coefficients for compression.
* Reconstructs images using IDCT.
* Displays original and compressed images side-by-side.
* Supports both grayscale and RGB color images.

## Technologies Used

* Python
* NumPy
* SciPy
* Scikit-Image
* Matplotlib
* Tkinter

## How It Works

1. The user selects an image from their computer.
2. The image is resized to improve processing speed.
3. A 2D Discrete Cosine Transform (DCT) is applied.
4. Small frequency coefficients are removed using thresholding.
5. The image is reconstructed using the Inverse DCT (IDCT).
6. The original and compressed images are displayed for comparison.

## Installation

Clone the repository:

```bash
git clone https://github.com/sserwanja11-code/dct-image-compression.git
cd dct-image-compression
```

Install the required packages:

```bash
pip install numpy scipy scikit-image matplotlib
```

## Running the Application

```bash
python cmpapp.py
```

Click the **"Add Picture"** button and select an image to begin compression.

## Learning Outcomes

This project demonstrates:

* Frequency-domain image processing
* Discrete Cosine Transform (DCT)
* Inverse Discrete Cosine Transform (IDCT)
* Image compression principles
* GUI development in Python
* Practical concepts behind JPEG compression

## Future Improvements

* Adjustable compression levels
* Compression ratio analysis
* PSNR and quality metrics
* Block-based JPEG compression (8×8 DCT)
* Web-based deployment

## Author

**Adrian Sserwanja**
Bachelor of Science in Software Engineering
Mbarara University of Science and Technology (MUST)

