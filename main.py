from tabulate import tabulate

# ======================================================
data_pasien = [
    {"id": "Pwd001", "nama": "Agus Imron", "jenis_kelamin": "L", "umur": 34, "alamat": "Madura", "nomor_hp": "08123456789"},
    {"id": "Pwd002", "nama": "Cristiano Madun", "jenis_kelamin": "L", "umur": 13, "alamat": "Gresik", "nomor_hp": "08234567890"},
    {"id": "Pwd003", "nama": "Ros Sally", "jenis_kelamin": "P", "umur": 26, "alamat": "Surabaya", "nomor_hp": "08345678910"},
]

data_reservasi = [{"id_pasien": "Pwd001","keluhan": "Demam Tinggi","tanggal": "20/06/2025","dokter": "dr. Andi","rawat": "Jalan","ruangan": "-"
    }]

data_dokter = [
    {"nama": "dr. Andi", "spesialis": "Umum", "hari": "Senin - Rabu"},
    {"nama": "dr. Budi", "spesialis": "Anak", "hari": "Kamis - Jumat"},
    {"nama": "dr. Clara", "spesialis": "Penyakit Dalam", "hari": "Sabtu"},
]


# ======================================================

def login():
    print("\n=== LOGIN SISTEM ===")
    role = input("Login sebagai (admin/pasien): ").lower()
    username = input("Username (ID Pasien / admin): ").strip()
    password = input("Password: ").strip()

    if role == "admin" and username == "admin" and password == "123":
        print("\nLogin Admin Berhasil!")
        return "admin", username
    elif role == "pasien" and any(p["id"] == username for p in data_pasien) and password == "123":
        print("\nLogin Pasien Berhasil!")
        return "pasien", username

    print("Login gagal.")
    return None, None

# ======================================================

def menu_admin():
    print("\n=== MENU ADMIN ===")
    print("1. Data Pasien")
    print("2. Data Reservasi")
    print("3. Data Dokter")
    print("4. Keluar")

def sub_menu_data():
    print("\n==== Menu Data Pasien Admin ====")
    print("1. Lihat Semua Data Pasien")
    print("2. Cari Data Pasien")
    print("3. Tambah Data Pasien")
    print("4. Ubah Data Pasien")
    print("5. Hapus Data Pasien")
    print("6. Keluar")

def sub_menu_reservasi():
    print("\n==== Menu Data Reservasi Admin ====")
    print("1. Lihat Semua Data Reservasi")
    print("2. Cari Data Reservasi")
    print("3. Ubah Data Reservasi")
    print("4. Hapus Data Reservasi")
    print("5. Keluar")

def sub_menu_dokter():
    print("\n==== Menu Data Dokter Admin ====")
    print("1. Lihat Jadwal Dokter")
    print("2. Tambah Jadawal Dokter")
    print("3. Ubah Jadwal Dokter")
    print("4. Hapus Jadwal Dokter")
    print("5. Keluar")

def menu_pasien():
    print("\n=== MENU PASIEN ===")
    print("1. Lihat Jadwal Dokter")
    print("2. Buat Reservasi")
    print("3. Ubah Data Diri")
    print("4. Hapus Reservasi")
    print("5. Keluar")

#============================================================
def id_pasien_baru():
    return f"Pwd{len(data_pasien)+1:03d}"


