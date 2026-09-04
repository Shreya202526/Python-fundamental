'''5.

Rearrange the array in alternating positive and negative items
Given an unsorted array Arr of N positive and negative numbers.
Your task is to create an array of alternate positive and negative numbers
without changing the relative order of positive and negative numbers.
Note: Array should start with positive number.

Example 1:
Input:
N = 9
Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
Output:
9 -2 4 -1 5 -5 0 -3 2
Example 2:
Input:
N = 10
Arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
Output:
5 -5 2 -2 4 -8 7 1 8 0'''
#take element of array and print array
n=int(input("Enter the sizes of list : "))
A=[]
for i in range(n):
    x=int(input(f"Enter the elements of list {i+1} : "))
    A.append(x)
print(A)
#separate positive and negative
negative=[]
positive=[]
result=[]
for i in range(n):
    if A[i]<0:
        negative.append(A[i])
    else:
        positive.append(A[i])
print(negative)
print(positive)
#print alternate element
flag=True
diff = abs(len(positive)-len(negative))
varr=min(len(positive),len(negative))
for i in range(varr):
        result.append(positive[i])
        result.append(negative[i])

'''for i in range(n-diff,len(positive)):
    result.append(positive[i])
print(result)'''
if len(positive)>len(negative):
 for i in range(diff,len(positive)):
     result.append(positive[i])
else:
    for i in range(diff,len(negative)):
         result.append(negative[i])
print("final result",result)

    


