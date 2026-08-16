'''7. Array Rotation Analyzer
==========================

Scenario

Rotate the array K times towards the right.

Requirements

* Read N and list elements from user
* Read K
* Rotate the array
* Display rotated array

Test Case 1

Input:
Array = [1, 2, 3, 4, 5]
K = 2

Output:
[4, 5, 1, 2, 3]

Test Case 2

Input:
Array = [10, 20, 30, 40]
K = 1

Output:
[40, 10, 20, 30]

---'''



n=int(input("Enter Size="))
arr=[]
i=0
while i<n:
    arr.append(int(input()))
    i=i+1
k=int(input("enter the rotation:"))
for i in range(k):
 last=arr[n-1]
 i=n-1
 while i>0:
    arr[i]=arr[i-1]
    i=i-1
    k=k-1
 arr[0]=last
print(arr)
