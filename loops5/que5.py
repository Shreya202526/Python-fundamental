'''Number Stability Analyzer
A scie5nce lab studies whether digits are in increasing order.
Write ay next digit is greater than previous print Stable Number
- using for-else loop:
- If ever

      Else Unstable Number
Input
12359
Output:
Stable Number'''
 
n=int(input("Enter the number"))
rev=0
i=1
while n>0:
      d=n%10
      rev=rev*10+d
      n=n//10
print(rev)

for i in  range(1,len(str(rev))):
      pre=rev%10 
      rev=rev//10
      next=rev%10
      print(pre)
      print(next)
      if pre>=next:
         print("unstable number")
         break 
else:
    print("stable ") 
      