
'''*11. Count Occurrence of a Digit*
A system logs repeated digits in a number for pattern analysis and reporting.
Write a program to *count how many times a given digit appears in a number using loops*.

Input: Number = 122312, Digit = 2
Output: 3'''

'''num=int(input("number="))
count=0
digit=int(input("Digit="))
for i in range(len(str(num))):
        n=num%10
        if n==digit:
           count=count+1
        num=num//10
print(count)'''



num=int(input("number="))
count=0
digit=int(input("Digit="))
while num>0:
   n=num%10
   if n==digit:
      count=count+1
   num=num//10
print(count)

