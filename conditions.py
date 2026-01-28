# A program often needs to choose between actions based on a condition.

# Real-life examples:

# If password is correct --> allow login, else --> deny.
# If marks ≥ 40 --> pass, else → fail.
# If item is in stock --> allow purchase, else --> show “out of stock”.

# Boolean values: True and False

# A Boolean is a value that is either:
# True
# False
# In Python, conditions evaluate to Booleans.

# Examples:

print(10 > 5)     
print(10 == 5)   
print("a" in "cat")  

# Conditions come from comparisons

# Comparisons produce True/False, which we use in if.

# Common comparison operators:
# > greater than
# < less than
# == equal to
# != not equal to
# >= greater than or equal
# <= less than or equal

# Example:
height = 6.0
print(height>=6.0)


# If Statement: (Basics):

# An if statement allows the program to run code only when a condition is True.
# IF something is true, then DO this

# Basic syntax of if
# if condition:
#     statement_1
#     statement_2

# Key rules:
# The condition must evaluate to True or False
# A colon : is mandatory
# Code inside if must be indented


# Indentation (important)
# Python uses indentation instead of braces {}.

# Code:
if 10 > 5:
    print("Ten is greater")

# if 10 > 5:
# print("Ten is greater")   # This throws IndentationError

# How Python reads an if

# Step by step:
# Evaluate the condition
# If condition is True, then execute indented code.
# If condition is False, then skip the block.

Age = 18

if Age >= 18:
    print("Eligible to Vote!")
else:
    print("Not Eligible!")

print("Program Ended!")

# Using comparison operators inside if

# Example: (positive/negative numbers)

num = 5

if num > 0:
    print("The number is positive!")
else:
    print("The number is negative!")

# Example (To check if the number is even or odd)

num = int(input("Enter the number please: "))

if num%2 == 0:
    print(f"{num} is even number.")
else:
    print("The number is odd!")


# Example (To check if the student is pass)

marks = int(input("Enter your marks please: "))

if marks >= 40:
    print("Pass")


# 3) if–else Statement:

# Why else is needed
# Use else when you want one of two paths to always run.

# Logic:
# IF condition is True THEN do this
# ELSE : do that

# Syntax:
# if condition:
#     code_if_true
# else:
#     code_if_false

# Flow of execution

# Python checks the if condition
# If True --> runs if block, skips else
# If False --> skips if, runs else

# Example : Pass / Fail

marks = 35

if marks >= 40:
    print("Pass")
else:
    print("Fail")

# Example: Login validation

password = "zeeson@123"

if password == "admin@123":
    print("Login Sucessfull")
else:
    print("Invalid Credential")