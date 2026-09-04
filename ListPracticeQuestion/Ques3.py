'''Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The ord
Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 
0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
 '''

n=int(input("Enter the number of element of list= "))
val=int(input("Enter the value:"))
arr=[]
result=[]
k=0
for i in range(1,n+1):
    print(f"Enter the element {i} : ",end=" ")
    arr.append(int(input()))
print(arr)
if len(arr)==0:
    k=0
else:
    i=0
    for j in range(n):
        if arr[j]!=val:
           arr[i]=arr[j]
           i+=1
k=i
print("Size of array: ",k)
print("Sorted List:",arr[:k])



