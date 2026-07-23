'''6. Sum of Factors
A puzzle-based game rewards users based on the sum of all factors of a chosen number. The system calculates the total score using all factors of the entered number.
Write a program to find sum of factors using loops.

Input:
6

Output:
Sum = 12'''


n=int(input("Enter the number:"))
counter=0
i=1
while i<n//2:
      if n%i==0:
         d=n
         counter=counter+d
      i=i+1
print("Sum:",counter)


n=int(input("Enter the number:"))
counter=0
for i in range(1,n//2):
      if n%i==0:
         d=n
         counter=counter+d
print("Sum:",counter)

