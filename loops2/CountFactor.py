'''5. Count Factors of Number
A mathematics learning app gives practice questions where students must know how many factors a number has. The app should automatically count the total factors of the entered number.
Write a program to count total factors of a number using loops.

Input:
12

Output:
Factors Count = 6'''


n=int(input("Enter the number:"))
counter=1
i=1
while i<=n//2:
      if n%i==0:
         counter=counter+1
      i=i+1
print("Counter:",counter)


n=int(input("Enter the number:"))
counter=1
for i in range(1,n//2+1):
      if n%i==0:
         counter=counter+1
print("Counter:",counter)



