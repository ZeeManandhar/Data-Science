# Dictionaries ---- Practice Questions:


# BASIC LEVEL

# Write a program to create a dictionary with 5 key–value pairs and print it.

students = {
    'Name':'Zeeson Manandhar',
    'Age': 22,
    'Address': "Koteshwor",
    'E-mail': "zeeson.manandhar11@gmail.com",
    'Contact no.': "+977-9841111111"
}

print(students)


# Write a program to create an empty dictionary and add three items to it.

fruits_colors = {}

fruits_colors["Apple"] = "Red"
fruits_colors["Banana"] = "Yellow"
fruits_colors["Grapes"] = "Green & Purple"

print(fruits_colors)

# Write a program to access the value of a given key from a dictionary.

car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2019,
    "color": "blue"
}

print(car['brand'])
print(car['year'])

# Write a program to check whether a key exists in a dictionary.

print("model" in car.keys())

# Write a program to print all keys of a dictionary.

X = car.keys()
print(X)

# Write a program to print all values of a dictionary.

Y = car.values()
print(Y)

# Write a program to print all key–value pairs of a dictionary.

Z = car.items()
print(Z)

# Write a program to count the number of key–value pairs in a dictionary.

count = 0
for item in car:
    count += 1
print(count)

# Write a program to safely access a key using .get().

mountains = {
    "Everest": 8848,
    "K2": 8611,
    "Kangchenjunga": 8586,
    "Lhotse": 8516,
    "Makalu": 8485
}

result = mountains.get("Everest")
print(result)

# Write a program to copy a dictionary into another dictionary.

new_dict = mountains.copy()
print(new_dict)


# INTERMEDIATE LEVEL

# Write a program to add a new key–value pair to an existing dictionary.

bikes = {
    "model": "NS200",
    "brand": "Bajaj",
    "year": 2021,
    "electric": False
}

bikes["colors"] = "silver,red & black"

print(bikes)

# Write a program to update the value of an existing key.

bikes["year"] = 2022
print(bikes)

# Write a program to remove a key using del.

del bikes["brand"]

print(bikes)

# Write a program to remove a key using pop() and print the removed value.

rem_val = bikes.pop("electric")
print(bikes)
print(rem_val)

# Write a program to clear all elements of a dictionary.

bikes.clear()
print(bikes)

# Write a program to loop through all keys in a dictionary.

players_scores = {
    'Alice': 150,
    'Bob': 200,
    'Charlie': 120
}

for item in players_scores.keys():
    print(item)

# Write a program to loop through all values in a dictionary.

for value in players_scores.values():
    print(value)

# Write a program to loop through all key–value pairs and print them.

for key , value in players_scores.items():
    print(f"key = {key}, value = {value}")

# Write a program to merge two dictionaries into one.

dict_1 = {
    "Name": "Salman Khan",
    "DOB": "1975-01-01",
}

dict_2 = {
    "country": "India",
    "Profession" : "Actor"
}
dict_1.update(dict_2)
print(dict_1)

# Alternative Way: 
new_dict = {**dict_1,**dict_2}
print(new_dict)

# Write a program to create a dictionary from two lists (keys list and values list).

list1 = ["Name", "Age", "Profession"]
list2 = ["Zeeson", 22, "Student"]

data = {}

for i in range(len(list1)):
    data[list1[i]] = list2[i]

print(data)



# LOGIC-BASED (IMPORTANT) 
# Write a program to count the frequency of each character in a string.

# Write a program to count the frequency of each word in a sentence.

# Write a program to find the key with the maximum value in a dictionary.

data = {
    "a":5,
    "b":15,
    "c":6
}
val = list(data.values())
max_value = max(val)
print(max_value)

l1 = []

for key, value in data.items():
    if value == max_value:
        l1.append(key)

print(f"The key with maximum value is {l1}")


# Write a program to find the key with the minimum value in a dictionary.

data1 = {
    "a": 6,
    "b": 7,
    "c": 8
}
min_val = min(data1)
print( f"The minimum value is {data1[min_val]} and its key is {[min_val]}")


# Write a program to check if a dictionary is empty or not.

student_scores = {
    "Alice": 95,
    "Bob": 88,
    "Charlie": 92
}

if len(student_scores) == 0:
    print("The Dictionary is empty")
else:
    print("Not Empty")


# Write a program to create a dictionary of numbers (1–10) and their squares.

num = {}

for i in range(1,11):
    num[i] = i**2
print(num)

# Write a program to create a dictionary of numbers and their cubes using dictionary comprehension.


cube_num = {item : item**3 for item in range(1,11)}
print(cube_num)

# Write a program to remove all duplicate values from a dictionary.

dict_1 = {"a": 10, "b": 20, "c": 10, "d": 30}
rem_val = {}
checked_val = set()

for key ,value in dict_1.items():
    if value not in checked_val:
        rem_val[key] = value
        checked_val.add(value)

print(rem_val)

# Write a program to sort a dictionary by its keys.

dict_1 = {
    'a' : 1,
    'c' : 3,
    'd' : 4,
    'b':2
}

dict_keys = dict_1.keys()
sort_keys = sorted(dict_keys)
print(sort_keys)

new_dict = {
}

for item in sort_keys:
    new_dict[item] = dict_1[item]

print(new_dict)
   

# ADVANCED / REAL-WORLD (31–40)

# Write a program to store student details (name, age, marks) using a nested dictionary.

# Write a program to access and print the marks of a specific student.

# Write a program to loop through all students and print their details.

# Write a program to simulate a simple login system using a dictionary.

# Write a program to count how many times each element appears in a list using a dictionary.

# Write a program to create a dictionary that stores even numbers as keys and their squares as values.

# Write a program to convert a list of tuples into a dictionary.

# Write a program to check whether two dictionaries are equal or not.

# Write a program to create a dictionary comprehension that filters values greater than 10.

# Write a program to build a frequency dictionary for the string "mississippi".