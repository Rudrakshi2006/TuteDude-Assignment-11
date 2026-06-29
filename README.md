# OpenCV Practicals

## Objective

The objective of this assignment is to learn basic image and video processing using the OpenCV library in Python. The practicals demonstrate how to perform common computer vision operations such as image manipulation, transformations, filtering, edge detection, and video processing.

---

## Requirements

Install the required libraries before running the programs.

```bash
pip install opencv-python numpy
```

---

## Folder Structure

```
OpenCVPracticals-Rudrakshi
│
├── image1.jpg
├── sample_video.mp4
├── 1_read_write_image.py
├── 2_resize_image.py
├── 3_flip_image.py
├── 4_shapes_text.py
├── 5_translation.py
├── 6_rotation.py
├── 7_threshold.py
├── 8_blur.py
├── 9_morphology.py
├── 10_canny.py
├── 11_video_read_write.py
├── 12_webcam.py
├── Screenshots.pdf
└── README.md
```

---

## Practicals Included

### 1. Read, Display and Save Image
- Read an image using OpenCV
- Display the image
- Save the image

### 2. Resize Image
- Resize image using `cv2.resize()`

### 3. Flip Image
- Horizontal Flip
- Vertical Flip
- Both Directions

### 4. Draw Shapes and Add Text
- Draw Line
- Draw Polygon
- Add Text

### 5. Image Translation
- Shift image using `warpAffine()`

### 6. Image Rotation
- Rotate image using `getRotationMatrix2D()`

### 7. Binary Thresholding
- Apply binary threshold on grayscale image

### 8. Image Blurring
- Gaussian Blur
- Median Blur

### 9. Morphological Operations
- Top Hat
- Black Hat

### 10. Edge Detection
- Canny Edge Detection

### 11. Video Processing
- Read Video
- Write Video

### 12. Webcam Capture
- Capture live video from webcam

---

## How to Run

Open the project folder in VS Code or any Python IDE.

Run any practical using:

```bash
python filename.py
```

Example:

```bash
python 1_read_write_image.py
```

---

## Expected Output

Each program opens one or more OpenCV windows displaying the processed image or video.

Some practicals also create output files such as:

- saved_image.jpg
- output.avi

Press any key (or **Q** for video/webcam programs) to close the window.

---

## Technologies Used

- Python 3.x
- OpenCV (cv2)
- NumPy

---

## Learning Outcomes

After completing this assignment, the following concepts are understood:

- Image Reading and Writing
- Image Resizing
- Image Flipping
- Drawing Shapes
- Adding Text
- Image Translation
- Image Rotation
- Thresholding
- Gaussian Blur
- Median Blur
- Morphological Operations
- Edge Detection
- Video Processing
- Webcam Access

---
