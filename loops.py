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


# 5. for Loop with Dictionary

# A dictionary is also iterable, but it works slightly differently than lists and strings.

