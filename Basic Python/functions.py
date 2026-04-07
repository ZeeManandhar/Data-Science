# 1. Functions

# A function is a block of code that:

# Has a name
# Does one specific task
# Can be used again and again
# In simple words, A function is a reusable piece of code.

# 1.1. Why Functions Are Needed:

# Code repetition
# Without functions, we have to repeat the same logic many times.
# Example (no function):

print("Hello User!")
print("Hello User!")
print("Hello User!")

# If later we want to change "Welcome" to "Hello" later, we must change it everywhere.

# using return
def welcome():
    return "Hello User!"

result = welcome()
print(result)

# using print inside function:

def welcome():
    print("Hello World!")

welcome()

# Use return when:
# The function produces data
# if we want to use that data later
# if we want to store it in a variable
# if we want to reuse it, modify it, or send it somewhere else

# Use print when:

# if we want to display something
# if we do not need the value again
# Output is final (just show on screen)


# 1.2 Real-Life Analogy

# Take Example of a washing machine:
# We put clothes (input)
# Machine washes (process)
# Clean clothes come out (output)

# A function works the same way:
# Input (optional)
# Logic inside
# Output (optional)

# 2. Types of Functions:

# 2.1 Built-In Functions:

# The functions which are provided by Python itself.

# Examples:

print("This is Zeeson Manandhar!")     # print returns NoNe
len([1,2,3])                           # len returns value
input("Enter your Name: ")             # input returns a string

# here, we donot define them, we just use them!!!

# 2.2) User-Defined Functions:

# The functions which we create ourself using def.

# For Example:

def student():
    data = input("Enter your Name: ")
    print(f"Hello {data}!")

student()
student()

# This is a valid user-defined, non-returnable function.


# 3. def Keyword & Function Syntax

# def means define a function.

def student1():
    print("Hello Student!")

student1()
student1()


# 3.1) Basic function structure (syntax)

def greet():
    print("Hello")


# here, 

# def -----> define
# greet ----> function name
# () -------> no inputs yet
# : --------> start of function body
# indented code -------> function logic


# 3.2) Indentation Rule:

# Everything inside a function must be indented

# def dog():
# print("Bark Bark!")                    # Wrong Way: This gives Indentation error.


def cat():
    print("Meow Meow!")

# Python uses indentation to know which code belongs to which function.


# 3.3) Function Naming Rules:

# Function names follow variable naming rules: 

# def greet_user():
# def add_numbers():

# These are valid.

# def greet user():   # space not allowed
# def 1greet():       # cannot start with number
# def for():          # keyword not allowed

# These are not valid.

# For Best practice:
# use lowercase
# use meaningful name
# use _ if needed

# 3.4) Important Concept To Memorize: defining a function is not running the function.

# Example:

def greet():
    print("Namaste!")

# This does nothing by itself.

# It runs only when called:
greet()


# 4.) Calling a Function

# Calling a Function basically means telling python to run the block of code inside the function.

# syntax to call a function: function_name()

# Example:

def bike():
    print("Boom Boom!")

bike()   #function call

# 4.1) Function Definition vs Function Call

# Function Definition / Declaration:

def car():
    print("Toyota!")

# Meaning:
# Instructions are stored
# Function is created
# Nothing runs yet


# Function Call:

car()

# Meaning:

# Python goes to the function
# Executes the code inside
# Comes back after finishing

# 4.2) Calling a Function Multiple Times

# Each call runs the function again.

car()
car()
car()

# 4.3) What if we don't call the Function:

def test():
    print("Python")

# here, 
# No output
# No error
# Function exists but never runs

# To Memorize: Functions run only when called using parentheses ()

# 5.) Non-Returnable Functions: 

# A non-returnable function is a function that doesnot return any value back. It cannot be reused.

def greet():
    print("Hello")

greet()

# This function returns nothing.

result = greet()
print(result)         # This gives None because it returned nothing to store in result variable!


# Rule to memorize: A function that has no return statement automatically returns None.

# 6.) Returnable Functions:

# A returnable function:

# Uses the return keyword
# Sends data back to the caller
# Allows the result to be stored and reused

def add(a,b):
    sum = a + b
    return sum

output = add(5,3)
print(output)

# 6.1) What return actually does

# return does two things:
# Sends a value back
# Stops the function immediately

def test():
    print("Start!")
    return
    print("Stop!")

test()

# The line after return never runs.

# 6.2) Storing returned values

# Returned values should be stored:

def add_num():
    return 2 + 3

x = add_num()
y = x + 10
print(y)

# 7.) Parameter and Arguments:

# 7.1.) Parameters:
# Parameters are variables inside the function definition.
# They receive values.

# For Example:

def food(name):
    print(f"The Food Name is {name}.")

food("Pizza")

# Here:
# name is the  parameter.

# 7.2) Arguments:

# Arguments are the actual values you pass when calling a function.

food("Burger")     # here, Burger ----> Argument

# Note: Parameters receive, while argument sends.

# 8.) Default Parameters:

# Default parameters are parameters that already have a value. Meaning: if no arguments are sent, it uses the default value.

