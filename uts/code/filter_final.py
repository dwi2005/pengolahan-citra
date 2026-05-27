import cv2
import numpy as np
import matplotlib.pyplot as plt

# =========================
# MEMBACA GAMBAR
# =========================

img = cv2.imread(
    r'D:\kuliah\pengolahan citra\UTS_PengolahanCitra\uts\foto\dwi.jpeg'
)

# cek gambar
if img is None:
    print("Gambar tidak ditemukan!")

else:

    # =========================
    # UBAH BGR KE RGB
    # =========================

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # =========================
    # MEMBUAT GAUSSIAN NOISE
    # =========================

    img_float = rgb.astype(np.float32)

    noise = np.random.normal(
        0,      # rata-rata noise
        25,     # kekuatan noise
        rgb.shape
    ).astype(np.float32)

    # tambah noise
    noisy = img_float + noise

    # batasi pixel
    noisy = np.clip(noisy, 0, 255)

    # kembali ke uint8
    noisy = noisy.astype(np.uint8)

    # =========================
    # MEAN FILTER
    # =========================

    mean = cv2.blur(
        noisy,
        (11,11)
    )

    # =========================
    # MEDIAN FILTER
    # =========================

    median = cv2.medianBlur(
        noisy,
        11
    )

    # =========================
    # TAMBAH SEDIKIT BRIGHTNESS
    # =========================

    mean = cv2.convertScaleAbs(
        mean,
        alpha=1.1,
        beta=10
    )

    median = cv2.convertScaleAbs(
        median,
        alpha=1.1,
        beta=10
    )

    # =========================
    # MENAMPILKAN HASIL
    # =========================

    fig, ax = plt.subplots(2,2, figsize=(10,8))

    # gambar asli
    ax[0,0].imshow(rgb)
    ax[0,0].set_title("Foto Asli")
    ax[0,0].axis('off')

    # gambar noise
    ax[0,1].imshow(noisy)
    ax[0,1].set_title("Gaussian Noise")
    ax[0,1].axis('off')

    # mean filter
    ax[1,0].imshow(mean)
    ax[1,0].set_title("Mean Filter")
    ax[1,0].axis('off')

    # median filter
    ax[1,1].imshow(median)
    ax[1,1].set_title("Median Filter")
    ax[1,1].axis('off')

    # mengatur jarak
    plt.subplots_adjust(
        left=0.15,
        right=0.85,
        top=0.90,
        bottom=0.08,
        wspace=0.25,
        hspace=0.25
    )

    plt.show()

    # =========================
    # MENYIMPAN HASIL
    # =========================

    cv2.imwrite(
        "hasil_noise.jpg",
        cv2.cvtColor(noisy, cv2.COLOR_RGB2BGR)
    )

    cv2.imwrite(
        "hasil_mean.jpg",
        cv2.cvtColor(mean, cv2.COLOR_RGB2BGR)
    )

    cv2.imwrite(
        "hasil_median.jpg",
        cv2.cvtColor(median, cv2.COLOR_RGB2BGR)
    )

    print("Semua hasil berhasil disimpan!")