# Tuple
# It is a container that groups multiple values together into one single unit.
# Let us assume tuple as a box and once it is sealed, the items inside cannot be changed.

# Examples from real life:
# a. GPS location → (latitude, longitude)
# b. Date → (day, month, year)
# c. Student record → (name, roll_no, section)

# Python separates data into:
# a. Changeable data → Lists
# b. Fixed, protected data → Tuples

# Tuples are intialized with ().


# We use tuple when:
# a. Values are related
# b. Order matters
# c. Data should not change
# d. You want clarity and safety

# Creating an empty Tuple: 

t = () # this is rarely used!!

# Example:
t1 = (10,20,30,40,50)
print(t1)

# Important Concept: Single-Element Tuple

t = (5) # This is considered as tuple.

# Python treats this as just the number 5. Parentheses alone does not create a tuple.

# To make it tuple:

t = (5,) # The comma creates the tuple, not the parentheses.

# So:
# (5,) --> tuple
# (5) --> integer
# 5, --> also a tuple


# Tuple Without Parentheses (Tuple Packing)

# Python allows tuples to be created without ().

# Lets try it:
t1 = 1,2,3,4,5,6,7,8,9  # This is still a tuple.
print(t1)

# Parentheses Are Optional (But Recommended for Beginners)

# All of these create tuples:
# a = (1, 2)
# b = 1, 2
# c = (1,)
# d = 1,



# Now lets try Accesing the Tuple Elements:

# Accessing means taking a value out of a tuple, without modifying the tuple

# Indexing: 
a = ("John","Harry","Tom","Jenna")
print(a[0])
print(a[1])
print(a[3])

# Negative Indexing: 
# Negative indexing counts from the end.

t1 = ("Chicago","Minnesote","Portland","Denver","Boston","Oklahoma")

print(t1[-1])
print(t1[-2])
print(t1[-3])

# Slicing: (Accessing a range of values)

# Slicing generally means taking certain portion or part of tuple.
# Syntax: Tuple[start:end] where start is inclusive and end is exclusive.

x = (1,2,3,4,5,6,7,8,9,10)
print(x[4:10])
print(x[0:5])


# Slicing with Step
# Syntax: [start:end:step] 
# Step decides how many positions to jump

print(x[::2])
print(x[4::3])

# Nested Tuples (Tuple inside Tuple)

# A tuple which contain another tuple inside it is referred as Nested Tuples.
# “A box inside a box”

t = (1, (2, 3), 4, 5, 6, 7)

print(t[1][0]) 
print(t[1][1])

# TUPLE IMMUTABILITY

# Immutable means:
# After creation, the object cannot be changed.

# For tuples, this means:

# We cannot change an element
# We cannot add a new element
# We cannot remove an element
# We cannot rearrange elements

# Once created, it is locked forever!

# This is what we cannot do inside tuple:

# t[0] = 99        # cannot change value
# t.append(40)    # no append method
# t.remove(20)    # no remove method

# Error will be shown: 'tuple' object does not support item assignment


# Mutable Objects Inside Immutable Tuples

# The tuple structure cannot change, but mutable elements inside it can. 
# It means Mutable objects inside tuples can still be modified

# Example:

t1 = ("Kathmandu","Bhaktapur","Lalitpur","Pokhara",["Lumbini","Kapilbastu"])

t1[4].append("Chitwan")
print(t1)

t1[4][0] = "lumbini"
print(t1)

t1[4].pop()
print(t1)

t1[4].remove("Kapilbastu")
print(t1)

# Key Concept: 
# We cannot change the references inside a tuple,
# but we can change the mutable objects they point to.


# Tuple Operations:

# 1️. len() --> Length of a Tuple
# len() shows how many elements are inside a tuple.

# “How many values does this tuple contain?”

t1 = (2,4,6,8,10,12,2,2)
t2 = len(t1)
print(t2)

tpl = ("Zeeson","Za","Rajiv","Sunil","Bella")
print(len(tpl))

# 2. count() — How Many Times a Value Appears

# count() tells the Number of Occurences of that Specific Value:
# “How many times does this value occur?”

result = tpl.count("Zeeson")
print(result)

print(t1.count(2))


# 3. index() — Position of First Occurrence

# index() returns: “At what position does this value first appear?”

t = (5, 10, 15, 10)
print(t.index(10))  # return only the index of first appearance  


# 4. Membership Testing (in and not in)

# Used to check whether a value exists in a tuple.

# Example (in Operation):

t1 = ("Ironman","Batman","Superman","Spiderman","Hulk","Thor")

print("Ironman" in t1)
print("Loki" in t1)

# Example (not in Operation):

print("Black Panther" not in t1)
print("Hulk" not in t1)

# 5. Iterating Through a Tuple

#  A. (Using For Loop)

tpl = ('A','B','C','D','E')

for item in tpl:
    print(item)

# B) Index-based iteration

tpl = ('A','B','C','D','E')

for i in range(len(tpl)):
    print((i, tpl[i]))


# TUPLE PACKING & UNPACKING


# Tuple Packing means: Putting multiple values into one tuple

x = 15,30,45
print(x)

# Tuple unpacking means taking values out from a tuple and keeping it into separte variable.


t1 = ("Zeeson","Manandhar")
c, d = t1
c = (c,) # type casting into tuple
print(c)
print(d)

# Extended Unpacking (* operator)

# We use this approach when we dont know how many values exist or want to group remaining values.

t1 = ("Zeeson","Manandhar", 9841626515, 22, "zeeson.manandhar35@gmail.com","Jadibuti, Narephat")

name,lastname,*extra_info,address = t1

print(name)
print(lastname)
print(extra_info)
print(extra_info[0])
print(address)

# Another Instance:

for x, y in [(1, 2), (3, 4)]:
    print(x,y)


# Important Rule:
# If you want to CREATE a tuple, then use commas.
# If you want to CONVERT an iterable, then use tuple().
