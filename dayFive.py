# Formatted String => f string


name = "Zeeson"
age = 29
position = "Developer"

# print("Name = ",name,"Age = ", age, "Position = ", position)

# Alternated way using f string
print(f"Name = {name}, Age = {age}, Position = {position}")


# Function

# Built- IN functions

# A block of code that performs a specific task


# types of arguments: 1. Positional arguments=> args  2. Keyword Arguments => kwargs

# 1. positional Arguments => the normal values we pass to the function.  
          #The parameters recieves the arguments according to their position

# Example:
def subtract(a,b):
    print(a-b)

subtract(10,5)

# 2. Keyword arguments => The arguments passed in a key value pair. 

# Lambda Functions => function in one line syntax: => variable = lambda parameters: statements
# Call lambda function => variable(arguments)


#Example:

add = lambda x,y : x + y

output = add(20,30)
print(output)