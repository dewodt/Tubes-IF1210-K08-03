import commands as cmd

# Program CANDI PRAMBANAN GAME
# Modul utama untuk menjalankan game

# Kamus
# masukan: string
# procedure load (input folder_load: string)
# { I.S. data-data CSV belum dibaca atau belum disimpan dalam program, F.S. data-data CSV terbaca dan disimpan dalam program}
# procedure run (output masukan: string)
# { I.S. program utama belum jalan, F.S. program utama jalan }

# Algoritma
# Load CSV
cmd.load()

# Program Utama Jalan
while True:
    masukan = input(">>> ")
    cmd.run(masukan)
    if masukan == "exit" or masukan == "ayamberkokok":
        break
