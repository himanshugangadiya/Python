
# Write a python script to calculate simple interest

amount = int(input("Enter amount : "))
time = int(input("Enter time of years : "))
rate = float(input("Enter rate : "))

interest = (amount*time*rate)/100

print("simple interest : ",interest)