# Magic Methods Practice Questions

# BASIC LEVEL (1–10)

# 1.) Write a program to create a class Student using __init__ to store student name and print the name.

class Student:
    
    def __init__(self,name):
        self.name = name

s1 = Student("Zeeson Manandhar")
print(s1.name)


# 2.) Write a program to create a class Car using constructor to store car brand and print it.

class Car:
    
    def __init__(self,brand):
        self.brand = brand

c1 = Car("Hyundai")
print(c1.brand)


# 3.) Write a program to create a class Teacher and use __str__ to return "This is Teacher Object".

class Teacher:
    def __str__(self):
        return "This is Teacher Object"

t1 = Teacher()
print(t1)

# 4.) Write a program to create a class Animal and use __str__ to return "Lion Animal" when object is printed.

# 5.) Write a program to create a class Box and use __len__ to return 5.

# 6.) Write a program to create a class Classroom and use __len__ to return total students as 30.

# 7.) Write a program to create a class Number and overload + operator using __add__ to add two objects.

# 8.) Write a program to create a class Money and add two money objects using __add__.

# 9.) Write a program to create a class Marks and subtract two objects using __sub__.

# 10.) Write a program to create a class Item and multiply two objects using __mul__.



# INTERMEDIATE LEVEL (11–20)


# 11.)  Write a program to create a class Book using __str__ to display book name and __len__ to return total pages.

# 12.)  Write a program to create a class BankAccount and overload + operator to add balances of two accounts.

# 13.)  Write a program to create a class Distance and overload - operator to subtract distances.

# 14.)  Write a program to create a class Product and overload * operator to multiply quantity and price.

# 15.)  Write a program to create a class Sentence and use __len__ to return total characters in a sentence.

# 16.)  Write a program to create a class Movie and use __str__ to display movie title.

# 17.)  Write a program to create a class Salary and overload + operator to add salaries of two employees.

# 18.)  Write a program to create a class Temperature and overload - operator to find temperature difference.

# 19.)  Write a program to create a class Vector and overload + operator to add vector values.

# 20.)  Write a program to create a class ShoppingCart and use __len__ to return total items in cart.


# ADVANCED LEVEL (21–30)


# 21.)  Write a program to create a class Student and overload + operator to add marks of two students.

# 22.)  Write a program to create a class BankAccount and overload + operator to combine account balances and return a new object.

# 23.)  Write a program to create a class Vector and overload +, -, and * operators.

# 24.)  Write a program to create a class Library and use __len__ to return total books.

# 25.)  Write a program to create a class Employee and use __str__ to display employee details.

# 26.)  Write a program to create a class Calculator and overload arithmetic operators for custom objects.

# 27.)  Write a program to create a class Wallet and overload + operator to combine money from multiple wallet objects.

# 28.)  Write a program to create a class CartItem and overload * operator to calculate total price using quantity and rate.

# 29.)  Write a program to create a class Team and use __len__ to return total players in team.

# 30.)  Write a program to create a class Result and combine polymorphism with magic methods by overloading operators differently for different objects.