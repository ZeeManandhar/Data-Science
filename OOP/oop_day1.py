# OOP => Object Oriented Programming
# A new concept of programming based on classes and objects

# Class => The blueprint to create objects
# Object => The instances of the class
# We can create multiple objects from a class

# class class_name:
#     attributes and methods
# Attributes are the variables inside the class
# Methods are the functions inside the class

class Student:
    name = "Zeeson"
    
    def move(self):
        print(self)
        print("Student is moving")
        
# Procedural Programming
# FUnctional Programming
# OOP

# list1 = [1,2,3,4,5]
# print(type(list1))

# To create a object of a class, we need to call a class
# std1 = Student()

# print(std1)

# std1.move()
# print(std1.name)

# std2 = Student()
# print(std2)
# std2.move()
# print(std2.name)

# std3 = Student()
# print(std3)
# std3.move()
# print(std3.name)


# Class Attributes: The attributes that donot change according to the objects
# Object Attributes : The attributes that changes according to the object

class Student:
    name ="Zeeson"
    def set_info(self, name, age, gender):
        self.name = name
        self.b = age
        self.c = gender
    def abc(self):
        print("ABC")
        
        
    def abc(self):
        print("DEF")
    
# std1 = Student()
# std1.set_info("Zeeson",29,["Zeeson","Priyanka","Deepika"])
# print(std1.c)
    
std2 = Student()
std2.set_info("Ram",27,"Male")
# print(std2.a)
print(std2.name)

    
# std3 = Student()
# std3.set_info("SHyam",29,"Male")
# print(std3.a)
    
std4 = Student()
# std4.set_info("Hari",27,"Male")
# print(std4.a)
# del std4.a
# print(std4.a)

std4.abc()
# del std4.abc
print(std4.abc())
# Question: 


# Create a class Book create its attributes

class Book:
    library_name = "Nepal Public Library"

    def set_info(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
book1 = Book()
book1.set_info("Python Basics", "Zeeson Manandhar", 250, 99)

print(book1.title)
print(book1.author)
print(book1.pages)
print(book1.price)
print(book1.library_name)


# Create a class Movies create its attributes
class Movies:
    def set_info(self, title, director, year, rating, genre):
        self.title = title
        self.director = director
        self.year = year
        self.rating = rating
        self.genre = genre
m1 = Movies()
m1.set_info("Avengers", "Josh Christopher", 2014, 9.6, "Sci-Fi")

print(m1.title)
print(m1.director)
print(m1.year)
print(m1.rating)
print(m1.genre)

# print(5+10)
# print("Zeeson"+"Manandhar")

