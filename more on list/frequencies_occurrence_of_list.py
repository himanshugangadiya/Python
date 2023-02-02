# Write a Python script to print distinct elements along with their frequencies of occurrence in the list.

list = [10,20,30,10,10,"hello",20,"t","t",True,"d",True,10]
list1 =[]
for x in list:
    if x in list1:
        continue
    list1.append(x)
for x in list1:
    print("frequencies value = {} , count = {}".format(x,list.count(x)))