import datetime

# Inisialisasi Global Variable

# Jumlah anggota array maksimum
NMaxCandi = 1000
NMaxJin = 100

# Simpan nilai awal (seed) untuk Random LCG dan menyimpan x ke n untuk perhitungan selanjutnya.
xn = int(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

# Menyimpan data user
users = [
    ["Bondowoso", "cintaroro", "bandung_bondowoso"],
    ["Roro", "Gasukabondo", "roro_jonggrang"],
    ["jinp1", "ngabs", "jin_pembangun"],
    ["jinp2", "ngabs", "jin_pembangun"],
    ["jinp3", "ngabs", "jin_pengumpul"],
    ["jinp4", "ngabs", "jin_pengumpul"],
    ["jinp5", "ngabs", "jin_pengumpul"],
    ["jinp6", "ngabs", "jin_pengumpul"],
    ["jinp7", "ngabs", "jin_pengumpul"],
    ["jinp8", "ngabs", "jin_pembangun"],
    ["jinp9", "ngabs", "jin_pembangun"],
    ["jinp10", "ngabs", "jin_pembangun"],
]
count_users = 12  # Update saat load CSV dan Nambah akun baru!\

# Menyimpan data candi
candi = [[0, "", 0, 0, 0] for i in range(NMaxCandi)]
candi[0] = [1, "jinp1", 1, 2, 3]
candi[1] = [2, "jinp1", 3, 4, 5]
candi[2] = [3, "jinp2", 2, 5, 3]
candi[3] = [4, "jinp3", 3, 1, 4]
candi[4] = [5, "jinp4", 5, 3, 2]
candi[5] = [6, "jinp4", 5, 3, 2]

# Menyimpan data bahan bangunan
bahan_bangunan = [
    ["pasir", "pasir adalah ...", 0],
    ["batu", "batu adalah ...", 0],
    ["air", "air adalah ...", 0],
]

# Menyimpan state game
logged_in_role = "bandung_bondowoso"

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
