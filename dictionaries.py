# Dictionaries

# 1. Definition {key : value pairs}

# A dictionary stores data in key : value pairs.

# For Example:
person = {"name":"Zeeson","age": 22,"address":"Koteshwor, Kathmandu-32"}
print(person)
print(person["name"])

# here, "name","age" and "äddress" are keys
# "Zeeson", 22 , Koteshwor, Kathmandu-32 are its values respectively.

# Keys are like “labels”. Values are the actual data.

# Real-world analogy:

# A dictionary is like:
# ID card / student record / database row
# Field name = key ("name", "age", "citizenship_no")
# Field value = value ("Zeeson", 20, "12345")


# 2.) Creating the Dictionary:

# a. Use curly braces { }
# b. Each item is written as key : value
# c. Separate pairs with commas

student = {
    "name":"Zeeson Manandhar",
    "program" : "BSc.IT",
    "grade": "First Class Honours"
}

print(student)

# 2.1) Creating an Empty Dictionary

dct = {}      # This Creates Empty Dictionary
print(dct)
print(type(dct))


# 2.2) Creating dictionary using dict() constructor

# Python also provides a built-in function dict().

bike = dict(name="NS200", brand = "Bajaj", CC = 200, price = 450000)
print(bike)

# 2.3) Duplicate keys behavior (overwrite rule):

# Dictionary keys must be unique.
# If the key is repeated, Python keeps the last value.

# For Example:

student = {
    "name": "Zeeson",
    "age": 20,
    "age": 22
}
print(student)

# "age": 20 is overwritten by "age": 22
# No error is raised
# Earlier value is lost

# 2.4) Valid vs invalid keys (immutability rule)
# Valid keys

# Keys must be immutable (cannot change).
# Allowed:strings,numbers,tuples (with immutable content)

data = {
    "name": "Zeeson",
     1: "one",
    (1, 2): "tuple key"
}

print(data)


# Invalid keys:

# Not allowed:
# list
# set
# dictionary

# data = {
#     [1,2,2,3]:"list Keys",
#     {"Hi",22}:"Set Keys"
# }

# print(data)   # this gives error i.e. TypeError: unhashable type: 'list'


# Accessing the Dictionary Data:

# 3.1 Accessing values using keys

# Syntax: dict_name[key]

# Example:

consultancy = {
    "name":"XYZ Consultancy",
    "address":"Putalisadak,KTM",
    "contact no." : 9820222222
}

print(consultancy["name"])
print(consultancy["contact no."])


# 3.2 KeyError problem

# If we try to access a key that does not exist, Python throws an error.

# print(consultancy["email"])

# 3.3 Safe access using get()

# To avoid KeyError, We can use .get().

print(consultancy.get("email"))               # this doesnot show error even if the keys are missing

# 3.4 Default values with get()

print(consultancy.get("email","Unavailable"))

# Using keys() method:

student = {
    "name":"Hari Bahadur",
    "student id": 101,
    "contact no.":985699999
}

print(student.keys())

# We use .keys() when:
# we want to see what data exists
# we want to check if a key is present
# we want to loop through keys

# For Example:

if "age" in student.keys():
    print("Age Exists!!")
else:
    print("Doesnot Exist!!")

# 3.5 Converting keys to a list

keys_list = list(student.keys())
print(keys_list)


# 4) Adding & Updating Data

# 4.1 Adding a new key-value pair

# Syntax: dict_name[new_key] = value

std = {
    "Name":"Zeeson Manandhar",
    "Program":"BSc.IT",
    "Age": 22
}

std["Grade"] = "First Class Honours"
print(std)

# 4.2 Updating an existing key
# Same syntax, but key already exists.

std["Age"] = 21
print(std["Age"])


# 4.3 Dynamic updates (important concept)
# We can update values using variables.

key_name = "Age"
std[key_name] = 25
print(std)

# 4.4 Using update() method
# update() allows adding multiple items at once.

std.update({
    "Address":"Tinkune, Kathmandu",
    "Currently_active": True,
    "Name":"Zeeson Mdhr"
})

print(std)

# This Update method:
# Adds new keys if missing
# Updates existing keys if present


# 5) Removing Data from a Dictionary

# There are multiple ways to remove data from a dictionary.
# Each exists for a specific reason.

# 5.1 del keyword
# del removes a key-value pair by key.

College = {
    "Name":"Ismt College",
    "Location":"Tinkune",
    "Established_Year": 2010
}

del College["Established_Year"]

print(College)

# 5.2 pop() method
# pop() removes a key and returns its value.

car = {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964
}

val = car.pop("year")

print(car)
print(val) # The key is removed but its value is returned.

# 5.3 popitem() method
# popitem() removes the last inserted key-value pair.

fruit_colors = {
    "Apple": "Red",
    "Banana": "Yellow",
    "Cherry": "Red",
    "Orange": "Orange",
    "Grape": "Purple"
}

rem_value = fruit_colors.popitem()

print(fruit_colors)
print(f"The last removed value is: {rem_value}")

# This popitem():

# Returns a tuple (key, value)
# Removes last item
# Useful in stack-like operations

# 5.4 clear() method
# clear() removes everything.

fruit_colors.clear()                 # returns empty dictionary
print(fruit_colors)


