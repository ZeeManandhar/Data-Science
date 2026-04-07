# Sets:

# A set in Python is a collection of items where:
# each item is unique (no duplicates), and
# the collection is unordered (no fixed position like 0, 1, 2…).
# Think of a set like a “bag of unique things”.

# For Example:

colors = {"red","blue","green","yellow","purple","brown","purple","black","red"}

print(colors)

# Sets are mainly used for two powerful reasons:

# A) To keep only unique values automatically

# If duplicates appear, the set removes them.

# B) To do fast checking

# Checking whether something exists inside a set is very fast compared to a list.


# Key properties:

# 1) Unordered
# A set does not store items by position i.e (index).
# So, it doesn’t guarantee “first item, second item…” order.

# For Example:

# set_1 = {"Apple","Mango","Peach","Kiwi","Orange"}
# set_1[0] = "Banana"
# print(set_1)

# 2) No duplicate values

# If we try to add duplicates, they collapse into one.

# For Example:

num = {1,1,1,1,1,2,2,2,2,2,3,3,3,3,3}

print(num)

# 3) Mutable (We can change the set)

# We can add/remove items after creation.

# For Example:

s1 = {"Zeeson","Tom","Jerry"}
s1.add("Batman")
print(s1)

# 4) Elements must be immutable (important)

# The set itself can change, but the items inside must be unchangeable types like:
# int, float, str, tuple

# For Example:

set_1 = {1,5.5,"Zee",(1,2,3),}
print(set_1)

# set_2 = {[1,2,3],[4,5,6],[7,8,9]} # this shows error i.e. unhashable type 
# print(set_2)

# Lists are unhashable because they are mutable.
# If a list could be hashed, its hash might change after modification, which would break the set’s internal structure.


# Section 2: Creating Sets

# 2.1 Creating a set using { }

# The simplest way to create a set is with curly braces.

number = {2,4,6,8,10,12,14,16,18,20}
print(number)

# 2.2 Order is NOT guaranteed

num = {10,20,30,40,50,60}
print(num)

# print(num[0]) # This is not acceptable (invalid)

# 2.3 Creating a set using set()

# This method is used when:

# we already have another collection (list/tuple)
# we want to remove duplicates

l1 = [1,2,3,4,5,6]

s1 = set(l1)
s1.remove(5)
print(s1)

# 2.4 Creating an empty set (MOST IMPORTANT ONE)

empty = {}   # this is not considered as empty set, it resolves as dictionary.

print(type(empty))

# The Correct Way to create an Empty Set

empty = set()

empty.add(1)
empty.add(2)

print(type(empty))
print(empty)

# Note to Remember: {} is reserved syntax for dictionaries in Python.

# 2.5 Checking the type
print(type({}))        
print(type(set()))     
print(type({1, 2}))    


# Quick Pratice:

# Convert this tuple into a set:

t = (10, 10, 20, 30)

s = set(t)
print(s)


# 3. Section 3 — Accessing & Iterating Sets

# 3.1 Why indexing is not allowed in sets ?

# Sets are unordered.
# No fixed positions like index 0, 1, 2.
# Python does not store items by position.
# So indexing does not make sense for sets.

# For Example: 

set_1 = {"Kathmandu","Bhaktapur","Lalitpur"}

# 3.2 How to access elements in Sets then?

# Using loop:

set1 = {"Nike","Puma","Adidas","Anta","Peak"}

for i in set1:
    print(i)

# for i in range(len(set1)):    This gives error, because range(len(...)) is only for index-based collections i.e. lists and tuples

#     print(set1[i])


# 3.3 Membership testing (in, not in) -> IMPORTANT

# This is one of the main reasons sets exist.

nums = {10, 20, 30, 40}

print(20 in nums)      
print(50 in nums)      
print(50 not in nums)  

# Checking membership in a set is very fast
# Much faster than checking in a list


# 4. Set Methods (Core Methods)

# 4.1 add() — add a single element

id = {101,201,301,401,501}
id.add(601)

print(id)

######

bikes = {"Triumph","KTM","BMW","Kawasaki","Suzuki","TVS"}
bikes.add("Bajaj")

print(bikes)

# 4.2 update() — add multiple elements

# Takes any iterable (list, tuple, set)

set_1 = {1,2,3,4,5}
set_1.update([5,6,7,8,9,10])
set_1.update("HI")

print(set_1)

# 4.3 remove() — remove a specific element (strict)

set_1 = {"Table","Chair","Whiteboard","Marker","Dustbin","AC"}
set_1.remove("AC")
# set_1.remove("Pen")  this shows key error because the element doesnot exists in set
print(set_1)


# 4.4 discard() — remove safely (no error)

set_1.discard("Dustbin")
print(set_1)

set_1.discard("Fan")  # Even the element doesnot exist in set, it will still give no error
print(set_1)


