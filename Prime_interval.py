# Python program to print all Prime numbers in an Interval
# Made by Vinay on 08 Sept 2021
print("Enter Range in Which you want to Find Prime Numbers!")

start = int(input("Start:"))
end = int(input("End:"))
count = 0

print("Prime Numbers in Given Range are:")

for num in range(start, end+1):
    # as 1 is neither prime or composite
    if num > 1:
        for d in range(2, num):
            if (num % d) == 0:
                break
        else:
            print(num)
            count = count + 1
print("Total Prime Number in Interval", start, "to", end, "is", count)
