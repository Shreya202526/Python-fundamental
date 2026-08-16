'''5. Equilibrium Index Finder
===========================

Scenario

Find an index where:

# Sum of elements on the left side

Sum of elements on the right side

Requirements

* Read N and list elements from user
* Find equilibrium index
* If not found, display message

Test Case 1

Input:
[1, 3, 5, 2, 2]

Output:
Equilibrium Index = 2

Explanation:
1 + 3 = 2 + 2

Test Case 2

Input:
[1, 2, 3]

Output:
No Equilibrium Index Found

---

===================================================================='''

n=int(input("enter size:"))
arr=[]
print("Enter the number one by one")
for i in range(n):
     arr.append(int(input()))
found=False
for k in range(len(arr)):
 left=0
 right=0
 for i in range(k):
   left+=arr[i]
 for j in range(k+1,len(arr)):
   right+=arr[j]
 if left==right:
     print("Equilibrium index",k)
     found=True
     break
if found==False:
   print("No Equilibrium found")


          