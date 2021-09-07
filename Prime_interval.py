# incomplete
s = int(input("Start"))
e = int(input("End"))

for i in range(s,e):
    d = range(2,i)
    for m in d:
        if i%m==0:
            break
        print(i,"is prime")
