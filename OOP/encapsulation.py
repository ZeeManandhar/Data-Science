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

# a.) Single Underscore (_variable) / Protected Variable:

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

# b.) Double Underscore (__variable) / Private Variable:

# For Example:

class Student:
    __age = 20

# Now:  
# s1 = Student()
# print(s1.__age)

# This will give error because Python hides the variable internally.
# This is also called Name Mangling.


# 4.) Accessing Private Data

# __variable is private
# Python hides it (name mangling)

class Student:
    __age = 55

s1 = Student()
# print(s1.__age)          Throws AttributeError: 'Student' object has no attribute '__age'

# When we write:
# __age
# Python changes it to:
# _Student__age

# So, here 
# We are asking for __age but Actual name is _Student__age.

# Important Concept here:
# --> Private variable is not removed
# ---> It is just hidden and renamed

# We can still acess it using:

print(s1._Student__age)

# This is not the proper way to access any data because: It breaks encapsulation
# It breaks encapsulation
# It is unsafe
# Not good practice

# Main Rule:
#  Never access private data directly
#  Always use methods 

# 5.) Getter Methods

# A getter is a method used to read (get) private data safely.
# We use getter to access data in a controlled way.

# Since We know:
# print(s1.__age)       throws error and  we cannot access the private data directly, so we use getter.

# For Example:

class Student:                           # Creating class
    __age = 15                           # Private variable (hidden)
    def getAge(self):                    # Method (getter)
        print(self.__age)                # Accessing private variable inside class
        
s1 = Student()
s1.getAge()

# Outside world cannot access __age directly But can access it through get_age().

# Simply, Getter = read private data safely

# 6.) Setter Methods
# A setter is a method used to change (set) private data safely.

# Without using setter:
class Amount:
    balance = 5000
    
a1 = Amount()
a1.balance = -2000
print(a1.balance)

# - No Control
# - Invalid Values Allowed

# Example using setter:

class Student:
    __age = 14        # private variable
    
    def std_info(self,new_age):    # setter method
        self.__age = new_age       # Updating values safely
            
s1 = Student()
s1.std_info(15)

# but here, in the above code: there is still a problem
s1.std_info(-5)          # Age cannot be in neagtive value.

# It is still allowing negative values.

# Example using Setter with proper Validation:

class Student:
    __age = 14
    
    def set_info(self,new_age):
        if new_age > 0:
            self.__age = new_age
            print(self.__age)
        else:
            print("Invalid Age!")
            
s1 = Student()
s1.set_info(10)

# 7.) Full Encapsulation Example

# Real-life Example: Bank Account
    # - Hide balance
    # - Read it using getter
    # - Update it using setter with rules
    
# Simple Code Example:

class Bank:
    __balance = 5000                # private data 
    
    def get_balance(self):         # getter method
        print(self.__balance)
        
    def add_balance(self,amount):     # setter method
        if amount > 0:                # validation
            print(f"Your New Balance is {self.__balance + amount}")
        else:
            print("Invalid Amount")       # prevents wrong value
            
b1 = Bank()
b1.get_balance()
b1.add_balance(5000)

# In Short, This shows:
    # Data is hidden 
    # Access is controlled 
    # Wrong values blocked   


# 8.) Data Hiding Concept:

# --> Data hiding means keeping important data hidden so it cannot be accessed or changed directly.
# --> Not everyone should access everything.

# Real-life examples:

# a.) Bank
# Balance should be hidden.
# Withdraw system should be allowed.

# b.) Login System
# Password should be hidden.
# Login Function is allowed.


# Why data hiding is important

    # a.) Security
    # Prevents misuse
    # Example:
    # No one can set balance = -10000

    # b.) Control 
    # Only allowed operations
    # Example:
    # Withdraw only if enough balance

    # c.) Prevent mistakes 
    # Avoid wrong data
    # Example:
    # Age cannot be negative

    # d.) Clean design 
    # User only sees what is needed


# Without data hiding:

b1.balance = -99999

# This breaks the System.

# With Data Hiding:
# b1.set_balance(-99999)   # Blocked


# 9.) Naming Convention in Python

# Python represents public, protected, and private data using naming convention.

# A.) Public Variable:

name = "Zeeson Manandhar"

# - No underscore
# - Fully open
# Accessing and Modifiying data are allowed here.

# B.) Protected Variable (_variable):

_age = 55

# Single underscore(_) used

# Meaning:
# “This is internal. Please don’t access it directly.”

# Still accessible But not recommended

# C.) Private Variable(__variable):

__age = 50

# Double underscore (__) used

# Meaning:
# “This is private. Do not access directly.”

# Direct access gives error and can be accessed via methods

# Simple Example:

# class Student:
#     __age = 20

# s1 = Student()
# print(s1.__age)   # throws error


# 10.) Private Methods in Python:

# A private method is a method that:
    # is used only inside the class
    # should not be called directly from outside
    
# Basic Syntax:
def __method(self):
    pass

# Double underscore (__) makes it private

# Simple Example:

class Bank:
    def __calculate_interest(self):
        print("Interest Calculated!")
        
    def show_interest(self):
        self.__calculate_interest()
        
b1 = Bank()
b1.show_interest()


# Name Mangling (same concept):
# __calculate_interest becomes _Bank__calculate_interest.

# Note
# Like private variables:
    # Can still be accessed using _ClassName__method
    # But NOT recommended
    
# Final Understanding:
# Private variable ---> hides data
# Private method -----> hides internal logic