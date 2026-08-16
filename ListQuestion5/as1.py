''''1. Count Pairs with Difference K

A company records the ages of employees. Find how many pairs of employees have an age difference exactly equal to K.

Problem Statement:

Given an array of employee ages and an integer K, count the number of pairs whose absolute difference is K.

Example:

Input:

N = 5
K = 2
ages[] = {1, 5, 3, 4, 2}

Output:

3

Explanation:

(1,3), (3,5), (2,4)
'''


m=int(input("Enter the sizes of list"))
k=int(input("enter target difference"))
arr=[]
for i in range(m):
    x=int(input("Enter the elements of list"))
    arr.append(x)
print(arr) 
count=0
for i in range(m):
    for j in range(m):
        if arr[i]-arr[j]==k:
            count+=1
print("Number of pairs",count)