'''5. Next Prime ID Generator – Smart Version
A company gives prime numbered employee IDs to premium staff.
Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3'''


n=int(input("enter the number="))
num=n+1
while True:
       print("num pri: ",num)
       for i in range(2,num//2+1):
        if num%i==0:
           num=num+1
           break
       else:
            next=num
            print("Next prime ID",next)
            break
diff=next-n
print("Gap=",diff)