# 1.) Abstraction:

# Abstraction simply means: Show only important things and hide unnecessary details.

# In very simple words
# - “Only what user needs to see”.

# Real-Life Examples:

# Example 1 – Car
# We drive car using:
    # steering
    # brake
    # accelerator

# But We DON’T see:
    # engine logic
    # internal wiring

# That is abstraction.

# Example 2 – ATM
# We insert card
    # enter PIN
    # withdraw money

# We DON’T see:
    # bank server
    # transaction processing

# That is abstraction


# Programming Meaning
# In Python:
# - User sees method
# - Hidden = how it is implemented

# Why We Use Abstraction?

# To:
    # hide complexity
    # show only necessary parts
    # make code clean
    # enforce rules
    
# Small Example:
def withdraw():
    print("Money withdrawn")
    
# User only sees:
# withdraw()
# Not how bank works internally

# In Conclusion, Abstraction = hide logic + show functionality.

# 2.) Abstract Method (Rule Concept)

# An abstract method is a method that:
    # has no complete implementation
    # acts like a rule
    # must be implemented by child classes

# In Simple Terms, “Abstract method is like a rule that every child must follow”.

# Real-Life Example:
# Think of it as a School Rule
# School says: “Every teacher must teach”
#  This is a rule
# But HOW they teach is different
    # - Math teacher : teaches math
    # - English teacher : teaches English

# Final Understanding:
    # -Abstract method does NOT do work
    # -It forces child class to do work
    

# 3.) ABC (Abstract Base Class)

# It is a special class used to:
    # create abstract methods
    # enforce rules on child classes

# Simple Definition: “A class that contains rules (abstract methods) for other classes”.

# Importing ABC:

from abc import ABC, abstractmethod

# ABC	---> base class for abstraction
# abstractmethod --->	used to define abstract methods

# Basic Structure with line-to-line explanation:

from abc import ABC, abstractmethod                     # importing tools for abstraction

class Parent(ABC):                                     # This is an abstract class. It inherits from ABC
    
    @abstractmethod                                    # This defines a rule. Must be implemented in child class
    def show(self):       
        pass                                           # Just placeholder

# Final Understanding:
    # ABC = base class with rules
    # abstractmethod = rule inside class
    
# 3.) Child Class Implementation

# If a child class inherits an abstract class, it must implement all abstract methods.

from abc import ABC, abstractmethod

class Teacher(ABC):
    
    @abstractmethod
    def teach(self):
        pass

# Here, Teacher says:
# Every child must have teach()

# Now for Child Classes:

class Math_Teacher(Teacher):
    def teach(self):
        print("I teach Math!")

# Creating the Object
m1 = Math_Teacher()
m1.teach()

# here,
# - MathTeacher followed the rule
# - It gave real logic for teach()

# Another Child Class:

class English_teacher(Teacher):
    
    def teach(self):
        print("Ï teach English!")

e1 = English_teacher()
e1.teach()

# - Same rule, different implementation

# Why This Is Powerful ?

# One parent rule:
    # teach()
    
# Many child versions:
# MathTeacher ----> teaches math
# EnglishTeacher ----> teaches english
# ScienceTeacher ----> teaches science


# Real-Life Analogy:
# Parent company says: “Every branch must open at 9 AM”
# Each branch follows rule differently:
# Branch A style
# Branch B style

# Final Understanding
# - Parent defines WHAT must exist
# - Child defines HOW it works

# Final Code Example:

from abc import ABC, abstractmethod                         # We import abstraction tools.

class Parent(ABC):                                      # Parent is an abstract class. It is used as a rule/template class.

    @abstractmethod                                     # This creates a compulsory rule: Every child class must have abcmethod()
    def abcmethod(self):
        print("This should be a part of every child class")

class Child1(Parent):                         # Child1 inherits all rules from Parent.

    def abcmethod(self):                                    # Child1 implements the required rule. This is called overriding.
        print("Abstract Method called from child class")

c1 = Child1()                         # Because child implemented abstract method.
c1.abcmethod()                       # Calling the method 
                  
# Important Understanding:
# Even though Parent had code inside abcmethod, Child1 still had to override it because it was marked @abstractmethod.

# Final Understanding:
# - @abstractmethod = compulsory rule
# - Child class must override
# -Then object creation is allowed

