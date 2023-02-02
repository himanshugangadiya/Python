# Write a python script to check whether a given number is divisible by 5 or not


# single line
print("Divisible" if(int(input("Enter a number"))%5==0) else "Not divisible" )


# if else
x = int(input("Enter a number : "))

if(x%5==0):
    print("Divisible")
else:
    print("Not divisible")
