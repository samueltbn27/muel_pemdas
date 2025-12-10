usia = int(input("Masukkan usia anda : "))
jenis_kelamin = input("Masukkan jenis kelamin anda : ")

if usia < 2:
    print(f"usia anda {usia}")
    print(f"jenis kelamin {jenis_kelamin}")
    print("masih diberi ASI")

elif 3 <= usia < 18:
    if jenis_kelamin == "laki-laki":
        asupan_air = 1.6
    elif jenis_kelamin == "perempuan":
        asupan_air = 1.4
    else:
        asupan_air = 0

    print(f"usia anda {usia}")
    print(f"jenis kelamin {jenis_kelamin}")
    print(f"rekomendasi asupan air adalah {asupan_air} liter")

elif 18 <= usia < 64:
    if jenis_kelamin == "laki-laki":
        asupan_air = 2.5
    elif jenis_kelamin == "perempuan":
        asupan_air = 2.0
    else:
        asupan_air = 0

    print(f"usia anda {usia}")
    print(f"jenis kelamin {jenis_kelamin}")
    print(f"rekomendasi asupan air adalah {asupan_air} liter")

else: 
    if jenis_kelamin == "laki-laki":
        asupan_air = 2.0
    elif jenis_kelamin == "perempuan":
        asupan_air = 1.8
    else:
        asupan_air = 0

    print(f"usia anda {usia}")
    print(f"jenis kelamin {jenis_kelamin}")
    print(f"rekomendasi asupan air adalah {asupan_air} liter")
