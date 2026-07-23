'''10.Zero Count Prime Scanner

A banking system checks account numbers.
Write a program to:
- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime'''

n=int(input("Enter the number="))
final=0
zero_count=0
sum=0
smallest=n%10
i=1
while n>0:
    d=n%10
    sum=sum+d
    if d==0 :
        zero_count=zero_count+1
    n=n//10 
    if  smallest>d:
        smallest=d
final=(zero_count+sum)*smallest
print(sum)
print(zero_count)
print(final)
print(smallest)
while i<final:
       if final%i==0:
          print("Not prime")
          break
       i=i+1
else:
    if final<=2:
        print("Not prime")
    else:
        print("prime")



