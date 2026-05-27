# =====================================================
# IMPORT LIBRARY
# =====================================================

import tkinter as tk
from tkinter import messagebox
import subprocess
from datetime import datetime

# =====================================================
# MEMBUAT WINDOW
# =====================================================

root = tk.Tk()

root.title("Aplikasi Pengolahan Citra Digital")

root.geometry("1100x750")

root.configure(bg="#1e1e1e")

# =====================================================
# JUDUL
# =====================================================

title = tk.Label(
    root,
    text="APLIKASI PENGOLAHAN CITRA DIGITAL",
    font=("Arial", 24, "bold"),
    bg="#1e1e1e",
    fg="white"
)

title.pack(pady=20)

# =====================================================
# SUB JUDUL
# =====================================================

subtitle = tk.Label(
    root,
    text="GUI Untuk Menjalankan Program Pengolahan Citra",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="#bbbbbb"
)

subtitle.pack(pady=5)

# =====================================================
# FRAME UTAMA
# =====================================================

main_frame = tk.Frame(
    root,
    bg="#1e1e1e"
)

main_frame.pack(pady=20)

# =====================================================
# FRAME BUTTON
# =====================================================

frame_button = tk.Frame(
    main_frame,
    bg="#1e1e1e"
)

frame_button.grid(row=0, column=0, padx=20)

# =====================================================
# FRAME INFORMASI
# =====================================================

frame_info = tk.Frame(
    main_frame,
    bg="#2b2b2b",
    width=350,
    height=500
)

frame_info.grid(row=0, column=1, padx=20)

frame_info.pack_propagate(False)

# =====================================================
# LABEL INFO
# =====================================================

label_info_title = tk.Label(
    frame_info,
    text="INFORMASI PROGRAM",
    font=("Arial", 16, "bold"),
    bg="#2b2b2b",
    fg="white"
)

label_info_title.pack(pady=15)

# =====================================================
# TEXT INFO
# =====================================================

text_info = tk.Text(
    frame_info,
    width=40,
    height=22,
    bg="#121212",
    fg="#00ff88",
    font=("Consolas", 10),
    wrap="word"
)

text_info.pack(padx=10, pady=10)

# =====================================================
# FUNCTION UPDATE INFO
# =====================================================

def update_info(title, desc, code):

    text_info.delete(
        1.0,
        tk.END
    )

    now = datetime.now().strftime("%H:%M:%S")

    info = f"""
PROGRAM :
{title}

DESKRIPSI :
{desc}

CODE UTAMA :
{code}

STATUS :
Program siap dijalankan

WAKTU :
{now}
"""

    text_info.insert(
        tk.END,
        info
    )

# =====================================================
# FUNCTION MENJALANKAN FILE
# =====================================================

def run_program(file_name):

    try:

        status_label.config(
            text="Status : Program Sedang Berjalan...",
            fg="yellow"
        )

        root.update()

        subprocess.run(
            ["python", file_name]
        )

        status_label.config(
            text="Status : Program Selesai Dijalankan",
            fg="#00ff88"
        )

    except:

        messagebox.showerror(
            "Error",
            "Program gagal dijalankan!"
        )

        status_label.config(
            text="Status : Error",
            fg="red"
        )

# =====================================================
# BUTTON CITRA DASAR
# =====================================================

btn_citra_dasar = tk.Button(
    frame_button,
    text="RGB - Grayscale - Binary",
    command=lambda: [
        update_info(
            "Citra Dasar",
            "Program untuk konversi RGB, Grayscale, dan Binary.",
            "cv2.cvtColor()\ncv2.threshold()"
        ),
        run_program("citra_dasar.py")
    ],
    width=35,
    height=3,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold"),
    relief="flat",
    cursor="hand2"
)

btn_citra_dasar.grid(
    row=0,
    column=0,
    padx=10,
    pady=10
)

# =====================================================
# BUTTON GRAYSCALE LEVEL
# =====================================================

