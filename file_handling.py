# File Handling

# 1.) File: A file is something stored on your computer.
# Examples:
# notes.txt
# data.txt
# users.txt
# It stores information permanently.

# When we create a variable: i.e.

name = "Zeeson"

# This is stored in RAM (memory).
# RAM is temporary.
# When we close Python, the data is gone 

# But if we save it in a file
# Even after closing Python, it stays saved


# 1.1.) Memory vs File:

# Memory (RAM):

# Temporary
# Fast
# Data disappears after program ends

# File (Disk):

# Permanent
# Slower than RAM
# Data stays saved


# 2.) Open() Function:

# Basic Syntax: open(filename, mode)

# where:
# filename ---> Name of the file
# mode ----> What you want to do with file

# For Instance: f = open("demo.txt", "w")

# 2.1.) What does open() return?

# It returns something called as File Object.

# Example:

file = open("zee.txt","w")

# Now f is a file object.

# Think of it like:
# f is a connection between Python and the file.

# 2.2) Why Must We Close File?

# After opening a file:

# we should close the file.
file.close()

# Because:

# It saves changes properly
# It frees memory
# It prevents file corruption
# If we forget to close:
# Sometimes file may not save properly

# Simple Example:
f = open("demo.txt", "w")
f.close()

# When we run it a new file, demo.txt is created.

# We opened file in "w" mode
# Since file didn’t exist ----> Python created it
# Then we closed it

# 3.) File Modes

# When we open a file:

# open("demo.txt", "mode") # This mode tells Python what we want to do with the file.

# 3.1) "r" --- READ MODE

f = open("demo1.txt", "r")
print(f.read())  
f.close()

# Meaning:

# Open file to read
# File MUST exist
# If file does not exist, it shows error.

# Use when:
# You only want to read content.


# 3.2) "w" -- Write Mode

f = open("demo.txt","w")
f.write("Today is Sunday! Have a Good Day!")
file.close()

# Meaning:

# Write into file.
# If file does NOT exist, then it creates it.
# If file exists, then it deletes old content and replaces it.

# Key Important To Remember: "w" erases old content.

# 3.3) "append" --- Append Mode

f = open("demo.txt","a")
f.write("\n Added New Text!")
f.close()

# Meaning:
# Add new content at the end (must use .write() method, there is no append method.)
# Does NOT delete old content
# Creates file if not exist

# 3.4) "x" --- Create Mode

# f = open("demo2.txt", "x")
# f.write("Hello! I am learning File Hnadling.")
# f.close()

# Meaning:

# Create new file only (Method used: write())
# If file already exists, then it throws an error 

# Used when:
# we want to ensure file does NOT already exist.

# 3.5) "r+" ---- Read and Write On

f = open("demo2.txt","r+")
f.write("Hi")
print(f.read())
f.close()

# Meaning:
# Read and write
# File must exist
# Does NOT erase automatically

# Key Note To Remember for ""r+": 
# It will overwrite from the start.
# It does NOT erase entire file like "w".
# It only overwrites from current position.


# 4.) Reading Files

# 4.1) read() Method

f = open("demo1.txt", "r")

print("First read:")
print(f.read())

# It reads the entire file
# Returns it as a string

# After read(), the cursor goes to the end of file.
# So if we try to read again:
print("Second read:")
print(f.read())

# It will print nothing.
# Because it already reached the end.

# 4.2) read(size):

# We can also read only some characters.

# For Example:

f = open("demo1.txt","r")
content = f.read(4)
print(content)
file.close()


# 4.3) readline():

# This method only reads one line at a time.

f = open("demo1.txt","r")
content = f.readline()
print(content)
first_content = f.readline()
print(first_content)
file.close()

# 4.4) readlines():

# This reads all lines and stores them inside a list.

# For Example:

file = open("demo.txt","r")
lines = file.readlines()
print(lines)
file.close()

# It returns list of lines.

# 5.) Writing Files: 

file = open("write.txt","w")
file.write("Hello Hi Hey! \nNew Day New Mood!!")
file.close()

# This will:
# Open file in write mode
# Delete old content
# Write new content

# Important: write() does NOT automatically go to new line. Must use \n for new line.

# 6.) Append Mode

file = open("write.txt","a")
file.write("\nChill out! Have Good Day")
file.close()

# Add new content at the END
# Do NOT delete old content

# 7.) with Statement (Very Important):

with open("write.txt","r") as file:
    content = file.read()
    print(content)

# here, 
# No close() needed.
# When the block ends, Python automatically closes the file.

# Think it like this:
# with = "Use file safely"
# When work is finished, it automatically close it.

# 7.1) Why Professionals Use with
# Cleaner code
# Safer
# Less errors
# Automatic closing

# Important Rule: Anything inside with block must be indented.

# 8.) File Handling Errors:

# Example:
# What happens if we do this:

# with open("unknown.txt", "r") as f:
#     content = f.read()
#     print(content)

# if unknown.txt does NOT exist? Then:

# Python will CRASH.
# We will see error like:

# FileNotFoundError: [Errno 2] No such file or directory: 'unknown.txt'

# This is called a runtime error.
# The program stops immediately.

# Common File Errors:
# a. File does not exist -----> FileNotFoundError
# b. No permission to open ----> PermissionError


# 10.) Basic try / except:

# Why Do We Need try / except?

# Example:

# num = int(input("Enter the Number: "))
# result = num/0
# print(result)

# This gives error and program crashes, which is not good in real applications.

# For this: We can use try/except:

# Basic Structure:

# try:
#     risky code
# except:
#     fallback code

# Example: 
try:
    num = int(input("Enter the Number Please: "))
    result = 5/num
    print(result)
except:
    print("Something Went Wrong.")

# Now, here:

# If user enters 0 or abc
# Program will NOT crash.
# Instead it prints: Something Went Wrong.

# Python says:
# "Try this code."
# "If any error happens, run the except block instead."

# 11. Specific Exceptions: