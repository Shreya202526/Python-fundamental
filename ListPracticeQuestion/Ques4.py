'''Given a sorted array of distinct integers and a target value, return the index if the target is
 found. 
If not, return the index where it would be if it were inserted in order.
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 '''

n=int(input("Enter the number: "))
arr=[]
for i in range(1,n+1):
    print(f"Enter the value of element {i} :",end=" ")
    arr.append(int(input()))
print(arr)
target=int(input("Enter the target value: "))
for i in range(n):
    if arr[i]>=target:
        print("Answer:",i)
        break
else:
    print("Answer:",n)
        
        