def tambah_pasien():
    print("\n=== Tambah Data Pasien ===")
    
    id_baru = id_pasien_baru()
    nama = input("Masukkan Nama Pasien: ").title()

    while True:
        jenis_kelamin = input("Jenis Kelamin (L/P): ").strip().upper()
        if jenis_kelamin in ["L", "P"]:
            break
        print("Jenis kelamin hanya boleh 'L' (Laki-laki) atau 'P' (Perempuan).")

    while True:
        try:
            umur = int(input("Umur: "))
            if umur > 0 and umur < 100:
                break
            print("Umur harus lebih dari 0 dan kurang dari 100.")
        except ValueError:
            print("Umur harus berupa angka.")

    alamat = input("Alamat: ").title()

    while True:
        nomor_hp = input("Nomor HP: ").strip()
        if nomor_hp.isdigit() and len(nomor_hp) <= 12:
            break
        print("Nomor HP harus berupa angka dan maksimal 12 digit.")

    pasien = {
        "id": id_baru,
        "nama": nama,
        "jenis_kelamin": jenis_kelamin,
        "umur": umur,
        "alamat": alamat,
        "nomor_hp": nomor_hp
    }

    print("\nData yang akan ditambahkan:")
    tabel = [[k.replace("_", " ").title(), v] for k, v in pasien.items()]
    print(tabulate(tabel, tablefmt="grid"))

    while True:
        konfirmasi = input("\nApakah data sudah benar dan ingin disimpan? (Y/N): ").strip().upper()
        if konfirmasi == "Y":
            data_pasien.append(pasien)
            print(f"Pasien berhasil ditambahkan dengan ID {pasien['id']}")
            break
        elif konfirmasi == "N":
            print("Penambahan data pasien dibatalkan.")
            break
        else:
            print("Input tidak valid. Harap masukkan 'Y' atau 'N'.")

def tampil_data_pasien():
    print("\n=== Semua Data Pasien ===")
    print(tabulate(data_pasien, headers="keys", tablefmt="grid"))

def cari_data_pasien():
    keyword = input("Masukkan nama pasien: ").lower()
    hasil = [p for p in data_pasien if keyword in p["nama"].lower()]
    if hasil:
        print(tabulate(hasil, headers="keys", tablefmt="grid"))
    else:
        print("Pasien tidak ditemukan.")

def ubah_data_diri(id_pasien):
    pasien = next((p for p in data_pasien if p["id"] == id_pasien), None)
    if not pasien:
        print("Data pasien tidak ditemukan.")
        return

    print("\n=== Data Diri Saat Ini ===")
    print(tabulate([pasien], headers="keys", tablefmt="grid"))

    print("\n=== Ubah Data Diri ===")
    perubahan = pasien.copy()  

    for key in ["nama", "jenis_kelamin", "umur", "alamat", "nomor_hp"]:
        new_val = input(f"{key.replace('_',' ').title()} baru (biarkan kosong jika tidak ingin mengubah): ")
        if new_val:
            if key == "umur":
                if new_val.isdigit():
                    perubahan[key] = int(new_val)
                else:
                    print("Umur harus berupa angka. Lewati.")
            elif key == "jenis_kelamin":
                if new_val.upper() in ["L", "P"]:
                    perubahan[key] = new_val.upper()
                else:
                    print("Jenis kelamin harus 'L' atau 'P'. Lewati.")
            elif key == "nomor_hp":
                if new_val.isdigit() and len(new_val) <= 12:
                    perubahan[key] = new_val
                else:
                    print("Nomor HP harus berupa angka maksimal 12 digit. Lewati.")
            elif key in ["nama", "alamat"]:
                perubahan[key] = new_val.title()
            else:
                perubahan[key] = new_val

    print("\n=== Data Diri Setelah Diubah (Pratinjau) ===")
    print(tabulate([perubahan], headers="keys", tablefmt="grid"))

    while True:
        konfirmasi = input("Apakah data sudah benar dan ingin disimpan? (Y/N): ").strip().lower()
        if konfirmasi == "y":
            pasien.update(perubahan)
            break
        elif konfirmasi == "n":
            print("Penambahan data pasien dibatalkan.")
            break
        else:
            print("Input tidak valid. Harap masukkan 'Y' atau 'N'.")

