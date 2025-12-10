akun_dummy = [
  ("Pak Budi", "admin1"),
  ("Bu Sari", "admin2"),
  ("Pak Rudi", "admin3"),
  ("Bu Wati", "admin4"),
  ("Pak Agus", "admin5")
]

masa_percobaan = 0
login_sukses = False

while masa_percobaan < 3:
  username = input("masukkan username anda : ")
  password = input("masukkan password : ")
  
  if (username, password) in akun_dummy:
    print(f"login berhasil, selamat datang {username} !")
    login_sukses = True
    break
  else:
    masa_percobaan += 1
    sisa = 3 - masa_percobaan
    if sisa > 0:
      print(f"login gagal masa percobaan {sisa}")
    else:
      print(f"mohon maaf akun terblokir ")
      exit()



if login_sukses:
  produksi = {
    "anak-anak" : 0.3,
    "remaja" : 0.5,
    "dewasa" : 0.8,
    "lansia" : 0.6
  }  
  
  komposisi = {
    "organik" : 0.5,
    "anorganik" : 0.3,
    "b3" : 0.05,
    "lainnya" : 0.15
  }
  
  pengurang = {
    "tidak" : 0.0,
    "rendah" : 0.10,
    "sedang" : 0.20,
    "tinggi" :0.35
  }


while True:
  try:
    jumlah = int(input("masukkan jumlah rumah tangga yang akan di proses : "))
    if jumlah > 0:
      break
    else:
      print(f"jumlah rumah tangga harus lebih dari 0")
  except ValueError:
    print(f"masukkan angka yang valid")

total_semua_rumah = 0


i = 1
while i <= jumlah:
  print(f"data rumah tangga ke {i}")
  nama = input("nama pemilik rumah : ")
  
  while True:
    try:
      anggota = int(input("masukkan jumlah anggota : "))
      if anggota > 0:
        break
      else:
        print(f"jumlah anggota harus lebih dari 0")
    except ValueError:
      print(f"masukkan angka yang valid")
  
  while True:
    try:
      usia = input("usia dominan ( anak / remaja / dewasa / lansia ) : ")
      if usia in produksi:
        break
    except ValueError:
      print(f"input tidak valid")
  
  while True:
    jenis = input("masukkan jenis sampah ( organik / anorganik / b3 / lainnya ) : ")
    if jenis in komposisi:
      break
    else:
      print("input tidak valid")
  
  while True:
    daur_ulang = input("daur ulang ( tidak / rendah / sedang / tinggi ) : ")
    if daur_ulang in pengurang:
      break
    else:
      print(f"input tidak valid")
  
  total_awal = anggota * produksi[usia]
  total_akhir = total_awal * (1 - pengurang[daur_ulang])
  
  organik = total_akhir * komposisi["organik"]
  anorganik = total_akhir * komposisi["anorganik"]
  b3 = total_akhir * komposisi["b3"]
  lainnya = total_akhir * komposisi["lainnya"]
  
  total_semua_rumah += total_akhir
  
  print("==hasil perhitungan==")
  print(f"nama rumah tangga : {nama}")
  print(f"total sebelum reduksi : {total_awal:.2f}")
  print(f"total sesudah reduksi : {total_akhir:.2f}")
  
  print("==rincian per jenis sampah")
  print(f"organik : {organik:.2f} kg")
  print(f"organik : {anorganik:.2f} kg")
  print(f"b3 : {b3:.2f} kg")
  print(f"lainnya : {lainnya:.2f} kg")
  
  if jenis == "organik":
      rekom = "Prioritaskan pembuatan kompos."
  elif jenis == "anorganik":
      rekom = "Pisahkan plastik dan logam untuk didaur ulang."
  elif jenis == "b3":
      rekom = "Buang ke tempat sampah khusus B3."
  elif jenis == "lainnya":
      rekom = "Periksa peluang daur ulang lebih lanjut."
  else:
      rekom = "Pisahkan sampah organik dan anorganik sejak awal."
      
  print(f"rekomendasi : {rekom}")
  
  i += 1
  

print("== rincian akhir==")
print(f"Total gabungan sampah harian sesudah pengurangan: {total_semua_rumah:.2f} kg")
print("Terima kasih telah menggunakan sistem ini.")