harga_burger = 35000
jumlah_burger = 10     # jumlah burger hari pertama
total_pendapatan = 0   # akumulasi pendapatan
hari = 1               # menghitung hari

while total_pendapatan < 1000000:
    pendapatan_harian = jumlah_burger * harga_burger
    
    print(f"Hari ke-{hari}: {jumlah_burger} burger terjual, pendapatan = Rp{pendapatan_harian:,}")
    
    # kenaikan jumlah burger per hari
    total_pendapatan += pendapatan_harian
    jumlah_burger += 2
    hari += 1

print(f"\nTotal pendapatan tercapai: Rp{total_pendapatan:,}")
