# 1.) Constructor:

# Definition: A constructor is a special method in OOP that automatically calls when an object is created.
# Simply, It is used to initialize (set up) the object with starting values.

# Why do we need Constructor actually?

# Without Constructor:
    # When we create object,it's empty
    # Then we manually assign values
    
# With Constructor:
    # Object is created with values already inside it
    
# So constructor helps to:
    # Save time
    # Make code clean
    # Ensure every object has proper data
    
# Simple Code without Constructor (Old Way):

# Example:

class Student:
    name = "std"
    age = 0
    
s1 = Student()
s1.name = "Zeeson Manandhar"
print(s1.name)
s1.age = 22
print(s1.age)

# Problem here:
# Object is created empty
# We assign values later (not efficient)

# Simple Code using Constructor (Better Way):

class Student:
    def __init__(self,name,age):
        self.Name = name
        self.Age = age

s1 = Student("Zeeson Manandhar",22)
print(f"Student Name = {s1.Name}")    # Student Name
print(f"Age = {s1.Age}")

# Now, Here:
# Object is created with values instantly
# Clean and professional

# Key Idea: 
# Constructor : “Automatic setup when object is created”   

# 2.) __init__ Method Basics:

# __init__ is the constructor method in Python.
# Syntax: def __init__(self):

# When does __init__ run?

# It runs immediately when we create an object.

# Very Simple Example:

class Example:                                   # Creating a class
    def __init__(self):                          # Defining constructor
        print("Constructor is Running!")        # this will execute automatically
        
e1 = Example()                                # Object is created → constructor runs automatically

# 3.) Creating Attributes using Constructor:

# Attribute is a variable that belongs to a class or object
# There are two types of attributes:
    # a.) Class Attribute (Shared) / Class Variable:
    
class Student:
    college_name = "XYZ College"
    
# This belongs to the class itself
# All objects share the same value 

    # b.) Object Attribute / Instance Variable (Created using constructor):

# self.name = name

# This belongs to each object separately
# Created inside __init__

# Real-Life Analogy

# Think of a college:
# All students ---> same college name ----> class attribute
# Each student ---> different name, age ---> object attributes

# Full Example Code:

class College:
    college_name = "ABC College"    # Class Attribute
    
    def __init__(self,name,age,address):
        self.Name = name                # Object Attribute
        self.Age = age                  # Object Attribute
        self.Address = address          # Object Attribute

s1 = College("Zeeson Manandhar",22,"Koteshwor-32")
s2 = College("Sunil Sah",23,"Jeetpur")

print(s1.college_name)
print(s2.college_name)

print(s1.Name)
print(s2.Name)
        