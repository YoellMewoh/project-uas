#permainan gunting,batu,kertas
import random

#memasukan pilihan
def permainan_gbk(pilihan_pemain):
    pilihan_komputer = random.choice(['gunting', 'batu', 'kertas'])
    
    print(f"\nPilihan Komputer: {pilihan_komputer}")
    print(f"Pilihan Pemain: {pilihan_pemain}")

#menunjukan hasil pemain menang,kalah,atau seimbang
    if pilihan_pemain == pilihan_komputer:
        return "Seimbang!"
    elif (pilihan_pemain == 'gunting' and pilihan_komputer == 'kertas') or \
         (pilihan_pemain == 'batu' and pilihan_komputer == 'gunting') or \
         (pilihan_pemain == 'kertas' and pilihan_komputer == 'batu'):
        return "Pemain Menang!"
    else:
        return "Komputer Menang!"

#Fungsi utama main berisi loop yang memungkinkan pemain untuk terus bermain hingga memilih untuk keluar
def main():
    print("Selamat datang di permainan Gunting-Batu-Kertas!")
    print("Pilihan: gunting, batu, kertas")

    while True:
        pilihan_pemain = input("\nMasukkan pilihan Anda: ").lower()

        if pilihan_pemain not in ['gunting', 'batu', 'kertas']:
            print("Pilihan tidak valid. Coba lagi.")
            continue

        hasil = permainan_gbk(pilihan_pemain)
        print(hasil)

        ulangi = input("\nIngin bermain lagi? (ya/tidak): ").lower()
        if ulangi != 'ya':
            print("Terima kasih telah bermain. Sampai jumpa!")
            break

if __name__ == "__main__":
    main()
