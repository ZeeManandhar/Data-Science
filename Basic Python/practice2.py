# Practice Question for Operators:

# 1. Write a program that calculates the area of a circle using:
# 𝜋r^2

radius = 7
PI = 3.14

area_of_circle = PI*radius**2
print(area_of_circle)

# 2. IF x=5 then
# Use assignment operators to update it:
# Add 5
# Multiply by 2
# Subtract 3
# Print the result after each step.

x = 5
x+=5
print(x)

x *= 2
print(x)

x -= 3
print(x)

# 3. Write a program that asks for two ages and prints:
# Is the first older?
# Are they equal?
# Is the second Older?

choice1 = int(input("Enter the First Child Age: "))
choice2 = int(input("Enter the Second Child Age: "))

if choice1 > choice2:
    print("First Child is actually Older!")
elif choice1 == choice2 :
    print("They both are of equal age!")
else:
    print("Second one is Older!")


# 4. Ask user for marks (0–100) and print:

# “Pass” if marks >= 40 and marks<=60 

# “Excellent” if marks > 60 and <= 100

# Otherwise “Fail”

marks = int(input("Enter your marks: "))

if marks >=40 and marks<=60 :
    print("You are pass!")

elif marks>60 and marks<=100 :
    print("Excellent")
else:
    print("You failed!")


# 5. Ask the user for a string and check:

# Does it contain the letter "a"?
# Does it contain "hello"? 

user = input("Enter the string: ")

if "a" in user:
    print("The string contains 'a'")
else:
    print("The string does not contain 'a'")

if "hello" in user:
    print("The string contains 'hello'")
else:
    print("The string does not contain 'hello'")

# 6. Write a program:

# Take a username list

# Ask user to enter their username

# Check if it exists using in

list1 = ["Zeeson123", "Sunildon","Chauhanbhai"]

username = input("Enter your Username Please: ")

if username in list1:
    print("Username Found !!")
else:
    print("Username not Found !!")



