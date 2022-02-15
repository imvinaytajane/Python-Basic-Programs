# Python Program for n-th Fibonacci number
# By Vinat Tajane on 9th Feb 2022

def fib(n):
    if n <= 0:
        print("incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


n = int(input("Enter Position of Fiboacci Number:"))
print("Your Fibonacci is ", fib(n))
