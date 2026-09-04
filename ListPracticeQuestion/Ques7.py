'''Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.
Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]
Output: 1

'''
s=int(input("Enter the elment of list:"))
list=list(map(int,input("Enter the element:" ).split(",")))
print(list)
'''i=0
for x in list:
    repeat=0
    for y in list:
        if x==y:
            repeat+=1
    if repeat==1 :
        i=x
print(i)
'''

for x in list:
    c=list.count(x)
    if c==1:
     print(x)





