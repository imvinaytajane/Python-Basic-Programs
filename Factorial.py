# Python Program for factorial of a number
# Made by Vinay on 06 Sept 2021
print("==== Let us find Factorial! ====")
n = int(input("Enter a Number to Find its Factorial:"))
num = n
fact = n

while n != 1:
    fact = fact * (n-1)
    n = n-1

print("Factrorial of", num, "is", fact)