btn_gray_level = tk.Button(
    frame_button,
    text="Grayscale Level 2,4,8,16",
    command=lambda: [
        update_info(
            "Grayscale Level",
            "Program kuantisasi grayscale menjadi beberapa level.",
            "quantize()\nimage // step"
        ),
        run_program("citra_grayscale.py")
    ],
    width=35,
    height=3,
    bg="#2196F3",
    fg="white",
    font=("Arial", 11, "bold"),
    relief="flat",
    cursor="hand2"
)

btn_gray_level.grid(
    row=1,
    column=0,
    padx=10,
    pady=10
)

# =====================================================
# BUTTON HISTOGRAM
# =====================================================

btn_histogram = tk.Button(
    frame_button,
    text="Histogram Equalization",
    command=lambda: [
        update_info(
            "Histogram Equalization",
            "Meningkatkan distribusi kontras pada citra.",
            "cv2.equalizeHist()"
        ),
        run_program("histogram_equalization.py")
    ],
    width=35,
    height=3,
    bg="#9C27B0",
    fg="white",
    font=("Arial", 11, "bold"),
    relief="flat",
    cursor="hand2"
)

btn_histogram.grid(
    row=2,
    column=0,
    padx=10,
    pady=10
)

# =====================================================
# BUTTON BRIGHTNESS
# =====================================================

btn_brightness = tk.Button(
    frame_button,
    text="Brightness & CLAHE Contrast",
    command=lambda: [
        update_info(
            "Brightness dan CLAHE",
            "Meningkatkan pencahayaan dan kontras gambar.",
            "cv2.convertScaleAbs()\ncv2.createCLAHE()"
        ),
        run_program("brightness_contras.py")
    ],
    width=35,
    height=3,
    bg="#FF9800",
    fg="white",
    font=("Arial", 11, "bold"),
    relief="flat",
    cursor="hand2"
)

btn_brightness.grid(
    row=3,
    column=0,
    padx=10,
    pady=10
)

# =====================================================
# BUTTON FILTER
# =====================================================

btn_filter = tk.Button(
    frame_button,
    text="Mean & Median Filter",
    command=lambda: [
        update_info(
            "Mean dan Median Filter",
            "Mengurangi noise menggunakan filter smoothing.",
            "cv2.blur()\ncv2.medianBlur()"
        ),
        run_program("filter_final.py")
    ],
    width=35,
    height=3,
    bg="#795548",
    fg="white",
    font=("Arial", 11, "bold"),
    relief="flat",
    cursor="hand2"
)

btn_filter.grid(
    row=4,
    column=0,
    padx=10,
    pady=10
)

# =====================================================
# BUTTON DOKUMEN
# =====================================================

btn_document = tk.Button(
    frame_button,
    text="Scanner Dokumen Otomatis",
    command=lambda: [
        update_info(
            "Scanner Dokumen",
            "Mendeteksi dokumen dan membuat efek scanner otomatis.",
            "cv2.Canny()\ncv2.findContours()\ncv2.warpPerspective()"
        ),
        run_program("dokumen_otomatis.py")
    ],
    width=35,
    height=3,
    bg="#F44336",
    fg="white",
    font=("Arial", 11, "bold"),
    relief="flat",
    cursor="hand2"
)

btn_document.grid(
    row=5,
    column=0,
    padx=10,
    pady=10
)

# =====================================================
# STATUS LABEL
# =====================================================

status_label = tk.Label(
    root,
    text="Status : Menunggu Program Dijalanakan",
    font=("Arial", 11, "bold"),
    bg="#1e1e1e",
    fg="#00ff88"
)

status_label.pack(pady=10)

# =====================================================
# FOOTER
# =====================================================

footer = tk.Label(
    root,
    text="UTS Pengolahan Citra Digital - OpenCV & Tkinter",
    font=("Arial", 10),
    bg="#1e1e1e",
    fg="gray"
)

footer.pack(side="bottom", pady=20)

# =====================================================
# MAINLOOP
# =====================================================

root.mainloop()