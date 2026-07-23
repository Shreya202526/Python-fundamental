'''13. Number Range Display System (if-elif with loops)*
A number analysis tool processes two input values and displays numbers between them based on their relationship.

* If the first number is less than the second, display numbers in ascending order
* If the first number is greater than the second, display numbers in descending order
* If both numbers are equal, display "Both numbers are same"

Write a program using *if-elif-else and loops* to implement this logic.

Input: 5, 10
Output: 5 6 7 8 9 10

Input: 10, 5
Output: 10 9 8 7 6 5

Input: 7, 7
Output: Both numbers are same'''



'''a=int(input("Enter the 1st  number="))
b=int(input("Enter the 2nd number="))
if a<b:
    for i in range(a,b+1,1):
        print(i,end=" ")
elif a>b:
    for i in range(a,b-1,-1):
        print(i,end=" ")
elif a==b:
        print("Both number are same")'''



a=int(input("Enter the 1st  number="))
b=int(input("Enter the 2nd number="))
if a<b:
    i=a
    while i<b:
        print(i,end=" ")
        i=i+1
elif a>b: 
    i=a
    while i>b:
        print(a,end=" ")
        i=i-1
elif a==b:
        print("Both number are same")

