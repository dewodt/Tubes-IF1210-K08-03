import loginnlogout as lg


def help(cond, role):  # (kondisi login, username yang masuk)
    kondisi = lg.periksa_login(cond)
    if kondisi:
        if role == "bandung_bondowoso":
            print("=========== HELP ===========")
            print("1. logout \n Untuk keluar dari akun yang digunakan sekarang")
            print("2. summonjin \n Memanggil jin dari dunia lain.")
            print(
                "Setelah memilih jenis jin yang ingin dipanggil, Bondowoso harus memilih username dan password untuk jin tersebut"
            )
            print("3. hapusjin \n menghapus jin dengan memasukkan username jin.")
            print("Jika jin terhapus, candi yang dibuat oleh jin juga ikut terhapus")
            print(
                "4. batchkumpul \n setelah command dijalankan, jin tipe pengumpul akan mengumpulkan bahan secara random"
            )
            print(
                "5. batchbangun \n Setelah command dijalankan setiap jin akan membangun candi dengan bahan yang di random untuk setiap candi"
            )
            print(
                "6. laporanjin \n Mengambil laporan jin untuk mengetahui kinerja para jin"
            )
            print(
                "7. laporancandi \n Mengambil laporan candi mulai dari total candi, ID Candi termahal/termurah, dan jumlah material yang digunakan"
            )

        elif role == "roro_jonggrang":
            print("=========== HELP ===========")
            print("1. logout \n Untuk keluar dari akun yang digunakan sekarang")
            print(
                "2. hancurkancandi \n Menghancurkan candi sesuai ID candi yang diinput"
            )
            print("3. ayamberkokok \n Menyelesaikan permainan")

        elif role == "pembangung":
            print("========== HELP ===========")
            print("1. logout \n Untuk keluar dari akun yang digunakan sekarang")
            print("2. bangun \n Jin akan membangun candi jika bahan bangunan cukup")

        elif role == "pengumpul":
            print("========== HELP ===========")
            print("1. logout \n Untuk keluar dari akun yang digunakan sekarang")
            print(
                "2. kumpul \n Jin pengumpul akan mencari bahan berupa pasir, batu, dan air secara random"
            )

    else:
        print("=========== HELP ===========")
        print("1. logout \n Untuk keluar dari akun yang digunakan sekarang")
        print("2. exit \n Untuk keluar dari sistem program")
