# BASIC LEVEL — Function Basics

# Write a program using a function to print "Hello World".

def greet():
    return "Hello World"

result = greet()
print(result)


# Write a program using a function to print your name.

def myName(name):
    return name

data = myName("Zeeson Manandhar")
print(data)

# Write a program using a function to add two numbers.

def add(num1,num2):
    result = num1 + num2
    return result

output = add(6,8)
print(output)

# Write a program using a function to subtract two numbers.

def subtract(num1,num2):
    return num1-num2

print(subtract(10,7))

# Write a program using a function to multiply two numbers.

def multiply(x,y):
    result = x * y
    return result

output = multiply(9,9)
print(output)

# Write a program using a function to divide two numbers.

def division(a,b):
    if b == 0:
        return "Cannot be divided by 0"
    else:
        return a/b

final = division(8,3)
print(final)

# Write a program using a function to check whether a number is even or odd.

def check(num):
    if num%2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

output = check(9)
print(output)

# Write a program using a function to find the square of a number.

def sqr(number):
    sqr_num = number**2
    return sqr_num

output = sqr(4)
print(output)

# Write a program using a function to find the cube of a number.

def Cube(num):
    return num**3

final = Cube(2)
print(final)

# Write a program using a function to check whether a number is positive, negative, or zero.

def check(num):
    if num > 0:
        return "Positive Number"
    elif num == 0:
        return "Zero"
    elif num < 0:
        return "Negative Number"
    else:
        return "Invalid Number"

print(check(-1))

# Write a program using a function to return the length of a string.

def check_len(data):
    length = len(data)
    return f"length of string : {length}"

output = check_len("Zeeson")
print(output)


# Write a program using a function to convert Celsius to Fahrenheit.

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

result = celsius_to_fahrenheit(5)
print(result)

# Write a program using a function to find the maximum of two numbers.

def max_num(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2

result = max_num(10,50)
print(result)

# Write a program using a function to find the minimum of two numbers.

def min_num(num1,num2):
    if num1 < num2:
        return num1
    else:
        return num2

result = min_num(10,2)
print(result)

# Write a program using a function to print numbers from 1 to N.

def range_num(num):
    for i in range(1,num+1,1):
        print(i)

range_num(25)


# INTERMEDIATE LEVEL — Return, Parameters, Defaults:

# Write a program using a function to return the sum of all elements in a list.

def sum_all(values):
    sum = 0
    for i in values:
        sum += i
    return sum
    
result = sum_all([1,2,3,4,5])
print(result)

# Note: Global variables should be used for reading only. (variable outside the function)
# Local variables should be used for modification. (varaible inside the function)


# Write a program using a function to count vowels in a string.

def count_vowels(str1):
    count = 0
    for i in str1:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            count = count + 1
    return count

result = count_vowels("zeeson")
print(f"The Total Number of Vowels in the String is {result}.")

# Write a program using a function to reverse a string.

def rev_str(str2):
    x = str2[::-1]
    return x

output = rev_str("Basketball")
print(output)

# Write a program using a function to check whether a string is a palindrome.

def palindrome(str3):
    if str3 == str3[::-1]:
        return "The String is Palindrome!"
    else:
        return "Not Palindrome String!"
    
output = palindrome("abba")
print(output)

print(palindrome("Hello"))

# Write a program using a function to calculate factorial of a number.

def factorial_num(number):
    fact_num = number
    for i in range(number-1,0,-1):
        fact_num = fact_num*i
    return fact_num

result = factorial_num(5)
print(result)

# Write a program using a function to generate Fibonacci series up to N terms.

def fibonacci(n):
    if n <= 0:
        return []

    if n == 1:
        return [0]

    series = [0, 1]

    for i in range(n - 2):
        next_num = series[-1] + series[-2]
        series.append(next_num)

    return series

result = fibonacci(10)
print(result)

# Write a program using a function to check whether a number is prime.

def prime(number):
    if number <= 1:
        print("Not a prime number")
        return

    for i in range(2, number):
        if number % i == 0:
            print("Not Prime Number!")
            return

    print("Prime Number!")

prime(8)
prime(5)

# Write a program using a function with a default parameter to calculate power of a number.

def power(exponent=2,base=2):
    return base**exponent

result = power(3)
print(result)


# Write a program using a function to return the largest element in a list.


def largest_num(l1):
    large_number = l1[0]

    for i in l1:
        if i > large_number:
            large_number = i
    return large_number

result = largest_num([1,2,99,5,6,3,9])
print(result)

# Write a program using a function to return the smallest element in a list.


def smallest_num(l2):
    small_number = l2[0]

    for n in l2:
        if n < small_number:
            small_number = n
    return small_number

output = smallest_num([2,5,6,1,9,7])
print(output)

# Write a program using a function to count how many times an element appears in a list.

def count_element(l1,target):
    count = 0
    for i in l1:
        if i == target:
            count = count + 1
    return count

output = count_element([1,0,2,3,6,6,6,6,5,5,9],6)
print(output)

# Write a program using a function to remove duplicates from a list.

def rem_duplicate(l1):
    emp_list = []

    for i in l1:
        if i not in emp_list:
            emp_list.append(i)
    return emp_list

result = rem_duplicate([1,2,2,2,2,3,3,3,3,4])
print(result)

# Write a program using a function to merge two lists.

def merge_list(l1,l2):
    set1 = set(l1)
    set2 = set(l2)
    merge_set = set1.union(set2)
    new_list = list(merge_set)
    return new_list

result = merge_list([1,2,3,4,5,6],[4,5,6,7,8,9])
print(result)


# Write a program using a function to sort a list in ascending order.

def sort_list(l1):
    l1.sort(reverse=False)
    return l1
    
print(sort_list(['A','C','D','B','E']))


# Write a program using a function to return only even numbers from a list.

def even_num(l1):
    even_list = []
    for i in l1:
        if i%2 == 0:
            even_list.append(i)
    return even_list

output = even_num([1,2,3,4,5,6,7,8,9])
print(output)


# ADVANCED LEVEL — *args, **kwargs, lambda, map, reduce, zip:

# Write a program using a function with *args to calculate sum of any number of values.

# Write a program using a function with *args to find the maximum value.

# Write a program using a function with **kwargs to display student details.

# Write a program using a function with **kwargs to count how many key-value pairs are passed.

# Write a program using a function that uses both *args and **kwargs.

# Write a program using a lambda function to add two numbers.

# Write a program using a lambda function to find square of a number.

# Write a program using map() to double all elements in a list.

# Write a program using map() to convert a list of strings to uppercase.

# Write a program using reduce() to find the sum of elements in a list.

# Write a program using reduce() to find the product of elements in a list.

# Write a program using zip() to combine two lists into a list of tuples.

# Write a program using zip() to create a dictionary from two lists.

# Write a program using map() and lambda together.

# Write a program using reduce() and lambda together.

# LOGIC and MINI-PROJECT STYLE:

# Write a program using functions to create a menu-driven calculator.

# Write a program using functions to implement a login system using dictionary.

# Write a program using functions to calculate student grade based on marks.

# Write a program using functions to count word frequency in a sentence.

# Write a program using functions to manage a simple contact list (add, view, search).