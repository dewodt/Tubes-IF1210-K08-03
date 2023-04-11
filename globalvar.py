# Inisialisasi Global Variable
# NOTE: BEBERAPA DATA DIBAWAH MASIH ASAL KARENA BLM DILOAD DGN CSV.
NMaxCandi = 1000
NMaxJin = 100

users = [
    ["Bondowoso", "cintaroro", "bandung_bondowoso"],
    ["Roro", "Gasukabondo", "roro_jonggrang"],
    ["jinp1, ngabs", "jin_pembangun"],
    ["jinp2, ngabs", "jin_pembangun"],
    ["jinp3, ngabs", "jin_pembangun"],
]

candi = [0 for i in range(NMaxCandi)]

bahan_bangunan = [
    ["pasir", "pasir adalah ...", 0],
    ["batu", "batu adalah ...", 0],
    ["air", "air adalah ...", 0],
]

logged_in_user = "Tes"

summoned_jin = [[] for i in range(NMaxJin)]
summoned_jin[0] = ["jinp1, ngabs", "jin_pembangun"]
summoned_jin[1] = ["jinp1, ngabs", "jin_pembangun"]
summoned_jin[2] = ["jinp1, ngabs", "jin_pembangun"]
# [username, role]

# Load Data
# load("file/user.csv", users)
# load("file/candi.csv", candi)
# load("file/bahan_bangunan.csv", bahan_bangunan)
