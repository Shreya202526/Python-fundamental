'''====================================================================
6. Product Except Self
======================

Scenario

For every element, calculate the product of all other elements except itself.

Requirements

* Read N and list elements from user
* Create a new list containing products
* Display the result

Test Case 1

Input:
[1, 2, 3, 4]

Output:
[24, 12, 8, 6]

Test Case 2

Input:
[2, 3, 5]

Output:
[15, 10, 6]

---
'''
n=int(input("enter size:"))
arr=[]
new_list=[]

print("Enter the number one by one")
for i in range(n):
     arr.append(int(input()))
found=False
for j in range(0,len(arr)):
    result=1
    for k in range(0,len(arr)):
        if k!=j:
            result*=arr[k]
    new_list.append(result)
print(new_list)

