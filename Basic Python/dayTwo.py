# Operators in Python:

# Operators are symbols that perform operations on values or variables.
# eg: 8+2 , where "+" is the operator and "8" and "2" are referred as operands


# 1. Arithmetic Operators

# These Type of Operations are used to perform Mathematical Operations (+-/*)

# Addition
print(5+8)

# Subtraction
print(5-2)

# Multiplication
print(3*8)

# Division
print(8/2)

# Modulus i.e. remainder

print(10 % 3) 

# Exponent (power):

print(5**5)

# 2. Assignment Operators:

# These type of operators are basically used to assign values to variables

#eg: x = 10, y += 10

# 1. Simple Assignment(=):
a = 4
# This stores 4 in variable a

# 2. Add and Assign(+=)

a = 8
a += 10    # i.e. a = a + 10
print(a)

# 3. Subtract and Assign (-=):

a = 10
a -= 5
print(a)

#4. Multiply and Assign(*=):

a = 15

a *= 5

print(a)

# 5. Divide and Assign (/=)

a = 10

a /= 2

print(a)

# Comparison Operators:

# Comparison operators are used to compare two values ie. They either returns True or False.

# 1. Greater than or equal (>=)

a = 10
print(a>=5)

# 2. Less than or Equal (<=)

a = 15
print(a<=16)

#3. Equal to (==)

a = 2
print(a==2)

# 4. Not equal (!=)

a = 5
result = a!=4
print(result)


# Note: "=" and "==" are not same.

# Logical Operators:

# are used to combine or modify comparison conditions, and the final result is always True or False.

# 1. and Operator:
# True only if BOTH conditions are True

a = 15
b = 10

result = a>b and b>5
print(result)


# 2. or Operator
# True if AT LEAST ONE condition is True
age = 15

output = age<18 or age>60
print(output)

# 3. not Operator

age = 18
final = not(age>10)
print(final)

# Identity Operator(is, is not):

# Identity operators check whether two variables refer to the same object in memory, not just the same value.

# In Python, everything is an object stored somewhere in memory.
# Identity operators compare the memory location, not just equality.

# There are two identity operators:

# 1. is operator:
# Checks if two variables point to the same object.
x = 8
y = 8
print(x is y)

# Important Note: Python stores small integers from -5 to 256 in the same memory location to save memory.

# 2. is not operator

# checks if they refer to different objects (different memory)

x =[1,2,3,4]
y = [1,2,3,4]

print(x is not y)

# Membership Operator(in, not in)

# Membership operators check whether a value exists inside a sequence such as:
# string
# list
# tuple
# set
# dictionary (keys by default)
# They return True or False.

# 1. in Operator

# Checks if a value is present inside a sequence.

# For String:
name = "zeeson"
result = "eez"in name

print(result)

# For list:

list1 = ["zeeson","sunil","niraj"]
check = "sunil" in list1
print(check)

# For Dictionary: 

dict_1 = {"name":"bella", "age": 4}

final = 4 in dict_1.values()
print(final)

# Note: Membership operators do NOT work with integers directly, because integers are treated as a single collection, not a container.

#2. not in Operator

# Opposite of in
# Returns True if the value is NOT found.

# For Strings:
name = "Zeeson"
output = "a" not in name
print(output)

# For lists:
sports = ["football","basketball","table tennis"]
final = "cricket" not in sports
print(final)

# 7. BITWISE OPERATORS (Final Operator Topic)

# Bitwise operators work on binary values (0s and 1s). 
# # very rarely used operator (almost never)




# Set
# Unordered grouped data type taht doesnot allow duplicates
# Set is wrapped with {}


set_one = {1,5,"Zeeson",7,8,"Manandhar"}
print(set_one)
print(type(set_one))

# Dictionary
# Comes in Key-value pair but is also warpped in {}

dict_one = {
    "name": "Zeeson",
    "lastname": "Surname",
    "age": 29,
    "marks": 85
}
print(dict_one.keys())
print(type(dict_one))


# Union in Sets

sports_one = {"football", "basketball","baseball"}
sports_two = {"football","Table tenis"}

result = sports_one.union(sports_two)
print(result)

# Create a list of username and take input from user and if it matches it

username = ["zeeson","ram","hari","syam"]
user = input("Enter your Username ?").lower()
if user in username:
    print("The user is Found")
else:
    print("Not Found!")


# Syntax of IF Else

#if conditions:
#     Statements
# else:
#      Statements


# Elif Ladder
# Elif ladder is used when you have multiple conditions

# Calculator using IF...ELSE with text choices

# Taking Input from User
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
if num2 != 0:
    div = num1 / num2 
else:
    div = "Cannot divide by zero"
    
print("Choose Operation: add, sub, mul, div")

choice = input("Enter your choice: ").lower()  

# Applying IF–ELSE 
if choice == "add":
    print("Result:", add)

elif choice == "sub":
    print("Result:", sub)

elif choice == "mul":
    print("Result:", mul)

elif choice == "div":
    print("Result:", div)

else:
    print("Invalid choice")


