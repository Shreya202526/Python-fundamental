'''8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime'''


n=int(input("Enter the number"))
larg=0
small=n%10
flag=0
while n>0:
      d=n%10
      if larg<d:
         larg=d
      if small>d:
          small=d 
      n=n//10
      
print(larg)
print(small)
sum=larg+small
for i in range(2,sum//2):
          if sum%i==0:
             flag=1
             break
else:
    print("prime no",sum)
if flag==1:
   print("not prime")
print(sum)


      