def multiply(a=2,b=2):
    return a * b

print(multiply())   # Here, It uses Default parameters to multiply


print(multiply(a = 5, b = 2))   # Here, it overrides the default parameter.

# 8.1 Rule for default parameters (VERY IMPORTANT)

# Default parameters must come AFTER non-default parameters

# def subtract(a=5,b):
#     return a - b

# print(subtract(b=2))   

# This causes SyntaxError!

def subtract(a,b=2):
    return a - b

print(subtract(a=5))

# This is Valid.
# To Remember: default comes last
# Python checks function definitions FIRST, before any function calls.

# 9.) *args (Variable Arguments):

# 9.1) The problem *args solves

# So far, functions expect a fixed number of arguments.

def number(*a):
    return a

print(number(4,5,6))

# if we don't know how many values will be passed then *args is used.
# *args allows a function to accept any number of positional arguments.

# For Example:

def show(*args):
    print(args)

show(1,2,3,4,5,6) 

# 9.2 What exactly is args?

# Inside the function, args is a tuple.

def car(*name):
    print(type(name))

car("Toyota","Chevrolet","Suzuki")

# Thus, *args collects all extra positional arguments into a tuple.

# 9.3 Looping over *args:

# Since args is a tuple, you can loop over it.

def loop(*num):
    l1 = []
    for i in num:
        sqr = i**2
        l1 = l1 + [sqr]
    return l1

result = loop(1,2,3,4,5,6)
print(result)

# 9.4 One important rule:

# *args receives positional arguments only
# Order matters

def demo(a,*args):
    print(a)
    print(args)

demo(1,2,3,4,5)

# Note to keep in mind: *args packs multiple positional arguments into a tuple.


# *args must come AFTER all normal positional parameters
# and BEFORE keyword-only parameters
# For Example:

def demo1(a, *args, b):
    print(a)
    print(args)
    print(b)

demo1(2,4,5,6,b=7)

# Note: Any parameter written after *args MUST be passed using its name.

# 10. Keywords Arguments (**kwargs)

# since, we know *args handles positional arguments. 
# But what if we want to pass:
# named values
# key–value pairs
# unknown number of keyword arguments?

# **kwargs allows a function to accept any number of keyword arguments.

# Example:

def student(**values):
    return values

result = student(name = "Zeeson Manandhar", age = 22, address = "Koteshwor,KTM - 32")
print(result)

# Kwargs resolves in dictionary.

def check(**data):
    return data

output = check(a = 1, b = 2)
print(type(output))

# **kwargs packs keyword arguments into a dictionary.

def bike_specs(name = "Ns200",**values):
    return name , values

result = bike_specs(brand = "Bajaj", made = 2012, cc = 200)
print(result)

# 10.1) Accessing values from **kwargs:

def flowers(**values):
    return values

result = flowers(red = "rose",white = "lily", yellow =  "sunflower", purple = "lavender")
print(result["red"])
print(result["purple"])

# 10.2) Looping over **kwargs:

# since, it is dictionary, we must use keys.

def mountains(**height):
    for key,value in height.items():
        print(f"key = {key}, value = {value}")

mountains(Everest=8848, k2 = 8611, Lhotse = 8516 )


# 11.) Combining *args and **kwargs Together

# Some functions need to accept:
# any number of positional arguments
# any number of keyword arguments

# 11.1) Correct Order to Follow When combining both *args and ** kwargs:

# The only valid order is:

# normal parameters -----> *args --------> **kwargs

def demo(a, *args, **kwargs):
    print("a = ", a)
    print("args = ", args)
    print("kwargs = ", kwargs)

demo(1,2,3,4,5,6, x = 7, y = 8)

# 11.2) Mistakes to Avoid:

# def test(**kwargs, *args):      # Wrong Order

# Positional argument after keyword:
# show(name="Ram", 5)


# Note:
# *args collects extra positional arguments,
# **kwargs collects extra keyword arguments. 

# 12. Lambda Functions:       
#
# A lambda function is a small, anonymous (nameless) function written in one line.      

# Normal Function Example:

def add(a, b):
    return a + b

# Using Same Logic with Lambda function:
 
add = lambda a,b: a+b
print(add(5,6))

# 12.1) Basic lambda syntax:

# lambda parameters : expressions

# 12.2) Important rules of lambda

# A lambda function:
# Has no name (unless we assign it)
# Can have any number of arguments
# Can have ONLY ONE expression
# Automatically returns the result

# Cannot contain:
# loops
# multiple statements
# return keyword

# Example Two:

square = lambda x : x**2
print(square(2))

# 12.3) When to use lambda 

# Use lambda when: 
# Logic is very small 
# Used once 
# Passed to another function (like map, filter)

# 12.4) When NOT to use lambda

# Do NOT use lambda when:
# Logic is complex
# Multiple steps are needed
# Readability matters


# 12.5) Immediate Invocation (printing the result without using variable in lambda function)

# We wrap the lambda in parentheses and call it:

print((lambda x,y:x*y)(2,3))

# Step-to-Step Walkthrough:

