# Write a Python script to create a list of city names taken from the user.


n,list,i = int(input("total enter number of city name = ")),[],0
while i<n: # i=0  i<n
    list.append(input("Enter city name = "))
    i+=1  # i+=1

print("city names list : ",list)