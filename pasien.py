print("==============================================")
print("       SISTEM DATA PASIEN RUMAH SAKIT")
print("==============================================")


obat = {
    1: ["Paracetamol", 5000, 20],
    2: ["Amoxicillin", 10000, 15],
    3: ["Antasida", 7000, 18],
    4: ["Vitamin C", 8000, 25],
    5: ["Ibuprofen", 9000, 12],
    6: ["Cetirizine", 6000, 10],
    7: ["OBH", 12000, 14],
    8: ["Oralit", 4000, 30],
    9: ["Omeprazole", 11000, 16],
    10: ["Salep Kulit", 15000, 8]
}


pasien = []


while True:

    print("\n==============================================")
    print("             INPUT DATA PASIEN")
    print("==============================================")

    
    nama = input("Nama Lengkap       : ")
    umur = int(input("Umur               : "))
    jenis_kelamin = input("Jenis Kelamin      : ")
    alamat = input("Alamat             : ")

  
    print("\n---------- DATA RAWAT INAP ----------")

    kamar = input("Nomor Kamar        : ")
    ruangan = input("Nama Ruangan       : ")

    status = input("Status (Opname)    : ")

    
    print("\n========== DAFTAR OBAT APOTEK ==========")

    for nomor, data in obat.items():
        print(nomor, ".", data[0],
              "| Harga: Rp", data[1],
              "| Stok:", data[2])

   
    pilihan = int(input("\nPilih Nomor Obat (1-10): "))
    jumlah = int(input("Jumlah Obat: "))

    nama_obat = "-"
    total = 0

    if pilihan >= 1 and pilihan <= 10:

        nama_obat = obat[pilihan][0]
        harga = obat[pilihan][1]
        stok = obat[pilihan][2]

        if jumlah > 0 and jumlah <= stok:

            total = harga * jumlah
            obat[pilihan][2] -= jumlah

            print("\nObat berhasil dicatat!")
            print("Nama Obat  :", nama_obat)
            print("Jumlah     :", jumlah)
            print("Total Harga: Rp", total)
            print("Sisa Stok  :", obat[pilihan][2])

        elif jumlah > stok:
            print("Stok obat tidak mencukupi!")

        else:
            print("Jumlah obat tidak valid!")

    else:
        print("Nomor obat tidak tersedia!")


    pasien.append({
        "nama": nama,
        "umur": umur,
        "jenis_kelamin": jenis_kelamin,
        "alamat": alamat,
        "kamar": kamar,
        "ruangan": ruangan,
        "status": status,
        "obat": nama_obat,
        "jumlah": jumlah,
        "total": total
    })


    print("\n==============================================")
    print("              DATA PASIEN")
    print("==============================================")

    print("Nama          :", nama)
    print("Umur          :", umur)
    print("Jenis Kelamin :", jenis_kelamin)
    print("Alamat        :", alamat)
    print("Nomor Kamar   :", kamar)
    print("Ruangan       :", ruangan)
    print("Status        :", status)
    print("Nama Obat     :", nama_obat)
    print("Jumlah Obat   :", jumlah)
    print("Total Harga   : Rp", total)

  
    print("\n==============================================")
    lanjut = input("Tambah Pasien Baru? (ya/tidak): ").lower()

    if lanjut != "ya":
        break


print("\n==============================================")
print("          LAPORAN SELURUH PASIEN")
print("==============================================")

for i, data in enumerate(pasien):

    print("\nPasien ke-", i + 1)
    print("Nama          :", data["nama"])
    print("Umur          :", data["umur"])
    print("Jenis Kelamin :", data["jenis_kelamin"])
    print("Alamat        :", data["alamat"])
    print("Nomor Kamar   :", data["kamar"])
    print("Ruangan       :", data["ruangan"])
    print("Status        :", data["status"])
    print("Obat          :", data["obat"])
    print("Jumlah Obat   :", data["jumlah"])
    print("Total Harga   : Rp", data["total"])

print("\nJumlah Seluruh Pasien:", len(pasien))

print("\n==============================================")
print("          PROGRAM SELESAI")
print("==============================================")