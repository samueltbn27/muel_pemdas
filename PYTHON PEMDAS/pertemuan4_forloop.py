# total = 0
  
# for i in range(5):
#   nilai = int(input("masukkan nilai mahasiswa : "))
#   total += nilai
  
#   rata = total / 5
#   print("rata rata", rata)
  
#   if rata >= 60:
#     print("lulus")
#   else:
#     print("tidak lulus")

harga_burger = 25000
burger = 10
total = 0

for i in range(1,6):
  pendapatan = harga_burger * burger
  print("hari ke", i, "burger", burger, "dengan pendapatan", pendapatan )
  
  total += pendapatan
  burger += 2
  
  print("total pendapatan", total) 