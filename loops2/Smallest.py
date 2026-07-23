'''2. Smallest Digit in Number
A manufacturing company prints serial numbers on products. During quality testing, the scanner needs to detect the smallest digit in the serial number to verify coding standards.
Write a program to find the smallest digit in a number using loops.

Input:
57294

Output:
Smallest Digit = 2'''


n=int(input("Enter the number:"))
min=9
while n>0:
      d=n%10
      if d<=min:
         min=d
      n=n//10
print("Smallest digit:",min)


n=int(input("Enter the number:"))
min=9
for i in range(len(str(n))):
      d=n%10
      if d<=min:
         min=d
         n=n//10
print("Smallest digit:",min)


