# Program Perkenalan Diri

# Fungsi untuk meminta input nama pengguna
def minta_nama():
    nama = input("Halo! Siapa namamu? : ")
    return nama

# Fungsi untuk meminta input umur pengguna
def minta_umur():
    umur = input("Berapa umurmu? : ")
    return umur

#Fungsi untuk meminta input asal pengguna
def minta_asal():
    asal = input ("Kamu berasal dari mana? : ")
    return asal

# Fungsi untuk menampilkan pesan perkenalan
def perkenalan(nama, umur):
    print(f"\nHai {nama}! Senang bertemu denganmu.")
    print(f"Aku berusia {umur} tahun.")

# Fungsi utama program
def main():
    nama_pengguna = minta_nama()
    umur_pengguna = minta_umur()
    asal_pengguna = minta_asal()
    perkenalan(nama_pengguna, umur_pengguna, asal_pengguna)

# Panggil fungsi utama
if __name__ == "__main__":
    main()
