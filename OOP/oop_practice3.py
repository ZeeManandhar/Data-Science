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

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Student Name = {self.name}")
        print(f"Student Age = {self.age}")
        
s1 = Student("Salman Khan",30)
s1.display()
    
# 9.) Write a class BankAccount with a constructor that stores name and balance. Add a method deposit(amount) to update balance.

class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance = self.balance + amount
        return f"Your Current Balance is {self.balance}"
    
b1 = BankAccount("Zeeson Manandhar",5000)
print(b1.name)
print(b1.balance)
print(b1.deposit(1000))

# 10.) Write a class Employee with a constructor that stores name and salary. Add a method show_details() to print both.

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def show_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: {self.salary} ")
    
e1 = Employee("Mukesh Ambani",50000000)
e1.show_details()

# 11.) Write a class Laptop with a constructor that stores brand and price. Add a method discount(amount) to reduce price.

class Laptop:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    def discount(self,amount):
        self.price = self.price - amount
        print(f"Your Final Price is: {self.price}")

l1 = Laptop("Nitro V16",145000)
print(l1.brand)
l1.discount(3000)

# 12.) Write a class UserProfile with a constructor that stores username and email. Add a method change_email(new_email).

class UserProfile:
    def __init__(self,username,email):
        self.username = username
        self.email = email
    def change_email(self,new_email):
        self.email = new_email
        
u1 = UserProfile("ZeesonMdr1","zeeson_manandhar12@gmail.com")
print(u1.username)
print(u1.email)

u1.change_email("Zeeson.manandhar11@gmail.com")            # Updated
print(u1.email)              

# 13.) Write a class Product with a constructor that stores name and price. Add a method increase_price(amount).

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def increase_price(self,amount):
        self.price = self.price + amount
        print(f"Final Price: {self.price}")

p1 = Product("Fan",4500)
print(p1.name)
print(p1.price)

p1.increase_price(500)

# 14.) Write a class Course with a constructor that stores course_name and duration. Add a method show_course().

class Course:
    def __init__(self,course_name,duration):
        self.course_name = course_name
        self.duration = duration
        
    def show_course(self):
        print(f"Course Name: {self.course_name}")
        print(f"Duration: {self.duration}")
        
c1 = Course("AI/ML", "3 Months")
c1.show_course()
        

# C.) ADVANCED LEVEL (15–20):

# 15.) Write a class Student with a constructor that stores name and marks. Add a method add_marks(extra) to increase marks.

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def add_marks(self,extra):
        self.marks = self.marks + extra

s1 = Student("Zeeson Manandhar",75)
print(s1.name)
print(s1.marks)    

s1.add_marks(5)
print(s1.marks)     

# 16.) Write a class BankAccount with a constructor that stores name and balance. Add two methods: deposit() and withdraw().

class BankAccount:
    def __init__(self,name,balance):
        self.name= name
        self.balance = balance
    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"Your Latest Balance: {self.balance}")
    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance - amount
            print(f"You have sucessfully withdrawn : Rs.{amount}")
        else:
            print("Invalid Amount!")
            
b1 = BankAccount("Zeeson Manandhar",6000)
print(b1.name)
print(b1.balance)

b1.deposit(4000)       # Latest balance after deposit
b1.withdraw(500)
print(b1.balance)


# 17.) Write a class Car with a constructor that stores brand and price (default price = 1000000). Create two objects (one with default price).

class Car:
    def __init__(self,brand,price = 1000000):
        self.brand = brand
        self.price = price

c1 = Car("Toyota",2000000)
print(c1.brand)
print(c1.price)

c2 = Car("BMW")
print(c2.brand)
print(c2.price)
        
# 18.) Write a class Employee with a constructor that stores name, salary, and department. Add a method to update salary.

class Employee:
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department
    def update_salary(self,new_salary):
        if new_salary > 0:
            self.salary = new_salary
        else:
            print("Invalid Salary!")

e1 = Employee("Zeeson",25000,"Software")
print(e1.name)
print(e1.salary)
print(e1.department)

e1.update_salary(28000)
print(e1.salary)

# 19.) Write a class User with a constructor that stores username and password. Add a method change_password(new_password).

class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def change_password(self,new_password):
        if self.password != new_password:
            self.password = new_password
            print("Password Changed Sucessfully!")
        else:
            print("Please Enter Different Password!")

u1 = User("ZeesonGroot","Zee@@@")
print(u1.username)
print(u1.password)

u1.change_password("Zee###")
print(u1.password)
        
# 20.) Write a class LibraryBook with a constructor that stores title and author. Add a method display_info() to print both.

class LibraryBook:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def display_info(self):
        print(f"Book Title: {self.title}")
        print(f"Book Author: {self.author}")

lb1 = LibraryBook("Think Like a Monk","Jay Shetty")
lb1.display_info()