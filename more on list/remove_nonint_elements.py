# Write a Python script to remove all non int values from a list.

list = [10,20,"hello",2.5,True,450]


i=0
list1=[]
for x in list:
    if type(x)==int:
        list1.append(x)

print(list1)
