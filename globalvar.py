# Inisialisasi Global Variable
# NOTE: BEBERAPA DATA DIBAWAH MASIH ASAL KARENA BLM DILOAD DGN CSV.
NMaxCandi = 1000
NMaxJin = 100

users = [
    ["Bondowoso", "cintaroro", "bandung_bondowoso"],
    ["Roro", "Gasukabondo", "roro_jonggrang"],
    ["jinp1", "ngabs", "jin_pembangun"],
    ["jinp2", "ngabs", "jin_pembangun"],
    ["jinp3", "ngabs", "jin_pembangun"],
    ["jinp4", "ngabs", "jin_pembangun"],
]
count_users = 6  # Update saat load CSV dan Nambah akun baru!

candi = [[0, "", 0, 0, 0] for i in range(NMaxCandi)]
candi[0] = [1, "jinp1", 1, 2, 3]
candi[1] = [2, "jinp1", 3, 4, 5]
candi[2] = [3, "jinp2", 2, 5, 3]
candi[3] = [4, "jinp3", 3, 1, 4]
candi[4] = [5, "jinp4", 5, 3, 2]
candi[5] = [6, "jinp4", 5, 3, 2]

bahan_bangunan = [
    ["pasir", "pasir adalah ...", 0],
    ["batu", "batu adalah ...", 0],
    ["air", "air adalah ...", 0],
]

logged_in_role = "bandung_bondowoso"

summoned_jin = [["", ""] for i in range(NMaxJin)]
summoned_jin[0] = ["jinp1, ngabs", "jin_pembangun"]
summoned_jin[1] = ["jinp1, ngabs", "jin_pembangun"]
summoned_jin[2] = ["jinp4, ngabs", "jin_pembangun"]
summoned_jin[3] = ["jinp2, ngabs", "jin_pengumpul"]
summoned_jin[4] = ["jinp3, ngabs", "jin_pengumpul"]
summoned_jin[5] = ["jinp4, ngabs", "jin_pengumpul"]
# [username, role]

# Load Data
# load("file/user.csv", users)
# load("file/candi.csv", candi)
# load("file/bahan_bangunan.csv", bahan_bangunan)
