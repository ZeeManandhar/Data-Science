# Pratice Questions:

# Python Exercises

# 1. Make a calculator program using Python functions and loop

# 2. Print a multiplication table of the number that is input by the user

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 3. Check if the given number is even or odd

num1 = int(input("Enter a number: "))

if num1 % 2 == 0:
    print(f"{num1} is Even")
else:
    print(f"{num1} is Odd")


# 4. Check if a given number is palindrome or not
num = input("Enter a number: ")

if num == num[::-1]:
    print("The Number is a Palindrome")
else:
    print("The Number is NOT a Palindrome")

# 5. Make a simple login system without registration using functions

users = {"ZeeMdr":"Zee123","Sunildev":"Sunil123","ArvindGroot":"Arbind123"}
login_username = input("Enter your username please: ")
login_password = input("Enter your password please: ")

if login_username in users:
    pass
    if login_password == users[login_username]:
        print("Welcome user!! Login Sucessful")
    else:
        print("Invalid credentials!!")



# 6. Make a login system using registration using function
# 7. Print all the even numbers in a list of numbers.

list1 = [1,2,3,4,5,6,7,8]

new_list = []

for i in list1 :
     if i % 2 == 0:
       new_list = new_list + [i]
print(new_list)
