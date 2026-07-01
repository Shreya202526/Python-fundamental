
''' Alternate Digit Prime Checker
A math lab adds alternate digits from right side.
Write a program to:
- Find sum of alternate digits
- Check whether sum is Prime or Not
Input:
12345
Output:
Alternate Sum = 9'''
n=int(input("Enter the number"))
sum=0
i=1
while n>0:
      d1=n%10
      sum=sum+d1
      n=n//100
print("Alternate sum",sum)
i=2
while i>sum//2+1:
      if sum%i==0:
         print(" not prime no")
         break
      i=i+1
else:
     if sum<=1:
          print("Not prime")
     else:
          print("Prime number")