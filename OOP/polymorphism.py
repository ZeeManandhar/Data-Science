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

