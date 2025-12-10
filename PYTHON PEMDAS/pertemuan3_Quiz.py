sistolik = float(input("Masukkan tekanan darah sistolik (mmHg) : "))
diastolik = float(input("Masukkan tekanna darah diastolik (mmHg) : "))
denyut_nadi = float(input("masukkan denyut nadi (bpm) : "))

if sistolik > 180 or diastolik > 120:
  print("rekomendasikan pasien untuk segera mencari bantuan medis karena ini merupakan krisis hipertensi")
else:
  if sistolik > 140 or diastolik > 90:
    print("disarankan untuk konsultasi dengan dokter mengenai hipertensi")
  elif (120 <= sistolik <= 139) or ( 80 <= diastolik <= 90):
    print("kategori hipertensi")
  elif sistolik < 120 and diastolik < 80:
    print("tekanan darah normal")
  else:
    print("data teknanan darah tidak termasuk dalam kategori umum")

if denyut_nadi > 100:
  print("sarankan untuk memeriksa kondisi kesehatan jantung")
elif denyut_nadi< 60:
  print("sarankan untuk memeriksa apakah ada gejala yang lain untuk mengiringi bradikardia")
else:
  print("denyut nadi normal")
