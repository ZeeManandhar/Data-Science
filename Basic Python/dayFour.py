# Loop Control Statement
#break => when break encounters, it terminates the loop
#continue => when continue encounters, it skips the current iteration but continues the loop


list1 = [1,2,3,4,5,6,7]

for i in list1:
    if i == 5:
        continue
    print(i)

for i in range(4):
    for j in range(3):
        if j == 1:
            break
        print(i,j)
    print(i)


# While Loop
# Syntax for While loop: 
# while Condition:
# Statements

a = 10 
while a < 20:
    print(a)
    a +=1

#Update the calculator program using loop

while True:

    num1 = int(input("Enter the First Number "))
    num2 = int(input("Enter the Second number "))
    choice  = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for exit: "))

    if choice == 1:
      print(num1+num1)
    elif choice == 2:
       print(num1-num2)
    elif choice == 3:
       print(num1*num2)
    elif choice == 4:
       print(num1/num2)
    elif choice == 5:
       break
    else:
        print("Invalid input")


