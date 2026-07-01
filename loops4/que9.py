'''9.Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime'''

n=int(input("Enter the number="))
count_even=0
count_odd=0
while n>0:
      d=n%10
      if d%2==0:
         count_even=count_even+1
      
      else:
         count_odd=count_odd+1
      n=n//10
print("Even Count=", count_even)
print("Odd Count=", count_odd)
diff=abs(count_even-count_odd)
flag=0
for i in range(2,diff//2):
    if diff%i==0:
       flag=1
else:
   if diff==0:
      print("Difference is not prime")
   else:
      print("Difference is prime")
if flag==1:
   print("Difference is not prime")
     
   



