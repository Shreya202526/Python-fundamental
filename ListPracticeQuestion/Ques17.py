'''Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]'''


arr=list(map(int,input("Enter the element of list: ").split(",")))
result=[]
print(arr)
for x in arr:
    sq=x**2
    result.append(sq)
new_result=sorted(result)
print((result))
print(new_result)

 