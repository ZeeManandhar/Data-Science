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
    pass
    def sound(self):
        print("Animal Makes Sound!")

a1 = Animal()
a1.sound()

# 6.) Create a class Phone with method call() that prints "Calling...".

class Phone():
    pass
    def call(self):
        return "Calling.....!"

p1 = Phone()
print(p1.call())

# 7.) Create a class Laptop with method start() that prints "Laptop started".

class Laptop:
    pass
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
    pass
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

# Create a class Student and set name using object like:
    # s1.name = "Ram"
    # Print it.






# Create 2 student objects and assign different names to both. Print both.






# Create a class Car, assign color to different objects, and print.







# Create a class Book, assign price to 2 objects and print both.






# Create a class Movie, assign name and rating to an object and print both.






# Create 2 objects of class Phone and assign different brands.





# Create a class Student, assign name and age to object and print.





# Create a class Animal, assign type to 2 objects and print.




# Create a class Laptop, assign brand and price to object.



# Create 3 objects of class Car, assign different colors to each.




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