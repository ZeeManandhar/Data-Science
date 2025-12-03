# Login, Register, View Balance system
import json

current_user = ""


def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    dict_credential = {username: password}
    json_credential = json.dumps(dict_credential)

    file = open("credentials.txt", "a")
    file.write(json_credential + "-")
    file.close()

    print("Registration Successful")


def view_balance():
    file = open("balance.txt", "r")
    content = file.read()
    file.close()

    list_bal = content.split("-")

    for i in list_bal:
        if i != "":
            d = json.loads(i)
            if current_user in d:
                print("Your Balance is:", d[current_user])
                return

    print("Your Balance is Zero!!")


def login():
    global current_user

    username = input("Enter your Username: ")
    password = input("Enter your valid password: ")

    file = open("credentials.txt", "r")
    content = file.read()
    file.close()

    list_credentials = content.split("-")

    for i in list_credentials:
        if i != "":
            dict_i = json.loads(i)

            if username in dict_i and dict_i[username] == password:
                current_user = username
                print(f"Welcome {username}, Login Successful")

                # only for viewing balance 
                while True:
                    choice_atm = int(input("Enter 1 to View Balance, 2 to Exit: "))

                    match choice_atm:
                        case 1:
                            view_balance()
                        case 2:
                            break
                        case _:
                            print("Invalid Input")

                break
    else:
        print("Login Failed")



while True:
    choice = int(input("Enter 1 for Register, 2 for Login, 3 for Exit: "))

    match choice:
        case 1:
            register()
        case 2:
            login()
        case 3:
            break
        case _:
            print("Invalid Input")
