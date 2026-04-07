# Constructor -- Practice Questions:

# A.) BASIC LEVEL (1–7):

# 1.) Write a class Student with a constructor that stores name. Create an object and print the name.

class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Zeeson Manandhar")
print(s1.name)
    
# 2.) Write a class Car with a constructor that stores brand and price. Create an object and print both values.

class Car:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

c1 = Car("BMW","$50000")
print(c1.brand)
print(c1.price)

# 3.) Write a class User with a constructor that stores username. Print the username using the object.

class User:
    def __init__(self,username):
        self.username = username

u1 = User("ZeesonGroot")
print(u1.username)

# 4.) Write a class Book with a constructor that stores title. Create two objects with different titles and print both.

class Book:
    def __init__(self,title):
        self.title = title
        
b1 = Book("Python-Basics(2025)")
print(b1.title)

b2 = Book("Machine Leraning Revised")
print(b2.title)

# 5.) Write a class Mobile with a constructor that stores model and price. Print both attributes.

class Mobile:
    def __init__(self,model,price):
        self.model = model
        self.price = price

m1 = Mobile("Samsung M31F",30000)
print(m1.model)
print(m1.price)

# 6.) Write a class Animal with a constructor that stores name. Create one object and print the name.

class Animal:
    def __init__(self,name):
        self.name = name
        
a1 = Animal("Dog")
print(a1.name)

# 7.) Write a class City with a constructor that stores city_name. Create an object and print it.

class City:
    def __init__(self,city_name):
        self.city_name = city_name
        
c1 = City("Bhaktapur")
print(c1.city_name)
        

# B) INTERMEDIATE LEVEL (8–14):

# 8.) Write a class Student with a constructor that stores name and age. Add a method display() to print both.



# 9.) Write a class BankAccount with a constructor that stores name and balance. Add a method deposit(amount) to update balance.


# 10.) Write a class Employee with a constructor that stores name and salary. Add a method show_details() to print both.


# 11.) Write a class Laptop with a constructor that stores brand and price. Add a method discount(amount) to reduce price.



# 12.) Write a class UserProfile with a constructor that stores username and email. Add a method change_email(new_email).



# 13.) Write a class Product with a constructor that stores name and price. Add a method increase_price(amount).


# 14.) Write a class Course with a constructor that stores course_name and duration. Add a method show_course().



# C.) ADVANCED LEVEL (15–20):

# Write a class Student with a constructor that stores name and marks. Add a method add_marks(extra) to increase marks.



# Write a class BankAccount with a constructor that stores name and balance. Add two methods: deposit(amount) and withdraw(amount).


# Write a class Car with a constructor that stores brand and price (default price = 1000000). Create two objects (one with default price).



# Write a class Employee with a constructor that stores name, salary, and department. Add a method to update salary.



# Write a class User with a constructor that stores username and password. Add a method change_password(new_password).



# Write a class LibraryBook with a constructor that stores title and author. Add a method display_info() to print both.