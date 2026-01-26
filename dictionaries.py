# Dictionaries

# 1. Definition {key : value pairs}

# A dictionary stores data in key : value pairs.

# For Example:
person = {"name":"Zeeson","age": 22,"address":"Koteshwor, Kathmandu-32"}
print(person)
print(person["name"])

# here, "name","age" and "address" are keys
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


# 6. Dictionary Methods (CORE)

# There are three core dictionary methods that is:
# keys()
# values()
# items()


# 6.1 keys() -> recap

mountains = {
    'Mount Everest': 8848,
    'K2': 8611,
    'Kangchenjunga': 8586,
    'Lhotse': 8516
}

x = mountains.keys()
print(x)

# Shows all keys
# Used for checking and looping

# 6.2 values() method
# values() returns all the values in the dictionary.

y = mountains.values()
print(y)

# When to use values()

# When we don’t care about keys
# When we want to:
# calculate
# count
# search values

# Example:

if 8848 in mountains.values():
    print(True)
else:
    print(False)


# 6.3 items() method (IMPORTANT)

# items() returns both key and value together as pairs.

bike = {
    "brand": "Giant",
    "model": "TCR Advanced Pro",
    "year": 2024,
    "electric": False
}

print(bike.items())

# Each item is a tuple: (key, value)

# It allows us to work with key and value at the same time.

# Example:

for key, value in bike.items():
    print(f"key = {key} , value = {value}")

# 7.) Looping Through Dictionaries:

students = {
    "John": "A",
    "Jane": "B",
    "Doe": "A+"
}

for i in students:         # This gives Keys only
    print(i)

# Its same as using keys():

for i in students.keys():
    print(i)


# When accessing values later using the key:

for i in students:         
    print(f"{i} => {students[i]}")                            # This returns keys with their respective values!


# 7.2 Looping through values

for value in students.values():
    print(value)

# 7.3 Looping through key–value pairs 

for key, value in students.items():
    print(key, "=>", value)

# This uses tuple unpacking

# Note: dictionaries are not index-based!!

# Using len():

data = {"a": 1, "b": 2, "c": 3}
print(len(data))

keys = list(data.keys())

for i in range(len(keys)):
    print(i, keys[i], data[keys[i]])

# 8) Dictionary Comprehension:

# Dictionary comprehension is a compact way to create dictionaries using logic.

# Basic syntax: new_dict = {key: value for item in iterable}

sqr = {i: i**2 for i in range(5)}
print(sqr)


# 8.1 Filtering data (using if)

even_sqr = {i: i**2 for i in range(10) if i%2 == 0}
print(even_sqr)


# 8.2 Tranforming the values

cars = {"Toyota":1500000,"Mercedes":2000000}              # Original Dictionary
new_cars = {item:price + 200000 for item,price in cars.items()}
print(new_cars)


# 8.3 Converting list to dictionary

num = [1,2,3,4,5,6]
new_dict = {item: item + 1 for item in num}
print(new_dict)


# 9. Nested Dictionaries:

# a dictionary inside another dictionary

# 9.1 Dictionary inside the dictionary:

students = {
    "std1":{"name":"Zeeson","Age":22},
    "std2":{"name":"Sunil","Age":21}
}

print(students["std1"])
print(students["std1"]["name"])


# 9.2 Looping through nested dictionaries

for std_id,info in students.items():
    print(f"std_id ={std_id}, Name = {info['name']}, Age = {info['Age']}")



