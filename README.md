# 🖼️ Image Compression Using K-Means Clustering

An **unsupervised machine learning project** that uses **K-Means Clustering** to compress images by reducing the number of unique colors while preserving the overall visual appearance.

Instead of storing thousands or millions of different colors, K-Means groups similar RGB pixel values into a smaller number of clusters. Each pixel is then replaced by the color of its corresponding cluster centroid.

---

## 📌 Project Overview

Digital images can contain a very large number of unique colors. Image compression can reduce storage requirements by representing an image using a smaller color palette.

In this project:

1. An image is loaded and converted into pixel data.
2. Each pixel is represented using its **RGB values**.
3. K-Means Clustering groups similar pixels together.
4. Cluster centroids represent the dominant colors.
5. Each pixel is replaced with its nearest centroid.
6. The original image is reconstructed using the reduced color palette.

This is an example of **lossy image compression**, because reducing the number of colors can remove some visual informat
