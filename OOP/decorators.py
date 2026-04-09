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
