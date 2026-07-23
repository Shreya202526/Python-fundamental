'''8. Count Multiples of 5 Between Two Numbers
A supermarket gives coupons to customers whose token numbers are multiples of 5. The manager enters a token range and wants to know how many eligible token numbers exist.
Write a program to count numbers divisible by 5 between two given numbers using loops.

Input:
1 20

Output:
Count = 4'''

a,b=map(int,input("Enter a number:").split(","))
counter=0
while a<=b:
      if a%5==0:
         counter=counter+1
         print(a,end=" ")
      a=a+1
print("Count=",counter)



a,b=map(int,input("Enter a roll number range:").split(","))
counter=0
for i in range(a,b+1):
      if a%5==0:
         counter=counter+1
         print(a,end=" ")
      a=a+1
print("Count=",counter)
