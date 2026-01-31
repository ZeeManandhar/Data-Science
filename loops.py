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

