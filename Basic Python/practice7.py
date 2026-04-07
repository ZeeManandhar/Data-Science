# 1. BASIC LEVEL (Foundations) 

# Write a program to check whether a number is positive.

num = 5

if num > 0:
    print(f"{num} is Positive Number.")
else:
    print(f"{num} is Negative Number.")


# Write a program to check whether a number is negative.

num = -1

if num < 0:
    print("Negative Number")
else:
    print("Not a Negative Number")

# Write a program to check whether a number is zero.

num = 0

if num == 0:
    print("Zero")
else:
    print("Not Zero")

# Write a program to check whether a number is greater than 100.

num1 = int(input("Enter a Number: "))

if num1 > 100:
    print(True)
else:
    print(False)


# Write a program to check whether a number is even.

number = 7

if number%2 == 0:
    print("Number is Even")
else:
    print("Not an Even Number")

# Write a program to check whether a number is odd.

number = 8

if number%2 != 0:
    print("Odd Number!")
else:
    print("Not an Odd Number!")

# Write a program to check whether a person is eligible to vote.

age = int(input("Enter your Age Please: "))

if age >= 18:
    print("Eligible to Vote!")
else:
    print("Not Eligible!")

# Write a program to check whether a temperature is above freezing point.

temp = float(input("Enter temperature in °C: "))
if temp > 0:
    print("Above freezing")
else:
    print("Not above freezing")

# Write a program to check whether a number is positive or negative.

num1 = int(input("Enter your number: "))

if num1 > 0:
    print("Positive Number!")
else:
    print("Negative Number!")

# Write a program to check whether a student has passed or failed (pass mark = 40).

marks = int(input("Enter your marks please: "))

if marks >= 40:
    print("You are Passed!")
else:
    print("You Failed")


# Write a program to compare two numbers and print the greater one.

num1 = int(input("Enter The First Number: "))
num2 = int(input("Enter The Second Number: "))

if num1 > num2 :
    print(num1)
else:
    print(num2)

