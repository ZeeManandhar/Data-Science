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
f.write("Added New Text!")
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

