import cv2
import matplotlib.pyplot as plt
import numpy as np

# baca gambar
img = cv2.imread(
    r'D:\kuliah\pengolahan citra\UTS_PengolahanCitra\uts\foto\foto 3 buram.jpeg',
    0
)

# cek gambar
if img is None:
    print("Gambar tidak ditemukan!")

else:

    # ======================
    # BRIGHTNESS
    # ======================

    bright = cv2.convertScaleAbs(
        img,
        alpha=1.8,
        beta=80
    )

    # ======================
    # CLAHE CONTRAST
    # ======================

    clahe = cv2.createCLAHE(
        clipLimit=3.0,
        tileGridSize=(8,8)
    )

    contrast = clahe.apply(img)

    # ======================
    # TAMPILKAN GAMBAR
    # ======================

    plt.figure(figsize=(15,5))

    plt.subplot(1,3,1)
    plt.imshow(img, cmap='gray')
    plt.title("Asli")
    plt.axis('off')

    plt.subplot(1,3,2)
    plt.imshow(bright, cmap='gray')
    plt.title("Brightness")
    plt.axis('off')

    plt.subplot(1,3,3)
    plt.imshow(contrast, cmap='gray')
    plt.title("CLAHE Contrast")
    plt.axis('off')

    plt.show()

    # ======================
    # HISTOGRAM
    # ======================

    plt.figure(figsize=(12,4))

    plt.subplot(1,2,1)
    plt.hist(img.ravel(),256,[0,256])
    plt.title("Histogram Asli")

    plt.subplot(1,2,2)
    plt.hist(contrast.ravel(),256,[0,256])
    plt.title("Histogram CLAHE")

    plt.show()