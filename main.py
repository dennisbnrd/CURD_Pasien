from tabulate import tabulate

print("========================================")
print("         Rumah Sakit Purwadhika")
print("========================================")

data_pasien = [{
    "id" : "Pwd001",
    "nama" : "Agus Imron",
    "jenis_kelamin" : "L",
    "umur" : 34,
    "alamat" : "Madura",
    "penyakit" : "Demam",
    "tanggal_masuk" : "07/06/2025",
    "rawat" : "Jalan",
    "ruangan" : "-",
    }, {
    "id" : "Pwd002",
    "nama" : "Cristiano Madun",
    "jenis_kelamin" : "L",
    "umur" : 13,
    "alamat" : "Gersik",
    "penyakit" : "Tifus",
    "tanggal_masuk" : "07/06/2025",
    "rawat" : "Inap",
    "ruangan" : "Rafflesia",
    }, {
    "id" : "Pwd003",
    "nama" : "Ros Sally",
    "jenis_kelamin" : "P",
    "umur" : 26,
    "alamat" : "Surabaya",
    "penyakit" : "Keracunana Makanan",
    "tanggal_masuk" : "09/06/2025",
    "rawat" : "Jalan",
    "ruangan" : "-",
    }]
def menu():
    print("1. Tampilkan Data Pasien")
    print("2. Buat Data Baru Pasien")
    print("3. Ubah Data Pasien")
    print("4. Hapus Data Pasien")
    print("5. Keluar")

def id_pasien():
    return f"Pwd{len(data_pasien)+1:03d}"    

def tambah_data():
    while True:
        tanggal_masuk = input("Masukan Tanggal Masuk Pasien (DD/MMY/YYY):")
        if tanggal_masuk.isdigit():
            continue
        else:
            break
    pasien = {
    "id" :id_pasien(),
    "nama" : input("Masukan Nama Pasien: ").title(),
    "jenis_kelamin" : input("Masukan Jenis Kelamin Pasien (L/P):").capitalize(),
    "umur" : int(input("Masukan Umur Pasien:")),
    "alamat" : input("Masukan Alamat Pasien: "),
    "penyakit" : input("Maasukan Jenis Penyakit Pasien:").capitalize(),
    # "tanggal_masuk" : int(input("Masukan Tanggal Masuk Pasien (DD/MMY/YYY):")),
    "tanggal_masuk": tanggal_masuk,
    "rawat" : input("Masukan Jenis Rawat Pasien (Inap/Jalan):").capitalize(),
    "ruangan" : input("Masukan Nama Ruangan Pasien:"),
    }
    data_pasien.append(pasien)

def cari_pasien():
    nama = input("Masukkan nama pasien: ")  
    hasil = []
    for cari in data_pasien:
        if nama in cari["nama"].lower():
            hasil.append(cari)

    if hasil:
        print(f"\n🔍 Ditemukan {len(hasil)} pasien yang cocok:\n")
        header = {
        "id": "ID Pasien",
        "nama": "Nama",
        "jenis_kelamin": "Jenis Kelamin",
        "umur": "Umur",
        "alamat":"Alamat",
        "penyakit" : "Penyakit",
        "tanggal_masuk" : "Tanggal Masuk",
        "rawat" : "Jenis Rawat",
        "ruangan" : "Ruangan",
    }       
        print("\nData Semua Pasien:\n")
        print(tabulate(hasil, headers=header, tablefmt="grid"))
    else:
        print("Data Pasien Tidak Ditemukan!!!")

def tampil_data():
    # header = ["ID", "Nama Pasien", "Jenis Kelamin", "Umur", "Alamat", "Penyakit", "Tanggal Masuk", "Jenis Rawat", "Ruangan"]
    header = {
    "id": "ID Pasien",
    "nama": "Nama",
    "jenis_kelamin": "Jenis Kelamin",
    "umur": "Umur",
    "alamat":"Alamat",
    "penyakit" : "Penyakit",
    "tanggal_masuk" : "Tanggal Masuk",
    "rawat" : "Jenis Rawat",
    "ruangan" : "Ruangan",
}
    print("\nData Semua Pasien:\n")
    print(tabulate(data_pasien, headers=header, tablefmt="grid"))

def menu_data():
    print("1. Report Seluruh Data Pasien")
    print("2. Report Data Pasien Tertentu")
    print("3. Kembali ke Menu Utama")

# def ubah_data():

# def data_pasien():
# def cari_pasien():
# def ubah_pasien():
# def hapus_pasien():
# def keluar():    

while True:
    print("\n   === Sistem Pasien RS Purwadhika ===")
    menu()
    pilih = input("\nPilih Menu:")

    if pilih == "1":
        while True:
            print("\n   === Data Pasien RS Purwadhika ===")
            menu_data()
            pilih = input("\nPilih Menu:")
            if pilih =="1":
                tampil_data()
                print()
            elif pilih == "2":
                cari_pasien()
                print()
            elif pilih == "3":
                break    
            else:
                print("Menu Tidak Valid")


        
    elif pilih == "2":
        tambah_data()    
    elif pilih == "3":
        cari_pasien()
    # elif pilih == "4":
    #     ubah_buku()
    # elif pilih == "5":
    #     hapus_buku()    
    # elif pilih == "6":
    #     keluar()    
    else:
        menu()             
