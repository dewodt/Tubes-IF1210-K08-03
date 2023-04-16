import csv


def login_input():  # masukan input username dan password dari username
    username = input("Username:")
    password = input("Password:")
    user_tuple = (username, password)
    return user_tuple  # return hasil input user


def login_req(user_input): #digunakan untuk login
    #input user
    username = user_input[0]
    password = user_input[1]  
    
    #menghubungkan csv
    with open("user.csv", 'r') as f:
        data = csv.reader(f, delimiter =";")
        condition = False
        for name in data: #username [0], password[1], role[2]
            if name[0] == username:
                condition = True
                if name[1] == password:
                    kondisi_login = True
                    print(f"Selamat datang, {username}!")
                    print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
                else:
                    print("Password salah!")
                    kondisi_login = False
    if not condition:
        print("Username tidak terdaftar!")
        kondisi_login = False
        
    return kondisi_login


def periksa_login(kondisi_login):
    if kondisi_login:  # player telah login
        return True
    else:  # player belum login
        return False


def logout_req():  # return kondisi_login user ke False
    kondisi_login = False
    return kondisi_login
