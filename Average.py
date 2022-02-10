# Python Program to Find Average of n Numbers
# By Vinay Tajane on September 2021
num = list()
print("==== Find Average of List of Your Numbers! ====")

while True:
    add = input("Enter Number:")
    print("\nEnter 'done' to end list")
    if add == 'done':
        break
    add = float(add)
    num.append(add)
avg = sum(num)/len(num)
print("==============================================================")
print(" Average of", num, "is", avg)
print("==============================================================")
