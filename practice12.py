# Inheritance (Practice Questions):

# Level 1 – Basics

# 1.) Create a class Animal with a method eat() that prints "Animal eats".

class Animal:
    def eat(self):
        print("Animal eats")
        
a1 = Animal()
a1.eat()

# 2.) Create a class Dog that inherits from Animal, create an object, and call eat().

class Animal:
    def eat(self):
        print("Animal Eats Food")

class Dog(Animal):
    pass

d1 = Dog()
d1.eat()


# 3.) Add a method sleep() in Animal, then call both eat() and sleep() using a Dog object.

class Animal:
    def sleep(self):
        print("Its Sleeping!")
        
    def eat(self):
        print("Its Eating!")
class Dog(Animal):
    pass
        
d1 = Dog()
d1.eat()
d1.sleep()


# 4.) Create a class Vehicle with method start(), then create a child class Car and call start().

class Vehicle:
    def start(self):
        print("Engine Turning On!")
        
class Car(Vehicle):
    pass

c1 = Car()
c1.start()


# 5.) Create a class Person with attribute name = "Unknown", then create a child class Student and print name.

class Person:
    name = "Unknown"
    
class Student(Person):
    pass

s1 = Student()
print(s1.name)


# Level 2 – Using Parent Features

# 6.) Create a class Animal with attribute type = "Living" and access it using a Dog object.

class Animal:
    type = "living"
    
class Dog(Animal):
    pass

d1 = Dog()
print(d1.type)

# 7.) Create a class Vehicle with method stop() and call it using a Bike object (child class).

class Vehicle:
    def stop(self):
        print("Engine Off!")
        
class Bike(Vehicle):
    pass

b1 = Bike()
b1.stop()

# 8.)  Create a class Bird with method fly() and call it using a Parrot object.

class Bird:
    def fly(self):
        print("Birds fly!")
        
class Parrot(Bird):
    pass

p1 = Parrot()
p1.fly()


# 9.)  Create a class Shape with method draw() and call it using a Circle object.

class Shape:
    def draw(self):
        print("Drawing!")
        
class Circle(Shape):
    pass

c1 = Circle()
c1.draw()
        

# 10.) Create a class Device with method power_on() and call it using a Mobile object.

class Device:
    def power_on(self):
        print("Power on!")
        
class Mobile(Device):
    pass

m1 = Mobile()
m1.power_on()

# Level 3 – Adding Child Features

# 11.) Create a class Animal with method eat() and a class Dog that adds method bark(), then call both methods.

class Animal:
    def eat(self):
        print("Animal eating")
        
class Dog(Animal):
    def bark(self):
        print("Dogs Barking")
        
d1 = Dog()
d1.bark()
d1.eat()

# 12.) Create a class Vehicle with method start() and a class Car that adds method drive(), then call both.

class Vehicle:
    def start(self):
        print("Engine Start!")
        
class Car(Vehicle):
    def drive(self):
        print("Driving!")
        
c1 = Car()
c1.start()
c1.drive()

# 13.) Create a class Person with method show() and a class Teacher that adds method teach(), then call both.

class Person:
    def show(self):
        print("Show Called!")
        
class Teacher(Person):
    def teach(self):
        print("Teaching!")
        
t1 = Teacher()
t1.show()
t1.teach()


# 14.)  Create a class Phone with method call() and a class SmartPhone that adds method camera(), then call both.

class Phone:
    def call(self):
        print("Phone Calling!")
        
class SmartPhone(Phone):
    def camera(self):
        print("Camera Clicking!")

s1 = SmartPhone()
s1.call()
s1.camera()

# 15.) Create a class Employee with method work() and a class Manager that adds method manage(), then call both.

class Employee:
    def work(self):
        print("Employee Working!")
        
class Manager(Employee):
    def manage(self):
        print("Manager managing!")
        
m1 = Manager()
m1.work()
m1.manage()


# Level 4 – Method Overriding

# 16.) Create a class Animal with method sound() that prints "Animal sound", then override it in Dog to print "Dog barks".

class Animal:
    def sound(self):
        print("Animal sound")
        
class Dog(Animal):
    def sound(self):
        print("Dog barks")

d1 = Dog()
d1.sound()

# 17.) Create a class Vehicle with method move() that prints "Vehicle moves", then override it in Car to print "Car runs fast".

class Vehicle:
    def move(self):
        print("Vehicle moves")

class Car(Vehicle):
    def move(self):
        print("Car runs fast")
        
c1 = Car()
c1.move()


# 18.) Create a class Person with method role(), then override it in Student with a different message.

class Person:
    def role(self):
        print("Normal Person")
        
class Student(Person):
    def role(self):
        print("Student")
        
s1 = Student()
s1.role()

# 19.) Create a class Shape with method area(), then override it in Circle with a different message.

class Shape:
    def area(self):
        print("Area of the Shape")
        
class Circle(Shape):
    def area(self):
        print("Area of Circle")

c1 = Circle()
c1.area()


# 20.) Create a class Account with method info(), then override it in SavingsAccount with a different message.

class Account:
    def info(self):
        print("Account Type")
        
class SavingsAccount(Account):
    def info(self):
        print("Saving Account")
        
s1 = SavingsAccount()
s1.info()

# Level 5 – Using super()

# 21.) Create a class Animal with method eat(), then override it in Dog and use super() to call both parent and child methods.

class Animal:
    def eat(self):
        print("Animal eats")
        
class Dog(Animal):
    def eat(self):
        super().eat()
        print("Dog eat bones")
        
d1 = Dog()
d1.eat()

# 22.) Create a class Vehicle with method start(), then override it in Car and use super() to call both methods.

class Vehicle:
    def start(self):
        print("Vehicle Starting.......!")
class Car(Vehicle):
    def start(self):
        super().start()
        print("Car Starting.....!")
c1 = Car()
c1.start()

# 23.) Create a class Person with method show(), then override it in Student and use super().

class Person:
    def show(self):
        print("Unknown Person")
        
class Student(Person):
    def show(self):
        super().show()
        print("Person is Student")

s1 = Student()
s1.show()


# 24.) Create a class Employee with method work(), then override it in Manager using super().

class Employee:
    def work(self):
        print("Its Employee!")

class Manager(Employee):
    def work(self):
        super().work()
        print("Its Manager!")

m1 = Manager()
m1.work()


# 25.) Create a class Device with method power_on(), then override it in Laptop and use super().

class Device:
    def power_on(self):
        print("Device power on!")

class Laptop(Device):
    def power_on(self):
        super().power_on()
        print("Laptop power on")
        
l1 = Laptop()
l1.power_on()

# Level 6 – Types of Inheritance

# 26.) Create a single inheritance example with Animal → Dog including methods eat() and bark().





# 27.) Create a multilevel inheritance example with Animal → Dog → Puppy and call all methods.




# 28.) Create a multiple inheritance example with Father → drive(), Mother → cook(), and Child inheriting both, then call both methods.




# 29.) Create classes A and B with method show(), then create class C(A, B) and call show() to observe MRO.






# 30.) Create a multilevel inheritance example Person → Employee → Manager, override a method in Manager, and use super().