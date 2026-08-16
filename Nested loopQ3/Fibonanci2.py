'''Fibonacci Population Growth Tracker

A wildlife research team is studying the growth of a rare species.  
They observe that the population follows a Fibonacci pattern:

- Month 1 → 0 animals  
- Month 2 → 1 animal  
- Every next month → sum of previous two months  

The researchers want to analyze the growth pattern.

Write a program to:

- Read number of months n
- Generate Fibonacci series up to n months using loop
- Print population for each month
- Find total population observed
- Count how many months population exceeded 5

Input:
8

Output:
Population Growth:
0 1 1 2 3 5 8 13

Total Population = 33
Months with Population > 5 = 2'''

n=int(input("Enter the number="))
month1=0
month2=1
next_month=0
i=1
while i<=n-1:
      total=month1+month2
      print(month1,end=" ")
      next_month= month1+ month2
      month1=month2
      month2=next_month
      i=i+1      
print(total)



