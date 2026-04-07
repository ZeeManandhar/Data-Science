# Sets — Practice Questions (35)

# Basic Level (1–10)

# Write a program using set to store five numbers and print the set.

set_1 = {10,20,30,40,50}
print(set_1)

# Write a program using set to remove duplicate elements from a list.

l1 = [2,3,3,3,4,5,5,6]
s1 = set(l1)

new_l1 = list(s1)
print(new_l1)

# Write a program using set to check whether a given number exists in a set.

num = {4,8,12,16,20,24,28,32,36,40}
number = 12
print(number in num)

# Write a program using set to add a new element to an existing set.

st = {'Z','E','E','S','O',}
st.add('N')

print(st)

# Write a program using set to remove an element safely from a set.

s1 = {"Peace","Problems","Patience","Proud"}
s1.discard("Problems")

print(s1)

# Write a program using set to find the length of a set.

s1 = {3,6,9,12,15,18}
length = len(s1)
print(length)

# Write a program using set to iterate through all elements and print them.

foods = {"Pizza","Fries","Tacos","Nachos","Momo","Sushi"}

for item in foods:
    print(item)

# Write a program using set to convert a tuple into a set.

veggies = ("Potatoe","Tomatoe","Brinjal","Ginger","Garlic")

s1 = set(veggies)
print(s1)

# Write a program using set to create an empty set correctly.

emp_set = set()

# Write a program using set to demonstrate that duplicate values are removed automatically.

ytb = {"Jesser","Jeffrey","Moochie","CashNasty","JDuB","Moochie"}

print(ytb)

# Method-Based Practice (11–18)

# Write a program using set to add multiple elements at once.

countries = {"Nepal","USA","Canada","Germany","France","Japan"}
countries.update(["India","Australia","Indonesia","Maldives"])

print(countries)

# Write a program using set to remove an element using remove() and observe the error when it does not exist.

# countries.remove("Korea")
# print(countries)                 //shows key error

# Write a program using set to remove an element using discard() and show that no error occurs.

countries.discard("Korea")
print(countries)

# Write a program using set to remove a random element.

countries.pop()
print(countries)

# Write a program using set to clear all elements from a set.

countries.clear()
print(countries)

# Write a program using set to check membership using in and not in.

Brand = {"StarBucks","Target","Temu","Best Buy","LV","Supreme"}

print("Target" in Brand)
print("Burger King" not in Brand)


# Write a program using set to explain why indexing is not allowed.

# X = Brand[0]
# print(X)

# Write a program using set to convert a set into a list and access elements by index.

set_1 = {"Tesla","Toyota","BMW","Suzuki","Audi","BYD"}

list_1 = list(set_1)

print(list_1)
print(list_1[1])

# Set Operations (19–25)

# Write a program using set to find the union of two sets.

x = {"Ram","Hari","Shyam","Geeta"}
y = {"Geeta","Hari","Bishnu","Krishna"}

output = x.union(y)
print(output)

# Write a program using set to find the intersection of two sets.

intersection = x.intersection(y)
print(intersection)

# Write a program using set to find the difference between two sets.

A = {2,4,6,8,10,12,14,16,18,20}
B = {3,6,9,10,12,15,18,21,24,27,30}

print(A - B)
print(B - A)

# Write a program using set to find the symmetric difference between two sets.

result = A.symmetric_difference(B)
print(result)

# Write a program using set to compare two sets and print common elements only.

result = A.intersection(B)
print(result)

# Write a program using set to find elements present in the first set but not in the second.

names = {"Salman","Aamir","Sharukh","Kartik","Varun"}
names1 = {"Kartik","Varun","Abhishek","Rahul"}

result = names.difference(names1)
print(result)

# Write a program using set to compare two lists and find unique values from both.

l1 = [5,10,15,20,25]
l2 = [10,20,30,40,50]

s1 = set(l1)
s2 = set(l2)

X = s1.symmetric_difference(s2)
print(X)


# Relations & Logic-Based (26–30)

# Write a program using set to check whether one set is a subset of another.

A = {4,5,6}
B = {1,2,3,4,5,6,7,8}

output = A.issubset(B)
print(output)

# Write a program using set to check whether one set is a superset of another.

output = B.issuperset(A)
print(output)

# Write a program using set to check whether two sets are disjoint.

dis_joint = A.isdisjoint(B)
print(dis_joint)

# Write a program using set to compare two datasets and print added and removed elements.

old_data = {101, 102, 103, 104}
new_data = {102, 103, 104, 105, 106}

added = new_data - old_data

removed = old_data - new_data

print(f"Newly Added Elements are: {added}")
print(f"Removed Elements are: {removed}")


# Write a program using set to validate user access using allowed IDs.

user_id = int(input("Enter your valid id: "))

valid_id = {101,103,201,202,301,302}

if user_id in valid_id:
    print("Access Granted!")
else:
    print("Not Granted!")


# Advanced Thinking (31–35)

# Write a program using set comprehension to generate squares of numbers from 1 to 10.

s1 = {i**2 for i in range(1,11)}
print(s1)


# Write a program using set comprehension to filter even numbers from a list.

s1 = {n for n in [3,6,9,12,15,18,21,24,27,30] if n%2 == 0}

print(s1)

# Write a program using set to store immutable collections using frozenset.

s1 = {"Knife","Chopping Board","Blender","Mixer"}
items = frozenset(s1)

print(items)


# Write a program using set to extract unique words from a sentence.

str = "python is easy and python is powerful"

split_words = str.split()
s1 = set(split_words)
print(s1)


# Write a program using set to explain (in comments) why sets are faster than lists for membership checking.

# because sets uses the concept of hashing, which is comparatively faster than checking each items in lists.