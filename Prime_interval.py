# Made by Vinay on 08 Sept 2021
print("Enter Range in Which you want to Find Prime Numbers!")

start = int(input("Start:"))
end = int(input("End:"))

print("Prime Numbers in Given Range are:")

for num in range(start, end+1):
    # as 1 is neither prime or composite
    if num > 1:
        for d in range(2,num):
            if (num % d)==0:
                break
        else:
           print(num)