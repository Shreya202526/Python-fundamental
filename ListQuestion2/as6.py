'''6.
A security system logs employee entry IDs during a day.
Only prime-numbered IDs are considered valid VIP entries.
Tasks:

Extract all prime IDs from the list
Find the sum of prime IDs
Find the maximum prime ID
Count how many prime entries exist

Input:
A list of integers (may contain duplicates and non-prime numbers)

Example 1

Input:
[12, 5, 7, 9, 11, 14, 17]

Output:
Prime IDs = [5, 7, 11, 17]
Sum = 40
Max = 17
Count = 4

Example 2

Input:
[4, 6, 8, 10]

Output:
Prime IDs = []
Sum = 0
Max = -1
Count = 0'''


n=int(input("Enter the length of list="))
arr=[]
primelist=[]
sums=0
max=-1
for i in range(n):
    x=int(input("Enter the element="))
    arr.append(x)
for x in arr:
    for i in range(2,x):
     if x%i==0:
        break
    else:
       if x==1 :
          break
       else:
        primelist.append(x)
print(primelist,end=" ")
print()
if len(primelist)==0:
   print("Prime Ids",primelist)
   print("sum",sums)
   print("maximum",max)
   print("Count",len(primelist))
else:
 for x in primelist:
   sums+=x
   if x>max:
      max=x
 print("Sum",sums)
 print("maximum",max)
 print("Count",len(primelist))


