'''6.Next Prime Cabin Number Generator
A luxury hotel gives only prime numbered cabins to VIP guests.
Manager enters the last allotted cabin number.
System must find the next available prime cabin number.
Write a program using loops.
Input:
24
Output:
Next Prime Cabin = 29'''
n=int(input("Enter the number="))
num=n+1
while True:
       i=2
       while i<num//2:
            if num%i==0:
               num=num+1
               break
            i=i+1
       else:
            print("Next Prime Cabin:",num)
            break
