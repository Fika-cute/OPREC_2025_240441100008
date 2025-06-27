# produk disimpan
produk = {
    "Laptop": 5500000,
    "Smartphone": 3000000, 
    "Tablet": 2000000, 
    "Smartwatch":1500000, 
    "Headphone": 500000
}

def transaksi():
    print ("==== STRUK PEMBELIAN ====")
    print (f"Nama Pembeli",nama)
    print (f"Produk Dibeli", gadget)

# proses perulangan
while True:
    print ("==TOKO PRODUK ELEKTRONIK==")
    print ("1. Beli Produk")
    print ("2. Cetak Struk")
    print ("3. Keluar")
    pilih = (input("Masukkan Pilihan: "))
    if pilih == 1 :
        nama = (input("masukkan nama: "))
        umur = (input("masukkan umur: "))
        member = (input("Apakah anda member? (y/t): "))
        if member == "y":
            hitung_diskon()
        else:
            print("bukan pilihan")
        print ("1. Laptop")
        print ("2. Smartphone")
        print ("3. Tablet")
        print ("4. Smartwatch")
        print ("5. Headphone")
        gadget = (input("Pilih Gadget: "))
        if gadget == "Laptop" :
            harga_unit = 5500000
        elif gadget == "Smartphone" :
            harga_unit = 3000000
        elif gadget == "Tablet" :
            harga_unit = 2000000
        elif gadget == "Smartwatch" :
            harga_unit = 1500000
        elif gadget == "Headphone" :
            harga_unit = 500000
        else :
            print ("tidak ada produk itu")
        jumlah = (input("masukkan jumlah Unit : "))
        tawar = (input("Apakah anda ingin melakukan penawaran? (y/t): "))
        if tawar == "y":
            harga_tawar = (input("Masukkan Harga Tawar"))
            if harga_tawar < harga_unit :
                cek_penawaran()
            else:
                print("Penawaran di tolak. Harga asli digunakan")
        else:
            print("bukan pilihan")
    elif pilih == 2:
        transaksi()
    elif pilih == 3 :
        break
    else:
        print("bukan pilihan")
