# Set
# Unordered grouped data type taht doesnot allow duplicates
# Set is wrapped with {}


set_one = {1,5,"Zeeson",7,8,"Manandhar"}
print(set_one)
print(type(set_one))

# Dictionary
# Comes in Key-value pair but is also warpped in {}

dict_one = {
    "name": "Zeeson",
    "lastname": "Surname",
    "age": 29,
    "marks": 85
}
print(dict_one.keys())
print(type(dict_one))



# Union in Sets

sports_one = {"football", "basketball","baseball"}
sports_two = {"football","Table tenis"}

result = sports_one.union(sports_two)
print(result)

# Create a list of username and take input from user and if it matches it

username = ["zeeson","ram","hari","syam"]
user = input("Enter your Username ?").lower()
if user in username:
    print("The user is Found")
else:
    print("Not Found!")


# Syntax of IF Else

#if conditions:
#     Statements
# else:
#      Statements


# Elif Ladder
# Elif ladder is used when you have multiple conditions

# Calculator using IF...ELSE with text choices

# Taking Input from User
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
if num2 != 0:
    div = num1 / num2 
else:
    div = "Cannot divide by zero"
    
print("Choose Operation: add, sub, mul, div")

choice = input("Enter your choice: ").lower()  

# Applying IF–ELSE 
if choice == "add":
    print("Result:", add)

elif choice == "sub":
    print("Result:", sub)

elif choice == "mul":
    print("Result:", mul)

elif choice == "div":
    print("Result:", div)

else:
    print("Invalid choice")


