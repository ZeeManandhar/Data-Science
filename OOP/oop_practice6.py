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

class Animal:
    
    def __str__(self):
        return "Lion Animal"

a1 = Animal()
print(a1)


# 5.) Write a program to create a class Box and use __len__ to return 5.

class Box:
    def __len__(self):
        return 5

b1 = Box()
print(len(b1))

# 6.) Write a program to create a class Classroom and use __len__ to return total students as 30.

class Classroom:
    
    def __len__(self):
        return 30

c1 = Classroom()
print(f"Total Students : {len(c1)}")

# 7.) Write a program to create a class Number and overload + operator using __add__ to add two objects.

class Number:
    
    def __add__(self, other):
        add_obj = self.value + other.value
        return add_obj

n1 = Number()
n1.value = 50

n2 = Number()
n2.value = 70

print(n1+n2)


# 8.) Write a program to create a class Money and add two money objects using __add__.

class Money:
    def __add__(self, other):
        add_obj = self.value + other.value
        return add_obj

m1 = Money()
m1.value = 20

m2 = Money()
m2.value = 30

print(m1+m2)


# 9.) Write a program to create a class Marks and subtract two objects using __sub__.

class Marks:
    def __sub__(self, other):
        return self.value - other.value

mrk1 = Marks()
mrk1.value = 82

mrk2 = Marks()
mrk2.value = 45

print(mrk1 - mrk2)


# 10.) Write a program to create a class Item and multiply two objects using __mul__.

class Item:
    
    def __mul__(self,other):
        return self.value * other.value

i1 = Item()
i1.value = 9

i2 = Item()
i2.value = 10

print(i1*i2)


# INTERMEDIATE LEVEL (11–20)

# 11.)  Write a program to create a class Book using __str__ to display book name and __len__ to return total pages.

class Book:
    
    def __str__(self):
        return "Python Programming(2026)"
    
    def __len__(self):
        return 215

b1 = Book()
print(f"Book Name : {b1}")
print(f"Total Pages : {len(b1)}")


# 12.)  Write a program to create a class BankAccount and overload + operator to add balances of two accounts.

class BankAccount:
    
    def __init__(self,value):
        self.value = value
    
    def __add__(self, other):
        return self.value + other.value

b1 = BankAccount(5000)
b2 = BankAccount(4000)

print(b1 + b2)

# 13.)  Write a program to create a class Distance and overload - operator to subtract distances.

class Distance:
    
    def __init__(self,value):
        self.value = value
        
    def __sub__(self, other):
        return self.value - other.value
    
d1 = Distance(15)
d2 = Distance(9)

print(d1-d2)


# 14.)  Write a program to create a class Product and overload * operator to multiply quantity and price.

class Product:
    def __init__(self,amount):
        self.amount = amount
    
    def __mul__(self, other):
        return self.amount * other.amount

p1 = Product(50)
p2 = Product(20)

print(p1*p2)

# 15.)  Write a program to create a class Sentence and use __len__ to return total characters in a sentence.

class Sentence:
    def __init__(self,words):
        self.words =  words
    
    def __len__(self):
        return len(self.words)

s1 = Sentence("I am a Data Scientist!")
print(len(s1))


# 16.)  Write a program to create a class Movie and use __str__ to display movie title.

class Movie:
    def __init__(self,title):
        self.title = title
    
    def __str__(self):
        return self.title

m1 = Movie("Machine Learning(2025)")
print(m1)

# 17.)  Write a program to create a class Salary and overload + operator to add salaries of two employees.

class Salary:
    def __init__(self,salary):
        self.salary = salary
    
    def __add__(self, other):
        return self.salary + other.salary

s1 = Salary(45000)
s2 = Salary(40000)

print(s1+s2)

# 18.)  Write a program to create a class Temperature and overload - operator to find temperature difference.

class Temperature:
    
    def __init__(self,temp):
        self.temp = temp 
    
    def __sub__(self, other):
        return self.temp - other.temp

t1 = Temperature(89)
t2 = Temperature(60)

print(t1 - t2)

# 19.)  Write a program to create a class Vector and overload + operator to add vector values.

class Vector:
    
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return self.value + other.value

v1 = Vector(10)
v2 = Vector(20)

print(v1 + v2)

# 20.)  Write a program to create a class ShoppingCart and use __len__ to return total items in cart.

class ShoppingCart:
    
    def __init__(self, total_items):
        self.total_items = total_items
    
    def __len__(self):
        return self.total_items

sc1 = ShoppingCart(125)

print(len(sc1))


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