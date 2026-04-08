# Decorators
# Decorators are the special type of function that recieves a function as a argument and help in modifying the function
# Without changing the original function
# Decorator always contain a inner function => Inner function help in modification
#To use a decorator , we use @ as prefix and the name of decorator is written just above the another function.

# Code:





# Static Method
# Abstract Method


class Student :
     @staticmethod
     def abc():              #using this @staticmethod, we don't have to take self as a parameter in method/function
          print("ÄBC")

s1 = Student()
s1.abc()



# Abstract Method
# Abstract Method tells that if a parent class is inherited from ABC and has an abstract method, then any child class that inherits the parent class should have abstract method
# ABC = Abstract Base Class

from abc import ABC, abstractmethod

class Parent:
     name = "parent"

     def abcmethod(self):
          print("This should be a part of every child class")

class Child1(Parent):
     pass
c1 = Child1()
c1.abcmethod()