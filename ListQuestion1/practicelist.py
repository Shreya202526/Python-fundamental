n=int(input("enter size="))
arr=[]
print("enter Elements one by one:")
for i in range(n):
    arr.append(int(input()))
print(arr)
peakindex=-1
for i in range(n):
    if i==0:
        if n==1 or arr[i]>=arr[i+1]:
            peakindex=i
            break
    elif i==n-1:
        if arr[i]>=arr[i-1]:
            peakindex=i
            break
    else:
        if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
            peakindex=i
            break
if peakindex!=-1:
    print("Peak index:",peakindex)
    print("value is:",arr[peakindex])