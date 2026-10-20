import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("800x500")
root.configure(bg="#0d0b24")

judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#0d0b24"
)
judul.pack(pady=20)

frame_kiri = tk.Frame(root, bg="#0d0b24")
frame_kiri.pack(side="left", padx=50)

frame_kanan = tk.Frame(
    root,
    bg="#17142f",
    width=350,
    height=350
)
frame_kanan.pack(side="right", padx=40)
frame_kanan.pack_propagate(False)

