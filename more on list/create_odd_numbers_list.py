# Write a Python script to create a list of first N odd natural numbers

n,list,i = int(input("Enter N = ")),[],1

# METHOD - 1
while i<=n*2:
    if(i%2==1):
        list.append(i)
    i+=1
print("Odd numbers list",list)

# METHOD - 2
list1=[x for x in range(1,int(input("Enter n = "))*2+1,2) ]
print("odd numbers list",list1)