try:
  angka1 = int(input("masukkan angka  : "))
  angka2 = int(input("masukkan angka kedua : "))
  penjumlahan = angka1 + angka2
  pengurangan = angka1 - angka2
except ZeroDivisionError:
  print("terjadi kesalahan pastikan input benar dan tidak nol")
except:
  print("input harus berupa angka")
else:
  print(f"hasil dari penjumlahan : {penjumlahan}")
  print(f"hasil dari pengurangan : {pengurangan}")
finally:
  print("program selesai")
