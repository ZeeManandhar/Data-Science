# Lists:
# Lists are python built-in Data Structure that is used to store multiple values in single variable.
# Lists are initialized using square brackets [ ].
# For example:
 
players = ["Steph Curry","Lebron James","Kevin Durant","Giannis Antetokumpho"]
print(players)

print(f"Among these the GOAT is {players[0]}") # Python uses 0-based indexing


# Every item in a list has a fixed position
# Position is called index
# Index starts from 0

print(players[-1]) # This is Called Negative Indexing!! Works backward

# Lists are muteable, that means it can be edited, updated or replaced once the list has been Created.

players[1] = "Michael Jordan"
print(players)


# Duplicate values are allowed in python list, meaning it can store same values more than one time.

numbers = [1,2,3,3,3,4,4,4,4,5]
print(numbers)

# A single list can store different types of data together.
# Unlike some languages, Python lists are not restricted to one data type.

data = ["Zeeson",'Manandhar', 22, True]
print(data)

# Nested List 

# A Nested list stands for a list inside a list.
# For Example:

info = ["Curry","James","Durant",[37,41,38]]
print(info)

print(info[3][1])

# Quick Practice:

matrix = [[1, 2], [3, 4]]
result = matrix[1][1]
print(result)

# List Operations:
#  1️. Adding Items
# Adds one item at the end of the list.
# Method a: append()

matrix.append([5,6])
print(matrix)

# Method b: insert()
# Adds an item at a specific index.


matrix.insert(1, [2,2])
print(matrix)

# Note: the difference between append and insert method in list, is append adds the item at the end while in contrast, insert adds the item to the given index.

# 2️. Removing Items
# There are three main ways to remove items from a list.

# a.) remove() – Remove by VALUE
# Removes the first occurrence of a value.
# Example:

matrix.remove([2,2])
print(matrix)

# b.) pop() – Remove by INDEX

matrix.pop(0)
print(matrix)

# c. del keyword
del matrix

# Difference Between these remove operations:

# remove() ---> removes by value
# pop() ------> removes by index
# del() ------> removes index or full list

# Quick Practice:

nums = [10, 20, 30, 40]

# Remove 20 using remove()
# Remove last item using pop()
# Print final list

nums.remove(20)
nums.pop()
print(nums)

# 3. len() (Length of List)
# It returns the total number of items in a list.

names = ["zeeson","sunil","niraj","arbind"]
print(len(names))

# Important Point
# len() returns a value
# It does not change the list

# Quick Practice
nums = [10, 20, 30, 40, 50]

# Print length of nums
output = len(nums)
print(output)

# 4️. count() Method
# Counts how many times a value appears in a list.

names = ["Ram", "Shyam", "Ram", "Hari"]

# Count how many times "Ram" appears
x = names.count("Ram")
print(x)


# Quick Practice:

data = ["pen", "book", "pen", "pencil"]

# 1. Print length
# 2. Count "pen"
# 3. Check if "eraser" exists

print(len(data))
print(data.count("pen"))

print("eraser" in data)


# 5. sort() 

# sort()-------> Sorting a List

# It arranges the list items in ascending order (by default).

sports = ["Football","Basketball","Badminton"]
sports.sort()
print(sports)

sports.sort(reverse=True) # Works in descending order
print(sports)

# using sort method with key argument:

fruits = ["apple","mango","banana","avocado","pear"]
fruits.sort(key=len)
print(fruits)


# Important Rule
# sort() modifies the list, so it returns None

# 6. reverse() – Reversing Order
# It reverses the current order of items.

sports.reverse()
print(sports)

# 7. Copy Method () 

# Assigning a list using = creates a reference to the same list, not a copy. 
# To create a new list, methods like copy() should be used.

a = [1,2,3,4,5,6,7,8,9] 
b = a.copy()
a.append(10)
print(b)
print(a)

# Alternative method for Copy method:

a = [10,20,30,40,50,60]
b = list(a)
a.append(10)
print(b)
print(a)

