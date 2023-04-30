import datetime

# Modul Global Variable
# Modul untuk tempat menyimapnnya variable-variabel global

# Kamus

# Algoritma
# Inisialisasi Global Variable
# Jumlah anggota array maksimum
NMaxCandi = 1000
NMaxUser = 102

# Menyimpan informasi user logged in
logged_in_role = ""
logged_in_username = ""

# Simpan nilai awal (seed) untuk Random LCG dan menyimpan x ke n untuk perhitungan selanjutnya.
xn = int(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

# Inisialisasi sebelum baca CSV dan menyimpan data yang dibaca nantinya
users = [["", "", ""] for i in range(NMaxUser)]
candi = [[0, "", 0, 0, 0] for i in range(NMaxCandi)]
bahan_bangunan = [
    ["", "", 0],
    ["", "", 0],
    ["", "", 0],
]

# Inisialisasi stack undo
undo_jin = [["", "", ""] for i in range(NMaxUser)]
undo_candi = [[0, "", 0, 0, 0] for i in range(NMaxCandi)]
