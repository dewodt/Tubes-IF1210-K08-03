import commands as cmd
import globalvar as gv

# Load CSV
cmd.load()

# Program Utama
while True:
    masukan = input(">>> ")
    cmd.run(masukan)
    if masukan == "exit" or masukan == "ayamberkokok":
        break
