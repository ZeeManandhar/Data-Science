# Loops:

# A loop repeats the same block of code again and again.
# Without loops, we would write the same line many times.
# With loops, we write it once, and Python repeats it.

# For example (using for loop):

x = [1,2,3]

for n in x:
    print(n)

# Logic in plain words:

# Python takes the list x = [1, 2, 3]
# It picks the first item , puts it in n then prints it
# Then picks the next item , prints it
# Repeats until items finish

# 4) Example (while loop):

count = 0

while count <= 3:
    print(count)
    count += 1


# Logic in plain words:
# Start count at 0
# While count is 1,2,3 --------> print it
# Increase count each time
# Stop when count becomes 4 (condition becomes false)

# 2. Key Terms To Understand:

# We must understand three core words:

# iterable
# iteration
# iterator 

# 2.1) Iterable
# An iterable is anything that contains multiple items and can be looped one by one.

# Common iterables:

# list
# string
# dictionary
# tuples

# Examples of iterables
[10, 20, 30]      # list
"Zeeson"         # string
{"a": 1, "b": 2} # dictionary

# something that python can go though item to item i.e. one by one

# 2.2) Iteration (the ACT of looping)

# Iteration means: One single round of a loop.

for x in [1, 2, 3]:
    print(x)

# What happens :
# 1st iteration, x = 1
# 2nd iteration, x = 2
# 3rd iteration, x = 3

# Each round equals to one iteration.

# 2.3) Iterator (the VARIABLE that holds items)

# The iterator is the loop variable that temporarily stores each item.

# Example:

for letter in "ABC":
    print(letter)


# Here:
# "ABC" = iterable
# letter  = iterator
# Values taken by letter ------ "A", "B", "C"

# Iterator is just a name or temporary variable that holds one item at a time.

# 3.) For Loops Basics:

# Syntax for (for loop ) :

# for variable in iterable:
#     statement

# Take items one by one from the iterable
# Store each item in variable
# Run the indented code for each item
# Indentation (spacing) is mandatory in Python.

# 3.1) Loop over a list (Example)

items = ["pen","pencil","eraser","books"]

for i in items:
    print(i)

# Step-by-step logic:

# Python looks at the list i.e. items = ["pen","pencil","eraser","books"]
# First iteration -------> n = 10 --------> print 10
# Second iteration -------> n = 20 --------> print 20
# Third iteration ---------> n = 30 --------> print 30
# List finished -----------> loop stops


# 3.2) Loop over a String: 

# Strings are also iterables
# Python takes one character at a time

# Example:

name = "Zeeson"

for char in name:
    print(char)

# Char becomes "Z","e","e","s","o","n" , one after one.

# 4. Range() in Loops

# range() is used when you want to loop a specific number of times.

# 4.1 range() example:

for i in range(5):                  # range gives 0,1,2,3,4 
    print(i)

# What happens:
# Starts from 0
# Stops before 5
# Prints: 0 1 2 3 4

# range(n) = numbers from 0 to n-1

# 4.2 range(Start , Stop)

for n in range(5,15):
    print(n)

# rule:  range(start, stop) -----> stop value is never included.


# 4.3 range(start, stop, step)

for i in range(1,10,2):
    print(i)

# Starts at 1
# Increases by 2 each time
# Stops before 10

# 4.4 range() with negative numbers

# range() always moves from start toward stop using step
# If it cannot move in that direction, nothing runs


# case 1 - when range is range(-5)

# for i in range(-5):
#     print(i)         

# The loop never runs:
# range(n) means: start at 0, stop before n
# Here n = -5
# Python tries: 0 --> -5
# But 0 is already greater than -5
# So Python has no numbers to generate


# case 2 - when range is range(-5,0)

for i in range(-5,0):
    print(i)

# Step-by-step:
# Start = -5
# Stop = 0 (not included)
# Step = +1 (default)

# case 3 - when range is range(-5, -1)

for n in range(-5,-1):
    print(n)

# case 4 - when range is range(-5, -1, -1)

for n in range(-5,-1,-1):
    print(n)

# here, loop never runs because:

# Start = -5
# Stop = -1
# Step = -1 (move backward)

# You are already at -5
# Moving backward means -6, -7...
# You will never reach -1

# Thus, Loop runs 0 times.

# case 5 - when range is range(-1, -6, -1)

for i in range(-1, -6, -1):
    print(i)

# Step-by-step:
# Start = -1
# Step = -1
# Stop before -6

# case 6 - when range is range(0, -5, -1)

# Universal rule: 

# For Positive step (+1, +2, ...)
# start < stop  ---> loop runs
# start > stop  ----> returns empty or nothing

# For Negative step (-1, -2, ...)
# start > stop  ---> loop runs
# start < stop  ----> returns empty or nothing


# 5.) for Loop with Dictionary

# A dictionary is also iterable, but it works slightly differently than lists and strings.

