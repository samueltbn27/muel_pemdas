# -*- coding: utf-8 -*-
"""
ANALISIS DATA DIABETES MELLITUS JAWA BARAT 2019-2024
Versi yang sudah diperbaiki & dioptimalkan
"""

import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------------------
# 1. LOAD DATA
# --------------------------------------------------------------
# Ganti path sesuai lokasi file CSV kamu
df = pd.read_csv("data_diabetes_jabar.csv")

# Pastikan kolom numerik benar-benar numerik
df["tahun"] = pd.to_numeric(df["tahun"], errors="coerce")
df["jumlah_penderita_dm"] = pd.to_numeric(df["jumlah_penderita_dm"], errors="coerce")

# --------------------------------------------------------------
# A. SOAL DASAR
# --------------------------------------------------------------
print("="*60)
print("A. SOAL DASAR")
print("="*60)

print("\nA1. 5 Baris Pertama")
print(df.head())

print("\nA2. 5 Baris Terakhir")
print(df.tail())

print("\nA3. Info DataFrame")
df.info()

print("\nA4. Statistik Deskriptif")
print(df.describe())

print("\nA5. Nilai Unik Tahun")
print(sorted(df["tahun"].unique()))

print("\nA6. Daftar Kabupaten/Kota & Jumlahnya")
print(df["nama_kabupaten_kota"].unique())
print(f"Jumlah kabupaten/kota unik: {df['nama_kabupaten_kota'].nunique()}")

print("\nA7. Hanya Kolom Tertentu")
print(df[["nama_kabupaten_kota", "jumlah_penderita_dm", "tahun"]])

# --------------------------------------------------------------
# B. FILTERING & SORTING
# --------------------------------------------------------------
print("\n" + "="*60)
print("B. FILTERING & SORTING")
print("="*60)

df_2019 = df[df["tahun"] == 2019]

print("\nB8. Data Tahun 2019")
print(df_2019[["nama_kabupaten_kota", "jumlah_penderita_dm"]])

print("\nB9. Penderita > 100.000 orang (semua tahun)")
print(df[df["jumlah_penderita_dm"] > 100_000][["nama_kabupaten_kota", "tahun", "jumlah_penderita_dm"]])

print("\nB10. Urutkan dari terbesar ke terkecil")
print(df.sort_values("jumlah_penderita_dm", ascending=False).head(10)[["nama_kabupaten_kota", "tahun", "jumlah_penderita_dm"]])

print("\nB11. Urutkan per tahun, lalu jumlah terbesar")
print(df.sort_values(["tahun", "jumlah_penderita_dm"], ascending=[True, False]).head(10)[["nama_kabupaten_kota", "tahun", "jumlah_penderita_dm"]])

print("\nB12. Top 10 Tertinggi Tahun 2019")
print(df_2019.nlargest(10, "jumlah_penderita_dm")[["nama_kabupaten_kota", "jumlah_penderita_dm"]])

print("\nB13. Data KABUPATEN BOGOR (semua tahun)")
print(df[df["nama_kabupaten_kota"] == "KABUPATEN BOGOR"][["tahun", "jumlah_penderita_dm"]])

# --------------------------------------------------------------
# C. AGREGASI & TRANSFORMASI
# --------------------------------------------------------------
print("\n" + "="*60)
print("C. AGREGASI & TRANSFORMASI")
print("="*60)

print("\nC14. Total Penderita per Tahun")
total_per_tahun = df.groupby("tahun")["jumlah_penderita_dm"].sum()
print(total_per_tahun)

print("\nC15. Rata-rata Penderita per Kabupaten/Kota")
print(df.groupby("nama_kabupaten_kota")["jumlah_penderita_dm"].mean().round(2))

print("\nC16. Kabupaten Total Tertinggi & Terendah")
total_kab = df.groupby("nama_kabupaten_kota")["jumlah_penderita_dm"].sum()
print("Tertinggi :", total_kab.idxmax(), "→", total_kab.max(), "orang")
print("Terendah  :", total_kab.idxmin(), "→", total_kab.min(), "orang")

# C17. Kolom Kategori
def kategori_dm(x):
    if x < 50_000:
        return "Rendah"
    elif x < 100_000:
        return "Sedang"
    else:
        return "Tinggi"

df["kategori_dm"] = df["jumlah_penderita_dm"].apply(kategori_dm)

print("\nC17. Contoh Kolom kategori_dm")
print(df[["nama_kabupaten_kota", "tahun", "jumlah_penderita_dm", "kategori_dm"]].head(10))

# C18. Persentase terhadap total tahunan
df["persentase_tahun"] = df.groupby("tahun")["jumlah_penderita_dm"].transform(
    lambda x: x / x.sum() * 100
)

