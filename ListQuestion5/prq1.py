'''1. Count Pairs with Difference K

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


n=int(input("Enter the size of the list: "))
ages=[]
for i in range(n):
    print("Enter the element :")
    ages.append(int(input()))
print(ages)
k=int(input("Enter the value of k:"))
for i in range(len(ages)):
    for j in range(len(ages)):
     if abs(ages[i]-ages[j])==k:
       print(ages[i],ages[j])
       '''
         

