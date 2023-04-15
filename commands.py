from random import randint

import globalvar as gv
import utils


def bangun():
    # Inisialisasi data awal
    init_pasir = gv.bahan_bangunan[0][2]
    init_batu = gv.bahan_bangunan[1][2]
    init_air = gv.bahan_bangunan[2][2]
    init_jin = gv.logged_in_user
    init_count_candi = utils.lenArray(gv.candi, gv.NMaxCandi)

    # Generate random number dari 1 sampai 5 untuk pasir, batu, dan air.
    gen_pasir = randint(1, 5)
    gen_batu = randint(1, 5)
    gen_air = randint(1, 5)

    # Jika pasir, batu, dan air cukup.
    if init_pasir >= gen_pasir and init_batu >= gen_batu and init_air >= gen_air:
        # Update sisa jumlah material.
        gv.bahan_bangunan[0][2] -= gen_pasir
        gv.bahan_bangunan[1][2] -= gen_batu
        gv.bahan_bangunan[2][2] -= gen_air

        # Update array candi.
        gv.candi[init_count_candi] = [
            init_count_candi - 1,
            init_jin,
            gen_pasir,
            gen_batu,
            gen_air,
        ]

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
    # Generate random number dari 0 sampai 5 untuk pasir, batu, dan air.
    gen_pasir = randint(0, 5)
    gen_batu = randint(0, 5)
    gen_air = randint(0, 5)

    # Update data jumlah pasir, batu, dan air.
    gv.bahan_bangunan[0][2] += gen_pasir
    gv.bahan_bangunan[1][2] += gen_batu
    gv.bahan_bangunan[2][2] += gen_air

    # Cetak pesan.
    print(f"Jin menemukan {gen_pasir} pasir, {gen_batu} batu, dan {gen_air} air.")


def batchbangun():
    # Inisialisasi data awal.
    init_pasir = gv.bahan_bangunan[0][2]
    init_batu = gv.bahan_bangunan[1][2]
    init_air = gv.bahan_bangunan[2][2]
    init_count_candi = utils.lenArray(gv.candi, gv.NMaxCandi)
    init_sisa_candi = 100 - init_count_candi
    init_count_jin_pembangun = 0
    for i in range(4):
        if gv.summoned_jin[i]:
            if gv.summoned_jin[i][1] == "jin_pembangun":
                print(gv.summoned_jin[i][1])
                init_count_jin_pembangun += 1
    batch_pasir = 0
    batch_batu = 0
    batch_air = 0

    # Looping n kali (n banyaknya jin yang tersummon).
    for i in range(init_count_jin_pembangun):
        # Generate random number dari 0 sampai 5 untuk pasir, batu, dan air.
        gen_pasir = randint(0, 5)
        gen_batu = randint(0, 5)
        gen_air = randint(0, 5)

        # Perbarui jumlah terkumpul.
        batch_pasir += gen_pasir
        batch_batu += gen_batu
        batch_air += gen_air

    # Jika pasir, batu, dan air cukup.
    if init_count_jin_pembangun > 0:
        if (
            init_pasir >= batch_pasir
            and init_batu >= batch_batu
            and init_air >= batch_air
        ):
            # Update data jumlah pasir, batu, dan air.
            gv.bahan_bangunan[0][2] -= gen_pasir
            gv.bahan_bangunan[1][2] -= gen_batu
            gv.bahan_bangunan[2][2] -= gen_air

            # Update array candi.
            for i in range(
                init_count_candi, init_count_candi + init_count_jin_pembangun
            ):
                gv.candi[i] = [
                    i,
                    "SEMUA JIN ATAU GMN???",
                    gen_pasir,
                    gen_batu,
                    gen_air,
                ]

            # Cetak pesan.
            print(
                f"Mengerahkan {init_count_jin_pembangun} jin untuk membangun candi dengan total bahan {batch_pasir} pasir, {batch_batu} batu, dan {batch_air} air."
            )
            if init_sisa_candi - init_count_jin_pembangun > 0:
                print(
                    f"Sisa candi yang perlu dibangun: {init_sisa_candi-init_count_jin_pembangun}."
                )
            else:
                print("Sisa candi yang perlu dibangun: 0.")
        else:
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")
    else:
        print(
            "Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu."
        )


def batchkumpul():
    # Inisialisasi data awal.
    init_count_jin_pengumpul = 0
    for i in range(4):
        if gv.summoned_jin[i]:
            if gv.summoned_jin[i][1] == "jin_pengumpul":
                print(gv.summoned_jin[i][1])
                init_count_jin_pengumpul += 1
    batch_pasir = 0
    batch_batu = 0
    batch_air = 0

    # Looping n kali (n banyaknya jin).
    for i in range(init_count_jin_pengumpul):
        # Generate random number dari 0 sampai 5 untuk pasir, batu, dan air.
        gen_pasir = randint(0, 5)
        gen_batu = randint(0, 5)
        gen_air = randint(0, 5)

        # Perbarui jumlah terkumpul.
        batch_pasir += gen_pasir
        batch_batu += gen_batu
        batch_air += gen_air

    # Update data jumlah pasir, batu, dan air.
    gv.bahan_bangunan[0][2] += gen_pasir
    gv.bahan_bangunan[1][2] += gen_batu
    gv.bahan_bangunan[2][2] += gen_air

    # Cetak pesan.
    print(
        f"Jin menemukan total {batch_pasir} pasir, {batch_batu} batu, dan {batch_air} air."
    )


def laporanjin():
    # Kasus role logged in bukan bandung bondowoso
    if gv.logged_in_role != "bandung_bondowoso":
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        # Hitung jumlah jin
        jin_total = 0
        jin_pembangun = 0
        jin_pengumpul = 0
        for i in range(gv.count_users):
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
        for i in range(gv.count_users):
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
        i = 0
        while i < gv.NMaxCandi and gv.candi[i][0] != 0:
            # Total candi
            total_candi += 1

            # Material total candi
            total_pasir += gv.candi[i][2]
            total_batu += gv.candi[i][3]
            total_air += gv.candi[i][4]

            # Candi termahal
            id_now = gv.candi[i][0]
            harga_now = (
                10000 * gv.candi[i][2] + 15000 * gv.candi[i][3] + 7500 * gv.candi[i][4]
            )

            # Jika dua candi sama-sama termahal/termurah, keluarkan indeks terendah.
            print(harga_now)
            # Update termahal
            if harga_now > harga_termahal:
                harga_termahal = harga_now
                id_termahal = id_now
            # Update termurah
            if harga_now < harga_termurah:
                harga_termurah = harga_now
                id_termurah = id_now

            # Iterasi selanjutnya
            i += 1

        # Cetak pesan
        print(f"> Total Candi: {total_candi}")
        print(f"> Total Pasir yang digunakan: {total_pasir}")
        print(f"> Total Batu yang digunakan: {total_batu}")
        print(f"> Total Air yang digunakan: {total_air}")
        print(f"> ID Candi Termahal: {id_termahal}")
        print(f"> ID Candi Termurah: {id_termurah}")
