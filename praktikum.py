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

