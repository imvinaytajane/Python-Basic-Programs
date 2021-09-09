# Made by Vinay on 09 Sept 2021
num = int(input("Enter Number:"))
for n in range(2,num-1):
    if num % n == 0:
        print(num ,"is Composite Number")
        break
else:
    print(num,"is Prime Number")