'''Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number'''


n=int(input("Enter the number="))
sum=0
i=1
while n>0:
      d=n%10
      sum=sum+d
      n=n//10
print("Sum=",sum)
for i in range(2,sum):
    if sum%i==0:
       sum=sum+1
       print("Normal no")
       break
else:
       print("Lucky  Number")
