# Practice Questions (File Handling and try except):

# BASIC LEVEL:

# Write a program to create a file named data.txt and write “Hello Python” into it.

file = open("data.txt", "w")
file.write("Hello Python")
file.close()

# Write a program to read and display the content of data.txt.

file = open("data.txt","r")
content = file.read()
print(content)
file.close()

# Write a program to append your city name to data.txt.

file = open("data.txt","a")
file.write("\nKathamdu,Nepal")
file.close()

# Write a program to count the number of characters in a file.

with open("test1.txt","r") as file:
    count = 0
    content = file.read()
    for i in content:
        count = count + 1
    print(f"There are altogether {count} characters present in a file.")

# Write a program to count the number of lines in a file.

with open("data.txt","r") as file:
    count = 0
    content = file.readlines()
    for line in content:
        count += 1
    print(f"Total Number of Lines = {count}")
       
# Write a program to read only the first 5 characters of a file.

with open("data.txt","r") as f:
    result = f.read(5)
    print(result)

# Write a program to read a file line by line using a loop.

with open("data.txt","r") as f:
    line_count = 1
    content = f.readlines()
    for line in content:
        print(f"line{line_count} : {line}")
        line_count = line_count + 1


# Write a program to handle FileNotFoundError while reading a file.
try:
    with open("test.txt","r") as f:
        result = f.read()
        print(result)
except FileNotFoundError:
    print("File Doesnot Exist!")


# Write a program to take a number from user and handle invalid input using try/except.

try: 
    num = int(input("Enter a number please: "))
    sqr_num = num**2
    print(sqr_num)
except ValueError:
    print("Invalid Input! Please Use Numbers Only!")

# Write a program to demonstrate try, except, else, and finally using a simple example.

try: 
    num = int(input("Enter a number please: "))
    cube_num = num**3
except ValueError:
    print("Invalid Input! Please Use Numbers Only!")
    
else:
    print(cube_num)
finally:
    print("Program Exceuted Sucessfully!")

# INTERMEDIATE LEVEL:

# Write a program to store 5 student names in a file and display them.

# count = 1

# while count <= 5:
#     data = input("Enter The Student Name: ").strip()
    
#     with open("Students.txt","a") as file:
#         file.write(data + "\n")
#     count = count + 1

# with open("Students.txt","r") as f:
#     print(f.read())


# Write a program to search for a name inside a file.

with open("Students.txt","r") as file:
    name = input("Enter the Name To Search: ").strip()
    found = False
    content = file.readlines()
    for line in content:
        if name == line.strip():
            print("Name Found!")
            found = True
            break
    if found == False:
        print("Name Not Found!")

# Write a program to store student name and marks in the format:

# Ram,80
# Sita,90
# Hari,75

while True:
    print("1. Add Details\n2. Exit")
    choice = int(input("Press 1 to Add Student's Info and 2 To Exit: "))
    
    if choice == 1:
        name = input("Enter the Student Name: ").strip()
        marks = int(input("Enter the mark: "))
        
        with open("marks.txt","a") as file:
            file.write(name+","+str(marks)+"\n")
            print("Detail Added!")
    
    elif choice == 2:
        break
        
# Write a program to read student data and display only students who scored above 80.

with open("marks.txt","r") as f:
    content = f.readlines()
    
    for line in content:
        name, marks = line.strip().split(",")
        marks = int(marks)
        if marks > 80:
            print(f"{name} = {marks}")

# Write a program to update a specific student’s marks in a file.

std_name = input("Enter The Student Name To Update Marks: ").strip()
new_marks = input("Enter the new marks: ").strip()

found = False
updated_list = []

try:
    with open("marks.txt", "r") as f:
        for line in f:
            name, marks = line.strip().split(",")

            if name == std_name:
                updated_list.append(name + "," + new_marks)
                found = True
            else:
                updated_list.append(line.strip())

    if found:
        with open("marks.txt", "w") as f:
            for line in updated_list:
                f.write(line + "\n")
        print("Marks Updated Successfully!")
    else:
        print("Student Not Found!")

