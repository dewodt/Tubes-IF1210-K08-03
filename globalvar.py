# Inisialisasi Global Variable
# NOTE: BEBERAPA DATA DIBAWAH MASIH ASAL KARENA BLM DILOAD DGN CSV.
NMaxCandi = 1000

users = [
    ["Bondowoso", "cintaroro", "bandung_bondowoso"],
    ["Roro", "Gasukabondo", "roro_jonggrang"],
]

candi = [0 for i in range(NMaxCandi)]

bahan_bangunan = [
    ["pasir", "pasir adalah ...", 0],
    ["batu", "batu adalah ...", 0],
    ["air", "air adalah ...", 0],
]

logged_in_user = "Tes"

# Load Data
# load("file/user.csv", users)
# load("file/candi.csv", candi)
# load("file/bahan_bangunan.csv", bahan_bangunan)
