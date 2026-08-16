'''====================================================================
4. Longest Consecutive Sequence
===============================

Scenario

Find the longest sequence of consecutive numbers present in the list.

Requirements

* Read N and list elements from user
* Find the length of the longest consecutive sequence
* Display the sequence length

Test Case 1

Input:
[100, 4, 200, 1, 3, 2]

Output:
Longest Consecutive Length = 4

Explanation:
Sequence = 1, 2, 3, 4

Test Case 2

Input:
[10, 11, 12, 20]

Output:
Longest Consecutive Length = 3

---'''

n=int(input("Enter Size="))
arr=[]
mising=0
c=0
print("enter elements one by one:")
for i in range(n):
    arr.append(int(input()))
    arr.sort()
print(arr)
for i in range(len(arr)):
  if arr[i]-arr[i-1]==1:
     c+=1
     
print("Longest consecutive count=",c)
