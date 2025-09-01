# 🏗️ Buildings Built in Minutes – Structure from Motion (SfM)

This project implements a Structure-from-Motion (SfM) pipeline to reconstruct sparse 3D models of urban environments from 2D image sequences. Developed as part of the final project for ENPM673 – Perception for Autonomous Robots.

---

## 📌 Project Objective

To reconstruct 3D structures from multiple 2D images using SfM techniques, leveraging keypoint detection, feature matching, camera pose estimation, triangulation, and 3D visualization.

---

## 📁 Repository Contents

| File | Description |
|------|-------------|
| `3dcode.py` | Main Python script for SfM pipeline |
| `image1.jpg`–`image4.jpg` | Input image sequence |
| `Final Project Perception.pptx` | Project presentation |
| `Buildings_Built_in_Minutes___Structure_from_Motion__SfM_.pdf` | Final project report |
| `.idea/*`, `.iml`, `*.xml` | PyCharm project files |

---

## 🧠 Key Components

- **Keypoint Detection & Matching** using SIFT or ORB
- **Fundamental Matrix Estimation** using RANSAC
- **Camera Pose Recovery** (Rotation, Translation)
- **Triangulation** for 3D point cloud generation
- **3D Visualization** using `matplotlib` and `OpenCV`

---

## 🚀 How to Run

1. Clone the repository
2. Ensure you have Python 3.12+ and OpenCV installed
3. Run:
```bash
python 3dcode.py
```

---

## 🖼️ Sample Input

![Sample View 1](image1.jpg)
![Sample View 2](image2.jpg)

---

## 📘 Course Info

- **Course**: ENPM673 – Perception for Autonomous Robots  
- **University**: University of Maryland  
- **Instructor**: Dr. Yiannis Aloimonos  
- **Semester**: Spring 2025  

---

## 📄 License

This project is for academic use only. Please contact the author for collaboration or reuse.