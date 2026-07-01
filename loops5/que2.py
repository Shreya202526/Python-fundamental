'''2. Multi Stage Prime Lock System A smart locker opens only if final derived number is prime.
Write a program to:
- Find sum of digits
- Find product of digits
- Find difference between product and sum
- Count digits in difference
- Add digit count to difference
- Check whether final result is Prime or Not
Input:
234
Output:
Sum = 9
Product = 24
Difference = 15
Digits = 2
Final Result = 17
Prime'''

n=int(input("Enter the number="))
prod=1
sum=0
i=1
while n>0:
      d=n%10
      sum=sum+d
      prod=prod*d
      n=n//10
diff=prod-sum
count_digit=len(str(diff))
final=diff+count_digit        
print(sum)
print(prod)
print(diff)
print(count_digit)
print(final)
i=2
while i<=final//2+1:
      if final%i==0:
         print("Not Prime")
         break
      i=i+1
else:
     if final<=1:
          print("Not Prime")
     else:  
           print("Prime no")
