def main():
    # Membuat list kota
    kota = ["Manado", "Tomohon", "Bitung", "Bandung", "Bekasi"]

    # Menampilkan list kota
    print("List Kota:")
    for nama_kota in kota:
        print(nama_kota)

    # Menambahkan kota baru ke dalam list
    kota.append("Makassar")

    # Menampilkan list kota setelah penambahan
    print("\nList Kota setelah penambahan:")
    for nama_kota in kota:
        print(nama_kota)

    # Mengakses elemen list berdasarkan indeks
    indeks = 2
    print(f"\nKota di indeks {indeks}: {kota[indeks]}")

    # Mengganti nama kota di indeks tertentu
    kota[1] = "Yogyakarta"

    # Menampilkan list kota setelah perubahan
    print("\nList Kota setelah perubahan:")
    for nama_kota in kota:
        print(nama_kota)

    # Menghitung jumlah kota dalam list
    jumlah_kota = len(kota)
    print(f"\nJumlah kota dalam list: {jumlah_kota}")

if __name__ == "__main__":
    main()
