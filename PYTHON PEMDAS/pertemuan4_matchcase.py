hari = input("Masukkan hari : ")

match hari:
  case "Senin":
    print("Data mining and retriveal information")
  case "Selasa":
    print("Basis Data Lanjut")
    print("Praktikum Teknik Multimedia")
    print("Praktikum Pemrograman Dasar")
  case "Rabu":
    print("Teknik Multimedia")
    print("Pemrograman Iot")
    print("Pemrograman Dasar")
  case "Kamis":
    print("Tidak ada mata kuliah")
  case "Jumat":
    print("Kecerdasan Buatan")
    print("Computer Vision")
  case "Sabtu":
    print("Praktikum Pemrograman Iot")
  case _:
    print("Masukkan hari yang valid")
    
