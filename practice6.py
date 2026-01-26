# Dictionaries ---- Practice Questions:


# BASIC LEVEL (1–10)

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


# INTERMEDIATE LEVEL (11–20)

# Write a program to add a new key–value pair to an existing dictionary.

# Write a program to update the value of an existing key.

# Write a program to remove a key using del.

# Write a program to remove a key using pop() and print the removed value.

# Write a program to clear all elements of a dictionary.

# Write a program to loop through all keys in a dictionary.

# Write a program to loop through all values in a dictionary.

# Write a program to loop through all key–value pairs and print them.

# Write a program to merge two dictionaries into one.

# Write a program to create a dictionary from two lists (keys list and values list).

# LOGIC-BASED (IMPORTANT) (21–30)

# Write a program to count the frequency of each character in a string.

# Write a program to count the frequency of each word in a sentence.

# Write a program to find the key with the maximum value in a dictionary.

# Write a program to find the key with the minimum value in a dictionary.

# Write a program to check if a dictionary is empty or not.

# Write a program to create a dictionary of numbers (1–10) and their squares.

# Write a program to create a dictionary of numbers and their cubes using dictionary comprehension.

# Write a program to remove all duplicate values from a dictionary.

# Write a program to sort a dictionary by its keys.

# Write a program to sort a dictionary by its values.

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