# Fimding Sum of n Numbers
# Made by Vinay on 05 Sept 2021
total = 0
print('======================================================')
print('---------- Calculate Sum of n Numbers ----------')
print('-NOTE------Enter "0(Zero)" to view sum--------')
print('======================================================')

while True:
    num = input("Enter Number:")
    if num == '0':
        break
    total = total + float(num)

print("Total Sum is:", total)
