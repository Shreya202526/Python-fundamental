'''Given an integer array nums, you need to find one continuous subarray such that if 
you only sort 
this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

Return the shortest such subarray and output its length.

 

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole arrays
orted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:
'''
l=[2,6,4,8,10,9,15]
left=-1
right=-1
ans=[]
for i in range(1,len(l)):
    if l[i-1]>l[i]:
        if left==-1:
            left=i-1
        right=i
print(left,right)
ans=l[left:right+1]
print(ans)
print(len(ans))