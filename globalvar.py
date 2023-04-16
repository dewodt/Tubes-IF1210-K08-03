import datetime

# Inisialisasi Global Variable
# Jumlah anggota array maksimum
NMaxCandi = 1000
NMaxUser = 1000
NMaxJin = 100

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

# Menyimpan data jin yang telah tersummon
summoned_jin = [["", "", ""] for i in range(NMaxJin)]
summoned_jin[0] = ["jinp1", "ngabs", "jin_pembangun"]
summoned_jin[1] = ["jinp2", "ngabs", "jin_pembangun"]
summoned_jin[2] = ["jinp3", "ngabs", "jin_pengumpul"]
summoned_jin[3] = ["jinp4", "ngabs", "jin_pengumpul"]
summoned_jin[4] = ["jinp5", "ngabs", "jin_pengumpul"]
summoned_jin[5] = ["jinp6", "ngabs", "jin_pengumpul"]
summoned_jin[6] = ["jinp7", "ngabs", "jin_pengumpul"]
summoned_jin[7] = ["jinp8", "ngabs", "jin_pembangun"]
summoned_jin[8] = ["jinp9", "ngabs", "jin_pembangun"]
summoned_jin[9] = ["jinp10", "ngabs", "jin_pembangun"]
