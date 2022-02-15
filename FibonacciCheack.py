# Python Program to check if a given number is Fibonacci number
# By Vinay Tajane on 9th Feb 2022

print("==== Fibonacci Number Check ====")
num = int(input("Enter Number:"))


def fib(n):
    if n <= 0:
        return
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


n = 0
f = None
while fib(n+1) <= num:
    n = n+1
    if num == fib(n):
        f = 'found'
if f == 'found':
    print('Yes,', num, 'is Fibonacci!')
else:
    print('Sorry,', num, 'is not Fibonacci!')
