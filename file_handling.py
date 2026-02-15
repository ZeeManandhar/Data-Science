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

