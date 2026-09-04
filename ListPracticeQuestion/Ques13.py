'''Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers 
in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]'''


'''nums=list(map(int,input("Enter the Element of list: ").split(",")))
print(nums)
b=[]
result=[]
for i in nums:
    if i not in b:
       b.append(i)
    b.sort()
print(b)
print(len(b))
for i in range(1,len(b)+1):
     if i!=b[i-1]:
        result.append(i)
print(result)
'''
nums=list(map(int,input("Enter the Element of list: ").split(",")))
print(nums)
b=[]
result=[]
for i in range(1,len(nums)+1):
    if i not in nums:
       b.append(i)
    b.sort()
print(b)