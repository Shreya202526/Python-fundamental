'''5.
Automorphic Number Lock
A high-security digital locker validates access codes using a special mathematical rule.
When a user enters a numeric code, the system squares the number and checks whether the last digits 
of the square match the original number.
 If it matches, the code is considered valid.
An Automorphic Number is a number whose square ends with the same number.
Task:
Write a Python program to check whether a given number is an Automorphic Number or not.

Example:
Input:
25

Output:
Automorphic Number'''

n=int(input("enter the number"))
sq=n*n
i=1
while n>0:
    x=n%10
    y=sq%10
    if x!=y:
       print("Not automorphic")
       break
    n=n//10
    sq=sq//10
else:
    print("Automorphic number")