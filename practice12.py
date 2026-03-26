# Inheritance (Practice Questions):

# Level 1 – Basics

# 1.) Create a class Animal with a method eat() that prints "Animal eats".

class Animal:
    def eat(self):
        print("Animal eats")
        
a1 = Animal()
a1.eat()

# 2.) Create a class Dog that inherits from Animal, create an object, and call eat().

class Animal:
    def eat(self):
        print("Animal Eats Food")

class Dog(Animal):
    pass

d1 = Dog()
d1.eat()


# 3.) Add a method sleep() in Animal, then call both eat() and sleep() using a Dog object.

class Animal:
    def sleep(self):
        print("Its Sleeping!")
        
    def eat(self):
        print("Its Eating!")
class Dog(Animal):
    pass
        
d1 = Dog()
d1.eat()
d1.sleep()


# 4.) Create a class Vehicle with method start(), then create a child class Car and call start().

class Vehicle:
    def start(self):
        print("Engine Turning On!")
        
class Car(Vehicle):
    pass

c1 = Car()
c1.start()


# 5.) Create a class Person with attribute name = "Unknown", then create a child class Student and print name.

class Person:
    name = "Unknown"
    
class Student(Person):
    pass

s1 = Student()
print(s1.name)


# Level 2 – Using Parent Features
# Create a class Animal with attribute type = "Living" and access it using a Dog object.
# Create a class Vehicle with method stop() and call it using a Bike object (child class).
# Create a class Bird with method fly() and call it using a Parrot object.
# Create a class Shape with method draw() and call it using a Circle object.
# Create a class Device with method power_on() and call it using a Mobile object.
# Level 3 – Adding Child Features
# Create a class Animal with method eat() and a class Dog that adds method bark(), then call both methods.
# Create a class Vehicle with method start() and a class Car that adds method drive(), then call both.
# Create a class Person with method show() and a class Teacher that adds method teach(), then call both.
# Create a class Phone with method call() and a class SmartPhone that adds method camera(), then call both.
# Create a class Employee with method work() and a class Manager that adds method manage(), then call both.
# Level 4 – Method Overriding
# Create a class Animal with method sound() that prints "Animal sound", then override it in Dog to print "Dog barks".
# Create a class Vehicle with method move() that prints "Vehicle moves", then override it in Car to print "Car runs fast".
# Create a class Person with method role(), then override it in Student with a different message.
# Create a class Shape with method area(), then override it in Circle with a different message.
# Create a class Account with method info(), then override it in SavingsAccount with a different message.
# Level 5 – Using super()
# Create a class Animal with method eat(), then override it in Dog and use super() to call both parent and child methods.
# Create a class Vehicle with method start(), then override it in Car and use super() to call both methods.
# Create a class Person with method show(), then override it in Student and use super().
# Create a class Employee with method work(), then override it in Manager using super().
# Create a class Device with method power_on(), then override it in Laptop and use super().
# Level 6 – Types of Inheritance
# Create a single inheritance example with Animal → Dog including methods eat() and bark().
# Create a multilevel inheritance example with Animal → Dog → Puppy and call all methods.
# Create a multiple inheritance example with Father → drive(), Mother → cook(), and Child inheriting both, then call both methods.
# Create classes A and B with method show(), then create class C(A, B) and call show() to observe MRO.
# Create a multilevel inheritance example Person → Employee → Manager, override a method in Manager, and use super().