def ubah_data_pasien():
    print(tabulate(data_pasien, headers="keys", tablefmt="grid"))
    id_pas = input("\nMasukkan ID Pasien yang ingin diubah: ").strip()
    pasien = next((p for p in data_pasien if p["id"] == id_pas), None)
    if not pasien:
        print("Data pasien tidak ditemukan.")
        return

    print("\n=== Data Saat Ini ===")
    print(tabulate([pasien], headers="keys", tablefmt="grid"))

    perubahan = pasien.copy()

    for key in ["nama", "jenis_kelamin", "umur", "alamat", "nomor_hp"]:
        new_val = input(f"{key.replace('_',' ').title()} baru (biarkan kosong jika tidak ingin mengubah): ")
        if new_val:
            if key == "umur":
                if new_val.isdigit():
                    perubahan[key] = int(new_val)
                else:
                    print("Umur harus berupa angka. Lewati.")
            elif key == "jenis_kelamin":
                if new_val.upper() in ["L", "P"]:
                    perubahan[key] = new_val.upper()
                else:
                    print("Jenis kelamin harus 'L' atau 'P'. Lewati.")
            elif key == "nomor_hp":
                if new_val.isdigit() and len(new_val) <= 12:
                    perubahan[key] = new_val
                else:
                    print("Nomor HP harus berupa angka maksimal 12 digit. Lewati.")
            elif key in ["nama", "alamat"]:
                perubahan[key] = new_val.title()
            else:
                perubahan[key] = new_val

    print("\n=== Data Setelah Perubahan (Pratinjau) ===")
    print(tabulate([perubahan], headers="keys", tablefmt="grid"))

    while True:
        konfirmasi = input("Apakah data sudah benar dan ingin disimpan? (Y/N): ").strip().lower()
        if konfirmasi == "y":
            pasien.update(perubahan)
            break
        elif konfirmasi == "N":
            print("Penambahan data pasien dibatalkan.")
            break
        else:
            print("Input tidak valid. Harap masukkan 'Y' atau 'N'.")



def hapus_data_pasien():
    global data_pasien
    global data_reservasi
    print(tabulate(data_pasien, headers="keys", tablefmt="grid"))
    id_pas = input("\nMasukkan ID Pasien yang ingin dihapus: ").strip()
    

    pasien = next((p for p in data_pasien if p["id"] == id_pas), None)
    if not pasien:
        print("Data pasien tidak ditemukan.")
        return

    print("\n=== Data Pasien Ditemukan ===")
    print(tabulate([pasien], headers="keys", tablefmt="grid"))

    while True:
        konfirmasi = input(f"Apakah Anda yakin ingin menghapus pasien dengan ID {id_pas}? (Y/N): ").strip().lower()
        if konfirmasi == "y":
            data_pasien = [p for p in data_pasien if p["id"] != id_pas]
            data_reservasi = [r for r in data_reservasi if r["id_pasien"] != id_pas]
            print(f"Data pasien dan semua reservasi dengan ID {id_pas} berhasil dihapus.")
            break
        elif konfirmasi == "n":
            print("Penghapusan dibatalkan.")
            break
        else:
            print("Input tidak valid. Silakan masukkan 'Y' atau 'N'.")

def lihat_jadwal_admin():
    print("\n=== Jadwal Dokter ===")
    if data_dokter:
        print(tabulate(data_dokter, headers="keys", tablefmt="grid"))
    else:
        print("Belum ada jadwal dokter.")

def tambah_jadwal_dokter():
    print("\n=== Tambah Jadwal Dokter ===")
    
    nama = input("Nama Dokter: ").title().strip()
    if not nama:
        print("Nama dokter tidak boleh kosong.")
        return
    if any(d["nama"] == nama for d in data_dokter):
        print("Dokter sudah terdaftar.")
        return

    spesialis = input("Spesialis: ").title().strip()
    if not spesialis:
        print("Spesialis tidak boleh kosong.")
        return

    hari = input("Hari Praktek (contoh: Senin - Rabu): ").title().strip()
    if not hari:
        print("Hari praktek tidak boleh kosong.")
        return

    calon_data = {"nama": nama, "spesialis": spesialis, "hari": hari}
    print("\n=== Data Jadwal Dokter Baru ===")
    print(tabulate([calon_data], headers="keys", tablefmt="grid"))

    while True:
        konfirmasi = input("Apakah data sudah benar dan ingin disimpan? (Y/N): ").strip().lower()
        if konfirmasi == "y":
            data_dokter.append(calon_data)
            print("Jadwal dokter berhasil ditambahkan.")
            break
        elif konfirmasi == "n":
            print("Penambahan dibatalkan.")
            break
        else:
            print("Input tidak valid. Silakan masukkan 'Y' atau 'N'.")


