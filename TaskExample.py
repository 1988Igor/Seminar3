from tkinter import N
from math import pow

def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)                #pow (fib(n+2), -fib(n+1)) 
n = int(input('Enter the number'))
lst = []
for element in range(1,n):
    lst.append(fib(element))
print(lst)

