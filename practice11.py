# OOP practice questions (Day 1):

# Level 1 – Basic (1–10)

# 1.) Create a class Student with an attribute name and print it using an object.

class Student:
    name = "Zeeson"

s1 = Student()
print(s1.name)

# 2.) Create a class Car with attribute wheels = 4 and print it.

class Car:
    wheels = 4

c1 = Car()
print(c1.wheels)

# 3.) Create a class Book with attribute title = "Python Basics" and print it.

class Book():
    title = "Python Basics"
    
b1 = Book()
print(b1.title)

# 4.) Create a class Movie with attribute rating = 9 and print it.

class Movie():
    rating = 9

m1 = Movie()
print(m1.rating)

# 5.) Create a class Animal with method sound() that prints "Animal makes sound".

class Animal:
    def sound(self):
        print("Animal Makes Sound!")

a1 = Animal()
a1.sound()

# 6.) Create a class Phone with method call() that prints "Calling...".

class Phone():
    def call(self):
        return "Calling.....!"

p1 = Phone()
print(p1.call())

# 7.) Create a class Laptop with method start() that prints "Laptop started".

class Laptop:
    def start(self):
        print("Laptop Started!")

l1 = Laptop()
l1.start()
    

# 8.) Create a class Student and create 2 objects, print the same attribute using both.

class Student:
    name = "Ramesh Rai"

s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)


# 9.) Create a class Car and create 3 objects, call a method using all.

class Car:
    def type(self,name):
        self.name = name

c1 = Car()
c1.type("Toyota")
print(c1.name)     
        
c2 = Car()
c2.type("Hyundai")
print(c2.name)

c3 = Car()
c3.type("Audi")
print(c3.name)

# 10.) Create a class Person with method greet() that prints "Hello".

class Person:
    def greet(self):
        print("Hello")

p1 = Person()
p1.greet()


# Level 2 – Using Object Attributes (11–20):

# 11.) Create a class Student and set name using object like:
    # s1.name = "Ram"
    # Print it.

class Student:
    name = ""
       
s1 = Student()
s1.name = "Ram"
print(s1.name)

# 12.) Create 2 student objects and assign different names to both. Print both.

class Student:
    def std_info(self, name, section):
        self.name = name
        self.section = section


s1 = Student()
s1.std_info("Ram Ghale", 'B')

s2 = Student()
s2.std_info("Bikash Thakur", 'D')

print(s1.name)
print(s2.name)


# 13.) Create a class Car, assign color to different objects, and print.

class Car:
    def car_color(self,color):
        self.Color = color

c1 = Car()
c1.car_color("Red Car")
print(c1.Color)

c2 = Car()
c2.car_color("Black Car")
print(c2.Color)

# 14.) Create a class Book, assign price to 2 objects and print both.

class Book:
    def book_prices(self,name,price):
        self.Name = name
        self.Price = price

b1 = Book()
b1.book_prices("Bhagvad Geeta", 450)
print(f"Book Name : {b1.Name}, Price : {b1.Price}")

b2 = Book()
b2.book_prices("Python Programming-2025", 425)
print(f"Book Name : {b2.Name}, Price : {b2.Price}")


# 15.) Create a class Movie, assign name and rating to an object and print both.

class Movie:
    def mov_rating(self,name,rating):
        self.Name = name
        self.Rating = rating

m1 = Movie()
m1.mov_rating("Lion King",9.7)
print(m1.Name)
print(m1.Rating)


# 16.) Create 2 objects of class Phone and assign different brands.

class Phone:
    def phone_brand(self,brand):
        self.Brand = brand

p1 = Phone()
p1.phone_brand("Samsung Galaxy A17 5G")
print(p1.Brand)

p2 = Phone()
p2.phone_brand("Iphone 17")
print(p2.Brand)


# 17.) Create a class Student, assign name and age to object and print.

class Student:
    def std_info(self,name,age):
        self.Name = name
        self.Age = age
        
s1 = Student()
s1.std_info("Shyam Ghale", 19)
print(s1.Name)
print(s1.Age)


# 18.) Create a class Animal, assign type to 2 objects and print.




# 19.) Create a class Laptop, assign brand and price to object.



# 20.) Create 3 objects of class Car, assign different colors to each.




# Level 3 – Using Methods & self (21–30):

# Create a class Student with method set_name(self, name) and store it using self.



# Create a class Car with method set_color(self, color) and print it.



# Create a class Book with method set_info(self, title, price) and print both.



# Create a class Movie with method set_data(self, name, rating) and print.



# Create a class Phone with method set_details(self, brand, price).




# Create 2 objects of Student and store different names using method.




# Create a class Laptop with method set_data(self, brand, ram) and print.



# Create a class Animal with method set_type(self, type) and print.



# Create a class Car with method set_info(self, brand, speed) and print.



# Create a class Person with method:
   # def set_info(self, name, age, city)
   # Store and print all values.