# Practice Questions for Day One: 

#  1. Print Statements

# Questions:

# a. Print your name.

print("Hey!!! its me Zeeson")

# b. Print your age.
print(22)

# c. Print any three sentences using separate print() statements.
print("The time right now is 3:30!")
print("And Today is December 1!")
print("Its so coldd")

# 2. User Input

# a. Ask the user for their favourite movie and print it.

choice = input("Enter your favourtite movie? ")
print(f"your favourite movie is {choice}")

# b. Ask the user for their city and print:
# eg: You live in <city>

choice = input("Enter your city? ")
print(f"you live in {choice}")

#  c. Ask for two words and print them together with a space.

name = input("Enter your Name: ")
age = input("Enter your Age: ")

result = (f"your Name is {name} and age is {age}")

print(result)

# d. Ask for your hobby and print:
# My hobby is: <hobby>

hobby = input("Enter your hobby: ")

print(f"My favourite Hobby is {hobby}")


# 4. Data Type Conversion (int / float)

# a. Ask the user for two numbers, convert them to int, and print the sum.

a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))

sum = a + b
print(sum)

# b. Ask for two decimal numbers (float) and print their multiplication.

c = float(input("Enter the first decimal number: "))
d = float(input("Enter the Second Decimal Number: "))

mul = c * d
print(mul)

# c. Take input "10" and "20" as strings—convert and print total 30.

a = "10"
b = "20"

result = int(a) + int(b)
print(result)

# 5. Type Casting

# a. Print the type of:

# 123

print(type(123))

# "Hello"

print(type("Hello"))

# 3.5

print(type(3.5))

# Take a user input and print what type it is (i.e. int or float or string).

val = input("Enter the number: ")
if "." in val and val.replace(".","",1).isdigit():
    val = float(val)
elif val.isdigit():
    val = int(val)
else:
    pass
print(type(val))

# 6. Mini Calculator Practice

# Ask the user for two numbers and show:

# addition

# subtraction

# multiplication

# division

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the Second Number: "))
add = num1+num2
subtract = num1-num2
multiply = num1*num2
div = num1/num2

print(f" Result for Addition: {add}\n Result for Subtraction: {subtract}\n Result for Multiplication: {multiply}\n Result for Division: {div}") # used escape sequence here i.e \n for breaking a line.

# Ask for two numbers and print only the average.
a = float(input("Enter the First Number: "))
b = float(input("Enter the Second Number: "))
avg = (a+b)/2
print(avg)