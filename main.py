import commands as cmd

# Load CSV
cmd.load()

# Program Utama
while True:
    masukan = input(">>> ")
    cmd.run(masukan)
    if masukan == "exit" or masukan == "ayamberkokok":
        break
