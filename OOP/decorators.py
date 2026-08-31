# Decorators

# Quick Revision for functions:
# ---> A function is a block of code that performs a specific task.
# ---> we write it once, and we can use it again and again.

# Simple Code Example:

def info():
    print("This is Zeeson.")
    
# Line-by-Line Explanation:
    # def -- keyword used to create a function
    # info -- function name
    # () -- parameters (empty)
    # : -- start of function body
    # print() -- what the function does

# Calling the Function:
info() 

# Why Functions Are Useful?

# Instead of writing same code again and again:
# Improper way:
print("Hello Zeeson")
print("Hello Zeeson")
print("Hello Zeeson")

# Proper way:
def greet():
    print("Hello Zeeson")
greet()
greet()
greet()

# This is called reusability.

# 2.) Functions as Objects

# In Python, functions are objects.
# Meaning:
# we can store them in a variable.
# we can pass them to another function.
# we can return them from function.

# a.) Part A – Assign Function to Variable:

def greet():
    print("Hello ZeesonGroot!")
    
x = greet
x()

# Explanation for this example:

    # def greet(): ---> creating a function
    # x = greet ----> we are not calling the function
    # we are storing the function inside variable x
    # x() now we call the function using x

# Important Note to Consider:

# x = greet() ---> this CALLS the function
# x = greet -----> this STORES the function

# b.) Part B – Passing Function as Argument:

def greet():
    print("Namaste!")

def call_function(func):
    func()
    
call_function(greet)

# Explanation:
# greet ----> a function
# call_func(func) -----> takes a function as input
# func() -----> executes the passed function
# call_func(greet) ----> passing function (NOT calling it)


# c.) Part C – Returning a Function from Another Function

def outer():                                         # Creating a function named outer
    def inner_function():                                  # Inside outer, we created another function called inner_function, also called nested function.
        print("Hello Python From Inner Function!")
    return inner_function                                # We are returning the function itself
    
x = outer()
x()

# Important:
# return inner ---> returns function.
# return inner() ----> calls the function first, then returns its result.

# 3.) Decorators:

# A decorator is a function that:
    # -takes another function as input
    # -adds some extra behavior
    # -without changing the original function

# Simple Example:

def decorator(func):      # This is a function named decorator.It takes another function as input i.e func. It becomes middle later
    def inner():                                  # This is a function inside decorator which will add extra behavior.
        print("Before the Function!")
        func()                               # Run original function i.e. func()
        print("After the Function!")
    return inner                              # We are returning the modified function (inner)

@decorator
def middle():               # it becomes like middle = decorator(middle)
    print("Middle of the Function")
    
middle()      # so now it internally becomes inner()

# 4.) Structure of Decorator

# Basic Structure:

def my_decorator(func):
    def inner_function():
        func()
    return inner_function

# Breaking it into 3 Parts:

# Part 1: Outer Function

# def my_decorators(func):

    # - This is the decorator function
    # - It takes another function as input (func)
    # - func = the function you want to modify

# Part 2: Inner Function

# def inner_function():

    # This is where we add extra behavior (Change/modify)

    # This function will:
    # - run extra code
    # - then call original function

# Part 3: Call Original Function

# func()

    # This runs the original function

    # Without this line:
    # original function will NEVER run

# Part 4: Return Inner Function

# return inner_function

    # - We return the modified version of function.
    # - This replaces the original function.
    
# Next Simple Code Example:

def decorator(func):                       # my_decorator takes a function as input. func = the function we pass i.e abc
    def inner_func():                      # This function will modify behavior
        for i in range(5):                 # This runs the function 5 times
            func()                         
    return inner_func                      # We return the modified function

@decorator
def abc():                                # Internally, it does, abc = my_decorator(abc)
    print("This is Zeeson Manandhar!")

abc()                        # Calling the function
abc()

# 5.) Manual vs @ Syntax

# @decorator is just a shortcut.

# Same thing can be written in 2 ways:

# Method-1 : Using @ (Shortcut)

@decorator
def xyz():
    print("Namaste! Greetings to you all")
xyz()

# Method-2: Manual Way
def greet():
    print("Hello From Python!")
    
greet = decorator(greet)
greet()

# What @decorator does?

@decorator
def efg():
    pass

# Python internally makes this:
# efg = decorator(efg)


# @decorator does NOT do magic
# It just rewrites code internally

# 6.) Why To Use Decorators?

# Main Purpose:
    # -To reuse code
    # -To avoid repeating same logic again and again 

# Problem Without Decorator:
# Example:

def greet():
    print("Before")
    print("Hello")
    print("After")

def bye():
    print("Before")
    print("Bye")
    print("After")

greet()
bye()

# Problem here is:
# - "Before" and "After" repeated 
# - Code becomes messy

# Solution with Decorator:

def my_decorator(func):
    def my_inner_function():
        print("Before!")
        func()
        print("After!")
    return my_inner_function

@my_decorator
def abc():
    print("Hello!")
abc()    

@my_decorator
def xyz():
    print("Bye!")
    
xyz()

# Now:
# - No repetition 
# - Clean code 
# - Easy to manage

# 8.) Static Method

# A static method is a function inside a class
# But it does NOT use self

# A method that belongs to a class but does not depend on object data.

# Basic Example:

class Student:               # Creating a class
    @staticmethod            # @staticmethod tells Python this method does NOT need self
    def std_info(): 
        print("Zeeson Manandhar")              # just prints output, No object data used

s1 = Student()
s1.std_info()

