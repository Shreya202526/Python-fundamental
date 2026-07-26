'''Perfect Number Analyzer

A mathematics research system analyzes special numbers within a given range.
The user enters a starting number and ending number.
The system checks every number in that range and displays all Perfect Numbers using nested loops.

(A Perfect Number is a number whose sum of proper divisors is equal to the number itself.)

Input:
Enter starting number: 1
Enter ending number: 1000

Output:
Perfect Numbers are:
6
28
496'''


a=int(input("Enter Starting number:"))
b=int(input("Enter Ending number:"))
while a<=b:
      n=a
      if n>2:
         i=2
         while i<=n//2:
                if n%i==0:
                   break
                i=i+1
         else:
              print(n)
      a=a+1


