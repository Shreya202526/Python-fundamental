'''You are given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.


 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]'''


n=int(input("Enter the number of element :"))
target=int(input("enter the target value"))
arr=[]

for i in range(1,n+1):
    print(f"Enter the element{i}:",end=" ")
    arr.append(int(input()))
print(arr)
index=[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
     if arr[i]+arr[j]==target:
        index.append(i)
        index.append(j)
        break
print(index)

