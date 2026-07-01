'''1. Triple Operation Prime Verification System
A cybersecurity company generates a security score from entered access code.
Write a program to:
- Find sum of digits of the number
- Reverse the number
- Find absolute difference between original number and reverse
- Add digit sum and difference
- Check whether final result is Prime or Not Prime
Input:
4215
Output:
Sum of Digits = 12
Reverse = 5124
Difference = 909
Final Result = 921
Not Prime'''

n=int(input("Enter the number="))
temp=n
rev=0
sum=0

while n>0:
      d=n%10
      rev=rev*10+d
      sum=sum+d
      n=n//10 
diff=abs(temp-rev)
final=sum+diff
print(rev)
print(sum)
print(diff)
print(final)
i=2
while i<final//2+1:
      if final%i==0:
         print("Not prime")
         break
      i=i+1
          
else:
     print("Prime no")
