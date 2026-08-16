'''====================================================================

1. First Non-Repeating Number
   ====================================================================

Scenario

An online voting system stores vote IDs in a list.

Find the first vote ID that appears only once.

Requirements

* Read N and list elements from user
* Find the first non-repeating number
* If no such number exists, display an appropriate message

Test Case 1

Input:
[4, 5, 1, 2, 1, 2, 4]

Output:
First Non-Repeating Number = 5

Test Case 2

Input:
[7, 7, 8, 8]

Output:
No Non-Repeating Number Found

---
'''

n=int(input("Enter Size="))
arr=[]
result=0
print("enter elements one by one:")
for i in range(n):
    arr.append(int(input()))
print(arr)
for i in range(len(arr)):
    c=0
    for j in range(len(arr)):
        if arr[i]==arr[j]:
         c+=1
    if c==1:
        result=arr[i]
        break
if result==0:
   print("no Non Reating Number found")
else:
   print(result)