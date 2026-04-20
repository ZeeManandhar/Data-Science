# 40 Practice Questions (Decorators & Static Methods & Abstraction)

# SECTION A – DECORATORS (1–15)
# Basic Level:
# 1.) Write a program to create a decorator that prints Starting... before a function runs.

def my_decorator(func):
    def inner_func():
        print("Starting...")
        func()
    return inner_func

@my_decorator
def state():
    print("Function is running")

state()

# 2.) Write a program to create a decorator that prints Finished... after a function runs.

def my_decorator(func):
    def inner_func():
        func()
        print("Finished...")
    return inner_func

@my_decorator
def new_state():
    print("Function running!")
    
new_state()

# 3.) Write a program to decorate a function that prints your name with Welcome before it.

def my_decorators(func):
    def inner_func(name):
        print("Welcome!")
        func(name)
    return inner_func

@my_decorators
def show_name(name):
    print(name)

show_name("Zeeson Manandhar")

# 4.) Write a program to create a decorator that runs a greeting function 3 times.

def my_decorators(func):
    def inner():
        for i in range(3):
            func()
    return inner

@my_decorators
def greeting():
    print("Namaste!")

greeting()

# 5.) Write a program to decorate a function that prints Login Successful before dashboard opens.

def my_decorator(func):
    def inner():
        print("Login Successful")
        func()
    return inner

@my_decorator
def dashboard():
    print("Dashboard Opening...")
    
dashboard()


# Intermediate Level:

# 6.) Write a program to create a decorator that checks if a user is logged in before opening profile page.

is_logged = True

def my_decorator(func):
    def inner_function():
        if is_logged == True:
            func()
        else:
            print("Please Login First!")
    return inner_function

@my_decorator
def profile():
    print("Opening the Profile Page!")
    
profile()

# 7.)  Write a program to create a decorator that prints execution started and ended around a payment function.

def my_decorator(func):
    def inner_func(confirmation):
        print("Execution Started...")
        if confirmation == True:
            func(confirmation)
        else:
            print("Payment Failed!")
        print("Execution Ended...")
    return inner_func

@my_decorator
def payment(confirmation):
    print("Payment Sucessful!")
    return confirmation

payment(True)

# 8.) Write a program to create a decorator that repeats an order confirmation message 5 times.

def my_decorator(func):
    def inner_func(confirmation):
        print("Program Started...!")
        if confirmation == True:
            for _ in range(5):
                func(confirmation)
        else:
            print("Order not Confirmed!")
    return inner_func

@my_decorator
def message(confirmation):
    print("Order Confirmed!!!")
    return confirmation

message(True)
        
# 9.) Write a program to create a decorator that says Please wait... before loading a report.

def my_decorator(func):
    def inner_func():
        print("Please Wait...!")
        func()
    return inner_func

@my_decorator
def report():
    print("Report loaded successfully!")

report()

# 10.) Write a program to create a decorator that prints date/time before running a backup function.

from datetime import datetime

def my_decorator(func):
    def inner_func():
        current = datetime.now()
        print(f"Backup Started at {current}...")
        func()
        print("Backup Successful!")
    return inner_func

@my_decorator
def backup():
    print("Backing up files...")
    
backup()

# Advanced Level:

# 11.) Write a program to create a decorator that blocks negative numbers before running a calculator function.


# 12.) Write a program to create a decorator that asks for admin permission before deleting a file.



# 13.) Write a program to create a decorator that counts how many times a function was called.



# 14.) Write a program to stack two decorators on one function: one prints Before, another prints After.



# 15.) Write a program to create a decorator for an ATM withdrawal function that logs every withdrawal.



# SECTION B – STATIC METHODS (16–27):

# Basic:

# 16.) Write a program to create a Calculator class with static method add(a,b).

class Calculator:
    
    @staticmethod
    def add(a,b):
        return a+b
    
c1 = Calculator()
print(c1.add(5,11))


