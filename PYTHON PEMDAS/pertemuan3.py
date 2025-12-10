nama = input("masukkan nama anda : ")
usia = int(input("masukkan usia anda : "))
jenis_kelamin = input("masukkan jenis kelamin : ")

if usia < 18:
  if jenis_kelamin == "laki-laki":
    asupan_air = 1.6 
  elif jenis_kelamin == "perempuan":
    asupan_air = 1.4
  else:
    asupan_air = None
elif 18 < usia < 64:
  if jenis_kelamin == "laki-laki":
    asupan_air = 2.5
  elif jenis_kelamin == "perempuan":
    asupan_air = 2.0
  else:
    asupan_air = None
else:
   if jenis_kelamin == "laki-laki":
      asupan_air = 2.0
   elif jenis_kelamin == "perempuan":
      asupan_air = 1.8
   else:
      asupan_air = None
  
print(f"nama anda {nama}")
print(f"usia anda adalah {usia}")
print(f"jenis kelamin anda adalah {jenis_kelamin}")
print(f"rekomendasi asupan air anda adalah {asupan_air}")









