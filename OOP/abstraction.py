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
    