# 4.5 pop() — remove a random element

# Since, Sets are unordered, it removes random element

s1 = {2,4,6,8,10,12,14,16,18,20}
s1.pop()
print(s1)


# 4.6 clear() — remove everything

s1.clear()
print(s1)

# Quick Practice:

# Add 100 to {10, 20}

s1 = {10,20}
s1.add(100)

print(s1)

# Add [3, 4] to {1, 2}

s1 = {1,2}
s1.update([3,4])
print(s1)

# Remove 5 safely from {1, 2, 3}

s1 = {1,2,3}
s1.discard(5)
print(s1)

# What happens if you call pop() twice on a 2-element set?

s1 = {1,2}
s1.pop()
s1.pop()

print(s1)

# This gives empty set

# When should you prefer discard() over remove()?

# --> when we are unaware if that element exists in set or not , as this will throw no error regardless.


# 5. Set Operations (MOST IMPORTANT)

# Consider it as a Venn-Diagram Logic.

# 5.1 Union

# It combines elements from both Sets. 

# For Example:

A = {1,2,3,4,5,6}
B = {6,7,8,9,10}

X = A.union(B)
print(X)

# or we can also use '|' for union operation

print(A | B)

# 5.2 Intersection

# It gives common elements present in both sets

A = {1,2,3,4,5,6}
B = {5,6,7,8,9}

y = A.intersection(B)
print(y)

# or we can also use '&' for intersection Operation.

print(A & B) 

# 5.3 Difference (A - B / B - A)

# Elements present in one set but not in other

A = {1,2,3,4,5}
B = {4,5,6,7,8,9}

z = A.difference(B)
print(z)

# Alternative Way:

print(A - B)
print(B - A)

# 5.4 Symmetric Difference — NOT common

# Elements that are in either set, but not in both

A = {1,2,3,4}
B = {3,4,5,6}

X = A.symmetric_difference(B)
print(X)

# or we can also use '^' for Symmetric Difference Operation:

print(A ^ B)

# 6. Set Comparisons & Relations

# 6.1 Subset (issubset)

# Every element of set A exists in set B

# For Example:

A = {1,2}
B = {1,2,3,4,5,6}

x = A.issubset(B)
print(x)

# Shortcut Operator:

print(A <= B)

# 6.2 Superset (issuperset)

# Set A contains all elements of set B

y = B.issuperset(A)
print(y)

# Shortcut Operator:
print(B>=A)

# 6.3 Disjoint Sets (isdisjoint)

# No common elements at all

X = {1, 2}
Y = {3, 4}
print(X.isdisjoint(Y))  

# 7. Set Immutability Rules & frozenset

# Sets are Mutable Containers.

s = {1, 2, 3}
s.add(4)
s.remove(2)
print(s)


# 7.2 Elements inside sets must be immutable

# Sets use hashing.
# Hash must stay the same
# Mutable objects can change, thus hash breaks

# So:
# int, float, str, tuple are allowed
# list, set, dict are not allowed


# 7.3 Why lists cannot be inside sets

# Lists are changeable

lst = [1, 2]
lst.append(3)

# Changing an element inside a set would destroy its structure.

# 7.4 frozenset (immutable set):

# A set that cannot be changed is a frozenset

fs = frozenset({2,3,4,5,6})

print(fs)

# fs.add(4)
# print(fs)

print(2 in fs) 

# frozenset exist because:
# Normal sets are mutable i.e. unhashable
# frozenset is immutable i.e. hashable

s = {frozenset([1, 2]), frozenset([3, 4])}
print(s)


# 8. Set Comprehension

# It is a  short syntax to create a set using a loop and conditions.

s1 = {x for x in range(5)}
print(s1)

# Note: (duplicate values are auto-removed)

# 8.1 Set Comprehension vs List Comprehension

# 1. List Comprehension

list1 = [ i for i in [1,2,3,4,5,15,20,6,85,85] if i > 10]

print(list1)

# 2. Set Comprehension

Set1 = { i for i in (1,2,3,4,5,15,20,6,85,85) if i > 10}
print(Set1)

# 8.2 Real use-case: removing duplicates

std = {"Ram","Hari","Geeta","Sabita","Shyam","Ram"}

std2 = {item for item in std}

print(std2)

# 8.3 Transforming values

words = {"hi", "hello"}
lengths = {len(word) for word in words}
print(lengths)


# Quick Practice Questions:

# 1. Create a set of squares of numbers from 1 to 5

s1 = {sqr**2 for sqr in range(1,6)}

print(s1)

# 2. Create a set of odd numbers from 1 to 10

set1 = {num for num in range(1,11) if num%2 == 1}
print(set1)

# 3. Remove duplicates from [1,1,2,3,3,4] using set comprehension

s1 = {item for item in [1,1,2,3,3,4]}
print(s1)