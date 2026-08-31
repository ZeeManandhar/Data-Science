# TUPLE PROGRAMMING PRACTICE:
# BASIC PROGRAMS (1–10)

# Write a program to create an empty tuple and print it.

t = ()
print(t)

# Write a program to create a tuple with one element and print its type.

t1 = ("Zeeson",)
print(type(t1))

# Write a program to create a tuple of 5 integers and print it.

t1 = (1,2,3,4,5)
print(t1)

# Write a program to access and print the first element of a tuple.

tup = ("Ram","Shyam","Hari","Geeta")
print(tup[0])

# Write a program to access and print the last element of a tuple.

print(tup[-1])


# Write a program to find the length of a tuple.

a = len(tup)
print(a)

# Write a program to check whether an element exists in a tuple.

t1 = ('A','B','C','D','E','F','G')
print('A' in t1)
print('H' in t1)

# Write a program to print all elements of a tuple using a for loop.

t = (10,20,30,40,50,60,70,80,90,100)

for item in t:
    print(item)

# Write a program to print tuple elements using index-based looping.

t1 = (20,40,60,80,100)

for item in range(len(t1)):
    print(item, t1[item])


# Write a program to create a tuple using tuple packing.

t = 5,4,3,2,1
print(t)


# INDEXING & SLICING (11–18):

# Write a program to slice a tuple from index 1 to 4.

dogs = ("Kalu","Dalli","Bella","Tony","Pinky","Jojo","Jimmy")

range_1 = dogs[1:4]
print(range_1)

# Write a program to print alternate elements of a tuple.

print(dogs[::2])

# Write a program to reverse a tuple using slicing.

mountains = ("Everest","Annnapurna","Macchapuchre","Gaurishankar","Lhotse")

print(mountains[::-1])

# Write a program to access an element from a nested tuple.

num = (1,2,3,4,5,(6,7,8,9,10))
print(num[5][2])

# Write a program to print the first 3 elements of a tuple.

t1 = (3,6,9,12,15,18,21)
print(t1[0:3])

# Write a program to print all elements except the first one.

print(t1[1:])

# Write a program to demonstrate negative indexing in a tuple.

print(t1[-1:-7:-1])

# Write a program to copy a tuple using slicing.

sports = ("Basketball","Cricket","Hockey","Football","Rugby")

copy_sports = sports[:]

print(copy_sports)



# IMMUTABILITY & THINKING (19–25):

# Write a program that tries to modify a tuple and observe the error.

tup = (1,2,3,4,5,6)
# # tup.append(7)
# print(tup)

# tup[0] = 15
# print(tup)


# Write a program where a tuple contains a list and modify the list.

tuple_1 = ("Jesser","ZachTTG","Jeffrey Bui","Moochie",[25,32,28,25])

tuple_1[4][3] = 26
print(tuple_1)

# Write a program to prove that tuple structure cannot be changed.

# del tuple_1[0]
# print(tuple_1)

# Write a program to show that tuple values cannot be reassigned.

# t1 = (5,4,3,2,1)
# t1[0] = 10
# print(t1)


# Write a program to store student details in a tuple and print them.

Std = ("Name: Ram Shrestha","Grade: 8","Roll no: 20","Address: Baneshwor,Ktm")
print(Std)

# Write a program to use a tuple for storing fixed configuration values.

conf_t = ("localhost",3000)
print(conf_t)


# PACKING & UNPACKING (26–33)

# Write a program to unpack values from a tuple into variables.

t1 = ("Zeeson", 22, "Jadibuti, Narephat")

name, age, address = t1
print(name)
print(age)
print(address)

# Write a program to swap two variables using tuple unpacking.

t1 = ("Zeeson","Manandhar",22,"Nepal")

a = t1
b = a
print(b)

# Write a program to unpack a tuple using * operator.

t = (1,2,3,4,5,6,7,8,9,10)

a, *b = t
print(a)
print(b)


# Write a program to store remaining unpacked values into a list.

cars = ("Toyota","Nissan","BMW","Audi")

first , *rest = cars
print(first)
print(rest)

# Write a program to unpack first and last elements using extended unpacking.

bikes = ("Bajaj","Yamaha","Honda","KTM","Triumph")

a, *b, c = bikes
print(a)
print(b)
print(c)

# Write a program to show unpacking error when variables don’t match.

# t1 = ("Kathmandu","Bhaktapur","Lalitpur")
# x, y = t1
# print(x)
# print(y)

# Write a program to convert unpacked list back into a tuple.
a = ['E','F','G','H']
t1 = tuple(a)
print(t1)

