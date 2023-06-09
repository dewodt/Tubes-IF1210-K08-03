import argparse
import os

import globalvar as gv
import utils as ut


def run(masukan: str):
    # I.S. program utama belum jalan, F.S. program utama jalan

    # Kamus Lokal
    # procedure login (input/output logged_in_username: string, input/output logged_in_role: string, output NMaxUser: int, input/output users: User)
    # { I.S. tidak terlogin, F.S. jika username dan password benar terlogin, jika tidak tidak terlogin }
    # procedure logout (input/output logged_in_username: string, input/output logged_in_role: string)
    # { I.S. terlogin ke suatu akun, F.S. keluar dari akun tersebut}
    # procedure summonjin (output logged_in_role: string, output NMaxUser: int, input/output users: User)
    # { I.S. suatu jin belum tersummon, F.S. jin dengan username dan role tertentu tersummon }
    # procedure hapusjin (output logged_in_role: string, output NMaxUser: int, output NMaxCandi: int, input/output users: User, input/output candi: Candi, input/output undo_jin: User, input/output undo_candi: Candi)
    # { I.S. suatu jin dgn username tertentu masih ada (tersummon), F.S. jin tersebut dimusnahkan }
    # procedure ubahjin (output logged_in_role: string, output NMaxUser: int, input/output users: User)
    # { I.S. suatu jin dengan role jin_pembangun atau jin_pengumpul, F.S. role jin diubah menjadi lawannya}
    # procedure bangun(output logged_in_role: string, output logged_in_username: string, input/output bahan_bangunan: Bahan_Bangunan, input/output candi: Candi, output NMaxCandi: int, output xn: int)
    # { I.S. material tersedia atau kosong, F.S. jin terbangun dan material berkurang }
    # procedure kumpul (output logged_in_role: string, input/output bahan_bangunan: Bahan_Bangunan, output xn: int)
    # { I.S. material tersedia atau kosong, F.S. jumlah material bertambah }
    # procedure batchbangun(output logged_in_role: string, output NMaxUser: int, output NMaxCandi: int, output xn: int, output users: User, input/output bahan_bangunan: Bahan_Bangunan, input/output candi: Candi)
    # { I.S. material tersedia atau kosong, F.S. jin terbangun dan material berkurang }
    # procedure batchkumpul(output logged_in_role: string, output NMaxUser: int, output xn: int, output users: User, input/output bahan_bangunan: Bahan_Bangunan)
    # { I.S. material tersedia atau kosong, F.S. jumlah material bertambah }
    # procedure laporanjin(output logged_in_role: string, output NMaxCandi: int, output NMaxUser: int, output users: User, output candi: Candi, output bahan_bangunan: Bahan_Bangunan)
    # { I.S. beberapa candi terbangun / beberapa material terkumpul, F.S. menampilkan laporan jin terajin dan termalas }
    # procedure laporancandi(output logged_in_role: string, output NMaxCandi: int, output candi: Candi)
    # { I.S. beberapa candi terbangun / beberapa material terkumpul, F.S. menampilkan laporan pembangunan candi }
    # procedure hancurkancandi(output logged_in_role: string, output NMaxCandi: int, input/output candi: Candi)
    # { I.S. beberapa candi dengan id tertentu sudah terbangun, F.S. candi dengan id tertentu dihancurkan }
    # procedure ayamberkokok (output logged_in_role: string, output NMaxCandi: int, output candi: Candi)
    # { I.S. beberapa candi sudah terbangun atau bahkan belum, F.S. game selesai dan ditentukan pemenang antara bandung bondowoso atau roro jonggrang }
    # procedure save (input/output undo_jin: User, input/output undo_candi: Candi)
    # { I.S. data-data game belum tersimpan, F.S. data-data game tersimpan }
    # procedure help (output logged_in_username: string, output logged_in_role: string)
    # { I.S. player melakukan login atau belum melakukan login, F.S. memberikan list command sesuai dengan role player atau kondisi login player }
    # procedure exit ()
    # { I.S. player dalam kondisi login atau belum melakukan login, F.S. memberikan opsi pada player untuk menyimpan data program sebelum keluar dari program }
    # procedure undo(output logged_in_role: string, output NMaxUser: int, input/output undo_jin: User, input/output undo_candi: Candi, input/output candi: Candi)
    # { I.S. data user atau candi yang sudah dihapus, F.S. mengembalikan data yang telah dihapus sebelumnya }

    # Algoritma
    if masukan == "login":
        login()
    elif masukan == "logout":
        logout()
    elif masukan == "summonjin":
        summonjin()
    elif masukan == "hapusjin":
        hapusjin()
    elif masukan == "ubahjin":
        ubahjin()
    elif masukan == "bangun":
        bangun()
    elif masukan == "kumpul":
        kumpul()
    elif masukan == "batchbangun":
        batchbangun()
    elif masukan == "batchkumpul":
        batchkumpul()
    elif masukan == "laporanjin":
        laporanjin()
    elif masukan == "laporancandi":
        laporancandi()
    elif masukan == "hancurkancandi":
        hancurkancandi()
    elif masukan == "ayamberkokok":
        ayamberkokok()
    elif masukan == "save":
        save()
    elif masukan == "help":
        help()
    elif masukan == "exit":
        exit()
    elif masukan == "undo":
        undo()


