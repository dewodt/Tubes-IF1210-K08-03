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
