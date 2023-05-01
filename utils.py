import math

import globalvar as gv


# Menerima range min, max, dan seed dan mengembalikan 3 bilangan random
def RandomLCG(min: int, max: int, seed: int) -> list[int]:
    # Menghasilkan array yang berisi tiga angka random dalam range [min, max]

    # Kamus Lokal
    # random_array: array [0..2] of int
    # a, c, m, normalized_value: int

    # Algoritma
    random_array = [0, 0, 0]
    a, c, m = 1103515245, 12345, 2**31 - 1
    gv.xn = (a * seed + c) % m

    for i in range(3):
        normalized_value = math.floor(min + (max - min + 1) * (gv.xn / m))
        random_array[i] = normalized_value
        gv.xn = (a * gv.xn + c) % m

    return random_array


# Read CSV
def read_csv(folder_name: str, file_name: str):
    # I.S. data global variable kosong, F.S. data terisi dari data CSV pada folder <folder_name>

    # Kamus Lokal
    # type User: array [0..NMaxUser] of array [0..2] of string
    # type Candi: array [0..NMaxCandi] of array [0..4] of string, int
    # type Bahan_Bangunan: array [0..2] of array [0..2] of string, int
    # temp_array: array [0..NRow] of array [0.. NCol] of string
    # { Untuk user.csv, NRow = NMaxUser-1 dan NCol = 2 }
    # { Untuk bahan_bangunan.csv, NRow = 2 dan NCol = 2 }
    # { Untuk candi.csv, NRow = NMaxCandi-1 dan NCol = 4 }
    # file : SEQFILE of
    # (*) cc : character
    # (1) “” { Empty }
    # i, kolom : int

    # Algoritma
    # Inisialisasi array sementara untuk concatenate string
    temp_array = []
    if file_name == "user.csv":
        temp_array = [["" for j in range(3)] for i in range(gv.NMaxUser)]
    elif file_name == "bahan_bangunan.csv":
        temp_array = [["" for j in range(3)] for i in range(3)]
    elif file_name == "candi.csv":
        temp_array = [["" for j in range(5)] for i in range(gv.NMaxCandi)]

    # Baca CSV
    file = open(f"save/{folder_name}/{file_name}", "r")
    i = -1
    # Iterasi setiap bari pada file
    for line in file:
        if i != -1:  # Jika buka baris pertama
            kolom = 0
            for j in range(len(line)):  # Looping sepanjang baris
                # Baca character dan menyimpannya ke global variable
                if line[j] != ";" and line[j] != "\n":
                    temp_array[i][kolom] += line[j]

                # Jika ganti kolom atau baris maka konversi data yang diperlukan ke integer dan simpan ke global var
                if line[j] == ";" or j == len(line) - 1:
                    if file_name == "user.csv":
                        gv.users[i][kolom] = temp_array[i][kolom]
                    elif file_name == "bahan_bangunan.csv":
                        if kolom == 2:
                            gv.bahan_bangunan[i][kolom] = int(temp_array[i][kolom])
                        else:
                            gv.bahan_bangunan[i][kolom] = temp_array[i][kolom]
                    elif file_name == "candi.csv":
                        if kolom != 1:
                            gv.candi[i][kolom] = int(temp_array[i][kolom])
                        else:
                            gv.candi[i][kolom] = temp_array[i][kolom]
                    kolom += 1
                # Next character
                j += 1
        # Next row
        i += 1
    file.close()


# Write CSV
def write_csv(folder_name: str, file_name: str):
    # I.S. Data terbaru belum tertulis di file CSV, F.S. Data tertulis di CSV

    # Kamus Lokal
    # type User: array [0..NMaxUser] of array [0..2] of string
    # type Candi: array [0..NMaxCandi] of array [0..4] of string, int
    # type Bahan_Bangunan: array [0..2] of array [0..2] of string, int
    # file : SEQFILE of
    # (*) cc : character
    # (1) “” { Empty }
    # i, j : int
    # message: string

    # Algoritma
    message = ""
    # Menuliskan array user menjadi string
    if file_name == "user.csv":
        for i in range(gv.NMaxUser):
            if i == 0:
                message += "username;password;role\n"
            for j in range(3):
                if gv.users[i][0] != "":
                    message += str(gv.users[i][j])
                    if j != 2:
                        message += ";"
                    else:
                        if gv.users[i + 1][0] != "":
                            message += "\n"
    # Menuliskan array candi menjadi string
    elif file_name == "candi.csv":
        for i in range(gv.NMaxCandi):
            if i == 0:
                message += "id;pembuat;pasir;batu;air\n"
            for j in range(5):
                if gv.candi[i][1] != "":
                    message += str(gv.candi[i][j])
                    if j != 4:
                        message += ";"
                    else:
                        if gv.candi[i + 1][1] != "":
                            message += "\n"
    # Menuliskan array bahan bangunan menjadi string
    elif file_name == "bahan_bangunan.csv":
        message += "nama;deskripsi;jumlah\n"
        message += (
            f"pasir;pasir adalah bahan untuk membuat semen;{gv.bahan_bangunan[0][2]}\n"
        )
        message += f"batu;batu adalah bahan untuk membuat tembok candi;{gv.bahan_bangunan[1][2]}\n"
        message += (
            f"air;air adalah bahan untuk mencairkan semen;{gv.bahan_bangunan[2][2]}"
        )

    # Menuliskan file
    file = open(f"save/{folder_name}/{file_name}", "w")
    file.write(message)
    file.close()
