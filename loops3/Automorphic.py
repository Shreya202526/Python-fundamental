'''6. Automorphic Number Checker

A digital security company designs smart lockers that open only for special self-matching numeric codes. When a user enters a number, the system squares the number and checks whether the result ends with the same digits as the original code. If yes, the locker grants access.
An automorphic number is a number whose square ends with the same number.
Example:
25² = 625

Write a program using loops to check whether the entered number is an Automorphic number.

Input:
25

Output:
Automorphic Number'''



n=int(input("Enter the number="))
temp=n
square=1
i=1
while i<=n:
      square=n*n
      i=i+1
num=n%10
d=square%10
if d==num:
   print("Automorphic Number")
else:
   print("Not Autotomorphic")




n=int(input("Enter the number="))
temp=n
square=1
for i in range(1,n):
      square=n*n
num=n%10
d=square%10
if d==num:
   print("Automorphic Number")
else:
   print("Not Autotomorphic")












