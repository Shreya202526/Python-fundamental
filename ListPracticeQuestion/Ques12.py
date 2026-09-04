'''Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.'''


nums=list(map(int,input("Enter the element of list: ").split(",")))
print(nums)
max_sub_array=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)+1):
        sub_array=nums[i:j]
        sum_array=sum(sub_array)
        print(sub_array)
        print("Sum=",sum_array)
        if sum_array>max_sub_array:
            max_sub_array=sum_array
            max_array=sub_array
print("max sub array sum:",max_sub_array)
print("maximum subarray",max_array)


 