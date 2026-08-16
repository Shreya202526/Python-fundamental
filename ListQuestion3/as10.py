'''====================================================================
10. Find Duplicate Numbers
==========================

Scenario

A company stores employee IDs in a list. Some IDs may appear more than once due to data entry errors.

Requirements

* Read N and list elements from user
* Find all duplicate numbers
* Store duplicates in another list
* Count total duplicate numbers
* Display duplicates in sorted order

Test Case 1

Input:
[1, 2, 3, 2, 4, 5, 1]

Output:
Duplicate Numbers = [1, 2]
Count = 2

Test Case 2

Input:
[10, 20, 30]

Output:
No Duplicate Numbers Found

---'''
n=int(input("enter size:"))
arr=[]
result=0
duplicate=[]
print("Enter the number one by one")
for i in range(n):
     arr.append(int(input()))
for j in range(len(arr)):
    c=0
    for k in range(len(arr)):
          if arr[j]==arr[k]:
               c+=1
    if c>=2:
        if arr[j] not in duplicate:
         duplicate.append(arr[j])
if len(duplicate)==0:
  print("No Duplicate Found")
else:
    print("Majority Element",duplicate)
    print("Count",len(duplicate))