from tabulate import tabulate

# =================== DATA ===================
data_pasien = [
    {"id": "Pwd001", "nama": "Agus Imron", "jenis_kelamin": "L", "umur": 34, "alamat": "Madura", "nomor_hp": "08123456789"},
    {"id": "Pwd002", "nama": "Cristiano Madun", "jenis_kelamin": "L", "umur": 13, "alamat": "Gresik", "nomor_hp": "08234567890"},
    {"id": "Pwd003", "nama": "Ros Sally", "jenis_kelamin": "P", "umur": 26, "alamat": "Surabaya", "nomor_hp": "08345678910"},
]

data_reservasi = []

data_dokter = [
    {"nama": "dr. Andi", "spesialis": "Umum", "hari": "Senin - Rabu"},
    {"nama": "dr. Budi", "spesialis": "Anak", "hari": "Kamis - Jumat"},
    {"nama": "dr. Clara", "spesialis": "Penyakit Dalam", "hari": "Sabtu"},
]


# =================== LOGIN ===================

def login():
    print("\n=== LOGIN SISTEM ===")
    role = input("Login sebagai (admin/pasien): ").lower()
    username = input("Username (ID Pasien / admin): ").strip()
    password = input("Password: ").strip()

    if role == "admin" and username == "admin" and password == "123":
        print("\n✅ Login Admin Berhasil!")
        return "admin", username
    elif role == "pasien" and any(p["id"] == username for p in data_pasien) and password == "123":
        print("\n✅ Login Pasien Berhasil!")
        return "pasien", username

    print("❌ Login gagal.")
    return None, None

# =================== MENU ===================

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

def sub_menu_reservasi():
    print("\n==== Menu Data Reservasi Admin ====")
    print("1. Lihat Semua Data Reservasi")
    print("2. Cari Data Reservasi")
    print("3. Ubah Data Reservasi")
    print("4. Hapus Data Reservasi")

def sub_menu_dokter():
    print("\n==== Menu Data Dokter ====")
    print("1. Lihat Jadwal Dokter")
    print("2. Tambah Jadawal Dokter")
    print("3. Ubah Jadwal Dokter")
    print("4. Hapus Jadwal Dokter")

def menu_pasien():
    print("\n=== MENU PASIEN ===")
    print("1. Lihat Jadwal Dokter")
    print("2. Buat Reservasi")
    print("3. Ubah Data Diri")
    print("4. Hapus Reservasi")
    print("5. Keluar")

# =================== FUNGSI PASIEN ===================

def id_pasien_baru():
    return f"Pwd{len(data_pasien)+1:03d}"

def tambah_pasien():
    print("\n=== Tambah Data Pasien ===")
    pasien = {
        "id": id_pasien_baru(),
        "nama": input("Masukkan Nama Pasien: ").title(),
        "jenis_kelamin": input("Jenis Kelamin (L/P): ").upper(),
        "umur": int(input("Umur: ")),
        "alamat": input("Alamat: ").title(),
        "nomor_hp": input("Nomor HP: ")
    }
    data_pasien.append(pasien)
    print(f"✅ Pasien berhasil ditambahkan dengan ID {pasien['id']}")

def tampil_data_pasien():
    print("\n=== Semua Data Pasien ===")
    print(tabulate(data_pasien, headers="keys", tablefmt="grid"))

def cari_data_pasien():
    keyword = input("Masukkan nama pasien: ").lower()
    hasil = [p for p in data_pasien if keyword in p["nama"].lower()]
    if hasil:
        print(tabulate(hasil, headers="keys", tablefmt="grid"))
    else:
        print("❌ Pasien tidak ditemukan.")

from tabulate import tabulate

