# Write a Python script to create a list, where each element of the list is a digit of a given number.

number = input("Enter number = ")
list =[]
for x in number:
    list.append(int(x))
print(list)