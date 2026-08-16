'''n=int(input("Enter Size="))
arr=[]
i=0
while i<n:
    arr.append(int(input()))
    i=i+1
k=2
for i in range(k):
 last=arr[n-1]
 i=n-1
 while i>0:
    arr[i]=arr[i-1]
    i=i-1
    k=k-1
 arr[0]=last
print(arr)
'''

'''
n=int(input("enter size="))
k=int(input("enter target sum"))
arr=[]
print("enter array elements ")
for i in range(n):
    arr.append(int(input()))
count=0
for i in range(n):
    for j in range(i+1,n):
        if arr[i]+arr[j]==k:
            count=count+1
print("Count=",count)



a=[1,2,3,4,5]
b=[val*val for val in a if val>3 and  val%2==0]
print(b)

'''

