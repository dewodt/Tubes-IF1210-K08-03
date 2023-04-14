import csv



def login_input(): #masukan input username dan password dari username
    username = input("Username:")
    password = input("Password:")
    user_tuple = (username,password)
    return user_tuple #return hasil input user


def login_req(kondisi_login, user_input): #digunakan untuk login
    #input user
    username = user_input[0]
    password = user_input[1]  
    
    arr_user = []
    arr_pass = []
    #menghubungkan csv
    with open("user.csv",'r') as file_user:
        for line in file_user:
            splitted_dat = line.split(';') #split data tetapi masih dalam bentuk list in list
            arr_user.insert(0, splitted_dat[0])
            arr_pass.insert(0, splitted_dat[1])
            

        #checking username dan password
        condition = False
        for idxuser in range (len(arr_user)-1, -1,-1):
            if username == arr_user[idxuser]:
                condition = True
                for idxpass in range (len(arr_pass)-1, -1, -1):
                    if password == arr_pass[idxpass]:
                        print(f"Selamat datang, {username}!")
                        print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
                        kondisi_login = True
                        return kondisi_login
                else:
                    print("Password salah!")
                    kondisi_login = False
    if not condition:
        print("Username tidak terdaftar")
        kondisi_login = False
        
    return kondisi_login, username


def periksa_login(kondisi_login):
    if kondisi_login: #player telah login
        return True
    else:             #player belum login
        return False

def logout_req(kondisi_login): #return kondisi_login user ke False
    kondisi_login = False       
    return kondisi_login

