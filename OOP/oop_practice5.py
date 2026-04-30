# Practice Questions (Polymorphism):

# BASIC (1–10):

# 1.) Write a program with two classes Cat and Dog, both having method sound() printing different outputs.

class Cat:
    name = "Cat Class"
    def sound(self):
        print("Cat Meows!")

class Dog:
    name = "Dog Class"
    def sound(self):
        print("Dog Barks!")
        
c1 = Cat()
c1.sound()

d1 = Dog()
d1.sound()

# 2.) Write a program with classes Car and Bike, both having start() method.

class Car:
    name = "Car Class"
    @staticmethod
    def start():
        print("Car is Starting...!")

class Bike:
    name = "Bike Class"
    @staticmethod
    def start():
        print("Bike is Starting...!")
        
c1 = Car()
c1.start()

b1 = Bike()
b1.start()

# 3.) Write a program with classes Teacher and Student, both having role() method.

class Teacher:
    name = "Teacher Class"
    def role(self):
        print("Teacher teaches...!")

class Student:
    name = "Student Class!"
    def role(self):
        print("Student learns...!")

t1 = Teacher()
t1.role()

s1 = Student()
s1.role()

# 4.) Write a program with classes Apple and Banana, both having color() method.

class Apple:
    @staticmethod
    def color():
        print("Color of Apple is Red!")

class Banana:
    @staticmethod
    def color():
        print("Color of banana is Yellow!")
        
a1 = Apple()
a1.color()

b1 = Banana()
b1.color()

# 5.) Write a program with classes Pen and Pencil, both having write() method.

class Pen:
    def write(self):
        print("Writing with Pen...!")

class Pencil:
    def write(self):
        print("Writing with Pencil...!")

p1 = Pen()
p1.write()

p2 = Pencil()
p2.write()

# 6.) Write a program with classes Mobile and Laptop, both having power_on() method.

class Mobile:
    name = "Mobile Class"
    def power_on(self):
        print("Mobile Turning On...!")

class Laptop:
    name = "Laptop Class"
    def power_on(self):
        print("Laptop Turning On...!")

mob = Mobile()
mob.power_on()

lap = Laptop()
lap.power_on()


# 7.) Write a program with classes Lion and Elephant, both having eat() method.

class Lion:
    @staticmethod
    def eat():
        print("Lions eat flesh")

class Elephant:
    @staticmethod
    def eat():
        print("Elephant eat herbs and grasses")
        
l1 = Lion()
l1.eat()

e1 = Elephant()
e1.eat()  

# 8.) Write a program with classes Singer and Dancer, both having perform() method.

class Singer:
    def perform(self):
        print("Singer sings!")

class Dancer:
    def perform(self):
        print("Dancer dances!")

s1 = Singer()
s1.perform()

d1 = Dancer()
d1.perform()

# 9.) Write a program with classes Clock and Watch, both having show_time() method.

class Clock:
    @staticmethod
    def show_time():
        print("Clock Showing Time!")

class Watch:
    @staticmethod
    def show_time():
        print("Watch Showing Time!")

c1 = Clock()
c1.show_time()

w1 = Watch()
w1.show_time()        

# 10.) Write a program with classes Fan and AC, both having turn_on() method.

class Fan:
    def turn_on(self):
        print("Turning On the Fan!")

class AC:
    def turn_on(self):
        print("Turning On the AC!")

f1 = Fan()
f1.turn_on()

a1 = AC()
a1.turn_on()



# INTERMEDIATE (11–20):

# 11.) Write a program to create a list of objects (Dog, Cat) and call sound() using loop.

class Dog:
    def sound(self):
        print("Dogs Bark!")
        
class Cat:
    def sound(self):
        print("Cats Meow!")
        

for i in [Dog(),Cat()]:
    i.sound()

# 12.) Write a program with Vehicle and child class Car overriding move() method.

class Vehicle:
    def move(self):
        print("Vehicle is Moving...!")

class Car(Vehicle):
    def move(self):
        print("Car is Moving...!")
    
c1 = Car()
c1.move()

# 13.) Write a program with Animal ---> Dog ---> Puppy and override sound() in each.

class Animal:
    def sound(self):
        print("Animal Makes Sound!")

class Dog(Animal):
    def sound(self):
        print("Dogs Bark!")

class Puppy(Dog):
    def sound(self):
        print("Puppies Barks too!")

p1 = Puppy()
p1.sound()


# 14.) Write a program with Shape and child classes Circle and Square, each having area().

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("The Area of Circle is pi*r**2.")

class Square(Shape):
    def area(self):
        print("The Area of Square is l**2.")
    
c1 = Circle()
c1.area()

s1 = Square()
s1.area()


# 15.) Write a program using loop polymorphism with Boy, Dog, Cow using eat().

class Boy:
    def eat(self):
        print("Boy eats Pizza.")

class Dog:
    def eat(self):
        print("Dog eats Bone.")

class Cow:
    def eat(self):
        print("Cow eats Grass.")

for x in [Boy(),Dog(),Cow()]:
    x.eat()

# 16.) Write a program with Employee and child classes Manager, Developer using work().

class Employee:
    def work(self):
        pass

class Manager(Employee):
    def work(self):
        print("Manager manages and supervise all the work!")
        
class Developer(Employee):
    def work(self):
        print("Developer writes and tests the code!")

m1 = Manager()
m1.work()

d1 = Developer()
d1.work()
    
# 17.) Write a program where different classes Bird, Plane use same method fly() (duck typing).

class Bird:
    def fly(self):
        print("Bird is Flying...!")
class Plane:
    def fly(self):
        print("Plane is Flying...!")

b1 = Bird()
b1.fly()

p1 = Plane()
p1.fly()

# 18.) Write a program to demonstrate built-in polymorphism using len() on string and list.

print(len("Namaste!!"))
print(len(["apple","mango","litchi"]))

# 19.) Write a program to demonstrate + operator with numbers and strings.

print(5+3)
print("Hello" + "Zeeson")

# 20.) Write a program where list contains mixed objects (Car, Dog, Human) and all use move().

class Car:
    def move(self):
        print("Car Moves!")

class Dog:
    def move(self):
        print("Dog Moves!")

class Human:
    def move(self):
        print("Human Moves!")

for x in [Car(),Dog(),Human()]:
    x.move()

# ADVANCED (21–30):

# 21.) Write a program with abstract class Animal having sound() and implement in Dog, Cat.
# 22.) Write a program where method overriding happens in Shape → Rectangle → Square.
# 23.) Write a program showing runtime polymorphism using BankAccount → SavingsAccount with interest().
# 24.) Write a program using duck typing where Duck, Robot both have walk().
# 25.) Write a program where Payment class has method pay() overridden by Cash, Card, UPI.
# 26.) Write a program using loop to call play() for objects Guitar, Piano, Drum.
# 27.) Write a program showing polymorphism in function arguments (pass different objects with same method).
# 28.) Write a program where Person, Robot both have work() and are used in same loop.
# 29.) Write a program using built-in polymorphism with * operator (number vs string).
# 30.) Write a program combining inheritance + overriding + loop polymorphism in one example.