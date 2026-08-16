'''2.
Step Difference Number Analyzer(3.5 marks)

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number'''

num=int(input("Enter the number"))
l=str(num)
l2=len(l)
temp=num
i=num
rev=0
count=0
sum1=0
large=0
while i>0:
      d=i%10
      rev=rev*10+d
      i=i//10
print("Reverse=",rev)
print("Step Difference=",end="")
j=rev
while j>0:
      d=j%10
      j=j//10
      d2=j%10
      if j>0:
         diff=abs(d2-d)
         if diff>large:
            large=diff
         print(diff,end=" ")
         k=diff
         while k>0:
            d=k%10
            sum1=sum1+d
            k=k//10
print()
print("sum=",sum1)
print(large)
if sum1%l2==0:
   print("Balanced Number")
else:
   print("Unbalanced Number")





