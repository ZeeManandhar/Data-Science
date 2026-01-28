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


# 4) if–elif–else Chain (Multiple Conditions)

# Sometimes there are more than two possibilities

# Example:
# Marks can be A, B, C, or Fail
# Traffic light can be Red, Yellow, or Green
# Menu choice can be 1, 2, 3, or Exit

# Syntax of if–elif–else:

# if condition_1:
#     code
# elif condition_2:
#     code
# elif condition_3:
#     code
# else:
#     code

# Rules:
# if : must come first
# elif : can be many
# else : optional, only one, always last

# Example 1:

choice = int(input("Enter the option to choose: "))

if choice == 1:
    print("Burger")
elif choice == 2:
    print("MOMO")
elif choice == 3:
    print("Pizza")
else:
    print("Option not Found!")


# Example 2: 

marks = 72

if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")

# 5) Membership Conditions — using in

# A membership condition checks whether something exists inside something else.

# It returns:

# True → item exists
# False → item does not exist

# in with a list

names = ["Zeeson","Dalli","Kaley"]

print("Kaley" in names)

if "Zeeson" in names:
    print("Item Available!")
else:
    print("Not Available!")

# in with a string

str1 = "I am a Developer!"

print("Developer" in str1)
print("Python" in str1)

if "@" in "admin@gmail.com":
    print(True)


# in with a dictionary

# Rule: in checks keys, not values (For Example)

students = {
    "Name" : "Ram Bahadur",
    "Age": 25,
    "Address": "Koteshwor"
}

if "Name" in students:
    print("Found!")
else:
    print("Not Found!")

# To check if the value exists or not:

if "Ram Bahadur" in students.values():
    print("FOUND")
else:
    print("NOT FOUND!")

# Quick Practice:

# to check if username exists:

username = input("Enter your Username: ")

users = ["admin123","Zeesondon1","Dallibhuntu1"]

if username in users:
    print("User Found!")
else:
    print("User not Found!")

# 6) Logical Operators — and, or, not

# Logical operators are used to combine conditions.
# They always work with True / False.

# and Operator:

# Both conditions must be True
age = 10

if (age >= 18 and age <= 60):
    print("Can Proceed!")
else:
    print("Cannot Proceed!")

# or operator:
# At least one condition must be True

day = input("Enter the day: ")

if day == "Saturday" or day == "Sunday":
    print("Holiday!")
else:
    print("Not Holiday!")


# not operator

# Reverses the result

is_active = False

if not is_active:
    print("Please Proceed")