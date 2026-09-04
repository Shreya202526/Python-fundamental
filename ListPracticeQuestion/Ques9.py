'''Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.'''


num1=list(map(int,input("Enter the element of num1: ").split(",")))
num2=list(map(int,input("Enter the element of num2: ").split(",")))
print(num1)
print(num2)
n_list=[]
for i in num1:
    for j in num2:
          if i==j:
           n_list.append(i)
           break
print(n_list)

