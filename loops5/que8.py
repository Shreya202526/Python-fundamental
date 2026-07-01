'''8.ATM Note Counter
A bank ATM dispenses ₹100 notes.
Write a program to:
- Read withdrawal amount
- Count how many ₹100 notes needed using loop
Input:
700
Output:
Notes = 7'''

n=int(input("Enter the number of notes="))
count=0
i=100
while n>=i:
    count=count+1
    n=n-i
    
print(count)


