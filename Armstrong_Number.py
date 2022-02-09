# Program to Check it is Armstrong Number or Not
# Made by Vinay on 06 Sept 2021
print("==== Armstrong Number Verify ====")
num = input("Enter a Number to check it is Armstrong Number or Not!\n")
power = len(num)
num = int(num)
num_check = num
i = 0
sum = 0
while i < power:
    temp = num % 10
    sum = sum + temp**power
    num = num//10
    i = i+1
if sum == num_check:
    print('Yes,', num_check, "is a Armstrong Number")
else:
    print("No,", num_check, "is not a Armstrong Number")
