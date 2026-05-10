# Magic Methods:

# Magic methods are special methods in Python.
# They start and end with double underscores.

# Some Examples of Magic Methods:

# __init__
# __str__
# __len__
# __add__

# They are also called dunder methods.

# Dunder means:
# double underscore

# So:

# __init__
# means:
# dunder init

# Magic methods are not usually called by us directly.
# Python calls them automatically in special situations.

# Example:
# print(obj)

# Python internally tries to call:
# obj.__str__()

# Simple Code Example:

class Student:                                           # We create a class named Student.
     
    def __str__(self):                                  # We create a magic method called __str__.
        return "I am a Student!"                        # This text will be returned when we print the object.

s1 = Student()                                          # We create an object of Student.
print(s1)                                               # Python internally does this: s1.__str__()


# 2.) Understanding __init__:

# - __init__ is a special method in OOP, also called Constructor, it initilize object data.

# Meaning:
# When an object is created, __init__ automatically gives values to the object.

# Simple Example:

class Student:                          # We create a class named Student.
    
    def __init__(self,name):            # This is the constructor magic method. Python automatically calls this when object is created.
        self.name = name                # Store value inside object.
        
s1 = Student("Zeeson Manandhar")        # Object is created.
print(s1.name)


# NOW VERY IMPORTANT:

# Python internally does this:

# s1 = Student()
# Student.__init__(s1, "John")


# VERY IMPORTANT

# You usually NEVER call __init__ yourself.
# Python calls it automatically during object creation.


# 3.) Understanding __str__

# __str is a special type of magic method and its job is to control how the object looks when printed.

# Basic Problem without using __str__():

class Car:
    name = "Toyota"
    
c1 = Car()
print(c1)

# This gives the memory location of the object and looks kind of confusing!

# Why?

# Because we did not tell Python:

# How object should appear when printed

# So Python shows default object information.

# Now, 

# Simple Code Example using __str__():

class Car:                         # Created Car class.
    
    def __str__(self):             # Magic method for string representation. Python automatically calls this during printing.
        return "Toyota"           # Return text to Python. __str__ MUST return a string.

c1 = Car()
print(c1)                    # Python internally does print(s1.__str__())

# Python expects:
# a string value
# from __str__. , That's why return is important.

# Example without return in __str__():

# class Student:

#     def __str__(self):
#         print("hello")

# s1 = Student()
# print(s1)

# This Gives Error! 

# 4.) Understanding __len__:
    
# Its job is:
# To Make custom objects work with len()


# Now Custom Object

# Example Without __len__:

# class Student:
#     pass

# s1 = Student()
# print(len(s1))               # This throws TypeError.

# Example using __len__():

class Student:

    def __len__(self):
        return 5

s1 = Student()
print(s1.__len__())


# 5.) Understanding __add__

# __add__ is a magic method.

# Its job is to control what happens when + is used
# This is called Operator Overloading.


# Now Custom Object

# Example Without __add__:

# class Number:
#     pass

# n1 = Number()
# n2 = Number()

# print(n1 + n2)

# This Gives Error!. because python doesnot know how to add these object as its class has no __add__.


# Solution using __add__:

class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(5)
n2 = Number(3)

print(n1 + n2)                            # n1.__add__(n2)


a = 5
b = 10 
c = 6
print(a.__add__(b).__add__(c))


# 6. Built-in Operators & Magic Methods Mapping

# Python converts normal operations into magic method calls internally.

# Main Concept

# We write a NORMAL code and Python secretly converts it into:
# magic method calls automatically.

# Example 1 using "+":

# We write:
a + b

# Python internally does:

print(a.__add__(b))

# Example 2 using "-"

# We write:
a - b

# Python internally:

print(a.__sub__(b))


# Example 3 using "*"

# We write:
a * b

# Python internally:

print(a.__mul__(b))

# Example 4 using len()

# We write:
# len(obj)

# Python internally:

# obj.__len__()


# THIS IS THE REAL MAGIC

# Python makes code look:
# simple and human-friendly

# But internally it runs:
# special magic methods


# 7.) Operator Overloading

# This is the BIG main concept behind magic methods.

# Very simple definition: Same operator behaving differently for different objects.


# Example 1 — Numbers:

print(5 + 3)

# Output:
# 8

# Here "+" means:
# addition

# Example 2 — Strings:

print("Hi " + "Bro")

# Output:
# Hi Bro

# Here same "+" means:
# joining strings

