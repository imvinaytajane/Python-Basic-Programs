# Python Program for simple interest
# Made by Vinay on 05 Sept 2021
print("==== Lets Find Simple Interest! ====")

p = int(input("Enter Principal Ammount:"))
r = int(input("Enter Rate of interest:"))
t = int(input("Time Interval of Interest:"))

si = (p*r*t)/100

print("Simple Interest is", si)
