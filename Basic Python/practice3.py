# BASIC LIST PRACTICE (1–15)

# Write a program to create a list of 5 integers and print it.

integers = [5,4,3,2,1]
for i in integers:
    print(i)

# Write a program to access and print the first and last element of a list.

dogs = ["Dalli","Belli","Tyson","Kaley"]
print(dogs[0])
print(dogs[-1])


# Write a program to find the length of a list without using len() (hint: loop).

num = [3,6,9,10,12]
count = 0

for i in num:
    count = count + 1
print(count)
    

# Write a program to check whether a given element exists in a list.

names = ["Zeeson","Sunil","Aman","Mauga"]

if "Zeeson" in names:
    print("Element exists")

# Write a program to print all elements of a list using a for loop.

num = [6,7,8,9]
for i in range(len(num)):
    print(num[i])


# Write a program to add an element to the end of a list using append().

dishes = ["Momo","Pizza","Burger","Fries","Samosa"]
dishes.append("Nachos")
print(dishes)

# Write a program to insert an element at a specific index in a list.

dishes.insert(1, "Laphing")
print(dishes)

# Write a program to remove a given element from a list.

dishes.remove("Burger")
print(dishes)

# Write a program to remove the last element from a list.

dishes.pop(-1)
print(dishes)

# Write a program to copy a list using slicing.

new_dish = dishes[:]
print(new_dish)

# Write a program to demonstrate that b = a does not copy a list.

a = [1,2,3,4,5]
b = a
print(b)
a.append(6)
print(a)

# Write a program to reverse a list using slicing.

bikes = ["NS 200","Hunter 350","MT15","RTR 310"]
reverse_bike = bikes[::-1]
print(reverse_bike)

# Write a program to print elements at even indexes.

elements = ["car","ball","gun","hippo","bat","watch"]
print(elements[1::2])

# Write a program to print elements at odd indexes.

print(elements[::2])


# LIST OPERATIONS & LOGIC (16–30)

# Write a program to find the sum of all elements in a list.

number = [5,10,15,20,25]
y = 0

for n in range(len(number)):
    y += number[n]

print(y)


# Write a program to find the product of all elements in a list.

number = [5,10,15,20,25]
y = 1

for n in range(len(number)):
    y *= number[n]

print(y)

# Write a program to find the maximum element in a list.

max_num = [10,20,60,40,50]
print(max(max_num))

# Alternative way (using loop):

max_value = max_num[0]

for n in max_num:
    if n > max_value:
        max_value = n

print(max_value)

# Write a program to find the minimum element in a list.

print(min(max_num))

# Write a program to count how many times a given number appears in a list.
number = [1,1,1,1,1,5,4,9,8,6,3]
x = number.count(1)
print(x)

# Write a program to sort a list in ascending order.

phones = ["Samsung","Vivo","Iphone","Oppo","Redmi"]
phones.sort()
print(phones)

# Write a program to sort a list in descending order.
phones.sort(reverse=True)
print(phones)

# Write a program to sort a list of strings by their length.
phones.sort(key=len)
print(phones)

# Write a program to create a new list containing squares of all numbers.

num = [2,4,6,8]
y = []
for n in range(len(num)):
    x = num[n] ** 2
    y.append(x)

print(y)

# Write a program to create a new list containing double of each element.

number = [5,6,7,8,9]
l1 = []

for n in range(len(number)):
    x = number[n]*2
    l1.append(x)
print(l1)
   

# Write a program to remove all duplicate elements from a list (logic-based).
num = [1, 2, 3, 2, 4, 1, 5]
new_list = []

for i in range(len(num)):
  if num[i] not in new_list:
      x = num[i]
      new_list.append(x)
print(new_list)
  

# Write a program to merge two lists into one list.

players = ["Lebron","Kobe","Timmy","Shaq","Steph"]
ages = [41,45,50,50,38]

players.append(ages)
print(players)

# Write a program to find the index of a given element.

for index, value in enumerate(players):
    print(index, value)

# Write a program to check if a list is empty.

x = []
if len(x) == 0:
     print("The list is Empty")

# Write a program to split a list into two halves.

l1 = [1,2,3,4,5,6]

half = int(len(l1) / 2)

l2 = l1[:half]
print(l2)