def login():
    # I.S. tidak terlogin, F.S. jika username dan password benar terlogin, jika tidak tidak terlogin

    # Kamus Lokal
    # type User: array [0..NMaxUser] of array [0..2] of string
    # username, password : string
    # username_found, password_valid : bool
    # i : int

    # Algoritma
    if gv.logged_in_username != "":
        print("Login gagal!")
        print(
            f'Anda telah login dengan username {gv.logged_in_username}, silahkan lakukan "logout" sebelum melakukan login kembali.'
        )
    else:
        username = input("Username: ")
        password = input("Password: ")
        # Inisialisasi boolean
        username_found = False
        password_valid = False

        # Looping untuk mengecek jika ada username yang cocok, dan jika ada apakah passwordnya juga cocok?
        for i in range(gv.NMaxUser):
            if gv.users[i][0] == username:
                username_found = True
                if gv.users[i][1] == password:
                    password_valid = True

        # Jika tidak ada username yang cocok
        if not username_found:
            print("Username tidak terdaftar!")
        else:
            # Jika username cocok namun password tidak valid
            if not password_valid:
                print("Password salah!")
            # Jika username cocok dan password valid
            else:
                # Update global variable logged in role
                gv.logged_in_username = username
                if username == "Bondowoso":
                    gv.logged_in_role = "bandung_bondowoso"
                elif username == "Roro":
                    gv.logged_in_role = "roro_jonggrang"
                else:
                    for i in range(gv.NMaxUser):
                        if gv.users[i][0] == username:
                            gv.logged_in_role = gv.users[i][2]
                            break

                # Cetak pesan
                print(f"Selamat datang, {gv.logged_in_username}!")
                print(
                    "Masukkan command “help” untuk daftar command yang dapat kamu panggil."
                )


def logout():
    # I.S. terlogin ke suatu akun, F.S. keluar dari akun tersebut

    # Kamus Lokal
    # Kosong

    # Algoritma
    if gv.logged_in_username == "":
        # Cetak pesan
        print("Logout gagal!")
        print(
            "Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout"
        )
    else:
        # Update global variable menjadi kosong
        gv.logged_in_username = ""
        gv.logged_in_role = ""


