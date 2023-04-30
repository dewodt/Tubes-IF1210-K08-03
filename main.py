import commands as cmd

# Program CANDI PRAMBANAN GAME
# Modul utama untuk menjalankan game

# Kamus

# Algoritma
# Load CSV
cmd.load()

# Program Utama Jalan
while True:
    masukan = input(">>> ")
    cmd.run(masukan)
    if masukan == "exit" or masukan == "ayamberkokok":
        break