# Another alternative way for Copy method:
# List Slicing 
a = [11,22,33,44,55,66]
b = a[:]
print(b)
print(a)

# 8. Clearing vs Deleting a List

# a. clear() — Clear the List

# Removes all elements from the list

# The list still exists
# Memory reference stays the same

# For Example:

num = [5,10,15,20,25,30]
num.clear()
print(num)         # Gives an empty list[] as an Output

# b. del — Delete the List

# Deletes the entire list variable
# Removes reference from memory

# del num
# print(num)

# Difference between clear and del method.

# clear()  ----> Empties list, keeps variable
# del list ------> Deletes list completely

# 9️. List Slicing (start : end : step)

# Slicing means extracting a part of a list.
# Syntax:
# list[start : end : step]

# Point to be Noted:
# start value is always inclusive and End value is always exclusive

# Simple Example: 

number = [2,4,6,8,10,12,14,16,18,20]
number[0:4]
print(number)

# If Start value is not given:
print(number[:4])   # starts from 0th index

# If End Value is not given:
print(number[1:]) # Starts for 1st index to last index

# Negative Slicing:

print(number[-4:-1])

print(number[-1:-4]) # throws an empty list

# Key Rule (Very Important)

# Slicing moves in the direction of the step.
# If no step is given, the default step is +1 (left → right).

# Step Value

print(number[::3])

print(number[-1:-4:-1]) # -1 as Step value reverses the list.


# LOOPS in List:

veggies = ["Tomatoe","Onion","Garlic","Potatoe"]

for i in veggies:
    print(i)

for i in range(len(veggies)):
    print(veggies[i])

# Alternative way
# if we dont want to use range(len()), use enumerate function, this gives both index with value of list:
for index, value in enumerate(veggies):
    print(index, value)


# Next Example:
nums = [1, 2, 3]
for i in range(len(nums)):
    nums[i] = nums[i] * 2
print(nums)

# same example with alternative way:

nums = [1, 2, 3]
y = []
for i in range(len(nums)):
    x = [nums[i] * 2]
    y += x

print(y)

# Next Example:

nums = [10, 25, 30, 45]

# Using Comparison Operator in list looping 
for n in nums:
    if n > 20:
        print(n)


nums = [1, 2, 3]
y = []





# List Comprehension

# List comprehension is a short and clean way to create a new list from another list.

number = [1,2,3,4,5,6]
even = [n%2 ==0 for n in number]
print(even) # This gives True/False for number list

# if we want to add the value, while the condition is True. we use:
# Syntax/Formula: [ VALUE   for VARIABLE in ITERABLE   if CONDITION ]
# Store n, for each n in number, if n is even
# The n comes first because it tells Python what value should be added to the new list.
# Filtering values using if condition:

even = [n for n in number if n%2==0]
print(even) # This gives the even number values

# To print square of numbers in list

num = [2,4,6,8]
sqr = [n**2 for n in num]
print(sqr)


# match case
# Match case is similar to c switch case and if else
# we define a variable in match and the value of that matches with case is executed

# a = float(input("Enter the First number? "))
# b = float(input("Enter the second number? "))

# choose = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for Division:"))

# match choose:
#     case 1:
#         print(a+b)
#     case 2:
#         print(a-b)
#     case 3:
#         print(a*b)
#     case 4: 
#         print(a/b)
#     case _:
#         print("invalid input! please retry it")

# Loops
# Loops are used to execute a same block of code repeateadly

# For loop => when we know the conditions i.e. start and stop conditions
# While Loop => when we know the stopping condition
# Iterator - it is simply a variable that stores a value while the loop is running
# Iterable - Group data type in which the loop is running
# Iteration - one complete execution of a loop

# list1 = [1,2,3,"Zeeson",[7,8,9]]
# # syntax of for loop
# # for iterator in iterable:
# #     statements

# for i in list1:
#     print(i)

# note: In dictionary, it only executes the keys #list1(i).get()

# range(Start,End, Step) => provides range of elements
# If one value is provided in range(), it will be for end value. End value is always is exclusive

