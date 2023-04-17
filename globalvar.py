import datetime

# Inisialisasi Global Variable
# Jumlah anggota array maksimum
NMaxCandi = 1000
NMaxUser = 102

# Menyimpan state game
logged_in_role = "bandung_bondowoso"

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
