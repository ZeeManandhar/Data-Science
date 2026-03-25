# 1.) Inheritance:

# In simple term, Inheritance is a way for one class to take features from another class.

# Assume it Like:
    # A parent class has some common features
    # A child class can reuse those features
    # The child can also add its own new features later
    
# Simple definition:

# Inheritance means:
    # A new class can use the data and methods of an existing class.
    # So instead of writing the same code again and again, we can reuse it.
    
# Real-life analogy

# Take an example of:

# Animal = general class
# Dog = specific class

# A dog is an animal.
# So if Animal has common things like:
# eating
# sleeping
# moving

# Then Dog can use those too, because a dog is already an animal.
# And later, Dog can also have its own special thing like:
# barking

# So:
# Animal = common features
# Dog = common features with its(+) special dog features


# Why inheritance is used

# Inheritance is used because it helps us:

    # a. Reuse code

    # If many classes share the same features, we do not need to rewrite them.

    # b. Save time

    # Write common logic once in the parent class, then use it in child classes.

    # c. Keep code organized

    # Common things stay in one place, special things go in child classes.

    # d. Make programs easier to manage

    # If you update the parent class, child classes can benefit from it too.


# 2.) Parent Class and Child Class

# What is a Parent Class?

# A parent class (also called base class) is: The class that provides common features (data & methods)
# It is like a source of properties.

# FOR EXAMPLE (CODE):

class Animal:
    def eat(self):
        print("Animal eats food")
        
# Here:
# Animal is the parent class.
# It has a method eat().

# What is a Child Class?

# A child class (also called derived class) is: The class that inherits from the parent class

# It gets:
# parent’s methods
# parent’s attributes

# For Example(code):

class Dog(Animal):
    pass

# Here:
# Dog is the child class
# It inherits from Animal

# Note (IMPORTANT):

# Child class:
# can use parent features 
# can add new features 
# can later modify features

# Memorize:
# Parent --> gives features
# Child ---> takes + uses + extends
