# Inheritance => The child class inherits the parent class

#Multiple Inheritance:

# class ABC:
#     name = "ABC"

# class Parent1:
#     name = "Parent1"
#     def Parent1(self):
#         print("Parent1 is called!!")

# class Parent2(ABC):
#     name = "Parent2"
#     def Parent2(self):
#         print("Parent2 is called!!")

# class Child(Parent2,Parent1):
#     # name = "Child"
#     def Child(self):
#         print("Child Method called")

# c1 = Child()
# print(c1.name)

# #MRO => Method Resolution Order i.e. mro() 

# print(Child.mro())


# Mutlilevel Inheritance:

class GrandParent:
    name = "GrandParent"
    def GrandParent(self):
        print("Grandparent Class Called")

class Parent(GrandParent):
    name = "Parent"
    def Parent(self):
        print("Parent Called")

class Child(Parent):
    name = "Child"
    def Child(self):
        print("Child called")

c1 = Child()
print(c1.name)
c1.GrandParent()

p1 = Parent()
print()