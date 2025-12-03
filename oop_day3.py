# Encapsulation = The concept of hiding the data i.e. (attributes and methods)
# To hide the data, we use __ prefix


class Credentials:
    username = "Zeeson"
    __password = "Zeeson123"

    new_password = __password # The hidden data can be accessed by Other attributes and methods inside the class

   
cre = Credentials()
print(cre.new_password)



# Constructor:
# Constructor is a special kind of method in OOP that automatically executes when an object is created

# There is only one constructor and that is __init__ (you have use this __init__everytime).

# The main use of constructor is to create the object attributes


class Student:
    def __init__(self, name, age, grade, gender):
        self.name = name
        self.age = age
        self.grade = grade
        self.gender = gender

    def display(self):
        print(self.name)
        print(self.age)
        print(self.grade)
        print(self.gender)

s1 = Student("Zeeson",22,"A+","male")
s1.display()