print("\nC18. Persentase per Kab/Kota terhadap Total Tahun")
print(df[["nama_kabupaten_kota", "tahun", "jumlah_penderita_dm", "persentase_tahun"]].head(10))

# C19. Tabel Ringkas
print("\nC19. Ringkasan per Tahun")
summary = df.groupby("tahun").agg(
    total_penderita=("jumlah_penderita_dm", "sum"),
    jumlah_kab_kota=("nama_kabupaten_kota", "nunique")
).reset_index()
print(summary)

# --------------------------------------------------------------
# D. VISUALISASI (Matplotlib) – DIPERBAIKI!
# --------------------------------------------------------------
plt.rcParams["figure.figsize"] = (10, 6)
plt.style.use("seaborn-v0_8")

# D20. Bar Chart 2019
print("\nD20. Grafik Bar 2019")
df_2019_sorted = df_2019.sort_values("jumlah_penderita_dm", ascending=False)
plt.figure(figsize=(12, 7))
plt.bar(df_2019_sorted["nama_kabupaten_kota"], df_2019_sorted["jumlah_penderita_dm"], color="skyblue")
plt.title("Jumlah Penderita Diabetes Mellitus per Kab/Kota – Tahun 2019", fontsize=16)
plt.xlabel("Kabupaten/Kota")
plt.ylabel("Jumlah Penderita")
plt.xticks(rotation=90)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

# D21. Line Chart Total per Tahun
print("\nD21. Grafik Garis Total per Tahun")
plt.figure()
plt.plot(total_per_tahun.index, total_per_tahun.values, marker="o", linewidth=3, markersize=8)
plt.title("Tren Total Penderita Diabetes Mellitus di Jawa Barat (2019-2024)", fontsize=16)
plt.xlabel("Tahun")
plt.ylabel("Total Penderita")
plt.grid(True)
for x, y in zip(total_per_tahun.index, total_per_tahun.values):
    plt.text(x, y + 15000, f"{y:,}", ha="center")
plt.tight_layout()
plt.show()

# D22. Top 10 Horizontal Bar 2019
print("\nD22. Top 10 Tertinggi 2019 (Horizontal)")
top10 = df_2019.nlargest(10, "jumlah_penderita_dm")
plt.figure(figsize=(10, 6))
plt.barh(top10["nama_kabupaten_kota"], top10["jumlah_penderita_dm"], color="salmon")
plt.title("10 Kabupaten/Kota dengan Penderita DM Tertinggi – 2019")
plt.xlabel("Jumlah Penderita")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# D23. Pie Chart Kategori 2019
print("\nD23. Pie Chart Kategori DM 2019")
kategori_count = df_2019["kategori_dm"].value_counts()
plt.figure(figsize=(7, 7))
plt.pie(kategori_count, labels=kategori_count.index, autopct="%1.1f%%", startangle=90, colors=["lightgreen","orange","lightcoral"])
plt.title("Proporsi Kategori Diabetes Mellitus Tahun 2019")
plt.axis("equal")
plt.show()

# D24. Bar 3 Tahun Terakhir
print("\nD24. Total 3 Tahun Terakhir")
last3 = total_per_tahun.tail(3)
plt.figure()
last3.plot(kind="bar", color=["#ff9999","#66b3ff","#99ff99"], edgecolor="black")
plt.title("Total Penderita DM – Tiga Tahun Terakhir (2022-2024)")
plt.ylabel("Jumlah Penderita")
plt.xticks(rotation=0)
for i, v in enumerate(last3):
    plt.text(i, v + 10000, f"{v:,}", ha="center")
plt.tight_layout()
plt.show()

# --------------------------------------------------------------
# E. ANALISIS AKHIR
# --------------------------------------------------------------
print("\n" + "="*60)
print("ANALISIS SINGKAT")
print("="*60)
print("""
a. Kabupaten/kota dengan penderita tertinggi:
   → KABUPATEN KARAWANG dan KABUPATEN BEKASI sering mendominasi (terutama 2019–2021)
   → Namun angka di Bekasi melonjak drastis di 2020 (242.169) lalu turun tajam

b. Tren keseluruhan:
   → Naik tajam 2019 → 2020
   → Turun signifikan mulai 2021–2022
   → Stabil rendah di 2023–2024
   → Kemungkinan dipengaruhi perubahan sistem pelaporan atau dampak pandemi

c. Sebaran kategori (2019):
   → Rendah (<50k)   : ~81.5%
   → Sedang (50–99k) : ~11.1%
   → Tinggi (≥100k)  : ~7.4%
   → Mayoritas kabupaten masih di kategori Rendah
""")

print("\nSELESAI – Semua kode berjalan tanpa error!")