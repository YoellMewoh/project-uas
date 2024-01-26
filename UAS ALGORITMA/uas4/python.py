#Menu adalah kelas untuk merepresentasikan item-menu dengan atribut nama dan harga
class Menu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

#Warkop adalah kelas utama yang menyimpan menu minuman, menu makanan, dan pesanan pelanggan 
class Warkop:
    def __init__(self):
        self.menu_minuman = [
            Menu("Kopi Hitam", 5000),
            Menu("Cappuccino", 8000),
            Menu("Teh Manis", 3000)
        ]

        self.menu_makanan = [
            Menu("Nasi Goreng", 12000),
            Menu("Mie Goreng", 10000),
            Menu("Roti Bakar", 5000)
        ]

        self.pesanan = []

#tampilkan_menu: Menampilkan menu berdasarkan jenis (minuman/makanan)
    def tampilkan_menu(self, jenis_menu):
        print(f"\nMenu {jenis_menu}:")
        for i, menu in enumerate(jenis_menu, 1):
            print(f"{i}. {menu.nama} - Rp {menu.harga}")

#pesan_menu: Menerima pesanan dari pelanggan dan menambahkannya ke dalam pesanan
    def pesan_menu(self, jenis_menu):
        self.tampilkan_menu(jenis_menu)
        nomor_pesanan = int(input("\nPilih nomor menu yang ingin dipesan: "))
        jumlah_pesanan = int(input("Masukkan jumlah pesanan: "))

        if jenis_menu == self.menu_minuman:
            pesanan = (self.menu_minuman[nomor_pesanan - 1].nama, jumlah_pesanan, self.menu_minuman[nomor_pesanan - 1].harga)
        elif jenis_menu == self.menu_makanan:
            pesanan = (self.menu_makanan[nomor_pesanan - 1].nama, jumlah_pesanan, self.menu_makanan[nomor_pesanan - 1].harga)

        self.pesanan.append(pesanan)
        print(f"{jumlah_pesanan} {jenis_menu[nomor_pesanan - 1].nama} telah ditambahkan ke pesanan.")

#Menghitung total harga pesanan
    def hitung_total(self):
        total = sum(item[1] * item[2] for item in self.pesanan)
        return total

#Mencetak struk pembayaran
    def cetak_struk(self):
        print("\nStruk Pembayaran:")
        for item in self.pesanan:
            print(f"{item[1]} {item[0]} - Rp {item[2]}")
        print(f"\nTotal Pembayaran: Rp {self.hitung_total()}")

#Fungsi main menjalankan program utama dengan memberikan opsi kepada pengguna untuk memesan minuman/makanan, melihat pesanan, atau selesai dan membayar
def main():
    warkop = Warkop()

    while True:
        print("\nSelamat datang di Warkop XYZ!")
        print("1. Pesan Minuman")
        print("2. Pesan Makanan")
        print("3. Lihat Pesanan")
        print("4. Selesai dan Bayar")
        print("5. Keluar")

        pilihan = input("Silakan pilih menu (1-5): ")

        if pilihan == '1':
            warkop.pesan_menu(warkop.menu_minuman)
        elif pilihan == '2':
            warkop.pesan_menu(warkop.menu_makanan)
        elif pilihan == '3':
            warkop.cetak_struk()
        elif pilihan == '4':
            warkop.cetak_struk()
            print("Terima kasih telah berkunjung di warkop xyz! hati-hati di jalan")
            break
        elif pilihan == '5':
            print("Terima kasih. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

#Program akan terus berjalan hingga pengguna memilih untuk keluar.
if __name__ == "__main__":
    main()
