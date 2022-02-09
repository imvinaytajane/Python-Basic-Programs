num = list()

while True:
    add = input("Enter Number:")
    if add == 'done':
        break
    add = float(add)
    num.append(add)
avg = sum(num)/len(num)
print("Average is", avg)
