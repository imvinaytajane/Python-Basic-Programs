# Fimding Sum of Two Number
# Made by Vinay on 05 Sept 2021
total = 0

while True:
    num = input("Enter Number:")
    if num == 'done':
        break
    total = total + float(num)

print("Total Sum is:",total)