import csv

def find_role(username):
    with open("user.csv",'r') as file_role:
        data = csv.reader(file_role, delimiter = ';')
        for l in data:
            if l[0] == username:
                role = l[2]
                
    # for role in arr_role:
    #     if username == role:
    #         print(role)
    return role

            