# Example:

student = {
    "Name": "Zeeson Manandhar",
    "Age" : 22,
    "Program": "Bsc.IT"
}

# 5.1) looping over Keys in Dictionary (Default Behaviour)

for key in student:
    print(key)

# This returns only the keys of dicitonary.

# Plain rule: for x in dict: --> loops over keys.

# 5.2) Looping over Values

for value in student.values():
    print(value)

# This gives values only.

# 5.3) Looping over both key and value

for key, value in student.items():
    print(f"{key} = {value}")

# .items() gives pairs (key, value)
# Two variables are needed  

# 6.) while Loop Basics

# A while loop repeats as long as a condition is True.

# Basic syntax:

# while condition:
#     statement

# Explanation:

# Check the condition
# If True, run the indented code.
# Go back and check again.
# Stop when condition becomes False.

# Example:

count = 1

while count <= 3:
    print(f"{count} Execution!")
    count += 1

# Explanation:
# Check the condition
# If True, run the indented code
# Go back and check again
# Stop when condition becomes False


# Infinite Loop Example with Count:

# count = 1

# while count <= 3:
#     print(count)

# This gives infinite loop because the count value remains 1 and condition stays True i.e. 1 <= 3. Thus, the loop runs indefinately.

# Infinite Loop Concept: 

user = input("Enter your Name please: ").strip()

while True:
    print(f"Welcome {user}!")
    break
    
# This loop:
# Has no stopping condition
# Runs forever unless stopped using break

# break immediately stops a loop, even if the condition is still True.


# 7.) Input-Driven while Loop

# This is one of the most important real-world loop patterns.

# 1) The idea (plain words)

# If We want to:
# Keep asking the user for input
# Stop only when the user types "exit"
# This is why while is perfect.

# while True:
#     name = input("Type Something: ")
#     print(name)

# The loop never ends!

# using break to terminate the loop

while True:
    text = input("Type Something: ").strip().lower()
    print(text)

    if text == "exit":
        break

# 8.) Loop Controls

# 8.1) continue — skip this iteration

# Skips the current iteration
# Goes directly to the next iteration
# Loop itself does not stop

# Example 1 (using while loop):

x = 0
while x < 5:
    x = x + 1
    if x == 3:
        continue
    print(x)

# Example 2 (using for loop):

for x in [1, 2, 3, 4]:
    if x == 2:
        continue
    print(x)


# 8.2) Pass -- do nothing (placeholder)

# Does nothing
# Used when syntax requires a statement
# Often used as a placeholder


# Example (using for loop):

for x in [1, 2, 3]:
    if x == 2:
        pass
    print(x)


# Example (using while loop):
num = 0

while num < 7:
    if num == 2:
        pass
    print(num)
    num += 1

# 8.3 Comparison between all the Loop Controls:

# break	--->Exit loop completely
# continue ----> Skip current iteration
# pass ----> Do nothing

# 9.) Loops and Conditions Core

# 9.1 Print only even numbers:

nums = [1,2,3,4,5,6,7,8,9,10]

for i in nums:
    if i%2 == 0:
        print(i)

# 9.2 Count positives and negatives:

nums = [-2,1,2,3,6,-9,-8,-7,-10]

neg_num = 0
pos_num = 0

for n in nums:
    if n>0:
        pos_num += 1
    else:
        neg_num += 1

print(f"Total Positive Numbers = {pos_num}")
print(f"Total Negative Numbers = {neg_num}")

# 9.3 Validation inside a loop (input keeps asking)

# keep asking until user enters a number between 1 and 5.

x = []
while True:
    num = int(input("Enter the Number = "))
    if num > 1 and num < 5:
        print("Valid!")
        break
    else:
        x.append(num)
        print("Try Different Number Please!")

print(f"Wrong inputs entered: {x}")


# 10 — Mini Project : Menu-Driven To-Do List 

tasks = []

while True:
    print("\n1. Add Tasks")
    print("2. View Tasks")
    print("3. Remove Tasks")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter the item to add: ").strip()
        tasks.append(task)
        print("Task Added!")

    elif choice == 2:
        if not tasks:
            print("No Tasks To View!")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}.) {tasks[i]}")

    elif choice == 3:
        if not tasks:
            print("No Items to Delete!")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}.) {tasks[i]}")

            print("Enter 1 to clear all, 2 to remove one item")
            rem_input = int(input("Please Enter your choice: "))

            if rem_input == 1:
                tasks.clear()
                print("All tasks cleared!")

            elif rem_input == 2:
                num = int(input("Enter the Number to Remove: "))
                if num >= 1 and num <= len(tasks):
                    tasks.pop(num - 1)
                    print("Task Removed Successfully!")
                else:
                    print("Invalid task number!")

            else:
                print("Invalid delete option!")

    elif choice == 4:
        print("Exiting...!")
        break

    else:
        print("Invalid Option!")




