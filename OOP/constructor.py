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
        
# 4.) Passing Value to Constructor:

# passing values to contructor simply means giving data at the time of object creation.

# Real-Life Analogy
# Think of creating a bank account
# When we open an account, we provide:
# Name
# Balance
# That is exactly like passing values to constructor

# Simple Code Example:

class Laptop:                             # Creating class
    def __init__(self,brand):             # Constructor takes parameter brand
        self.brand = brand                # Store value inside object

l1 = Laptop("Dell")                       # What happens internally: Laptop.__init__(s1, "Zeeson") where, l1 = self and brand = Dell
print(l1.brand)   


# Important Concept to Remembre:
    # -The values inside () when creating object are called Arguments.
    # -The variables inside __init__ are called Parameters.

# 5.) Multiple Attributes:

# A constructor can store multiple values (attributes) inside an object

# Example:
# Think of a Student Profile
    # Each student has:
    # Name
    # Age
    # Course
    # So one object needs multiple attributes
    
class Student:                                    # Creating class
    def __init__(self,name,age,course):           # Constructor with 3 parameters
        self.name = name                          # Store name
        self.age = age                            # Store age
        self.course = course                      # Store Course

s1 = Student("Zeeson Manandhar",22,"Bsc.IT")
s2 = Student("Shyam Ghale",20,"BHM")

# Accessing Attributes:
print(s1.name)
print(s2.name)


# Key Note To Remember:
    # One object can store many attributes
    # Each attribute holds different data

# Important Rule:
#  Order of arguments must match parameters

# 6.) Constructor and Normal Method:

# Any function inside a class other than __init__ is a Normal Method.

# Example:
def std_info(self):     
    pass

# Full Code Example:

class Student:
    def __init__(self, name):
        self.name = name   # constructor

    def display(self):
        print(self.name)   # normal method

s1 = Student("Ram Shrestha")
s1.display()

# 7.) Default Values in Constructor

# We can give default values to parameters in constructor
# So even if user does not pass value, it will still work

# Basic Example:

class Student:
    def __init__(self,age,name = "Unknown"):          # name has a default value
        self.name = name
        self.age = age
        
s1 = Student(age = 22, name = "Zeeson Manandhar")     # overrides default
print(s1.name)

s2 = Student(age = 20)                                # uses default value, if no value is passed
print(s2.name)

# Important Rule:
# Default parameters must come after normal parameters

# 8.) Updating Values After Creation

# After creating an object, we can change (update) its attributes

# For Example:

class Student:
    def __init__(self, name):
        self.name = name

    def update_name(self, new_name):
        self.name = new_name

s1 = Student("Zeeson")
print(s1.name)   
s1.update_name("Sunil")
print(s1.name)   


# Attributes are not fixed
#  We can change them anytime using methods

