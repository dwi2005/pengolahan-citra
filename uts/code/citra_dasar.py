import cv2
import matplotlib.pyplot as plt

# membaca gambar
img = cv2.imread(r'D:\kuliah\pengolahan citra\UTS_PengolahanCitra\uts\foto\foto 1 berwarna.jpeg')

# konversi RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# konversi grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# konversi binary
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# ukuran array
print("Ukuran RGB:", rgb.shape)
print("Ukuran Grayscale:", gray.shape)
print("Ukuran Binary:", binary.shape)

# tampilkan gambar
plt.figure(figsize=(12,5))

plt.subplot(1,3,1)
plt.imshow(rgb)
plt.title("RGB")

plt.subplot(1,3,2)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale")

plt.subplot(1,3,3)
plt.imshow(binary, cmap='gray')
plt.title("Binary")

plt.show()