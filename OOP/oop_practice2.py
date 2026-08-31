# Practice Question on Encapsulation:

#  BASIC LEVEL (1–15):

# 1.) Write a program to create a class Student with a private variable __name and a getter method to print it.

class Student:
    __name = "Zeeson Manandhar"
    def get_name(self):
        return self.__name

s1 = Student()
print(s1.get_name())

# 2.) Write a program to create a class Person with a private variable __age and a method to display age.

class Person:
    __age = 22
    def get_age(self):
        return self.__age

p1 = Person()
print(p1.get_age())

# 3.) Write a program to create a class Car with private variable __brand and print it using a getter.

class Car:
    __brand = "Toyota"
    def get_brand(self):
        print(self.__brand)

c1 = Car()
c1.get_brand()

# 4.)  Write a program to create a class Book with private variable __title and access it using a method.

class Book:
    __title = "Wonder"
    def get_title(self):
        print(self.__title)

b1 = Book()
b1.get_title()

# 5.) Write a program to create a class User with private variable __username and print it safely.

class User:
    __username = "ZeesonGroot"
    def get_username(self):
        return self.__username
usr = User()
print(usr.get_username())

# 6.) Write a program to create a class Mobile with private variable __price and return it using a method.

class Mobile:
    __price = 50000
    def get_price(self):
        return self.__price
m1 = Mobile()
print(m1.get_price())

# 7.) Write a program to create a class Laptop with private variable __model and display it.

class Laptop:
    __model = "Dell 3511"
    def get_model(self):
        print(self.__model)

l1 = Laptop()
l1.get_model()

# 8.) Write a program to create a class City with private variable __name and print it using a getter.

class City:
    __name = "Kathmandu"
    def get_city_name(self):
        print(self.__name)

c1 = City()
c1.get_city_name()


# 9.) Write a program to create a class Animal with private variable __type and display it.

class Animal:
    __type = "Wild Animal"
    def get_type(self):
        print(self.__type)
        
a1 = Animal()
a1.get_type()
    

# 10.) Write a program to create a class Movie with private variable __rating and print it.

class Movie:
    __rating = 8
    def get_rating(self):
        print(self.__rating)

m1 = Movie()
m1.get_rating()


# 11.) Write a program to create a class Employee with private variable __salary and show it using a method.

class Employee:
    __salary = 18000
    def get_salary_info(self):
        print(self.__salary)
        
e1 = Employee()
e1.get_salary_info()

# 12.) Write a program to create a class Bank with private variable __balance and print it.

class Bank:
    __balance = 7000
    def check_balance(self):
        print(self.__balance)

b1 = Bank()
b1.check_balance()

# 13.) Write a program to create a class Teacher with private variable __subject and display it.

class Teacher:
    __subject = "Programming"
    def get_subject(self):
        print(self.__subject)

t1 = Teacher()
t1.get_subject()

# 14.) Write a program to create a class Food with private variable __name and print it.

class Food:
    __name = "Pizza"
    def get_food_name(self):
        print(self.__name)

f1 = Food()
f1.get_food_name()

# 15.) Write a program to create a class Country with private variable __capital and access it using a getter.

class Country:
    __capital = "Kathmandu"
    def get_capital(self):
        print(self.__capital)

c1 = Country()
c1.get_capital()


#  INTERMEDIATE LEVEL (16–30):

# 16.) Write a program to create a class Student with private variable __marks and use getter and setter methods.

class Student:
    __marks = 0
    def get_marks(self):
        return self.__marks
    
    def update_marks(self,new_marks):
        if new_marks >= 0 and new_marks <=100:
            self.__marks = new_marks

s1 = Student()
s1.update_marks(55)
print(s1.get_marks())


# 17.) Write a program to create a class Person with private variable __age and validate age > 0 in setter.

