# Loops Pratice Questions:

# BASIC LEVEL:

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
    

# INTERMEDIATE LEVEL 

# Write a program to find the sum of all numbers in a list.

num = [2,4,6,8,9,10]
sum = 0
for i in range(len(num)):
    sum = sum + num[i]

print(sum)

# Write a program to count how many even and odd numbers are in a list.

l1 = [5,10,15,20,25,30,35,40,45,50,2]

even_count = 0
odd_count = 0

for n in l1:
    if n%2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Even Numbers Count: {even_count}")
print(f"Odd Numbers Count: {odd_count}")


# Write a program to count how many positive and negative numbers are in a list.

list_1 = [-3,-2,-1,5,6,7,8,9]

pos_count = 0
neg_count = 0

for n in list_1:
    if n > 0:
        pos_count += 1
    else:
        neg_count += 1

print(pos_count)
print(neg_count)

# Write a program to find the largest number in a list using a loop.

l1 = [5,2,9,10,56,99,6,33]

largest_num = l1[0]

for i in l1:
    if i > largest_num:
        largest_num = i

print(f"The largest number in the list is {largest_num}.")

# Write a program to find the smallest number in a list using a loop.

l2 = [0,1,5,6,9,10,5]

smallest_num = l2[0]

for i in range(len(l2)):
    if l2[i] < smallest_num:
        smallest_num = l2[i]

print(f"The Smallest Number in the List is {smallest_num}")

# Write a program to count how many times a specific number appears in a list.

nums = [2, 4, 6, 4, 8, 4, 10]
target = 4

count = 0

for n in nums:
    if n == target:
        count = count + 1

print(f"{target} appears {count} times")


# Write a program to print numbers from 1 to 50 but skip multiples of 5.

for i in range(1,51):
    if i%5 == 0:
        continue
    else:
        print(i)

# Write a program to stop printing numbers when number 7 appears.

while True:
    data = int(input("Enter your number please: "))
    if data == 7:
        print("Stopping.....!")
        break
    else:
        print(data)


# Write a program to print all numbers except 3 using continue.

t1 = (5,4,3,2,1)                # Tried in Tuple just for pratice

for i in t1:
    if i == 3:
        continue
    else:
        print(i)
    
# Write a program that keeps asking the user for input until they type "exit".

while True:
    data = input("Type Something: ").strip().upper()

    if data == "EXIT":
        print("Exiting.........")
        break
    else:
        print(data)

# Write a program that keeps asking for a positive number until user enters one.

while True:
    data = int(input("Enter the Positive Number = "))

    if data > 0:
        break
    else:
        print(data)

# Write a program to reverse a string using a loop.

str1 = "PYTHON"
str2 = ""

for i in range(len(str1)-1, -1, -1):
    str2 = str2 + str1[i]

print(str2)


# Write a program to count vowels in a string using a loop.


str1 = "zeeson"
count = 0
for i in str1:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" :
        count = count + 1
print(f"Total count of vowels in string: {count}")
        

# Write a program to print a multiplication table of a number.

num = int(input("Enter a number please: "))

for i in range(1,11,1):
    print(f"{num} * {i} = {num*i}")



# Write a program to validate user input until they enter a number between 1 and 10.

while True:
    num = int(input("Enter the Number = "))
    if num >= 1 and num <= 10:
        print("Valid!")
        break
    else:
        print("Try Again! Invalid Number")


# LOGICAL / REAL-WORLD LEVEL 

# Write a program to check if a number exists in a list using a loop.

num = 5
l1 = [1,2,3,4,5,6,7,8,9,10,11]

for i in l1:
    if num == i:
        print("The Number Exist!!")
  
# Write a program to remove all negative numbers from a list using a loop.

l1 = [-5,1,2,3,-4,-6,10]
l2 = []

for i in l1:
    if i > 0:
        l2.append(i)

print(f"List with No Negative Numbers : {l2}")

# Write a program to print duplicate elements from a list.

num = ["Zeeson","Sunil","Aman","Zeeson","Bella","Bella"]

list_1 = []

for i in num:
    count = 0
    for j in num:
        if i == j:
            count = count + 1

    if count > 1 and i not in list_1:
        list_1.append(i)

print(f"Duplicate Elements are: {list_1}")

# Write a program to count the frequency of each element in a list.

elements = ["apple", "banana", "apple", "orange", "banana", "apple"]

freq = {}

for item in elements:
    if item in freq:
        freq[item] = freq[item] + 1
    else:
        freq[item] = 1
print(freq)

# Write a program to simulate a login system (3 attempts max).

credentials = {
    "admin1": "admin@123",
    "ZeesonGroot": "Zee123#"
}

count = 0

while count < 3:
    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()

    if username in credentials and credentials[username] == password:
        print("Login Successful!")
        break
    else:
        count += 1
        print(f"Invalid Credentials. Attempts left: {3 - count}")

if count == 3:
    print("Account locked. Too many failed attempts.")


# Write a program to display a menu repeatedly until user exits.

while True:
    print("\nMenu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("You selected Option 1.")
    elif choice == "2":
        print("You selected Option 2.")
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")


# Write a program to build a simple calculator using a loop and menu.

while True:
    data1 = int(input("Choose 1 for Addition, 2 for Subtraction, 3 for Multiplication, 4 for Division and 5 to Exit: "))
    input1 = int(input("Enter First Number: ")) 
    input2 = int(input("Enter Second Number: ")) 

    match data1:
        case 1:
            sum = input1 + input2
            print(f"Addition of {input1} and {input2} is {sum}")
        case 2:
            subtract = input1 - input2
            print(f"Subtraction of {input1} and {input2} is {subtract}")
        case 3:
            multiply = input1 * input2
            print(f"Multiplication of {input1} and {input2} is {multiply}")
        case 4:
            division = 0
            if input2 != 0:
                division = input1 / input2
                print(f"Division of {input1} and {input2} is {division}")
            else:
                print("Error: Division by zero is not allowed.")
        case 5:
            print("Exiting the Calculator!")
            break
        case _:
            print("Invalid choice. Please try again.")
            


# Write a program to keep adding numbers until user types "done", then print the sum.

total = 0
while True:
    choice = input("Choose the option: type 'add' to add numbers, type 'done' to exit:").strip().lower()

    if choice == "add":
        
        data = int(input("Enter the Number to add: "))
        total = total + data

    elif choice == "done":
        break
    else:
        print("Error!!")

print(f"total sum is {total}")

# Write a program to build a menu-driven To-Do List using loops and conditions.
todo_list = []
while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")                                            
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter the task to add: ").strip()
        todo_list.append(task)
        print("Task Added!")

    elif choice == 2:
        if not todo_list:
            print("No tasks in the list.")
        else:
            for i in range(len(todo_list)):
                print(f"{i + 1}. {todo_list[i]}")

    elif choice == 3:
        if not todo_list:
            print("No tasks to remove.")
        else:
            for i in range(len(todo_list)):
                print(f"{i + 1}. {todo_list[i]}")
            if todo_list:
                num = int(input("Enter the number of the task to remove: "))
                if 1 <= num <= len(todo_list):
                    todo_list.pop(num - 1)
                    print("Task removed successfully!")
                else:
                    print("Invalid task number.")

    elif choice == 4:
        print("Exiting To-Do List application.")
        break