# (lambda x,y:x*y) ---> This creates the Function
# (2,3) -------> This calls the function
# Result 6 is returned automatically.
# Print() displays it


# Next Example:
(lambda : print("Hello User!"))()

# same logic using variable:

say_hello = lambda: print("Hello")
say_hello()

# More Alternative Ways to do it:
(lambda name: print(name))(name="hello zeeson")

# 13.) Map() Function:

# map():
# takes a function
# takes an iterable (like list)
# applies the function to each element
# returns a map object

# BASIC SYNTAX FORM: map(function, iterable)


# Example Without Map():

num1 = [2,4,6,8,10]
sqr = []

for n in num1:
    output = n**2
    sqr.append(output)

print(sqr)

# Same Logic Using Map() Function:

def square(x):
    return x**2

num = [2,4,6,8,10]
result = map(square, num)

print(list(result))             # map returns map object, so we use list


# Same Example using lambda Function 

num = [2,4,6,8,10]

output = map(lambda x: x**2, num)
print(list(output))

# Note: Map() is cleaner for small logic.

# To Understand:  map() applies a function to every element of an iterable.

# 14.) reduce() Function:

# reduce():
# takes a function
# takes an iterable
# applies the function cumulatively
# returns one final value

# Examples:
# sum of numbers
# product of numbers
# maximum value
# cumulative result


# reduce() is not built-in by default.
# We must import it.

from functools import reduce

# Basic Form of Reduce(): reduce(function, iterable)

# Simple Example without using reduce():

number = [2,4,6,8]

sum = 0
for i in number:
    sum = sum + i
print(sum)

# Same Logic using Reduce: 

number = [2,4,6,8]

result = reduce(lambda a,b: a + b, number)
print(result)

# using def function:

def add(a,b):
    result = a + b
    return result

number = [2,4,6,8]

output = reduce(add, number)
print(output)

# a always stores the accumulated result  (Accumulated value = total so far)
# b always takes the next list value

# Most Important Rule To Keep in Mind: reduce() always works with TWO values at a time e.g. x,y.


# 15.) Zip function

# Sometimes you have multiple lists and you want to:
# combine them element by element
# treat corresponding items together

# zip():
# takes two or more iterables
# pairs elements by position
# returns a zip object

# Example:

# names = ["Ram", "Sita", "Hari"]
# ages  = [20, 22, 25]

# zip returns this as:

# Basix Form of Zip(): zip(iterable1, iterable2, ...)

# Simple Example:

std = ["Zeeson","Sunil","Niraj","Aman"]
age = [22,21,23,23]

result = zip(std,age)
print(list(result))

# 15.1) What Zip Function Does Internally?

# zip() pairs elements one by one:

# 1st pair --> (names[0], ages[0])
# 2nd pair ---> (names[1], ages[1])
# 3rd pair ----> (names[2], ages[2])

# Index-based pairing

# 15.2) What if Lists are of Different Lengths?

# zip() stops at the shortest list.

# Example:
a = [1,2,3,4,5,6]
b = [7,8,9]

data = zip(a,b)
print(list(data))

# Remaining elements are ignored.

# 15.3) Looping over Zip()

names = ["Steph","Lebron","Giannis","Victor"]
age = [38,41,29,23]

for name, age in zip(names,age):
    print(f"{name} --> {age}")


# 15.4 Zipping more than two lists

ids = [1, 2, 3]
names = ["Ram", "Sita", "Hari"]
cities = ["KTM", "PKR", "BKT"]

print(list(zip(ids, names, cities)))

# To Memorize: zip() combines multiple iterables element-wise into tuples.

# 16.) When to use what?

# 16.1 Normal Function (def) vs Lambda

# Use normal function (def) when:
# Logic is more than 1 line
# want readability
# will reuse the function
# building real programs

# Example:

def calculate_total(prices):
    total = 0
    for p in prices:
        total += p
    return total

# Use lambda when:

# Logic is very small
# One-line expression
# Used once
# Passed into another function

# Example:

list(map(lambda x: x * 2, [1, 2, 3]))

# Mini-Project Practice:

# Practice one: Menu-driven calculator

def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    if b == 0:
        return "Cannot be Divided by 0"
    else:
        return a/b
    
def calculator(choice,a,b):
    if choice == 1:
        return addition(a,b)
    elif choice == 2:
        return subtraction(a,b)
    elif choice == 3:
        return multiplication(a,b)
    elif choice == 4:
        return division(a,b)
    else:
        return "Invalid Option!"
    
result = calculator(4,10,5)
print(result)

# Here, we used to the concept of functional delegation.

# Functional delegation means:
# One function does not perform all the work by itself.
# Instead, it delegates (hands over) specific tasks to other functions.

# Functional Delegation: One function assigns parts of its work to other functions.
                                 
# Practice Two: Login System Using Functions

credentials = {
    "ZeeGroot":"Zeeson123#",
    "Dalli1":"Dalli123#"
}

def login(username,password):
    if username in credentials and credentials[username] == password:
        return "Login Sucessfull!"
    else:
        return "Invalid Credentials!"

result = login("ZeeGroot","Zeeson123#")
print(result)

