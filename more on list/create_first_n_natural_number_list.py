# Write a Python script to create a list of first N natural numbers.

n = int(input("Enter value of N ="))
list,i =[],1


# METHOD - 1
while i<=n:
    list.append(i)
    i+=1
print(list)

# METHOD - 2
list1 = [x for x in range(1,int(input("Enter n = "))+1)]
print(list1)