# Write a program to unpack values from a list of tuples in a loop.

t1 = ([10,15,20],[5,10,15],[4,8,12])

for x,y,z in t1:
    print(x,y,z)

# for i in range(len(t1)):
#     x = t1[i]
#     for item in x:
#         print(item)



# LIST & TUPLE CONVERSION (34–40):

# Write a program to convert a list into a tuple.

l1 = ["apple","mango","banana","grapes"]
print(tuple(l1))


# Write a program to convert a tuple into a list.

t1 = ("Nepal","India","Bhutan","Bangladesh","Sri lanka")
x =list(t1)
print(x)

# Write a program to modify tuple data by converting it into a list.


t = (1,2,3,4,5,6,7,8,9)
l1 = list(t)
l1[0] = 0
print(l1)

# Write a program to append an element to a tuple using conversion.

tpl = ("Nepal","India","Bangladesh","Bhutan")

l1 = list(tpl)
l1.append("Pakistan")

new_tuple = tuple(l1)
print(new_tuple)


# Write a program to delete an element from a tuple using conversion.

t1 = (2,4,6,8,10,12,14,16,18,20)

l1 = list(t1)
l1.remove(4)

t2 = tuple(l1)
print(t2)

# Write a program to use a tuple as a dictionary key.

locations = {
    (27.7, 85.3): "Kathmandu",
    (28.2, 83.9): "Pokhara"
}

print(locations)


# BONUS CHALLENGE:

# Write a program to find the maximum and minimum values in a tuple.

t = (25,10,6,80,75,66,2,8)

x = max(t)
y = min(t)

print(f"The maximun value is {x}")
print(f"The minimum value is {y}")

# Write a program to count repeated elements in a tuple.

t = ("Steph","Lebron","Kobe","Shaq","Steph")

t1 = t.count("Steph")
print(t1)

# Write a program to check if a tuple is a palindrome.

t = (11,22,33,22,11)

if t == t[::-1]:
    print("The number is Palindrome!")
else:
    print("Not palindrome")

# Write a program to merge two tuples.

t1 = (1, 2, 3)
t2 = (4, 5, 6)

merged = t1 + t2
print(merged)


# Write a program to find common elements between two tuples.

t1 = (1,2,3,5,6,9,9)
t2 = (5,4,5,6,8)

for i in range(len(t1)):
    if t1[i] in t2:
        print(t1[i])


# LOGIC-BASED TUPLE QUESTIONS (FOR-LOOP FOCUSED)

# a. Write a program to iterate through a tuple of numbers and print only the even numbers.

tpl = (1,2,3,4,5,6,7,8,9,10)

for item in tpl:
    if item % 2 == 0:
        print(item)


# b. Write a program to count how many elements in a tuple are greater than a given number.

num = 99

count = 0

tpl = (20,60,45,88,111,80,75,214)

for item in tpl:
    if item > num:
        count = count + 1
print(count)

# c. Write a program to find the sum of all numeric elements in a tuple using a for loop.

tpl = (3,6,9,12,15,18,21)
count = 0

for i in range(len(tpl)):
    count = count + tpl[i]
print(f"The sum of all elements is {count}")


# d. Write a program to find the largest and smallest elements in a tuple without using min() or max().


tpl = (10,15,12,18,5,6,7)

largest_num = tpl[0]
smallest_num = tpl[0]

for i in range(len(tpl)):
    if tpl[i] > largest_num:
        largest_num = tpl[i]
    if tpl[i] < smallest_num:
        smallest_num = tpl[i]

print(f"The Largest number is {largest_num}")
print(f"The Smallest number is {smallest_num}")


# e. Write a program to iterate through a tuple of tuples and print each element separately using unpacking.

# Example input idea:

# ((1, 2), (3, 4), (5, 6))

t = ((1, 2), (3, 4), (5, 6))

for x,y in t:
    print(x)
    print(y)
    

# f. Write a program to count how many tuples inside a tuple contain a specific value.

# Example idea:

# ((1, 2), (3, 1), (4, 5))

tpl = ((1, 2), (3, 1), (4, 5))

count = 0

for item in range(len(tpl)):
    if 1 in tpl[item]:
        count = count + 1

print(f"The count is {count}")


# g. Write a program to reverse a tuple using a for loop (do not use slicing).


tpl = ("Mercury","Venus","Earth","Mars","Jupiter")

reverse_tpl = ()

for i in range(len(tpl)-1, -1,-1):
    reverse_tpl = reverse_tpl + (tpl[i],)

print(reverse_tpl)

