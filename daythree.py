# match case
# Match case is similar to c switch case and if else
# we define a variable in match and the value of that matches with case is executed



a = float(input("Enter the First number? "))
b = float(input("Enter the second number? "))

choose = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for Division:"))

match choose:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4: 
        print(a/b)
    case _:
        print("invalid input! please retry it")

# Loops
# Loops are used to execute a same block of code repeateadly

# For loop => when we know the conditions i.e. start and stop conditions
# While Loop => when we know the stopping condition
# Iterator - it is simply a variable that stores a value while the loop is running
# Iterable - Group data type in which the loop is running
# Iteration - one complete execution of a loop

list1 = [1,2,3,"Zeeson",[7,8,9]]
# syntax of for loop
# for iterator in iterable:
#     statements

for i in list1:
    print(i)

# note: In dictionary, it only executes the keys #list1(i).get()

# range(Start,End, Step) => provides range of elements
# If one value is provided in range(), it will be for end value. End value is always is exclusive