def summonjin():
    # I.S. suatu jin belum tersummon, F.S. jin dengan username dan role tertentu tersummon

    # Kamus Lokal
    # type User: array [0..NMaxUser] of array [0..2] of string
    # jenis_jin, kode_jenis_jin, username, password : string
    # tersedia : bool
    # count_summoned_jin, i : int

    # Algoritma
    if gv.logged_in_role != "bandung_bondowoso":
        print("summonjin hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        # Validasi jumlah jin yang tersummon
        count_summoned_jin = 0
        for i in range(gv.NMaxUser):
            if gv.users[i][2] == "jin_pembangun" or gv.users[i][2] == "jin_pengumpul":
                count_summoned_jin += 1

        # Jika jin yang disummon sudah 100
        if count_summoned_jin == 100:
            print(
                "Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu"
            )
        else:
            # Pemilihan jenis jin
            print("Jenis jin yang dapat dipanggil:")
            print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
            print(" (2) Pembangun - Bertugas membangun candi")
            # Validasi input
            jenis_jin = ""
            kode_jenis_jin = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
            while kode_jenis_jin != "1" and kode_jenis_jin != "2":
                print(f'Tidak ada jenis jin bernomor "{kode_jenis_jin}"!')
                kode_jenis_jin = input(
                    "Masukkan nomor jenis jin yang ingin dipanggil: "
                )
            # Cetak pesan jin terpilih
            if kode_jenis_jin == "1":
                print('Memilih jin "Pengumpul".')
                jenis_jin = "jin_pengumpul"
            else:
                print('Memilih jin "Pembangun".')
                jenis_jin = "jin_pembangun"

            # Validasi username
            username = input("Masukkan username jin: ")
            tersedia = False
            while not tersedia:
                for i in range(gv.NMaxUser):
                    if gv.users[i][0] == username:
                        print(f'Username "{username}" sudah diambil!')
                        username = input("Masukkan username jin: ")
                        break
                    elif i == gv.NMaxUser - 1:
                        tersedia = True

            # Validasi password
            password = input("Masukkan password jin: ")
            while len(password) < 5 or len(password) > 25:
                print("Password panjangnya harus 5-25 karakter!")
                password = input("Masukkan password jin: ")

            # Update global variable
            for i in range(gv.NMaxUser):
                # Mengisi array users pertama yang ketemu kosong
                if gv.users[i][0] == "":
                    # Update array users
                    gv.users[i] = [username, password, jenis_jin]
                    break

            # Cetak pesanSummon jin
            print("Mengumpulkan sesajen...")
            print("Menyerahkan sesajen...")
            print("Membacakan mantra...")
            print(f"{username} berhasil dipanggil!")


def hapusjin():
    # I.S. suatu jin dgn username tertentu masih ada (tersummon), F.S. jin tersebut dimusnahkan

    # Kamus Lokal
    # type User: array [0..NMaxUser] of array [0..2] of string
    # type Candi: array [0..NMaxCandi] of array [0..4] of string, int
    # username, konfirmasi : string
    # found : bool
    # index_found, index_undo, i, j : int

    # Algoritma
    if gv.logged_in_role != "bandung_bondowoso":
        print("hapusjin hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        # Inisialisasi input
        found = False
        index_found = -1
        username = input("Masukkan username jin : ")

        # Mengecek bila username ditemukan dan role jin
        for i in range(gv.NMaxUser):
            if gv.users[i][0] == username and (
                gv.users[i][2] == "jin_pembangun" or gv.users[i][2] == "jin_pengumpul"
            ):
                found = True
                index_found = i
                break

        # Bila ditemukan
        if not found:
            print("Tidak ada jin dengan username tersebut.")
        else:
            konfirmasi = input(
                f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)? "
            )
            if konfirmasi == "Y":
                # Cari index kosong terkecil pada array undo_jin
                index_undo = -1
                for j in range(gv.NMaxUser):
                    if gv.undo_jin[j][0] == "":
                        index_undo = j
                        break

                # Update array undo jin
                gv.undo_jin[index_undo] = gv.users[index_found]

                # Update array user
                gv.users[index_found] = ["", "", ""]
                print("Jin telah berhasil dihapus dari alam gaib.")

                # Hapus data candi yang dibuat oleh jin tersebut
                for i in range(gv.NMaxCandi):
                    # Jika candi dibuat oleh jin tersebut
                    if gv.candi[i][1] == username:
                        # Update array undo candi
                        gv.undo_candi[i] = gv.candi[i]

                        # Update array candi
                        gv.candi[i] = [0, "", 0, 0, 0]


def ubahjin():
    # I.S. suatu jin dengan role jin_pembangun atau jin_pengumpul, F.S. role jin diubah menjadi lawannya

    # Kamus Lokal
    # type User: array [0..NMaxUser] of array [0..2] of string
    # username, tipe_ganti, konfirmasi : string
    # found : bool
    # index_found, i : int

    # Algoritma
    if gv.logged_in_role != "bandung_bondowoso":
        print("ubahjin hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        # Inisialisasi input
        found = False
        index_found = -1
        username = input("Masukkan username jin : ")

        # Mengecek bila username ditemukan dan merupakan role jin
        for i in range(gv.NMaxUser):
            if gv.users[i][0] == username and (
                gv.users[i][2] == "jin_pembangun" or gv.users[i][2] == "jin_pengumpul"
            ):
                found = True
                index_found = i
                break

        # Jika tidak ketemu
        if not found:
            print("Tidak ada jin dengan username tersebut.")
        else:
            # Menentukan target ganti
            tipe_ganti = ""
            if gv.users[index_found][2] == "jin_pembangun":
                tipe_ganti = "jin_pengumpul"
            else:
                tipe_ganti = "jin_pembangun"

            # Input konfirmasi
            konfirmasi = input(
                f'Jin ini bertipe "{gv.users[index_found][2]}". Yakin ingin mengubah ke tipe "{tipe_ganti}" (Y/N)? '
            )

            # Bila konfirmasi benar
            if konfirmasi == "Y":
                gv.users[index_found][2] = tipe_ganti


def bangun():
    # I.S. material tersedia atau kosong, F.S. jin terbangun dan material berkurang

    # Kamus Lokal
    # type Candi: array [0..NMaxCandi] of array [0..4] of string, int
    # type Bahan_Bangunan: array [0..2] of array [0..2] of string, int
    # init_jin : string
    # init_pasir, init_batu, init_air, init_count_candi, i, gen_pasir, gen_batu, gen_air : int
    # function RandomLCG (min: int, max: int, seed: int) → array [0..2] of int
    # { Menghasilkan array yang berisi tiga angka random dalam range [min, max] }

    # Algoritma
    # Kasus role logged in bukan jin pembangun
    if gv.logged_in_role != "jin_pembangun":
        print("bangun hanya dapat diakses oleh akun Jin Pembangun.")
    else:  # role logged in jin pembangun
        # Inisialisasi data awal
        init_pasir = gv.bahan_bangunan[0][2]
        init_batu = gv.bahan_bangunan[1][2]
        init_air = gv.bahan_bangunan[2][2]
        init_jin = gv.logged_in_username
        # Hitung jumlah candi awal
        init_count_candi = 0
        for i in range(gv.NMaxCandi):
            if gv.candi[i][0] != 0:
                init_count_candi += 1

        # Generate 3 bilangan random number dari 1 sampai 5 untuk pasir, batu, dan air dengan algoritma LCG.
        gen_pasir, gen_batu, gen_air = ut.RandomLCG(1, 5, gv.xn)

        # Jika pasir, batu, dan air cukup.
        if init_pasir >= gen_pasir and init_batu >= gen_batu and init_air >= gen_air:
            # Update sisa jumlah material.
            gv.bahan_bangunan[0][2] -= gen_pasir
            gv.bahan_bangunan[1][2] -= gen_batu
            gv.bahan_bangunan[2][2] -= gen_air

            # Update array candi dengan mengisi index terkecil terlebih dahulu
            for i in range(gv.NMaxCandi):
                if gv.candi[i][0] == 0:
                    gv.candi[i] = [i + 1, init_jin, gen_pasir, gen_batu, gen_air]
                    break  # Hanya menambahkan satu candi

            # Cetak pesan.
            print("Candi berhasil dibangun.")
            if 100 - init_count_candi > 0:
                print(f"Sisa candi yang perlu dibangun: {100-init_count_candi-1}.")
            else:
                print("Sisa candi yang perlu dibangun: 0.")
        else:
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")


def kumpul():
    # I.S. material tersedia atau kosong, F.S. jumlah material bertambah

    # Kamus Lokal
    # type Bahan_Bangunan: array [0..2] of array [0..2] of string, int
    # gen_pasir, gen_batu, gen_air : int
    # function RandomLCG (min: int, max: int, seed: int) → array [0..2] of int
    # { Menghasilkan array yang berisi tiga angka random dalam range [min, max] }

    # Algoritma
    # Kasus role logged in bukan jin pengumpul
    if gv.logged_in_role != "jin_pengumpul":
        print("Kumpul hanya dapat diakses oleh akun Jin Pengumpul.")
    else:
        # Generate 3 bilangan random number dari 0 sampai 5 untuk pasir, batu, dan air dengan algoritma LCG.
        gen_pasir, gen_batu, gen_air = ut.RandomLCG(0, 5, gv.xn)

        # Update data jumlah pasir, batu, dan air.
        gv.bahan_bangunan[0][2] += gen_pasir
        gv.bahan_bangunan[1][2] += gen_batu
        gv.bahan_bangunan[2][2] += gen_air

        # Cetak pesan.
        print(f"Jin menemukan {gen_pasir} pasir, {gen_batu} batu, dan {gen_air} air.")


def batchbangun():
    # I.S. material tersedia atau kosong, F.S. jin terbangun dan material berkurang

    # Kamus Lokal
    # type User: array [0..NMaxUser] of array [0..2] of string
    # type Candi: array [0..NMaxCandi] of array [0..4] of string, int
    # type Bahan_Bangunan: array [0..2] of array [0..2] of string, int
    # init_pasir, init_batu, init_air, batch_pasir, batch_batu, batch_air, init_count_candi, init_count_jin_pembangun, i, j, gen_pasir, gen_batu, gen_air, count_terbangun, kurang_pasir, kurang_batu, kurang_air : int
    # init_aray_jin_pembangung : array [0..init_count_jin_pembangun-1] of array [0..3] of int, string
    # function RandomLCG (min: int, max: int, seed: int) → array [0..2] of int
    # { Menghasilkan array yang berisi tiga angka random dalam range [min, max] }

    # Algoritma
    # Kasus role logged in bukan bandung bondowoso
    if gv.logged_in_role != "bandung_bondowoso":
        print("Batch bangun hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        # Inisialisasi data awal.
        init_pasir = gv.bahan_bangunan[0][2]
        init_batu = gv.bahan_bangunan[1][2]
        init_air = gv.bahan_bangunan[2][2]
        batch_pasir = 0
        batch_batu = 0
        batch_air = 0

        # Hitung jumlah candi awal
        init_count_candi = 0
        for i in range(gv.NMaxCandi):
            if gv.candi[i][0] != 0:
                init_count_candi += 1

        # Hitung jumlah jin pembangun awal
        init_count_jin_pembangun = 0
        for i in range(gv.NMaxUser):
            if gv.users[i][2] == "jin_pembangun":
                init_count_jin_pembangun += 1

        # Jika tidak ada jin pembangun tersummon
        if init_count_jin_pembangun == 0:
            print(
                "Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu."
            )
        else:
            # Bikin array berisi nama jin pembangun dan generate material yang dipakainya untuk membangun sebuah candi
            init_array_jin_pembangun = [
                ["", 0, 0, 0] for i in range(init_count_jin_pembangun)
            ]

            # Untuk mengisi nama-nama jin pembangun dan material yang digeneratenya
            j = 0
            for i in range(gv.NMaxUser):
                if gv.users[i][2] == "jin_pembangun":
                    # Generate 3 bilangan random number dari 1 sampai 5 untuk pasir, batu, dan air dengan algoritma LCG.
                    gen_pasir, gen_batu, gen_air = ut.RandomLCG(1, 5, gv.xn)

                    # Update array jin pembangun
                    init_array_jin_pembangun[j] = [
                        gv.users[i][0],
                        gen_pasir,
                        gen_batu,
                        gen_air,
                    ]

                    # Perbarui jumlah terkumpul dalam 1 batch
                    batch_pasir += gen_pasir
                    batch_batu += gen_batu
                    batch_air += gen_air

                    # Next iteration
                    j += 1

            print(
                f"Mengerahkan {init_count_jin_pembangun} jin untuk membangun candi dengan total bahan {batch_pasir} pasir, {batch_batu} batu, dan {batch_air} air."
            )
            # Kasus bahan cukup
            if (
                init_pasir >= batch_pasir
                and init_batu >= batch_batu
                and init_air >= batch_air
            ):
                # Update data jumlah pasir, batu, dan air.
                gv.bahan_bangunan[0][2] -= batch_pasir
                gv.bahan_bangunan[1][2] -= batch_batu
                gv.bahan_bangunan[2][2] -= batch_air

                # Update array candi dari array terkecil
                i = 0
                count_terbangun = 0
                while i < gv.NMaxCandi and count_terbangun < init_count_jin_pembangun:
                    if gv.candi[i][0] == 0:
                        gv.candi[i] = [
                            i + 1,
                            init_array_jin_pembangun[count_terbangun][0],
                            init_array_jin_pembangun[count_terbangun][1],
                            init_array_jin_pembangun[count_terbangun][2],
                            init_array_jin_pembangun[count_terbangun][3],
                        ]
                        count_terbangun += 1
                    i += 1

                # Cetak pesan.
                # Kasus jika jumlah jin pembangun kurang atau sama dengan sisa slot array candi
                if init_count_jin_pembangun <= gv.NMaxCandi - init_count_candi:
                    print(
                        f"Jin berhasil membangun total {init_count_jin_pembangun} candi."
                    )
                else:  # Kasus jika jin pembangun lebih dari sisa slot array candi
                    print(
                        f"Jin berhasil membangun total {gv.NMaxCandi - init_count_candi} candi."
                    )
            else:  # Bahan tidak cukup
                # Mencari jumlah kekurangan bahan
                kurang_pasir = 0
                kurang_batu = 0
                kurang_air = 0
                if init_pasir < batch_pasir:
                    kurang_pasir = batch_pasir - init_pasir
                if init_batu < batch_batu:
                    kurang_batu = batch_batu - init_batu
                if init_air < batch_air:
                    kurang_air = batch_air - init_air
                print(
                    f"Bangun gagal. Kurang {kurang_pasir} pasir, {kurang_batu} batu, dan {kurang_air} air."
                )
                print("# Candi yang terbangun 0")


def batchkumpul():
    # I.S. material tersedia atau kosong, F.S. jumlah material bertambah

    # Kamus Lokal
    # type User: array [0..NMaxUser] of array [0..2] of string
    # type Bahan_Bangunan: array [0..2] of array [0..2] of string, int
    # batch_pasir, batch_batu, batch_air, init_count_jin_pengumpul, i, gen_pasir, gen_batu, gen_air : int
    # function RandomLCG (min: int, max: int, seed: int) → array [0..2] of int
    # { Menghasilkan array yang berisi tiga angka random dalam range [min, max] }

    # Algoritma
    # Kasus role logged in bukan bandung bondowoso
    if gv.logged_in_role != "bandung_bondowoso":
        print("Batch kumpul hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        # Inisialisasi data awal.
        batch_pasir = 0
        batch_batu = 0
        batch_air = 0
        init_count_jin_pengumpul = 0
        for i in range(gv.NMaxUser):
            if gv.users[i][2] == "jin_pengumpul":
                init_count_jin_pengumpul += 1

        # Kasus jin pengumpul ada yang tersummon
        if init_count_jin_pengumpul > 0:
            # Looping n kali (n banyaknya jin).
            for i in range(init_count_jin_pengumpul):
                # Generate 3 bilangan random number dari 0 sampai 5 untuk pasir, batu, dan air dengan algoritma LCG.
                gen_pasir, gen_batu, gen_air = ut.RandomLCG(0, 5, gv.xn)

                # Perbarui jumlah terkumpul.
                batch_pasir += gen_pasir
                batch_batu += gen_batu
                batch_air += gen_air

            # Update data jumlah pasir, batu, dan air.
            gv.bahan_bangunan[0][2] += batch_pasir
            gv.bahan_bangunan[1][2] += batch_batu
            gv.bahan_bangunan[2][2] += batch_air

            # Cetak pesan.
            print(
                f"Mengerahkan {init_count_jin_pengumpul} jin untuk mengumpulkan bahan."
            )
            print(
                f"Jin menemukan total {batch_pasir} pasir, {batch_batu} batu, dan {batch_air} air."
            )
        else:  # Kasus tidak ada jin pengumpul tersummon
            # Cetak pesan
            print(
                "Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu."
            )


def laporanjin():
    # I.S. beberapa candi terbangun / beberapa material terkumpul, F.S. menampilkan laporan jin terajin dan termalas

    # Kamus Lokal
    # type User: array [0..NMaxUser] of array [0..2] of string
    # type Candi: array [0..NMaxCandi] of array [0..4] of string, int
    # type Bahan_Bangunan: array [0..2] of array [0..2] of string, int
    # jin_total, jin_pembangun, jin_pengumpul, i, count_terajin, count_termalas, count_now, j, pasir_now, batu_now, air_now : int
    # nama_terajin, nama_termalas, nama_now : string

    # Algoritma
    # Kasus role logged in bukan bandung bondowoso
    if gv.logged_in_role != "bandung_bondowoso":
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        # Hitung jumlah jin
        jin_total = 0
        jin_pembangun = 0
        jin_pengumpul = 0
        for i in range(gv.NMaxUser):
            if gv.users[i][2] == "jin_pembangun":
                jin_pembangun += 1
            elif gv.users[i][2] == "jin_pengumpul":
                jin_pengumpul += 1
        jin_total = jin_pembangun + jin_pengumpul

        # Cari Terajin dan Termalas
        nama_terajin = "-"
        count_terajin = -1
        nama_termalas = "-"
        count_termalas = gv.NMaxCandi + 1  # Jumlah candi maksimum
        for i in range(gv.NMaxUser):
            if gv.users[i][2] == "jin_pembangun":
                nama_now = gv.users[i][0]
                count_now = 0
                j = 0
                while j < gv.NMaxCandi and gv.candi[j][0] != 0:
                    if gv.candi[j][1] == nama_now:
                        count_now += 1
                    j += 1

                # Update terajin
                if count_now > count_terajin:
                    count_terajin = count_now
                    nama_terajin = nama_now
                elif count_now == count_terajin:  # Kasus count sama
                    if nama_now < nama_terajin:  # Bandingkan leksografis
                        count_terajin = count_now
                        nama_terajin = nama_now

                #  Update termalas
                if count_now < count_termalas:
                    count_termalas = count_now
                    nama_termalas = nama_now
                elif count_now == count_termalas:  # Kasus count sama
                    if nama_now > nama_termalas:  # Bandingkan leksografis
                        count_termalas = count_now
                        nama_termalas = nama_now

        # Jumlah material saat ini
        pasir_now = gv.bahan_bangunan[0][2]
        batu_now = gv.bahan_bangunan[1][2]
        air_now = gv.bahan_bangunan[2][2]

        # Cetak pesan
        print(f"> Total Jin: {jin_total}")
        print(f"> Total Jin Pengumpul: {jin_pengumpul}")
        print(f"> Total Jin Pembangun: {jin_pembangun}")
        print(f"> Jin Terajin: {nama_terajin}")
        print(f"> Jin Termalas: {nama_termalas}")
        print(f"> Jumlah Pasir: {pasir_now} unit")
        print(f"> Jumlah Air: {air_now} unit")
        print(f"> Jumlah Batu: {batu_now} unit")


def laporancandi():
    # I.S. beberapa candi terbangun / beberapa material terkumpul, F.S. menampilkan laporan pembangunan candi

    # Kamus Lokal
    # type Candi: array [0..NMaxCandi] of array [0..4] of string, int
    # total_candi, total_pasir, total_batu, total_air, harga_termahal, harga_termurah, i, harga_now: int
    # id_termahal, id_termurah, id_now: string

    # Algoritma
    # Kasus role logged in bukan bandung bondowoso
    if gv.logged_in_role != "bandung_bondowoso":
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        total_candi = 0
        total_pasir = 0
        total_batu = 0
        total_air = 0
        id_termahal = "-"
        harga_termahal = -1
        id_termurah = "-"
        harga_termurah = 200000  # Pasir, batu, air maks 5 -> harga pasti < 200000

        # Hitung total candi, material yang digunakan, dan cari candi termahal.
        for i in range(gv.NMaxCandi):
            if gv.candi[i][0] != 0:
                # Total candi
                total_candi += 1

                # Material total candi
                total_pasir += gv.candi[i][2]
                total_batu += gv.candi[i][3]
                total_air += gv.candi[i][4]

                # Candi termahal
                id_now = gv.candi[i][0]
                harga_now = (
                    10000 * gv.candi[i][2]
                    + 15000 * gv.candi[i][3]
                    + 7500 * gv.candi[i][4]
                )

                # Jika dua candi sama-sama termahal/termurah, keluarkan indeks terendah.
                # Update termahal
                if harga_now > harga_termahal:
                    harga_termahal = harga_now
                    id_termahal = id_now
                # Update termurah
                if harga_now < harga_termurah:
                    harga_termurah = harga_now
                    id_termurah = id_now

        # Cetak pesan
        print(f"> Total Candi: {total_candi}")
        print(f"> Total Pasir yang digunakan: {total_pasir}")
        print(f"> Total Batu yang digunakan: {total_batu}")
        print(f"> Total Air yang digunakan: {total_air}")
        print(f"> ID Candi Termahal: {id_termahal}")
        print(f"> ID Candi Termurah: {id_termurah}")


def hancurkancandi():
    # I.S. beberapa candi dengan id tertentu sudah terbangun, F.S. candi dengan id tertentu dihancurkan

    # Kamus Lokal
    # type Candi: array [0..NMaxCandi] of array [0..4] of string, int
    # candi_found : bool
    # id_hancurkan, konfirmasi: string

    # Algoritma
    if gv.logged_in_role != "roro_jonggrang":
        print("Hancurkan candi hanya dapat diakses oleh akun Roro Jonggrang.")
    else:
        # Input id candi yang ingin dihancurkan
        id_hancurkan = int(input("Masukkan ID candi: "))

        # Looping untuk mencari id yang cocok dengan input user dan tidak boleh 0 (id 0 adalah item kosong)
        candi_found = False
        for i in range(gv.NMaxCandi):
            if gv.candi[i][0] == id_hancurkan and id_hancurkan != 0:
                candi_found = True
                break

        # Jika candi tidak ketemu
        if not candi_found:
            print("Tidak ada candi dengan ID tersebut.")
        else:  # Jika ketemu
            konfirmasi = input(
                f"Apakah anda yakin ingin menghancurkan candi ID: {id_hancurkan} (Y/N)? "
            )
            # Jika konfirmasi Y
            if konfirmasi == "Y":
                # Update global variable
                gv.candi[id_hancurkan - 1] = [0, "", 0, 0, 0]

                # Cetak pesan
                print("Candi telah berhasil dihancurkan.")


def ayamberkokok():
    # I.S. beberapa candi sudah terbangun atau bahkan belum, F.S. game selesai dan ditentukan pemenang antara bandung bondowoso atau roro jonggrang

    # Kamus Lokal
    # type Candi: array [0..NMaxCandi] of array [0..4] of string, int
    # count_candi, i : integer

    # Algoritma
    if gv.logged_in_role != "roro_jonggrang":
        print("Ayam berkokok hanya dapat diakses oleh akun Roro Jonggrang.")
    else:
        # Hitung banyak candi
        count_candi = 0
        for i in range(gv.NMaxCandi):
            if gv.candi[i][0] != 0:
                count_candi += 1
        # Cetak pesan awal
        print("Kukuruyuk.. Kukuruyuk..")
        print(f"Jumlah Candi: {count_candi}")
        # Jika roro jongrang menang
        if count_candi < 100:
            print("Selamat, Roro Jonggrang memenangkan permainan!")
            print("*Bandung Bondowoso angry noise*")
            print("Roro Jonggrang dikutuk menjadi candi.")
        else:  # Jika bandung bondowoso menang
            print("Yah, Bandung Bondowoso memenangkan permainan!")


def load():
    # I.S. data-data CSV belum dibaca atau belum disimpan dalam program, F.S. data-data CSV terbaca dan disimpan dalam program

    # Kamus Lokal
    # parser : ArgumentParser
    # args : NameSpace
    # folder_load : string
    # procedure read_csv(output folder_name : string, output file_name : string, output NMaxCandi: int, output NMaxUser: int, input/output users: User, input/output bahan_bangunan: Bahan_Bangunan, input/output candi: Candi)
    # { I.S. data global variable kosong, F.S. data terisi dari data CSV pada folder <folder_name>}

    # Algoritma
    # Argparse untuk menerima nama folder
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "folder",
        default="",
        nargs="?",
    )
    args = parser.parse_args()
    folder_load = args.folder

    # Bila tidak memberikan argumen
    if folder_load == "":
        print("Tidak ada nama folder yang diberikan!")
        print("Usage: python main.py <nama_folder>")
    else:
        # Bila nama folder tidak ada
        if not os.path.exists(f"save/{folder_load}"):
            print(f'Folder "{folder_load}" tidak ditemukan.')
        else:
            # Bila folder ada
            print("Loading...")
            print('Selamat datang di program "Manajerial Candi"')

            # Membaca data dan menyimpannya di global variable
            ut.read_csv(folder_load, "user.csv")
            ut.read_csv(folder_load, "candi.csv")
            ut.read_csv(folder_load, "bahan_bangunan.csv")


def save():
    # I.S. data-data game belum tersimpan, F.S. data-data game tersimpan

    # Kamus Lokal
    # type User: array [0..NMaxUser] of array [0..2] of string
    # type Candi: array [0..NMaxCandi] of array [0..4] of string, int
    # folder_save: string
    # procedure write_csv(output folder_name : string, output file_name : string, output NMaxCandi: int, output NMaxUser: int, input/output users: User, input/output bahan_bangunan: Bahan_Bangunan, input/output candi: Candi)
    # { I.S. Data terbaru belum tertulis di file CSV, F.S. Data tertulis di CSV }

    # Algoritma
    folder_save = input("Masukkan nama folder: ")
    print("Saving...")

    # Jika directory save tidak ada
    if not os.path.exists("save"):
        print("Membuat folder save...")
        os.mkdir("save")

    # Jika directory save/<nama_folder> tidak ada
    if not os.path.exists(f"save/{folder_save}"):
        print(f"Membuat folder save/{folder_save}...")
        os.mkdir(f"save/{folder_save}")

    # Write file
    ut.write_csv(folder_save, "user.csv")
    ut.write_csv(folder_save, "candi.csv")
    ut.write_csv(folder_save, "bahan_bangunan.csv")
    print(f"Berhasil menyimpan data di folder save/{folder_save}!")

    # Reset undo array
    gv.undo_jin = [["", "", ""] for i in range(gv.NMaxUser)]
    gv.undo_candi = [[0, "", 0, 0, 0] for i in range(gv.NMaxCandi)]


def help():
    # I.S. player melakukan login atau belum melakukan login, F.S. memberikan list command sesuai dengan role player atau kondisi login player

    # Kamus Lokal
    # Kosong

    # Algoritma
    if gv.logged_in_username != "":
        if gv.logged_in_role == "bandung_bondowoso":
            print("=========== HELP ===========")
            print("1. logout")
            print("Untuk keluar dari akun yang digunakan sekaran")
            print("2. summonjin")
            print("Memanggil jin dari dunia lain.")
            print("3. hapusjin")
            print(
                "Menghapus jin dengan memasukkan username jin. Jika jin terhapus, candi yang dibuat oleh jin juga ikut terhapus"
            )
            print("4. ubahjin")
            print("Mengubah tipe jin dari username jin tertentu")
            print("5. undo")
            print(
                "Mengundo jin yang telah anda hapus. Setelah save, memory undo direset."
            )
            print("6. batchkumpul")
            print(
                "Setelah command dijalankan, jin tipe pengumpul akan mengumpulkan bahan secara random"
            )
            print("7. batchbangun")
            print(
                "Setelah command dijalankan setiap jin akan membangun candi dengan bahan yang di random untuk setiap candi"
            )
            print("8. laporanjin")
            print("Mengambil laporan jin untuk mengetahui kinerja para jin")
            print("9. laporancandi")
            print(
                "Mengambil laporan candi mulai dari total candi, ID Candi termahal/termurah, dan jumlah material yang digunakan"
            )
        elif gv.logged_in_role == "roro_jonggrang":
            print("=========== HELP ===========")
            print("1. logout")
            print("Untuk keluar dari akun yang digunakan sekarang")
            print("2. hancurkancandi")
            print("Menghancurkan candi sesuai ID candi yang diinput")
            print("3. ayamberkokok")
            print("Menyelesaikan permainan")
        elif gv.logged_in_role == "jin_pembangun":
            print("========== HELP ===========")
            print("1. logout")
            print("Untuk keluar dari akun yang digunakan sekarang")
            print("2. bangun")
            print("Jin akan membangun candi jika bahan bangunan cukup")
        elif gv.logged_in_role == "jin_pengumpul":
            print("========== HELP ===========")
            print("1. logout")
            print("Untuk keluar dari akun yang digunakan sekarang")
            print("2. kumpul")
            print(
                "Jin pengumpul akan mencari bahan berupa pasir, batu, dan air secara random"
            )
    else:
        print("=========== HELP ===========")
        print("1. login \n Untuk masuk menggunakan akun")
        print("2. exit \n Untuk keluar dari sistem program")


def exit():
    # I.S. player dalam kondisi login atau belum melakukan login, F.S. memberikan opsi pada player untuk menyimpan data program sebelum keluar dari program

    # Kamus Lokal
    # konfirmasi: string
    # procedure save (input/output undo_jin: User, input/output undo_candi: Candi)
    # { I.S. data-data game belum tersimpan, F.S. data-data game tersimpan }

    # Algoritma
    # Input dan Validasi Konfirmasi
    konfirmasi = input(
        "Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) "
    )
    while konfirmasi != "y" and konfirmasi != "n":
        konfirmasi = input(
            "Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) "
        )

    # Bila konfirmasi "y"
    if konfirmasi == "y":
        save()


def undo():
    # I.S. data user atau candi yang sudah dihapus, F.S. mengembalikan data yang telah dihapus sebelumnya

    # Kamus Lokal
    # type User: array [0..NMaxUser] of array [0..2] of string
    # type Candi: array [0..NMaxCandi] of array [0..4] of string, integer
    # konfirmasi, undo_username : string
    # found, ketemu_kosong_1, ketemu_kosong_2, ketemu_kosong_3 : boolean
    # i, j, k : integer

    # Algoritma
    if gv.logged_in_role != "bandung_bondowoso":
        print("Hanya Bandung Bondowoso yang dapat melakukan undo hilangkan jin.")
    else:
        found = False
        # Mencari jin paling atas dari array undo_jin
        for i in range(gv.NMaxUser - 1, -1, -1):
            # Ketemu
            if gv.undo_jin[i][0] != "":
                found = True
                # Save nama jin yang diundo
                undo_username = gv.undo_jin[i][0]

                # Tambahkan yang mau diundo ke array user
                for j in range(gv.NMaxUser):
                    # Mengisi slot kosong dari indeks terkecil
                    if gv.users[j][0] == "":
                        gv.users[j] = gv.undo_jin[i]
                        break

                # Hilangkan jin tersebut dari array undo jin
                gv.undo_jin[i] = ["", "", ""]

                for j in range(gv.NMaxCandi):
                    # Mencari semua candi di undo_candi dengan pembanbgun jin username yang sama
                    if gv.undo_candi[j][1] == undo_username:
                        # Mengisi slot candi kosong dari indeks terkecil
                        for k in range(gv.NMaxCandi):
                            # Ketemu slot kosong
                            if gv.candi[k][0] == 0:
                                # Update array candi
                                gv.candi[k] = [
                                    k + 1,
                                    undo_username,
                                    gv.undo_candi[j][2],
                                    gv.undo_candi[j][3],
                                    gv.undo_candi[j][4],
                                ]

                                # Hilangkan candi dari array undo_candi
                                gv.undo_candi[j] = [0, "", 0, 0, 0]

                                # Hanya isi sekali
                                break
                # Hanya lakukan 1 jin pada array undo_jin
                break
        if found:
            print("Undo hapus jin berhasil dilakukan.")
        else:
            print("Anda belum pernah menghapus jin.")
