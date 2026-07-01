'''2. Count Numbers Divisible by 7 Between Two Numbers

A company filters lucky coupon numbers divisible by 7.
Write a program using loops to count such numbers in range.

Input:
1 30

Output:
Count = 4'''


a,n =map(int,input("Enter the number=").split())
count=0
i=a
while i<=n:
      if i%7==0:
          count=count+1
      i=i+1
print(count)



a,n =map(int,input("Enter the number=").split())
count=0
i=a
for i in range(a,n+1):
      if i%7==0:
          count=count+1
      i=i+1
print(count)