def ubah_data_diri(id_pasien):
    pasien = next((p for p in data_pasien if p["id"] == id_pasien), None)
    if not pasien:
        print("❌ Data pasien tidak ditemukan.")
        return

    print("\n=== Data Diri Saat Ini ===")
    print(tabulate([pasien], headers="keys", tablefmt="grid"))

    print("\n=== Ubah Data Diri ===")
    for key in ["nama", "jenis_kelamin", "umur", "alamat", "nomor_hp"]:
        new_val = input(f"{key.replace('_',' ').title()} baru (biarkan kosong jika tidak ingin mengubah): ")
        if new_val:
            if key == "umur":
                if new_val.isdigit():
                    pasien[key] = int(new_val)
                else:
                    print("❌ Umur harus berupa angka. Lewati.")
            elif key == "jenis_kelamin":
                if new_val.upper() in ["L", "P"]:
                    pasien[key] = new_val.upper()
                else:
                    print("❌ Jenis kelamin harus 'L' atau 'P'. Lewati.")
            elif key == "nomor_hp":
                if new_val.isdigit():
                    pasien[key] = new_val
                else:
                    print("❌ Nomor HP harus berupa angka. Lewati.")
            elif key in ["nama", "alamat"]:
                pasien[key] = new_val.title()
            else:
                pasien[key] = new_val

    print("✅ Data diri berhasil diperbarui.")

def ubah_data_pasien():
    id_pas = input("Masukkan ID Pasien yang ingin diubah: ").strip()
    pasien = next((p for p in data_pasien if p["id"] == id_pas), None)
    if not pasien:
        print("❌ Data pasien tidak ditemukan.")
        return
    for key in ["nama", "jenis_kelamin", "umur", "alamat", "nomor_hp"]:
        new_val = input(f"{key.replace('_',' ').title()} baru (biarkan kosong jika tidak ingin mengubah): ")
        if new_val:
            pasien[key] = int(new_val) if key == "umur" else new_val.title() if key in ["nama", "alamat"] else new_val
    print("✅ Data pasien berhasil diperbarui.")

def hapus_data_pasien():
    id_pas = input("Masukkan ID Pasien yang ingin dihapus: ").strip()
    global data_pasien
    global data_reservasi
    data_pasien = [p for p in data_pasien if p["id"] != id_pas]
    data_reservasi = [r for r in data_reservasi if r["id_pasien"] != id_pas]
    print(f"✅ Data pasien dan reservasi dengan ID {id_pas} berhasil dihapus.")

# =================== FUNGSI RESERVASI ===================

def lihat_jadwal_admin():
    print("\n=== Jadwal Dokter ===")
    if data_dokter:
        print(tabulate(data_dokter, headers="keys", tablefmt="grid"))
    else:
        print("❌ Belum ada jadwal dokter.")

def tambah_jadwal_dokter():
    print("\n=== Tambah Jadwal Dokter ===")
    nama = input("Nama Dokter: ").title()
    if not nama:
        print("❌ Nama dokter tidak boleh kosong.")
        return
    if any(d["nama"] == nama for d in data_dokter):
        print("❌ Dokter sudah terdaftar.")
        return
    spesialis = input("Spesialis: ").title()
    if not spesialis:
        print("❌ Spesialis tidak boleh kosong.")
        return
    hari = input("Hari Praktek (contoh: Senin - Rabu): ").title()
    if not hari:
        print("❌ Hari praktek tidak boleh kosong.")
        return
    data_dokter.append({"nama": nama, "spesialis": spesialis, "hari": hari})
    print("✅ Jadwal dokter berhasil ditambahkan.")

    print("\n=== Tambah Jadwal Dokter ===")
    nama = input("Nama Dokter: ").title()
    spesialis = input("Spesialis: ").title()
    hari = input("Hari Praktek (contoh: Senin - Rabu): ")
    data_dokter.append({"nama": nama, "spesialis": spesialis, "hari": hari})
    print("✅ Jadwal dokter berhasil ditambahkan.")

def ubah_jadwal_dokter():
    lihat_jadwal_admin()
    nama = input("Masukkan nama dokter yang ingin diubah: ").title()
    dokter = next((d for d in data_dokter if d["nama"] == nama), None)
    if not dokter:
        print("❌ Dokter tidak ditemukan.")
        return
    print("\nBiarkan kosong jika tidak ingin mengubah.")
    spesialis = input("Spesialis baru: ").title()
    hari = input("Hari praktek baru: ").title()
    if spesialis:
        dokter["spesialis"] = spesialis
    if hari:
        dokter["hari"] = hari
    print("✅ Jadwal dokter berhasil diubah.")


