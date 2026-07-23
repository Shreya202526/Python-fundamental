'''Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407'''

a=int(input("Enter the starting Number:"))
b=int(input("Enter the Ending Number:"))
for i in range(a,b+1):
    n=i
    temp=i
    rev=0
    power=0
    p=len(str(n))
    for j in range(len(str(n))):
        d=n%10
        power=power+d**p
        n=n//10
    if temp==power:
       print(temp)
