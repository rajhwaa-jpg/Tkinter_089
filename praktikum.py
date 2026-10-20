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

entries = []

for i in range(10):
    label = tk.Label(
        frame_kiri,
        text=f"Nilai Mata Pelajaran {i+1}",
        fg="white",
        bg="#0d0b24",
        font=("Arial", 10)
    )
    label.grid(row=i, column=0, pady=5, sticky="w")

    entry = tk.Entry(
        frame_kiri,
        width=10,
        bg="#211e3d",
        fg="white",
        insertbackground="white"
    )
    entry.grid(row=i, column=1, padx=15)

    entries.append(entry)

tk.Label(
    frame_kiri,
    text="Pilihan Jurusan Anda",
    fg="white",
    bg="#0d0b24",
    font=("Arial", 10, "bold")
).grid(row=10, column=0, pady=15)

jurusan = ttk.Combobox(
    frame_kiri,
    values=[
        "Teknologi Informasi",
        "Sistem Informasi",
        "Informatika"
    ],
    state="readonly",
    width=18
)
jurusan.grid(row=10, column=1)
jurusan.set("Teknologi Informasi")

def prediksi():
    try:
        nilai = [float(entry.get()) for entry in entries]

        if any(n < 0 or n > 100 for n in nilai):
            messagebox.showerror(
                "Error",
                "Nilai harus berada antara 0 sampai 100!"
            )
            return

        rata_rata = sum(nilai) / len(nilai)

        if rata_rata >= 75:
            hasil = "Teknologi Informasi"
        elif rata_rata >= 65:
            hasil = "Sistem Informasi"
        else:
            hasil = "Informatika"

        hasil_label.config(
            text=f"Prediksi Prodi:\n{hasil}\n\n"
                 f"Rata-rata Nilai: {rata_rata:.2f}"
        )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Masukkan semua nilai terlebih dahulu!"
        )

tombol = tk.Button(
    frame_kiri,
    text="Hasil Prediksi",
    command=prediksi,
    bg="#29254d",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=15,
    pady=5
)
tombol.grid(row=11, column=1, pady=20)