l3 = l1[half:]
print(l3)


#  LIST COMPREHENSION PRACTICE:

# Write a program to create a list of squares using list comprehension.

num = [4,8,12,16]
sqr_num = [n**2 for n in num]
print(sqr_num)

# Write a program to create a list of even numbers using list comprehension.

num = [10,12,13,14,45,18]
even_num = [n for n in num if n%2 == 0]

print(even_num)

# Write a program to create a list of odd numbers using list comprehension.

odd_num = [n for n in num if n%2 != 0]
print(odd_num)

# Write a program to create a list of numbers greater than 10.

l1 = [15,5,8,11,21,2,90]
l2 = [ i for i in l1 if i > 10]
print(l2)

# Write a program to create a list of True/False values for even numbers.

even_num = [3,6,9,12,15,18]
check_even = [n%2 == 0 for n in even_num]
print(check_even)

# Write a program to convert all strings in a list to uppercase.

cities = ["kathmandu","Bhaktapur","lalitpur","pokhara","lumbini"]
cpt = [i.upper() for i in cities]
print(cpt)

# Write a program to extract only strings with length greater than 5.

l1 = ["ball","bat","badminton","bad"]
l2 = [l1[i] for i in range(len(l1)) if len(l1[i])>5]

print(l2)

# Write a program to remove vowels from a list of characters.

char = ["F","A","E","U","G"]
vowels = ["A","E","I","O","U"]
new_list = []

for i in char:
    if i not in vowels:
        new_list.append(i)
print(new_list)


# Write a program to flatten a list like [[1,2],[3,4]] into [1,2,3,4].
l1 = [[1,2],[3,4]]
flat_list = []

for sublist in l1:
    for item in sublist:
        flat_list = flat_list + [item]
print(flat_list)

# Write a program to create a list of numbers divisible by both 3 and 5.

l1 = [6,25,4,1,9,45]
l2 = [n for n in l1 if n%3 == 0 and n%5 == 0]

print(l2)

# Write a program to replace negative numbers with 0 using list comprehension.

l1 = [5,4,-3,-2,1]
l2 = [0 if n<0 else n for n in l1]
print(l2)

# Write a program to generate a list of first 10 multiples of 7.

l1 = [n*7 for n in range(1,11)]
print(l1)

# Write a program to swap uppercase to lowercase and vice versa in a list.

char = ['a','B','c','D']
new_list = [c.swapcase() for c in char] # used swapcase method as it converts lower strings to uppercase and vice versa.
print(new_list)

# Write a program to filter numbers whose square is greater than 50.

l1 = [5,4,9,10,8]
l2 = [n for n in l1 if n**2 > 50]
print(l2)

#  THINKING / INTERVIEW-STYLE QUESTIONS:

# Write a program to find the second largest number in a list.

num1 = [5,10,15,20,25,30,35,40]
x = []
largest_num = max(num1)

# print(largest_num)

for n in range(len(num1)):
    if num1[n] != largest_num:
        x.append(num1[n])

# Printing the second Largest number present in the list:
second_largest = max(x)
print(second_largest)

# Alternative way:
largest_num = max(num1)

num1.remove(largest_num) # used remove method to delete the largest number from the list
second_largest= max(num1)
        
print(second_largest)


# Write a program to rotate a list to the right by one position.
nums = [1, 2, 3, 4, 5]
last_element = [nums[-1]]
nums.pop()

last_element.extend(nums)
print(last_element)

# Note: append add the elements as one item while extend adds the elements individually.


# Write a program to check if a list is a palindrome.

l1 = ["11","22","33","22","11"]

if l1 == l1[::-1]:
    print("Palindrome List")
else:
    print("Not Palindrome List")

# Write a program to find common elements between two lists.

l1 = [1,2,3,4,5]
l2 = [2,4,6,8,10]
l3 = []

for i in l1:
    if i in l2:
        l3.append(i)
print(l3)

# Write a program to remove all elements greater than the average of the list.

l1 = [1,2,3,4,5,6]
l3 = []

total = 0
for i in range(len(l1)):
    total+= l1[i]

avg = total/len(l1)

for j in range(len(l1)):
    if l1[j] <= avg:
        l3.append(l1[j])

print(l3)