import carirole as rf

import commands as cmd
import globalvar as gv
import help as hf
import loginnlogout as lg

# File Utama
kondisi_login = False  # set kondisi login awal False
username = "None"
role = ""
masukan = input(">>> ")
while True:
    if masukan == "login":
        if lg.periksa_login(kondisi_login):
            print("Login gagal!")
            print(
                f'Anda telah login dengan username {username}, silakan lakukan "logout" sebelum melakukan login kembali'
            )

        else:
            user_input = lg.login_input()
            username = user_input[0]
            kondisi_login = lg.login_req(user_input)
            role = rf.find_role(username)

    if masukan == "help":
        hf.help(kondisi_login, role)

    if masukan == "logout":
        if lg.periksa_login(kondisi_login):
            kondisi_login = lg.logout_req()

        else:
            print("Logout gagal!")
            print(
                "Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout"
            )

    masukan = input(">>> ")
    # cmd.kumpul()
    # cmd.bangun()
    # cmd.batchbangun()
    # cmd.batchkumpul()
    # Note : untuk command nya letak di atas loop var masukan
    # Note : tiap conditional tidak perlu lagi diberi input,
    # karena input akan jalan setelah kondisional command selesai
    # Note : file main.py belum memiliki function exit,
    # jadi file masih dalam kondisi infinite loop meminta input user
