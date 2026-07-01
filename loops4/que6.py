'''6. Composite Number Detector – Risk Version

A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2'''


'''n=int(input("Enter the number")) 
smallest=n
i=2
fac=2
flag=0
while i<n:
      if n%i==0:
         print(i)
         if smallest>i:
            smallest=i
         flag=flag+1
         fac=fac+1
      i=i+1
if  flag==0:
    print("Not Composite")
else:
    print("Composite")  
print("Factors count",fac) 
print("smallest",smallest)'''
n=int(input("Enter the number"))
count=0
i=2
smallest=100
while n>i:
      if n%i==0:
         if smallest>i:
            smallest=i
         count=count+1
      i+=1
else:
      if count>1:
         print("Composite number",count+2)
         print(i)
      else:
         print(" Not Composite number")