# 17.) Write a program to create a MathTools class with static method to subtract two numbers.

class MathTools:
    
    @staticmethod
    def subtract(a,b):
        return a-b

m1 = MathTools()
print(m1.subtract(80,50))

# 18.) Write a program to create a Converter class with static method to convert Celsius to Fahrenheit.

class Converter:

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

print(Converter.celsius_to_fahrenheit(30))


# 19.) Write a program to create a Validator class with static method to check if age is above 18.
class Validator:
    
    @staticmethod
    def valid(age):
        if age > 18:
            print("Valid Age!")
        else:
            print("Invalid Age!")

v1 = Validator()
v1.valid(20)
    
# 20.) Write a program to create a TextTools class with static method to count letters in a word.

class TextTools:
    
    @staticmethod
    def count(data):
        count = 0
        for _ in data:
            count = count + 1
        return count
  
t1 = TextTools()
print(t1.count("Zeeson"))      

# Intermediate:

# 21.) Write a program to create a Bank class with static method to calculate simple interest.

class Bank:
    
    @staticmethod
    def calculate_interest(p,t,r):
        si = (p*t*r)/100
        return si

b1 = Bank()
print(f"The Simple Interest is {b1.calculate_interest(10000,2,6)}")
        
    
# 22.) Write a program to create a Shop class with static method to calculate discount price.

class Shop:
    
    @staticmethod
    def check_discount(price,discount_rate):
        discount_price = (discount_rate/100) * price
        print(f"Discount Price : {discount_price}")

s1 = Shop()
s1.check_discount(5000,5)
        
# 23.) Write a program to create a Geometry class with static method to calculate rectangle area.

class Geometry:
    
    @staticmethod
    def area(length,breadth):
       area = length * breadth 
       print(f"The area of rectangle is {area}")

g1 = Geometry()
g1.area(6,5)


# 24.) Write a program to create a Utility class with static method to check if a number is even.

class Utility:
    
    @staticmethod
    def check_even(num):
        if num%2 == 0:
            print("Even")
        else:
            print("Not Even")

u1 = Utility()
u1.check_even(23)

# 25.) Write a program to create an Exam class with static method to calculate percentage.

class Exam:
    
    @staticmethod
    def calc_percentage(obtain_mark,total_mark):
        total_percentage = (obtain_mark/total_mark) * 100
        return total_percentage
        
e1 = Exam()
print(e1.calc_percentage(356,500))


# Advanced:

# 26.) Write a program to create a PasswordChecker class with static method to validate password length.




# 27.) Write a program to create a Salary class with static method to calculate yearly salary from monthly salary.




# SECTION C – ABSTRACTION / ABC (28–40)
# Basic
# Write a program to create an abstract class Animal with abstract method sound().
# Write a program to create child classes Dog and Cat implementing sound().
# Write a program to create abstract class Vehicle with method start().
# Write a program to create child class Car implementing start().
# Write a program to create abstract class Shape with abstract method area().
# Intermediate
# Write a program to create child classes Circle and Rectangle implementing area().
# Write a program to create abstract class Employee with abstract method work().
# Write a program to create child classes Manager and Developer implementing work().
# Write a program to create abstract class Payment with abstract method pay().
# Write a program to create child classes EsewaPayment and CardPayment.
# Advanced
# Write a program to create abstract class HospitalStaff with abstract method duty(), then implement Doctor and Nurse.
# Write a program to create abstract class UniversityTeacher with abstract method teach(), then implement MathTeacher and ScienceTeacher.
# Write a program to create abstract class DeliveryService with abstract method deliver(), then implement BikeDelivery and TruckDelivery.
# BONUS CHALLENGE (Mix Concepts)
# Write a program to create an abstract class User with method login(), then use a decorator to print Checking Security... before login.
# Write a program to create a class with static method tax() and use it inside salary system.
# Write a program to create an abstract class FoodOrder and decorate child method with order confirmation.