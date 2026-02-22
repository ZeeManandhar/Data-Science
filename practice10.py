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

# Write a program to search for a name inside a file.

# Write a program to store student name and marks in the format:

# Ram,80
# Sita,90
# Hari,75

# Write a program to read student data and display only students who scored above 80.

# Write a program to update a specific student’s marks in a file.

# Write a program to prevent duplicate usernames during registration.

# Write a program to build a simple login system using file storage.

# Write a program to handle division by zero and invalid input together.

# Write a program to copy content from one file to another safely using try/except.

# Write a program to create a file only if it does not already exist using "x" mode.

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

# Write a program to replace a specific word in a file.

# Write a program to lock login after 3 failed attempts.

# Write a program to build a note-taking system with:

# Add note

# View notes

# Delete note

# Exception handling

# Write a program to count how many users have balance greater than 1000.

# Write a program to sort usernames alphabetically and rewrite the file.

# Write a program to create a password-based login system with file storage.

# Write a program to build a menu-driven file manager system with full exception handling.