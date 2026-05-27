import cv2
import numpy as np
import matplotlib.pyplot as plt

# =========================
# MEMBACA GAMBAR
# =========================

img = cv2.imread(
    r'D:\kuliah\pengolahan citra\UTS_PengolahanCitra\uts\foto\dokumen.jpeg'
)

# cek gambar
if img is None:
    print("Gambar tidak ditemukan!")

else:

    # =========================
    # RESIZE GAMBAR
    # =========================

    img = cv2.resize(img, (700, 800))

    # copy gambar asli
    original = img.copy()

    # =========================
    # GRAYSCALE
    # =========================

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    # =========================
    # GAUSSIAN BLUR
    # =========================

    blur = cv2.GaussianBlur(
        gray,
        (5,5),
        0
    )

    # =========================
    # EDGE DETECTION
    # =========================

    edge = cv2.Canny(
        blur,
        75,
        200
    )

    # =========================
    # MENCARI CONTOUR
    # =========================

    contours, _ = cv2.findContours(
        edge.copy(),
        cv2.RETR_LIST,
        cv2.CHAIN_APPROX_SIMPLE
    )

    contours = sorted(
        contours,
        key=cv2.contourArea,
        reverse=True
    )

    document = None

    # =========================
    # MENCARI BENTUK 4 SISI
    # =========================

    for c in contours:

        peri = cv2.arcLength(c, True)

        approx = cv2.approxPolyDP(
            c,
            0.02 * peri,
            True
        )

        # jika memiliki 4 titik
        if len(approx) == 4:

            document = approx
            break

    # =========================
    # GAMBAR CONTOUR
    # =========================

    contour_img = original.copy()

    cv2.drawContours(
        contour_img,
        [document],
        -1,
        (0,255,0),
        3
    )

    # =========================
    # PERSPECTIVE TRANSFORM
    # =========================

    pts = document.reshape(4,2)

    rect = np.zeros((4,2), dtype="float32")

    # menentukan titik
    s = pts.sum(axis=1)

    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis=1)

    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    (tl, tr, br, bl) = rect

    # menghitung lebar
    widthA = np.linalg.norm(br - bl)
    widthB = np.linalg.norm(tr - tl)

    maxWidth = max(int(widthA), int(widthB))

    # menghitung tinggi
    heightA = np.linalg.norm(tr - br)
    heightB = np.linalg.norm(tl - bl)

    maxHeight = max(int(heightA), int(heightB))

    # tujuan transformasi
    dst = np.array([
        [0,0],
        [maxWidth -1,0],
        [maxWidth -1,maxHeight -1],
        [0,maxHeight -1]
    ], dtype="float32")

    # matriks transformasi
    M = cv2.getPerspectiveTransform(
        rect,
        dst
    )

    # warp perspective
    scan = cv2.warpPerspective(
        original,
        M,
        (maxWidth, maxHeight)
    )

    # =========================
    # THRESHOLD SCANNER EFFECT
    # =========================

    scan_gray = cv2.cvtColor(
        scan,
        cv2.COLOR_BGR2GRAY
    )

    threshold = cv2.adaptiveThreshold(
        scan_gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    # =========================
    # MENAMPILKAN HASIL
    # =========================

    plt.figure(figsize=(16,10))

    # asli
    plt.subplot(2,3,1)
    plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    plt.title("Dokumen Asli")
    plt.axis('off')

    # grayscale
    plt.subplot(2,3,2)
    plt.imshow(gray, cmap='gray')
    plt.title("Grayscale")
    plt.axis('off')

    # edge
    plt.subplot(2,3,3)
    plt.imshow(edge, cmap='gray')
    plt.title("Edge Detection")
    plt.axis('off')

    # contour
    plt.subplot(2,3,4)
    plt.imshow(cv2.cvtColor(contour_img, cv2.COLOR_BGR2RGB))
    plt.title("Contour Detection")
    plt.axis('off')

    # hasil scan
    plt.subplot(2,3,5)
    plt.imshow(cv2.cvtColor(scan, cv2.COLOR_BGR2RGB))
    plt.title("Perspective Transform")
    plt.axis('off')

    # scanner effect
    plt.subplot(2,3,6)
    plt.imshow(threshold, cmap='gray')
    plt.title("Scanner Effect")
    plt.axis('off')

    plt.tight_layout()

    plt.show()

    # =========================
    # MENYIMPAN HASIL
    # =========================

    cv2.imwrite("scanner_result.jpg", scan)

    cv2.imwrite("scanner_threshold.jpg", threshold)

    print("Scanner dokumen berhasil dibuat!")