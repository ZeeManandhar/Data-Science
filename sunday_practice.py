
# 1. Write a program to read a text file and print each line with line numbers.

#Opening the File:

file = open("sample.txt", "r")

line_num = 1

for line in file:
    print(f"{line_num} : {line}")
    line_num = line_num + 1

# Closing the file:
file.close()

# 2. Write a program to create a file and write five lines of text into it.

file = open("Zeeson.txt","w")
file.write("Welcome User!! \n")
file.write("This is the first line! \n")
file.write("This is the Second line! \n")
file.close()

# 3. Write a program to count the number of words in a given text file.

count = 0
file = open("sample.txt","r")

for line in file:
    a = line.split()
    count = count + len(a)

print(count)

file.close()

# 4. Write a program that takes two numbers and handles the error if division by zero occurs.

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")

# 5. Write a program that handles the error when trying to open a file that does not exist.

try:
    file = open("Zeeson1.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found.")


# 6. . Write a program that asks the user for an integer and handles invalid input.

try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)

except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")

# 7.Create a class with two attributes and print the values using objects.

class Student:
    name = "Zeeson"
    age = 22

std1 = Student()

print(std1.name)
print(std1.age)

# 8. 