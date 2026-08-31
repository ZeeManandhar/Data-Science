# Login and Register system with username and password 

import json
def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
   
    dict_credential = {username:password}
    json_credential = json.dumps(dict_credential)
    file = open("credentials.txt","a")
    file.write(json_credential + "-")
    file.close

def login():
   username = input("Enter your Username: ")
   password = input("Enter your valid password: ")

   file = open("credentials.txt", "r")
   content = file.read()
   file.close()
   list_credentials = content.split("-")

   for i in list_credentials:
       if i != "" :
         dict_i = json.loads(i)
         if username in dict_i and dict_i[username] == password :
             print(f"welcome {username}, Login Sucessfull")
             break
       else :
        print("Login Failed")
   

while True:
    choice = int(input("Enter 1 for register, Enter 2 for login, 3 for exit: "))

    match choice :
        case 1 :
            register()
        case 2:
            login()
        case 3:
            break
        case _:
            print("Invalid Input")