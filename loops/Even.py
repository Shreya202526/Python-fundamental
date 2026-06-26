'''Even Numbers Between Two Numbers*
A teacher wants to assign only even roll numbers for a special activity. The system should display all even numbers between two given numbers.
Write a program to *display all even numbers between two numbers using loops*.

Input: 10, 20
Output: 10 12 14 16 18 20'''

'''a=int(input("Enter the number="))
b=int(input("Enter the number="))
for a in range(a,b+1):
    if a%2==0:
       print(a,end=" ")'''



a=int(input("Enter the 1st  number="))
b=int(input("Enter the 2nd number="))
while a<b:
    if a%2==0:
       print(a,end=" ")
    a=a+1