def hapus_jadwal_dokter():
    lihat_jadwal_admin()
    nama = input("Masukkan nama dokter yang ingin dihapus: ").title()
    global data_dokter
    awal = len(data_dokter)
    data_dokter = [d for d in data_dokter if d["nama"] != nama]
    if len(data_dokter) < awal:
        print("✅ Jadwal dokter berhasil dihapus.")
    else:
        print("❌ Dokter tidak ditemukan.")

def tambah_reservasi(id_pasien):
    print("\n=== Buat Reservasi ===")
    keluhan = input("Masukkan Keluhan: ").capitalize()
    tanggal = input("Masukkan Tanggal (DD/MM/YYYY): ")
    dokter = input("Masukkan Nama Dokter: ").title()
    rawat = input("Rawat (Inap/Jalan): ").title()
    ruangan = input("Nama Ruangan (kosong jika rawat jalan): ") if rawat.lower() == "inap" else "-"
    data_reservasi.append({
        "id_pasien": id_pasien,
        "keluhan": keluhan,
        "tanggal": tanggal,
        "dokter": dokter,
        "rawat": rawat,
        "ruangan": ruangan
    })
    print("✅ Reservasi berhasil ditambahkan.")

def ubah_data_reservasi():
    id_pas = input("Masukkan ID Pasien untuk ubah reservasi: ").strip()
    reservasi = next((r for r in data_reservasi if r["id_pasien"] == id_pas), None)
    if not reservasi:
        print("❌ Data reservasi tidak ditemukan.")
        return
    print("\n=== Ubah Data Reservasi ===")
    new_keluhan = input("Keluhan baru (kosong jika tidak ingin mengubah): ")
    new_tanggal = input("Tanggal baru (kosong jika tidak ingin mengubah): ")
    new_dokter = input("Dokter baru (kosong jika tidak ingin mengubah): ")
    new_rawat = input("Rawat (Inap/Jalan): ")
    new_ruangan = input("Ruangan (kosong jika rawat jalan): ")
    if new_keluhan: reservasi["keluhan"] = new_keluhan
    if new_tanggal: reservasi["tanggal"] = new_tanggal
    if new_dokter: reservasi["dokter"] = new_dokter
    reservasi["rawat"] = new_rawat.title()
    reservasi["ruangan"] = new_ruangan if new_rawat.lower() == "inap" else "-"
    print("✅ Reservasi berhasil diperbarui.")

def hapus_reservasi():
    id_pas = input("Masukkan ID Pasien untuk hapus reservasi: ").strip()
    global data_reservasi
    awal = len(data_reservasi)
    data_reservasi = [r for r in data_reservasi if r["id_pasien"] != id_pas]
    if len(data_reservasi) < awal:
        print("✅ Reservasi berhasil dihapus.")
    else:
        print("❌ Reservasi tidak ditemukan.")

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
        print("❌ Belum ada data reservasi.")

# =================== MAIN LOOP ===================

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
                        cari_data_pasien()
                        print()
                    elif pilih == "3":
                        ubah_data_reservasi()
                        print()
                    elif pilih == "4":
                        hapus_reservasi()
                        print()

            elif pilih == "3":
                while True:
                    sub_menu_dokter()
                    pilih_dokter = input("Pilih Menu: ")
                    if pilih_dokter == "1":
                        lihat_jadwal_admin()
                    elif pilih_dokter == "2":
                        tambah_jadwal_dokter()
                    elif pilih_dokter == "3":
                        ubah_jadwal_dokter()
                    elif pilih_dokter == "4":
                        hapus_jadwal_dokter()
                    else:
                        print("❌ Menu tidak valid.")
                        break

            elif pilih == "4":
                print("👋 Keluar dari sistem admin...")
                break
            else:
                print("❌ Menu tidak valid.")
    elif role == "pasien":
        while True:
            menu_pasien()
            pilih = input("Pilih menu: ")
            if pilih == "1": lihat_jadwal_admin()
            elif pilih == "2": tambah_reservasi(user)
            elif pilih == "3": ubah_data_diri(user)
            elif pilih == "4": hapus_reservasi()
            elif pilih == "5":
                print("👋 Keluar dari sistem pasien...")
                break
            else:
                print("❌ Menu tidak valid.")
