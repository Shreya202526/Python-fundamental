'''8.
Trimorphic Number Analyzer
A coding system checks cube-based patterns.
A Trimorphic Number:
Cube of number ends with the same number.
Example:
4³ = 64

Write a program to check Trimorphic Number.

Input:
4

Output:
Trimorphic Number'''



n=int(input("enter the number"))
cube=n**3
i=1
while n>0:
    x=n%10
    y=cube%10
    if x!=y:
       print("Not automorphic")
       break
    n=n//10
    cube=cube//10
else:
    print("Trimorphic number")