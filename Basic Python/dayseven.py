# File Handling

# File Handling Flow
# OPen the file => open()
# Perform the operation in file => read "r" read(), write "w" Write(), append "a" write()
# Close the file => close()


# Write operation

file = open("test1.txt","w") #Opening the file
file.write("I am a Data Scientist!") # Operation on File
file.close() # Close the file

# If a file is opened in read mode, and the file doesnot exist then it  throws an error.
# If a file is opened in write mode, and the file doesnot exist then it creates a new file.
# We can only write string and JSON in File

#Append operations
file = open("test2.txt","a") #Opening the file
file.write("Its me Zeeson Manandhar!") # Operation on File
file.close() # Close the file

#Read
file = open("test2.txt","r") #Opening the file
content = file.read() # Operation on File
file.close() # Close the file

print(content)


# Login and register system without password 

#Creating a Function for regsiter

def register():
    username = input("Enter your Username: ")
    file = open("credentials.txt","a")
    file.write(username + "-")
    file.close()

def login():
    username1 = input("Enter your created username please: ")
    file = open("credentials.txt","r")
    content = file.read()
    
 
while True:
    choice = int(input("Enter 1 for register, 2 for login, 3 for exit: "))
    match choice:
        case 1:
            register()
        case 2:
            login()
        case 3:
            break
        case _:
            print("Invalid Operations")

print("Thank you for Visiting Us!!!")           