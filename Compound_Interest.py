# To Find Compound Intrest
# Made by Vinay on 05 Sept 2021
print("==== Lets Find Compound Interest! ====")

p = int(input("Enter Principal Ammount:"))
r = float(input("Enter Rate of interest:"))
t = int(input("Time Interval of Interest in Terms of Year:"))

pi = p*(1+r/100)**t

print("Compound Interest is:",pi)