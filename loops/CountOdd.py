'''8. Count Odd Digits*
A banking system flags IDs with too many odd digits for further verification.
Write a program to *count the number of odd digits in a given number using loops*.

Input: 123456
Output: Odd digits count = 3'''

num=int(input("Enter the number"))
count=0
for i in range(len(str(num))):
    n=num%10
    num=num//10
    if n%2!=0:
       count=count+1
print("Even digits count",count)
    