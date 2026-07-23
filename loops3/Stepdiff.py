'''9.
Step Difference Number Analyzer

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
Unbalanced Number
'''

n=int(input("Enter the number"))
m=len(str(n))-1
diff=0
rev=0
sum=0
largest=1
while n>0:
      rev= rev*10 + n%10
      n=n//10
print(rev,end=" ")
while rev>0:
      d1=rev%10
      rev=rev//10
      d2=rev%10
      if rev>0:
         diff=abs(d1-d2)
         print(diff)
         sum=sum+diff
         if diff>largest:
            largest=diff
print("Sum=",sum)
print("largest=",largest)
if sum%m==0:
    print("Balanced number")
else:
      print("UnBalanced number")


      
      