class Person:
    __age = 25
    def set_age(self,new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("Not a Valid Age!")
            
    def get_age(self):
        return self.__age

p1 = Person()
p1.set_age(35)
print(p1.get_age())


# 18.) Write a program to create a class Bank with private variable __balance and update it using setter only if amount ≥ 0.

class Bank:
    __balance = 1000

    def set_balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Invalid amount!")

    def check_balance(self):
        return self.__balance
    
b1 = Bank()
b1.set_balance(5500)
print(b1.check_balance())


# 19.) Write a program to create a class Product with private variable __price and prevent negative price.

class Product:
    __price = 0
    
    def set_price(self,new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Negative Price not accepted!")

    def get_price(self):
        return self.__price
    
p1 = Product()
p1.set_price(4500)
print(p1.get_price())


# 20.) Write a program to create a class Account with private variable __balance and allow deposit only if amount > 0.

class Account:
    __balance = 0
    def set_balance(self,new_balance):
        if new_balance > 0:
            self.__balance = self.__balance + new_balance
        else:
            print("Invalid Amount!")
    
    def get_balance(self):
        return self.__balance
    
a1 = Account()
a1.set_balance(6745)
print(a1.get_balance())


# 21.) Write a program to create a class Account with private variable __balance and allow withdrawal only if balance is sufficient.

class Account:
    __balance = 1000   

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn successfully!")
        else:
            print("Insufficient balance!")


a1 = Account()
# Check balance
print("Initial Balance:", a1.get_balance())

# Withdraw money
a1.withdraw(600)
print("Remaining Balance:", a1.get_balance())


# 22.) Write a program to create a class Employee with private variable __salary and increase salary using setter.

class Employee:
    __salary = 15000
    def increase_salary(self,amount):
        self.__salary += amount
    def check_salary(self):
        return self.__salary

e1 = Employee()
print("Previous Salary:",e1.check_salary())

e1.increase_salary(3000)
print("Latest Salary:",e1.check_salary())


# 23.) Write a program to create a class Temperature with private variable __celsius and validate it is not below absolute zero.

class Temperature:
    __celsius = 0

    def set_temperature(self, temp):
        if temp >= -273.15:
            self.__celsius = temp
        else:
            print("Invalid temperature! Below absolute zero.")

    def get_temperature(self):
        return self.__celsius


t1 = Temperature()

t1.set_temperature(25)      
print(t1.get_temperature())

t1.set_temperature(-300)    


# 24.) Write a program to create a class User with private variable __password and method to check password.

class User:
    __password = "ZeesonGroot123#"
    def check_password(self,password):
        if self.__password == password:
            print("Password Matched!")
        else:
            print("Invalid Password!")

use = User()
use.check_password("ZeesonGroot123#")

# 25.) Write a program to create a class Exam with private variable __marks and ensure marks are between 0 and 100.

class Exam:
    __marks  = 0
    
    def set_marks(self,new_marks):
        if new_marks >= 0 and new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Invalid Marks")
            
    def get_marks(self):
        return self.__marks

e1 = Exam()
e1.set_marks(55)
print(e1.get_marks())
    
# 26.) Write a program to create a class Car with private variable __speed and restrict speed limit.

class Car:
    __speed = 0

    def set_speed(self, speed):
        if speed <= 50:
            self.__speed = speed
        else:
            print("Speed limit exceeded!")

    def get_speed(self):
        return self.__speed
    
c1 = Car()
c1.set_speed(40)

print(c1.get_speed())


# 27.) Write a program to create a class Wallet with private variable __money and methods to add and spend money.

class Wallet:
    __money = 500
    
    def add_money(self,money):
        if money > 0:
            self.__money += money
            print(f"Your total money: {self.__money}")
        else:
            print("Invalid Amount!")
            
    def spend_money(self,amount):
        if amount > 0 and amount <= self.__money:
            self.__money -= amount
            print(f"Your Total Money left after spending: {self.__money}")
            print(f"Spent Amount : {amount}")
        else:
            print("Insufficient Money!")
            
w1 = Wallet()
w1.add_money(100)

w1.spend_money(10)

# 28.) Write a program to create a class Laptop with private variable __battery and prevent battery level > 100.

class Laptop:
    __battery = 0
    
    def set_battery(self,battery):
        if battery >= 0 and battery <= 100:
            self.__battery = battery
        else:
            print("Warning : Battery Level Exceeded!")
            
    def check_battery_status(self):
        return self.__battery
    
l1 = Laptop()
l1.set_battery(90)
print(l1.check_battery_status())


# 29.) Write a program to create a class Library with private variable __books and return count using getter.

class Library:
    __books = 5

    def get_books(self):
        return self.__books

l1 = Library()
print(l1.get_books())

# 30.) Write a program to create a class Game with private variable __score and update score using setter.

class Game:
    __score = 0
    def set_score(self,new_score):
        self.__score = new_score
    
    def get_score(self):
        return self.__score

g1 = Game()
g1.set_score(50)
print(g1.get_score())


# ADVANCED LEVEL (31–38):

# 31.) Write a program to create a class Bank with private variable __balance, and methods for deposit, withdraw, and check balance with full validation.

class Bank:
    __intial_balance = 1000
    
    def deposit(self,balance):
        if balance > 0:
            self.__intial_balance = self.__intial_balance + balance
            print(f"Rs.{balance} has been deposited sucessfully!")
        else:
            print("Enter valid amount please! Try Again")

    def withdraw(self,amount):
        if amount > 0 and amount <= self.__intial_balance:
            self.__intial_balance -= amount
            print(f"Rs.{amount} has been sucessfully withdrawn from your account!")
        else:
            print("Invalid Amount")
            
    def check_balance(self):
        return self.__intial_balance
    
b1 = Bank()
b1.deposit(5000)
b1.withdraw(500)
print("Your Current Balance:",b1.check_balance())

# 32.) Write a program to create a class ATM with private method __authenticate() and public method login().

class ATM:
    __username = "Zeesonmdr"
    __password = "Admin@123"
    
    def __authenticate(self,username,password):
        if self.__username == username and self.__password == password:
            print("Login sucessfull!")
        else:
            print("Invalid Credentials!")
            
    def login(self,username,password):
        self.__authenticate(username,password)

a1 = ATM()
a1.login("Zeesonmdr","Admin@123")

# 33.) Write a program to create a class Calculator with private method __add() and public method calculate().

class Calculator:
    def __add(self,num1,num2):
         return num1 + num2
        
     
    def calculate(self,num1,num2):
         return self.__add(num1,num2)   

c1 = Calculator()
print(c1.calculate(5,6))
  
# 34.) Write a program to create a class LoginSystem with private variable __password and method to verify login.

class LoginSystem:
    __password = "admin@123"
    
    def login(self,password):
        if self.__password == password:
            print("Login Sucessful")
        else:
            print("Invalid Password!")
            
l1 = LoginSystem()
l1.login("admin@123")

# 35.) Write a program to create a class Student with private variable __marks and calculate grade internally using private method.

class Student:
    __marks = 80
    def __calculate_grade(self):
        if self.__marks >= 90 and self.__marks <=100:
            print("A+")
        elif self.__marks >= 80 and self.__marks < 90:
            print("A")
        elif self.__marks >= 70 and self.__marks < 80:
            print("B+")
        elif self.__marks >= 60 and self.__marks < 70:
            print("B")
        elif self.__marks >= 50 and self.__marks < 60:
            print("C+")
        elif self.__marks >= 40 and self.__marks < 50:
            print("C")
        elif self.__marks >= 0 and self.__marks < 40:
            print("Fail")
        else:
            print("Invalid Mark!")
            
    def get_grade(self):
        self.__calculate_grade()

s1 = Student()
s1.get_grade()

# 36.) Write a program to create a class ShoppingCart with private variable __items and methods to add/remove items.

class ShoppingCart:
    __items = []
    
    def add_items(self,items):
        self.__items.append(items)
        return self.__items
    
    def remove_items(self,item):
        if item in self.__items:
            self.__items.remove(item)
        else:
            print("Item Not Found!")
            
    def view_items(self):
        return self.__items
    
sc = ShoppingCart()
sc.add_items("Laptop")
sc.add_items("Phone")
sc.add_items("Charger")

sc.remove_items("Phone")

print(sc.view_items())

# 37.) Write a program to create a class UserProfile with private variables and control updates using setters.

class UserProfile:
    __name = "Zeeson Manandhar"
    __email = "zeeson.manandhar11@gmail.com"
    __age = 22
    
    def set_name(self,name):
        self.__name = name
    
    def set_email(self,email):
        if "@" in email:
            self.__email = email
        else:
            print("Invalid Email Format!")
    
    def set_age(self,age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid Age!")
            
    def get_info(self):
        return self.__name, self.__age, self.__email
        
u1 = UserProfile()
u1.set_name("Zeeson Mdr")
u1.set_email("zeeson.manandhar12@gmail.com")
u1.set_age(23)    
            
print(u1.get_info())   


# 38.) Write a program to create a class SecureSystem with private method for encryption and public method to send data.

class SecureSystem:
    def __encrypt_data(self,data):
        result = data[::-1]
        return result
    
    def send_data(self,data):
        print(self.__encrypt_data(data))
        
ss = SecureSystem()
ss.send_data("Zeeson")

