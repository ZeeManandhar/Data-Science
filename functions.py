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



