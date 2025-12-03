# Concept of Map
list1 = [1,2,3,4,5]
result = list(map(lambda i : i+5, list1))
print(result)
result=[]

# Same thing done using (For loop)
for i in list1:
    result.append(i+5)
print(result)


# Concept of filter
list2 = [1,2,3,4,5]
result=list(filter(lambda x : x+5>=10, list2))
print(result)

# Alternative Way: 

for i in list2:
    if i+5>=10 :
        print([i])

# Concept of Reduce
from functools import reduce
result = reduce(lambda x,y : x+y ,list1)
print(result)

# Alternative Way:
output = 0
for i in list2:
    output = output + i
print(output)

# Concept of zip
names = ["Zeeson","Sunil","Arbind","Niraj"]
age = [22,24,25,30]
result = tuple(zip(names,age))
print(result)

# Alternative Way:

new_result = []

for i in range(len(names)):
    for j in range(len(age)):
        if i == j:
            new_result= new_result + [(names[i], age[j])]
print(tuple(new_result))

# # List comprehension
# list1 = [i for i in range(1,101)]
# print(list1)

# # Indexing and Slicing

# print(list1[-2])

# # Slicing
# # print(list1[5:10])
# # print(list1[:10])
# # print(list1[:])
# # print(list1[50:])


# # print(list1[5:10:2])
# # print(list1[:10:3])
# # print(list1[::2])
# # print(list1[50::3])

# print(list1[50:10:-2])

