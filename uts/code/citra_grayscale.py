import cv2
import numpy as np
import matplotlib.pyplot as plt

# baca gambar
gray = cv2.imread(r'D:\kuliah\pengolahan citra\UTS_PengolahanCitra\uts\foto\foto 2 banyak detail.jpeg',0)

# cek gambar
if gray is None:
    print("Gambar tidak ditemukan!")

else:

    # fungsi kuantisasi
    def quantize(image, level):
        step = 256 // level
        return (image // step) * step

    # proses
    q2 = quantize(gray, 2)
    q4 = quantize(gray, 4)
    q8 = quantize(gray, 8)
    q16 = quantize(gray, 16)

    # tampilkan
    plt.figure(figsize=(12,8))

    plt.subplot(2,2,1)
    plt.imshow(q2, cmap='gray')
    plt.title("2 Level")
    plt.axis('off')

    plt.subplot(2,2,2)
    plt.imshow(q4, cmap='gray')
    plt.title("4 Level")
    plt.axis('off')

    plt.subplot(2,2,3)
    plt.imshow(q8, cmap='gray')
    plt.title("8 Level")
    plt.axis('off')

    plt.subplot(2,2,4)
    plt.imshow(q16, cmap='gray')
    plt.title("16 Level")
    plt.axis('off')

    plt.show()