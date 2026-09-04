'''You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order
Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0]'''

n=int(input("Enter the number: "))
arr=[]
k=0
for i in range(1,n+1):
    print(f"Enter the value of element {i} :",end=" ")
    arr.append(int(input()))
print(arr)
for i in range(n-1,-1,-1):
    if arr[i]==9:
        arr[i]=0
    else:
        print(f"{arr[i]}={arr[i]+1}")
        arr[i]=arr[i]+1
        break
print(arr)
if n==1:
    arr.insert(0,1)
print(arr)
    


