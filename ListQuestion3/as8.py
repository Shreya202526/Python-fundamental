'''====================================================================
8. Majority Element Detector
============================

Scenario

Find an element occurring more than N/2 times.

Requirements

* Read N and list elements from user
* Find majority element
* If not present, display appropriate message

Test Case 1

Input:
[2, 2, 1, 2, 3, 2, 2]

Output:
Majority Element = 2

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Majority Element Found

---'''


n=int(input("enter size:"))
arr=[]
result=0
print("Enter the number one by one")
for i in range(n):
     arr.append(int(input()))
for j in range(len(arr)):
    c=0
    for k in range(len(arr)):
          if arr[j]==arr[k]:
               c+=1
    if c>=n/2:
        result=arr[i]
if result==0:
     print("No majority Element ")
else:
  print("Majority Element",result)
    
          