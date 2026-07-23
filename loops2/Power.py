'''7. Power of a Number
A scientific calculator app is used by engineering students for repeated multiplication operations. It should calculate the value of a number raised to a given power.
Write a program to calculate n raised to power p using loops.

Input:
2 5

Output:
32'''


n,p=map(int,input("Enter n and p:").split(","))
power=1
i=1
while i<p:
      power=n**p
      i=i+1
print(power)


n,p=map(int,input("Enter n and p:").split(","))
power=1
i=1
for i in range(i,p):
      power=n**p
      i=i+1
print(power)
