# Write a Python script to create a list of first N even natural numbers.



# METHOD - 1

x = int(input("Enter N = "))
i,list =1,[]
while i<=x*2:
    if i%2==0:
        list.append(i)
    i+=1
print(list)

# METHOD - 2
list1= [x for x in range(1,int(input("Enter N = "))*2+1)  if(x%2==0)]
print(list1)