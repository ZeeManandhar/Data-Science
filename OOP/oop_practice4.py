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

def my_decorator(func):
    def inner_func(num1,num2):
        if num1 >= 0 and num2 >= 0:
            func(num1,num2)
        else:
            print("Negative Number cannot be calculated!")
    return inner_func

@my_decorator
def calculate(num1,num2):
    print(f"Addition : {num1+num2}")
    print(f"Subtraction : {num1-num2}")
    print(f"Multiplication : {num1*num2}")

calculate(11,6)

# 12.) Write a program to create a decorator that asks for admin permission before deleting a file.

def my_decorator(func):
    def inner_func(is_admin):
        if is_admin == True:
            func()
        else:
            print("Permission Denied!!")
    return inner_func

@my_decorator
def delete_file():
    print("File Deleted Sucessfully!")
    
delete_file(True)

# 13.) Write a program to create a decorator that counts how many times a function was called.

count = 0

def my_decorator(func):
    def inner_func():
        global count
        count += 1
        print(f"Function called for {count} times.")
        func()
    return inner_func

@my_decorator
def greet():
    print("Hello User!")

greet()
greet()
greet()

# 14.) Write a program to stack two decorators on one function: one prints Before, another prints After.

def my_decorator_one(func):
    def inner():
        print("First Decorator!")
        func()
    return inner

def my_decorator_two(func):
    def inner():
        print("Second Decorator!")
        func()
    return inner

@my_decorator_one
@my_decorator_two

def execute():
    print("Executed Sucessfully!")
    
execute()

# 15.) Write a program to create a decorator for an ATM withdrawal function that logs every withdrawal.

def my_decorator(func):
    def inner(amount):
        print(f"Transaction Log: Rs.{amount}")
        func(amount)
    return inner

@my_decorator
def withdraw(amount):
    print(f"Rs.{amount} Withdrawn Successfully!")

withdraw(5000)

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
        Final_Price = price - discount_price 
        print(f"Final Price after Discount: {Final_Price}")

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

class PasswordChecker:
    
    @staticmethod
    def validate(password):
        if len(password) > 6:
            print("Strong Password!")
        else:
            print("Not a Strong Password! Please Try Different Password!")

pc1 = PasswordChecker()
pc1.validate("Zeeson123")


# 27.) Write a program to create a Salary class with static method to calculate yearly salary from monthly salary.

class Salary:
    
    @staticmethod
    def calc_yearly_salary(salary):
        yearly_salary = salary * 12
        print(f"Annual Salary : Rs.{yearly_salary}")

s1 = Salary()
s1.calc_yearly_salary(50000)
        

# SECTION C – ABSTRACTION / ABC (28–40):

# Basic

# 28.) Write a program to create an abstract class Animal with abstract method sound().

from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        print("Animals Make Different Sounds!")
        
class Dog(Animal):
    def sound(self):
        print("bhau bhau bhau!")

d1 = Dog()
d1.sound()

# 29.) Write a program to create child classes Dog and Cat implementing sound().

from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def sound():
        pass

class Dog(Animal):
    def sound(self):
        print("Dog Barks")
    
class Cat(Animal):
    def sound(self):
        print("Cat Meows!")
        
d1 = Dog()
d1.sound()

c1 = Cat()
c1.sound()

# 30.) Write a program to create abstract class Vehicle with method start().

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Bike(Vehicle):
    
    @staticmethod
    def start():
        print("Bike Starting on...!")

b1 = Bike()
b1.start()

# 31.) Write a program to create child class Car implementing start().

class Car(Vehicle):
    
    @staticmethod
    def start():
        print("Car Starting On...!")

c1 = Car()
c1.start()


# 32.) Write a program to create abstract class Shape with abstract method area().

from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area():
        pass

class Square(Shape):
    @staticmethod
    def area(length):
        print(length**2)
        
s1 = Square()
s1.area(5)
        
# Intermediate:

