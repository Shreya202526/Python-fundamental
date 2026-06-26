'''6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to *check whether a number is an Armstrong number using loops*.

Input: 153
Output: Armstrong'''



'''num=int(input("Enter the number"))
org_num=num
temp=0
for i in range(len(str(num))):
    n=num%10
    temp=n**3+temp
    num=num//10
if(org_num==temp)
   print("Armstrong")
else:
   print("Not Armstrong")'''



num=int(input("Enter the number"))
org_num=num
temp=0
while num>0:
    n=num%10
    temp=n**3+temp
    num=num//10
if(org_num==temp):
   print("Armstrong")
else:
   print("Not Armstrong")

    


	
    