# Write a program to check whether a person is adult or minor.
age = int(input("Enter your Age Please: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")

# Write a program to check whether a year is leap year or not .

year = int(input("Enter the year: "))

if year % 4 == 0 and year % 100 != 0:
    print("Leap Year!")
else:
    print("Not a Leap Year!")

# 2. INTERMEDIATE LEVEL (Control Flow & Decisions) 

# Write a program to validate a password.

password = input("Enter your Password Please: ")
valid_password = ["admin@123","ktm123#","Zeeson1@@"]

if password in valid_password:
    print(True)
else:
    print(False)

# Write a program to check whether a user is logged in or not.

# Write a program to print grades based on marks.

marks = int(input("Enter your mark please: "))

if marks >= 90 and marks <= 100:
    print("Grade: A+")
elif marks >=80 and marks < 90:
    print("Grade: A")
elif marks >= 70 and marks < 80:
    print("Grade: B+")
elif marks >= 60 and marks < 70:
    print("Grade: B")
elif marks>=50 and marks < 60:
    print("Grade: C+")
elif marks >= 40 and marks <50:
    print("Passed!!")
elif marks < 40:
    print("Failed!")
else:
    print("Invalid Input!!")

# Write a program to print traffic signal action (red, yellow, green).

color = input("input the signal: ").strip().lower()

match color:
    case "red":
        print("Stop!")
    case "yellow":
        print("Get Ready to Stop/Go!")
    case "green":
        print("Go!!!!")
    case _:
        print("Default Signal!")


# Write a program to classify a number as positive, negative, or zero.

number = int(input("Enter the Number to Check Positive, Negative or Zero = "))

if number > 0:
    print("Positive!")
elif number < 0:
    print("Negative!")
elif number == 0:
    print("Zero")
else:
    print("Invalid Number!")

# Write a program to print day type (weekday/weekend).

day = input("Enter the Day: ").strip().lower()

match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("Weekday")
    case "saturday" | "sunday":
        print("Weekend")
    case _:
        print("Not a Valid Day!")

# Write a program to create a simple menu system using numbers.

choice = int(input("Choose Food Options: 1, 2, 3, 4 : "))

match choice:
    case 1:
        print("MoMo")
    case 2:
        print("Club Sandwich!")
    case 3:
        print("French Fries")
    case 4:
        print("Pizza")

    case _:
        print("Sorry! We dont have further options!!")



# Write a program to check whether a username exists in a predefined list.

username = input("Enter your username please: ")

usernames = ["ZeesonGroot1","DalliDon@","SunilChintu#111"]

if username in usernames:
    print("User Exits!!!")
else:
    print("User not Found!!!")

# Write a program to check whether a character exists in a string.

text = input("Enter a text: ")
ch = input("Enter a character: ")
if ch in text:
    print("Character found")
else:
    print("Character not found")


# Write a program to check whether a key exists in a dictionary.

bikes = {
    "Name": "Duke 200",
    "Brand" : "KTM",
    "Made Year" : 2007
}

if "Brand" in bikes:
    print("Key exits!")
else:
    print("Key doesnot exits!")


# Write a program to check whether an item is available in stock.

item = input("Enter the item to check its availability: ").strip().lower()

stock = ["pen","pencil","eraser","notebook","ruler","stickers"]

if item in stock:
    print("Item Available!")
else:
    print("out of stock!!")

# 3. LOGICAL LEVEL (Reasoning & Combination) 

# Write a program to validate email format using in.

email = input("Enter your email: ")

if "@" in email and ".com" in email:
    print("Email Valid!")
else:
    print("Email not Valid")


# Write a program to check eligibility based on age and citizenship.

age = int(input("Enter your Age please: "))
has_citizenship = input("Do you have citizenship: (True/False)")

if age >=18:
    if has_citizenship is True:
        print("You meet the eligibility Criteria!")
    else:
        print("You donot meet the criteria!")


# Write a program to validate login using username and password.

username = input("Enter your registered username please: ").strip()
password = input("Enter your password please: ").strip()

credentials = {
    "Zeeson1":"Zee123456#",
    "SunilDon": "Sunil123@"
}

if (username,password) in credentials.items():
    print("Welcome User!")
else:
    print("Invalid username and password!")
    

# Write a program to check access permission using multiple conditions.

is_logged_in = True
role = "editor"
account_active = True

if is_logged_in and (role == "admin" or role == "editor") and account_active:
    print("Access Granted")
else:
    print("Access Denied")

# Write a program to deny access if a user is not logged in.

logged_in = False

if not logged_in:
    print("Permission Denied!")
else:
    print("Access Granted!!")


# 4. ADVANCED LEVEL (Pattern Matching & Structure): 

# Write a program to build a calculator using match.

num1 = int(input("Enter the First NUmber: "))
num2 = int(input("Enter the Second Number: "))

choice = int(input("Enter 1 for Addition, 2 for Subtration, 3 for Multiplication and 4 for Division: "))

match choice:
    case 1:
        print(num1 + num2)
    case 2:
        print(num1 - num2)
    case 3:
        print(num1*num2)
    case 4:
        print(num1/num2)
    case _:
        print("Invalid Operation")


# Write a program to match multiple variables using tuple pattern in match.


item = input("Enter the Item Name: ").strip().lower()

match item:
    case "pen" | "pencil" | "books" | "stickers" | "glue":
        print("Stationary Items!")
    case "pizza"|"burger" | "fries" | "hot dog" | "momo" | "tachos":
        print("Restaurant Items!")
    case "jacket" | "coat" | "sweater" | "pant" | "t-shirt":
        print("Clothing Items")
    case _:
        print("Default Items!")


# Write a program to use match with guard (if) to classify number ranges.

num = int(input("Enter a number: "))

match num:
    case _ if num >= 80:
        print("Grade A")
    case _ if num >= 60:
        print("Grade B")
    case _ if num >= 40:
        print("Grade C")
    case _:
        print("Fail")
