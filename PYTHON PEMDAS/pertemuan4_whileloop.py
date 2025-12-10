while True:
    total = 0
    nilai = int(input("masukkan nilai mahasiswa : "))
    total += nilai
    
    rata = total / 5
    print("rata rata", rata)
    
    if rata >= 60:
      print("lulus")
    else:
      print("tidak lulus")
      
    ulang = input("apakah anda ingin mengulang nilai nya ( ya / tidak ) ? ")
    if ulang == "tidak":
      print("terimakasih")
      break