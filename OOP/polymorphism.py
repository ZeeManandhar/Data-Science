# Polymorphism:

# Word Meaning:
# Poly = many
# Morph = forms

# So:  Polymorphism = many forms

# One thing can behave in many different ways.

# In Python OOP:
# Same method name, different behavior
# That means many classes can have the same method name, but each class does different work.

# Real-Life Analogy

# Think of a button named start()

# Car start() ---- Engine starts
# Computer start() ----- System boots
# Game start() ---- Game opens

# Same name:
# start()

# Different result.
# This is polymorphism.

# Let us take an Example of it:

class Boy:
    def speak():
        print("Boy speaks...!")

class Dog:
    def speak():
        print("Dog Barks...!")

# Both have, speak() method, but the results are different. thus, this is called Polymorphism.


# Loop Polymorphism:

# One loop, many forms.

class Dog:
    def eat(self):
        print("Dogs eat Bones!")

class Boy:
    def eat(self):
        print("Boys eat Pizza!")
        
for x in [Dog(),Boy()]:
    x.eat()


# Line-by-Line Explanation:

# [Boy(), Dog()]

# This means:
# Create two objects and put inside list.

# Like:
# [boy_object, dog_object]

# Actually:
# Boy() = object of Boy class
# Dog() = object of Dog class

# So list contains objects.

# Now Loop Starts:

# for x in [Boy(), Dog()]:

# Meaning:
# Take one item from list and store in x

# Round 1
# First item is:
# Boy()

# So now:
# x = Boy()
# Now inside loop:
# x.eat()

# Since x currently stores Boy object:
# Boy().eat()
# So Python runs Boy class eat()

# Output:
# Boys eat Pizza!

# Round 2
# Second item is:
# Dog()

# Now:
# x = Dog()

# Then:
# x.eat()
# means:
# Dog().eat()

# Output:
# Dogs eat Bone!


# Inheritance Polymorphism (Method Overriding):

# Here, We Use Inheritance with Polymorphism

# Code Example with Explanation:

class Animal:                                       # Base class (parent).
    name = "Main Class"                             # Class Attribute
    def eat(self):                                  # Method Name
        print("Animals eat food!")                  # Default behavior.
        
class Dog(Animal):                                 # Child Class where Dog inherits from Animal.
    
    def eat(self):                                # Same Method Name Again, i.e. Method Overriding
        print("Dog eats Bone!")                   # Dog gives its own behavior.
        
# Now Object
d1 = Dog()
d1.eat()
print(d1.name)

# So, here:
# Python checks:
# Dog has its own eat(), if YES
# So it uses Dog’s method

# If Dog DID NOT have sound():
# Then Python would go to parent:
# Animal ----> eat()

# Key Idea:

# Same method:
# sound()

# Different behavior:
# Animal ----> "Animals eat food1"
# Dog -------> "Dogs eat bone!"

# This is polymorphism using inheritance.


# Built-In Polymorphism:

# Polymorphism is not only in classes.
# Python already uses it in built-in functions and operators.

# Example One:

len("Zeeson")
len([2,0,6,0])

# Explanation:
# here,
# "Hi" has length of 2.
# [1, 2, 3] has length length of 3.

# We know, we have used same function:
# len()
# thus, it shows different behavior depending on data. this is called polymorphism.

