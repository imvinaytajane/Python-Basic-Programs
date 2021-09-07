# Made by Vinay on 07 Sept 2021
s = int(input("Start:"))
e = int(input("End:"))
prime = None
if s==1 or s==2:
    print(2)

for i in range(s,e):
    d = range(2,i)
    for m in d:
        if i%m==0:
            break
        elif prime!=i and prime!=None:
            print(prime)
        prime = i

print(prime)