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
    def set_balance(self,new_balance):
        self.__balance = self.__balance + new_balance
       
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


# 24.) Write a program to create a class User with private variable __password and method to check password.



# 25.) Write a program to create a class Exam with private variable __marks and ensure marks are between 0 and 100.



# 26.) Write a program to create a class Car with private variable __speed and restrict speed limit.



# 27.) Write a program to create a class Wallet with private variable __money and methods to add and spend money.



# 28.) Write a program to create a class Laptop with private variable __battery and prevent battery level > 100.




# 29.) Write a program to create a class Library with private variable __books and return count using getter.




# 30.) Write a program to create a class Game with private variable __score and update score using setter.




# ADVANCED LEVEL (31–40):
# Write a program to create a class Bank with private variable __balance, and methods for deposit, withdraw, and check balance with full validation.
# Write a program to create a class ATM with private method __authenticate() and public method login().
# Write a program to create a class Calculator with private method __add() and public method calculate().
# Write a program to create a class LoginSystem with private variable __password and method to verify login.
# Write a program to create a class Student with private variable __marks and calculate grade internally using private method.
# Write a program to create a class ShoppingCart with private variable __items and methods to add/remove items.
# Write a program to create a class BankAccount with private variable __balance and maintain transaction history.
# Write a program to create a class UserProfile with private variables and control updates using setters.
# Write a program to create a class Hospital with private patient data and methods to access limited info.
# Write a program to create a class SecureSystem with private method for encryption and public method to send data.