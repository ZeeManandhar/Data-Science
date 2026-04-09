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

# Why Functions Are Useful
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

# This is called reusability