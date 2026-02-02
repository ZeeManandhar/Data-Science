# Loops Pratice Questions:

# BASIC LEVEL (1–15):

# Write a program to print numbers from 1 to 10 using a for loop.

for i in range(1,11):
    print(i)

# Write a program to print numbers from 10 to 1 using a for loop.

for n in range(10,0,-1):
    print(n)

# Write a program to print all elements of a list using a for loop.

elements = ["Mountains","Trees","Forests","Lakes"]

for element in elements:
    print(element)

# Write a program to print each character of a string using a loop.

str1 = "PYTHON"

for char in str1:
    print(char)

# Write a program to print only even numbers from a list.

numbers = [3,6,9,12,15,18,21,24,27,30]

for n in numbers:
    if n%2 == 0:
        print(n)


# Write a program to print only odd numbers between 1 and 20.

for i in range(1,21):
    if i%2 != 0:
        print(i)

# Write a program to print the square of each number in a list.

l1 = [2,4,6,8,10,12,14,16,18,20]

for i in l1:
    result = i**2
    print(result)

# Write a program to count how many elements are in a list using a loop.

list1 = ["Zee","son","Steph","Lebron","Giannis","Shaq"]

count = 0

for i in list1:
    count += 1

print(count)


# Write a program to print numbers from 0 to 5 using range().

for num in range(0,6,1):
    print(num)

# Write a program to print numbers from 5 to 15 using range(start, stop).

for i in range(5,16):
    print(i)

# Write a program to print numbers from 1 to 10 with a step of 2.

for i in range(1,11,2):
    print(i)

# Write a program to print all keys of a dictionary using a loop.

dict_1 = {
    "Brand":"Bajaj",
    "Name" : "NS400Z",
    "Made Year": 2012
}

for i in dict_1:
    print(i)

# Write a program to print all values of a dictionary using a loop.

for i in dict_1.values():
    print(i)

# Write a program to print both key and value from a dictionary.

for key,value in dict_1.items():
    print(f"{key} = {value}")


# Write a program to print “Hello” five times using a while loop.

i = 1

while i <= 5:
    i += 1
    print("Hello")
    

# INTERMEDIATE LEVEL (16–30)

# Focus: logic + conditions inside loops

# Write a program to find the sum of all numbers in a list.

# Write a program to count how many even and odd numbers are in a list.

# Write a program to count how many positive and negative numbers are in a list.

# Write a program to find the largest number in a list using a loop.

# Write a program to find the smallest number in a list using a loop.

# Write a program to count how many times a specific number appears in a list.

# Write a program to print numbers from 1 to 50 but skip multiples of 5.

# Write a program to stop printing numbers when number 7 appears.

# Write a program to print all numbers except 3 using continue.

# Write a program that keeps asking the user for input until they type "exit".

# Write a program that keeps asking for a positive number until user enters one.

# Write a program to reverse a string using a loop.

# Write a program to count vowels in a string using a loop.

# Write a program to print a multiplication table of a number.

# Write a program to validate user input until they enter a number between 1 and 10.

# LOGICAL / REAL-WORLD LEVEL (31–40)

# Focus: thinking + flow control

# Write a program to check if a number exists in a list using a loop.

# Write a program to remove all negative numbers from a list using a loop.

# Write a program to print duplicate elements from a list.

# Write a program to count the frequency of each element in a list.

# Write a program to simulate a login system (3 attempts max).

# Write a program to display a menu repeatedly until user exits.

# Write a program to build a simple calculator using a loop and menu.

# Write a program to keep adding numbers until user types "done", then print the sum.

# Write a program to build a menu-driven number list manager
#   (add / view / remove / exit).

# Write a program to build a menu-driven To-Do List using loops and conditions.