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



