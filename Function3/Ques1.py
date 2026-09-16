'''Assignment 1: Smart Street Lights (Fibonacci Series)

A smart city installs street lights in a newly developed area. The number of lights installed each month follows the Fibonacci pattern.

Month 1 → 0 lights
Month 2 → 1 light
Every following month, the number of lights installed is the sum of the previous two months.

As a software developer, your task is to help the city planning department generate the installation schedule.

Task

Write a recursive function to print the first N Fibonacci numbers.

Input
Enter the number of months:
7
Output
0 1 1 2 3 5 8


def fibonacci(n):
    if n==0:
        return 
    elif n==1:
        return 1
    else:
     return fibonacci(n-1)+fibonacci(n-2)
n = int(input("Enter the number of terms: "))

for i in range(n):
    print(fibonacci(i), end=" ")'''

def fibonacci(n,a=0,b=1):
    if n == 0:
        return
    print(a,end=" ")
    fibonacci(n-1,b,a+b) 
n = int(input("Enter the number: "))
fibonacci(n)