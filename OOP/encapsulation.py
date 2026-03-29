# 1.) Encapsulation:

# Definition: Putting data and methods together inside a class, and controlling access by hiding sensitive data and only allowing safe access.

# Real-life analogy: ATM machine

# Think about an ATM.
# We use the ATM to:
    # check balance
    # withdraw money
    # deposit money
# But do we directly touch the bank’s internal system or change the balance ourself?
# No, We only use the allowed buttons/options.

# So:
# Balance = data
# withdraw() / deposit() / check_balance() = methods
# ATM hides internal system = encapsulation

# This is the main idea:
# we should not allow everyone to directly change important data.
# Instead, we give safe ways to use it.

# Why encapsulation is used?

# We use encapsulation because it helps us:

    # a.) Protect data
    # Some data should not be changed directly.

    # b.) Control access
    # We decide how data can be read or changed.

    # c.) Keep code safe and organized
    # Data and related methods stay in one place.

    # d.) Prevent wrong use
    # Users of the class do not directly change sensitive values.


# 2.) Public vs Private Concept:

# In Python, data can be:

    # A.) Public (Open to everyone)

    # Public data means:
        # Anyone can access it
        # Anyone can change it
        
# For Example:
# Case 1:
class Student:
    name = "Ram"

s1 = Student()
s1.name = "Zeeson" # modify
print(s1.name) # access

# This is public data

# Problem with Public Data:

class Bank:
    balance = 1000
    
b1 = Bank()

b1.balance = -5000   # wrong change
print(b1.balance)

# Wrong value
# No control
# Unsafe

    # B.) Private (Hidden / Restricted):
        # Private data means:
        # You should NOT access it directly
        # It is hidden for safety

# Like: 
b1.balance = -5000  # not allowed

# Understand it like: 
# Name ----> public 
# Password ---> private 

# 3.) Private Variables in Python

# Ways to make data private in Python:

# a.) Single Underscore (_variable):

# For Example:

class Student:
    _age = 22
    
# _age means:

# “This is internal data”
# “Please don’t access directly”

# Important:
# It is just a warning (convention)
# We can still access it

# Example:
s1 = Student()
print(s1._age)   # still works 

# b.) Double Underscore (__variable):

# For Example:

class Student:
    __age = 20

# Now:  
# s1 = Student()
# print(s1.__age)

# This will give error because Python hides the variable internally.
# This is also called Name Mangling.

# Very simple idea
# _age --> “please don’t touch”
# __age ---> “you really can’t touch directly”