def ubah_jadwal_dokter():
    lihat_jadwal_admin()
    nama = input("Masukkan nama dokter yang ingin diubah: ").strip()
    dokter = next((d for d in data_dokter if d["nama"] == nama), None)

    if not dokter:
        print("Dokter tidak ditemukan.")
        return

    print("\n=== Data Jadwal Saat Ini ===")
    print(tabulate([dokter], headers="keys", tablefmt="grid"))

    print("\nBiarkan kosong jika tidak ingin mengubah.")
    spesialis_baru = input("Spesialis baru: ").title().strip()
    hari_baru = input("Hari praktek baru: ").title().strip()

    perubahan = dokter.copy()
    if spesialis_baru:
        perubahan["spesialis"] = spesialis_baru
    if hari_baru:
        perubahan["hari"] = hari_baru

    print("\n=== Pratinjau Perubahan ===")
    print(tabulate([perubahan], headers="keys", tablefmt="grid"))

    while True:
        konfirmasi = input("Apakah Anda yakin ingin menyimpan perubahan ini? (Y/N): ").strip().lower()
        if konfirmasi == "y":
            dokter.update(perubahan)
            print("Jadwal dokter berhasil diubah.")
            break
        elif konfirmasi == "n":
            print("Perubahan dibatalkan.")
            break
        else:
            print("Input tidak valid. Silakan masukkan 'Y' atau 'N'.")

def hapus_jadwal_dokter():
    lihat_jadwal_admin()
    nama = input("Masukkan nama dokter yang ingin dihapus: ").strip()
    global data_dokter

    dokter = next((d for d in data_dokter if d["nama"] == nama), None)
    if not dokter:
        print("Dokter tidak ditemukan.")
        return

    print("\n=== Data Dokter Ditemukan ===")
    print(tabulate([dokter], headers="keys", tablefmt="grid"))

    while True:
        konfirmasi = input(f"Apakah Anda yakin ingin menghapus jadwal dokter {nama}? (Y/N): ").strip().lower()
        if konfirmasi == "y":
            data_dokter = [d for d in data_dokter if d["nama"] != nama]
            print(f"Jadwal dokter '{nama}' berhasil dihapus.")
            break
        elif konfirmasi == "n":
            print("Penghapusan dibatalkan.")
            break
        else:
            print("Input tidak valid. Silakan masukkan 'Y' atau 'N'.")

def tambah_reservasi(id_pasien):
    print("\n=== Buat Reservasi ===")
    if data_dokter:
        print(tabulate(data_dokter, headers="keys", tablefmt="grid"))

    keluhan = input("\nMasukkan Keluhan: ").strip().capitalize()
    if not keluhan:
        print("Keluhan tidak boleh kosong.")
        return

    tanggal = input("Masukkan Tanggal (DD/MM/YYYY): ").strip()
    if not tanggal:
        print("Tanggal tidak boleh kosong.")
        return

    dokter = input("Masukkan Nama Dokter: ").strip().title()
    if not dokter:
        print("Nama dokter tidak boleh kosong.")
        return

    rawat = input("Rawat (Inap/Jalan): ").strip().title()
    if rawat not in ["Inap", "Jalan"]:
        print("Input rawat hanya boleh 'Inap' atau 'Jalan'.")
        return

    ruangan = input("Nama Ruangan (kosong jika rawat jalan): ").strip() if rawat == "Inap" else "-"

    reservasi_baru = {
        "id_pasien": id_pasien,
        "keluhan": keluhan,
        "tanggal": tanggal,
        "dokter": dokter,
        "rawat": rawat,
        "ruangan": ruangan
    }

    print("\n=== Pratinjau Reservasi ===")
    print(tabulate([reservasi_baru], headers="keys", tablefmt="grid"))

    while True:
        konfirmasi = input("Apakah data sudah benar dan ingin disimpan? (Y/N): ").strip().lower()
        if konfirmasi == "y":
            data_reservasi.append(reservasi_baru)
            print("Reservasi berhasil ditambahkan.")
            break
        elif konfirmasi == "n":
            print("Reservasi dibatalkan.")
            break
        else:
            print("Input tidak valid. Masukkan 'Y' atau 'N'.")


