# incomplete
s = int(input("Start:"))
e = int(input("End:"))
prime = None

for i in range(s,e):
    d = range(2,i)
    for m in d:
        if i%m==0:
            break
        elif prime!=i:
            print(prime)
        prime = i

print(prime)