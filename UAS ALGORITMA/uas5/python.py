#Fungsi untuk menghitung luas persegi 
#Menerima panjang sisi dan mengembalikan luas persegi
def hitung_luas_persegi(sisi):
    luas = sisi * sisi
    return luas

#Fungsi untuk menghitung luas lingkaran
#Menerima jari-jari dan mengembalikan luas lingkaran
def hitung_luas_lingkaran(jari_jari):
    luas = 3.14 * jari_jari ** 2
    return luas

#Fungsi untuk menentukan bilangan ganjil atau genap
#Menerima angka dan mengembalikan "Ganjil" atau "Genap" berdasarkan kondisi
def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

#Fungsi untuk menggabungkan dua kata
#Menerima dua kata dan mengembalikan hasil penggabungan    
def gabung_kata(kata1, kata2):
    hasil = kata1 + " " + kata2
    return hasil

#Fungsi utama
#Merupakan fungsi utama yang menjalankan contoh penggunaan fungsi-fungsi di atas 
def main():
    # Contoh penggunaan fungsi-fungsi di atas
    sisi_persegi = 5
    luas_persegi = hitung_luas_persegi(sisi_persegi)
    print(f"Luas Persegi dengan sisi {sisi_persegi} adalah: {luas_persegi}")

    jari_jari_lingkaran = 7
    luas_lingkaran = hitung_luas_lingkaran(jari_jari_lingkaran)
    print(f"Luas Lingkaran dengan jari-jari {jari_jari_lingkaran} adalah: {luas_lingkaran}")

    angka_ganjil_genap = 10
    status = cek_ganjil_genap(angka_ganjil_genap)
    print(f"{angka_ganjil_genap} adalah bilangan {status}")

    kata1 = "Hello"
    kata2 = "World"
    hasil_gabung = gabung_kata(kata1, kata2)
    print(f"Gabungan kata: {hasil_gabung}")

if __name__ == "__main__":
    main()
