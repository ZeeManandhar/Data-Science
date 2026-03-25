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


# 3.) Syntax of Inheritance:

# Basic Syntax:

class Parent:
    pass
class Child(Parent):       # This means child class is inheriting from parent class
    pass

# For Example (Simple Code):

class Animal:                                         # We create a parent class
    def sleep(self):                                  # A method inside parent class
        print("Animal is Sleeping!")
        
class Dog(Animal):                  # Dog is a child class and it inherits from Animal
    pass

d1 = Dog()
d1.sleep()        # Even though Dog has no sleep() method,it can still use it because it inherited from Animal             


# 4.) Using Parent Attributes and Methods

# For Example:

class Animal:
    name = "Animal class Called!"           # Parent class has an attribute called name
    
    def walk(self):                             # Parent class has a method
        print("Animal moves here and there!")
        
class Dog(Animal):                              # Dog inherits everything from Animal
    pass

d1 = Dog()
print(d1.name)                                 # Child is accessing parent attribute
d1.walk()                                      # Child is using parent method


# Key Understanding
    # Child class can directly use:
    # -> Parent attributes 
    # -> Parent methods 
    # -> Even if child class has nothing inside it


# 5.) Adding Child-Specific Features

# A child class can add its own features in addition to inherited ones. 

# For Example:

class Animal:
    name = "Animal Class Called"
    
    def eat(self):
        print("Animal eats food!")
        
class Dog(Animal):
    def bark(self):                      # This is new method added by child class
        print("Dogs Barks!")
        
d1 = Dog()
d1.bark()
d1.eat()    

# 6.) Creating Objects of Child Class

# For Example:

class Animal:
    def eat(self):
        print("Animal eats food")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d1 = Dog()

# When we create a child object, it can access:
    # Parent methods 
    # Parent attributes 
    # Child methods 
    # Child attributes
    
# 7.) Types of Inheritance:

# There are 3 different types of Inheritance:

# a.) Single Inheritance:

# Here, child class inherits the attributes and methods from a single parent.
# One Parent ---> One Child

# For Example:

class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")
        
# b.) Multiple Inheritance:

# Here, child class inherits the attributes and methods from multiple parent classes.
# one child ----> multiple parents

# For Example:
class Father:
    def skill1(self):
        print("Driving Skill!")
        
class Mother:
    def skill2(self):
        print("Cooking Skill!")

class Child(Father,Mother):
    pass

c1 = Child()
c1.skill1()

# Child inherits from both Father and Mother

# c.) Multilevel Inheritance:

# Here, Child class inherits the attributes and methods from parent class and the parent class also inherits the arributes and methods from its parent class.
# Chain of inheritance

# For Example:

class Animal:
    def eat(self):
        print("Animal Eats")
        
class Dog(Animal):
    def bark(self):
        print("Dog Barks!")
        
class Puppy(Dog):
    def weep(self):
        print("Puppy Weeps!")
        
p1 = Puppy()
p1.eat()
p1.bark()
p1.weep()

# Understanding:
# Puppy ---> Dog -----> Animal
# Puppy gets features from BOTH.

# 8.) Method Overriding (Very Important)

# If a child class creates a method with the same name as the parent
    # The child method replaces the parent method.
    # This is called Method Overriding.