except FileNotFoundError:
    print("File does not exist!")


# Write a program to prevent duplicate usernames during registration.

username = input("Please Enter Username: ").strip()

found = False
try:
    with open("users.txt", "r") as file:
        for line in file:
            if username == line.strip():
                found = True
                break

except FileNotFoundError:
    print("File not Found!")
if found:
    print("This Username Already Exists! Please Try Different Username.")
else:
    with open("users.txt", "a") as file:
        file.write(username + "\n")
    print("Registered Successfully!")

# Write a program to build a simple login system using file storage.

print("1.) Register\n2.) Login")
choice = int(input("Choose the operation: "))

if choice == 1:
    username = input("Please Enter the Username to Register: ").strip()
    password = input("Please Enter a Strong Password: ").strip()
    found = False
    try:
        with open("new_cred.txt","r") as f:
            content = f.readlines()
            for i in content:
                if "," in i:
                    u,p = i.strip().split(",")
                    if u == username:
                        found = True
                        print("Username Already Exists! Please Try A Different Username!")
                        break
                
        if found == False:
            with open("new_cred.txt","a") as file:
                file.write(username+","+password+"\n")
                print("Registration Sucessful!")
                    
    except FileNotFoundError:
        print("The File Doesnot Exist!")
        
elif choice == 2:
        username = input("Enter valid username: ").strip()
        password = input("Enter valid password: ").strip()
        
        found = False
        with open("new_cred.txt","r") as file:
            content = file.readlines()
            for line in content:
                if "," in line:
                    u,p = line.strip().split(",")
                    if username == u and password == p:
                        print(f"Welcome {username}! Login Sucessful!")
                        found = True
                        break
        if found == False:
            print("Invalid Credential! Please Try Again!")
                        
# Write a program to handle division by zero and invalid input together.

try:
    num1 = int(input("Enter the first number please: "))
    num2 = int(input("Enter the Second Number Please: "))
    output = num1/num2 
    print(output)
except ZeroDivisionError:
    print("Cannot be Divided By Zero!")
except ValueError:
    print("Invalid Input! Please Enter Numbers Only!")
    
    
# Write a program to copy content from one file to another safely using try/except.

try:
    with open("Students.txt","r") as f:
        content = f.read()
    with open("new_std.txt","w") as file:
        file.write(content)
    
except FileNotFoundError:
    print("The File Doesnot Exist!")


# Write a program to create a file only if it does not already exist using "x" mode.

try:
    with open("file.txt","x") as f:
        pass
except FileExistsError:
    print("The File already exist!")

# ADVANCED LEVEL (Mini Projects + Real Logic)

# Write a program to build a complete ATM system with:

# Register

# Login

# Check Balance

# Deposit

# Withdraw

# Persistent storage in file

# Write a program to maintain transaction history in a separate file.

# Write a program to delete a specific user from a file.

user = input("Enter the user to remove: ").strip()
new_user = []
found = False

try:
    with open("new_cred1.txt","r") as file:
        content = file.readlines()
        for line in content:
            n , a = line.strip().split(",")
            if n == user:
                found = True
                continue
            else:
                new_user.append(line.strip())
                
    if found == True:
        with open("new_cred1.txt","w") as f:
            for line in new_user:
                f.write(line + "\n")
                print("User Deleted SucessFully!")
    else:
        print("User Not Found!")
            
except FileNotFoundError:
    print("File Not Found!")

# Write a program to replace a specific word in a file.

# Write a program to lock login after 3 failed attempts.

# Write a program to build a note-taking system with:

# Add note

# View notes

# Delete note

# Exception handling

# Write a program to count how many users have balance greater than 1000.

# Write a program to sort usernames alphabetically and rewrite the file.


# Write a program to build a menu-driven file manager system with full exception handling.