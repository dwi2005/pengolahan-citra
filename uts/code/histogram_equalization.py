import cv2
import matplotlib.pyplot as plt

# membaca gambar
img = cv2.imread(r'D:\kuliah\pengolahan citra\UTS_PengolahanCitra\uts\foto\foto 4 detail wajah.jpeg',0)

# cek gambar
if img is None:
    print("Gambar tidak ditemukan!")

else:

    # histogram equalization
    equal = cv2.equalizeHist(img)

    # tampilkan gambar
    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    plt.imshow(img, cmap='gray')
    plt.title("Citra Asli")
    plt.axis('off')

    plt.subplot(1,2,2)
    plt.imshow(equal, cmap='gray')
    plt.title("Histogram Equalization")
    plt.axis('off')

    plt.show()

    # histogram asli
    plt.hist(img.ravel(),256,[0,256])
    plt.title("Histogram Asli")
    plt.show()

    # histogram equalization
    plt.hist(equal.ravel(),256,[0,256])
    plt.title("Histogram Equalization")
    plt.show()