# 33.) Write a program to create child classes Circle and Rectangle implementing area().

class Circle(Shape):
    
    @staticmethod
    def area(r):
        pi = 3.14
        print(f"Area of Circle : {pi*r**2}")

c1 = Circle()
c1.area(5)

class Rectangle(Shape):
    
    @staticmethod
    def area(l,b):
        print(f"Area of Rectangle : {l*b}")

r1 = Rectangle()
r1.area(5,6)
 
# 34.) Write a program to create abstract class Employee with abstract method work().

from abc import ABC, abstractmethod

class Employee(ABC):
    
    @abstractmethod
    def work(self):
        pass


# 35.) Write a program to create child classes Manager and Developer implementing work().

class Manager(Employee): 
    def work(self):
        print("Manager manages all the work!")

m1 = Manager()
m1.work()

class Developer(Employee):
    def work(self):
        print("Developer writes the code and tests it!")

d1 = Developer()
d1.work()


# 36.) Write a program to create abstract class Payment with abstract method pay().

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

# 37.) Write a program to create child classes EsewaPayment and CardPayment.

class EsewaPayment(Payment):
    def pay(self):
        print("Payment Done through Esewa...!")

ep = EsewaPayment()
ep.pay()

class CardPayment(Payment):
    def pay(self):
        print("Payment Done Through Cash...!")

cp = CardPayment()
cp.pay()

# Advanced:

# 38.) Write a program to create abstract class HospitalStaff with abstract method duty(), then implement Doctor and Nurse.

from abc import ABC, abstractmethod

class HospitalStaff(ABC):
    @abstractmethod
    def duty(self):
        pass

class Doctor(HospitalStaff):
    def duty(self):
        print("Diagnosing and treating the patient.")

d1 = Doctor()
d1.duty()


class Nurse(HospitalStaff):
    def duty(self):
        print("Caring for patients, communicating with doctors and administering medicine.")

n1 = Nurse()
n1.duty()

# 39.)Write a program to create abstract class UniversityTeacher with abstract method teach(), then implement MathTeacher and ScienceTeacher.

from abc import ABC, abstractmethod

class UniversityTeacher(ABC):
    
    @abstractmethod
    def teach(self):
        pass

class MathTeacher(UniversityTeacher):
    
    def teach(self):
        print("Teaches Math...!")

m1 = MathTeacher()
m1.teach()

class ScienceTeacher(UniversityTeacher):
    
    def teach(self):
        print("Teaches Science...!")

s1 = ScienceTeacher()
s1.teach()
    
# 40.) Write a program to create abstract class DeliveryService with abstract method deliver(), then implement BikeDelivery and TruckDelivery.

class DeliveryService(ABC):
    
    @abstractmethod
    def deliver(self):
        pass

class BikeDelivery(DeliveryService):
    def deliver(self):
        print("Delivery Done Through Bike.")

bd = BikeDelivery()
bd.deliver()

class TruckDelivery(DeliveryService):
    def deliver(self):
        print("Delivery Done Through Truck.")

td = TruckDelivery()
td.deliver()

# BONUS CHALLENGE (Mix Concepts):

# 41.) Write a program to create an abstract class User with method login(), then use a decorator to print Checking Security... before login.

def my_decorator(func):
    def inner_function(self):
        print("Checking Security...!")
        func(self)
    return inner_function

class User(ABC):
    
    @abstractmethod
    def login(self):
        pass

class AdminUser(User):
    @my_decorator
    def login(self):
        print("Login Successful!")

au = AdminUser()
au.login()

# 42.) Write a program to create a class with static method tax() and use it inside salary system.

class TaxSystem:
    
    @staticmethod
    def tax(salary,tax_rate):
        tax = (salary*tax_rate)/100
        print(f"Tax Amount : {tax}")
        final_salary = salary - tax
        print(f"Salary After Tax Deduction : {final_salary}")

t1 = TaxSystem()
t1.tax(50000,1)


