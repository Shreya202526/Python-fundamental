'''4.Spy Number Detector
A cybersecurity system flags special numeric codes.
A number is called a Spy Number if:
Sum of digits = Product of digits
Write a program to check whether the entered number is Spy Number or Not.
Input:
1124
Output:
Spy Number'''

num=int(input("Enter the number"))
i=num
sum=0
prod=1
while num>0:
    d=num%10
    sum=sum+d
    print(sum)
    prod=prod*d
    print(prod)
    num=num//10
if sum==prod:
    print("Spy Number")  
else:
    print("Not Spy Number")  
