

'''4. Strong Number Checker
A digital lock opens only for strong numbers.
A strong number is a number whose sum of factorial of digits equals the number.
Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number'''

num =int(input("Enter the number="))
temp=num
sum=0
fact=1
while num>0:
      n=num%10
      while n>0:
            fact=fact*n
            n-=1
      sum=sum+fact
      fact=1
      num=num//10         
if sum==temp:
   print("Strong number")
else: 
   print("Not Strong number")
      