def ubah_data_reservasi():
    print(tabulate(data_reservasi, headers="keys", tablefmt="grid"))

    id_pas = input("Masukkan ID Pasien untuk ubah reservasi: ").strip()
    reservasi = next((r for r in data_reservasi if r["id_pasien"] == id_pas), None)
    
    if not reservasi:
        print("Data reservasi tidak ditemukan.")
        return

    print("\n=== Data Reservasi Saat Ini ===")
    print(tabulate([reservasi], headers="keys", tablefmt="grid"))

    print("\n=== Ubah Data Reservasi ===")
    new_keluhan = input("Keluhan baru (kosong jika tidak ingin mengubah): ").strip()
    new_tanggal = input("Tanggal baru (kosong jika tidak ingin mengubah): ").strip()
    new_dokter = input("Dokter baru (kosong jika tidak ingin mengubah): ").strip()
    new_rawat = input("Rawat (Inap/Jalan, kosong jika tidak ingin mengubah): ").strip().title()
    new_ruangan = input("Ruangan (kosong jika rawat jalan atau tidak ingin mengubah): ").strip()

    calon = reservasi.copy()
    if new_keluhan: calon["keluhan"] = new_keluhan
    if new_tanggal: calon["tanggal"] = new_tanggal
    if new_dokter: calon["dokter"] = new_dokter
    if new_rawat in ["Inap", "Jalan"]:
        calon["rawat"] = new_rawat
        calon["ruangan"] = new_ruangan if new_rawat == "Inap" else "-"
    elif new_rawat:
        print("Rawat hanya boleh 'Inap' atau 'Jalan'. Perubahan dibatalkan.")
        return

    print("\n=== Pratinjau Perubahan ===")
    print(tabulate([calon], headers="keys", tablefmt="grid"))

    while True:
        konfirmasi = input("Apakah Anda yakin ingin menyimpan perubahan ini? (Y/N): ").strip().lower()
        if konfirmasi == "y":
            reservasi.update(calon)
            print("Reservasi berhasil diperbarui.")
            break
        elif konfirmasi == "n":
            print("Perubahan dibatalkan.")
            break
        else:
            print("Input tidak valid. Masukkan 'Y' atau 'N'.")

def cari_data_reservasi():
    keyword = input("Masukkan ID atau Nama Pasien yang ingin dicari: ").strip().lower()

    hasil = []
    for r in data_reservasi:
        pasien = next((p for p in data_pasien if p["id"] == r["id_pasien"]), None)
        if pasien and (keyword in pasien["id"].lower() or keyword in pasien["nama"].lower()):
            hasil.append({
                "ID Pasien": pasien["id"],
                "Nama": pasien["nama"],
                "Dokter": r["dokter"],
                "Tanggal": r["tanggal"],
                "Keluhan": r["keluhan"],
                "Rawat": r["rawat"],
                "Ruangan": r["ruangan"]
            })

    if hasil:
        print("\n=== Hasil Pencarian Reservasi ===")
        print(tabulate(hasil, headers="keys", tablefmt="grid"))
    else:
        print("❌ Tidak ada data reservasi yang cocok.")


def hapus_reservasi():
    global data_reservasi

    print(tabulate(data_reservasi, headers="keys", tablefmt="grid"))

    id_pas = input("Masukkan ID Pasien untuk hapus reservasi: ").strip()

    reservasi_ditemukan = [r for r in data_reservasi if r["id_pasien"] == id_pas]

    if not reservasi_ditemukan:
        print("Reservasi tidak ditemukan.")
        return

    print("\n=== Data Reservasi Ditemukan ===")
    print(tabulate(reservasi_ditemukan, headers="keys", tablefmt="grid"))

    while True:
        konfirmasi = input(f"Apakah Anda yakin ingin menghapus semua reservasi untuk pasien ID {id_pas}? (Y/N): ").strip().lower()
        if konfirmasi == "y":
            data_reservasi = [r for r in data_reservasi if r["id_pasien"] != id_pas]
            print(f"Semua reservasi untuk pasien ID {id_pas} berhasil dihapus.")
            break
        elif konfirmasi == "n":
            print("Penghapusan dibatalkan.")
            break
        else:
            print("Input tidak valid. Silakan masukkan 'Y' atau 'N'.")


