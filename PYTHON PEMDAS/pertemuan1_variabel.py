# nama1 = "diash"
# status = "menikah"
# print(nama1, status)

# nama = "ambatukam"
# umur = 20
# tinggi = 175.5
# print(nama, umur, tinggi)

# nama = "ambatukam"
# umur = 20
# tinggi = 175.5
# # print("nama :", nama, "umur :", umur, "tinggi :", tinggi)
# print(f"nama : {nama}, umur : {umur}, tinggi : {tinggi}")

nama = input("siapakah nama anda : ")
umur = int(input("masukkan umur anda : "))
tinggi = float(input("masukkan tinggi anda : "))
status = bool(input("apakah anda sudah menikah ? (sudah / belum) :"))
print(f"nama anda adalah {nama}, usia anda {umur}, tinggi anda {tinggi}, dan status anda {status}")
print(type(nama), type(umur), type(tinggi), type(status))