def hapus_reservasi_pasien(id_pasien):
    global data_reservasi  

    reservasi_pasien = [r for r in data_reservasi if r["id_pasien"] == id_pasien]
    
    if not reservasi_pasien:
        print("Anda belum memiliki reservasi.")
        return

    print("\n=== Reservasi Anda Saat Ini ===")
    print(tabulate(reservasi_pasien, headers="keys", tablefmt="grid"))

    while True:
        konfirmasi = input("Apakah Anda yakin ingin menghapus semua reservasi Anda? (Y/N): ").strip().lower()
        if konfirmasi == "y":
            data_reservasi = [r for r in data_reservasi if r["id_pasien"] != id_pasien]
            print("Semua reservasi Anda berhasil dihapus.")
            break
        elif konfirmasi == "n":
            print("Penghapusan dibatalkan.")
            break
        else:
            print("Input tidak valid. Silakan masukkan 'Y' atau 'N'.")


def tampil_data_gabungan():
    print("\n=== Data Gabungan Pasien & Reservasi ===")
    data_gabungan = []
    for reservasi in data_reservasi:
        pasien = next((p for p in data_pasien if p["id"] == reservasi["id_pasien"]), None)
        if pasien:
            data_gabungan.append({
                "ID Pasien": pasien["id"],
                "Nama": pasien["nama"],
                "Nomor HP": pasien["nomor_hp"],
                "Alamat": pasien["alamat"],
                "Keluhan": reservasi["keluhan"],
                "Tanggal": reservasi["tanggal"],
                "Dokter": reservasi["dokter"],
                "Rawat": reservasi.get("rawat", "-"),
                "Ruangan": reservasi.get("ruangan", "-")
            })
    if data_gabungan:
        print(tabulate(data_gabungan, headers="keys", tablefmt="grid"))
    else:
        print("Belum ada data reservasi.")


while True:
    print("="*40)
    print("     SELAMAT DATANG DI RS PURWADHIKA")
    print("="*40)
    role, user = login()
    if role == "admin":
        while True:
            menu_admin()
            pilih = input("Pilih menu: ")
            if pilih == "1":
                while True:
                    sub_menu_data()
                    pilih = input("Pilih menu: ")

                    if pilih == "1":
                        tampil_data_pasien()
                        print()
                    elif pilih =="2":
                        cari_data_pasien()
                        print()
                    elif pilih == "3":
                        tambah_pasien()
                        print()
                    elif pilih == "4":
                        ubah_data_pasien()
                        print()
                    elif pilih == "5":
                        hapus_data_pasien()
                        print()    
                    elif pilih == "6":
                        break
                    else:
                        print("Menu Tidak Valid")    

            elif pilih == "2":
                while True:
                    sub_menu_reservasi()
                    pilih = input("Pilih menu: ")

                    if pilih == "1":
                        tampil_data_gabungan()
                        print()
                    elif pilih =="2":
                        cari_data_reservasi()
                        print()
                    elif pilih == "3":
                        ubah_data_reservasi()
                        print()
                    elif pilih == "4":
                        hapus_reservasi()
                        print()
                    elif pilih == "5":
                        break
                    else:
                        print("Menu Tidak Valid")     

            elif pilih == "3":
                while True:
                    sub_menu_dokter()
                    pilih = input("Pilih Menu: ")
                    if pilih == "1":
                        lihat_jadwal_admin()
                    elif pilih == "2":
                        tambah_jadwal_dokter()
                    elif pilih == "3":
                        ubah_jadwal_dokter()
                    elif pilih == "4":
                        hapus_jadwal_dokter()
                    elif pilih == "5":
                        break    
                    else:
                        print("Menu tidak valid.")

            elif pilih == "4":
                print("\nKeluar dari sistem admin...")
                break
            else:
                print("\nMenu tidak valid.")
    elif role == "pasien":
        while True:
            menu_pasien()
            pilih = input("Pilih menu: ")
            if pilih == "1": lihat_jadwal_admin()
            elif pilih == "2": tambah_reservasi(user)
            elif pilih == "3": ubah_data_diri(user)
            elif pilih == "4": hapus_reservasi_pasien(user)
            elif pilih == "5":
                print("Keluar dari sistem pasien...")
                break
            else:
                print("Menu tidak valid.")
