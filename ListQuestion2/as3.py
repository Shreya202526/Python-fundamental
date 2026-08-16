'''3.
Industrial Sensor Peak Energy Monitoring System

Problem Statement

A factory machine records energy consumption at regular intervals.

A peak is defined as a value greater than or equal to its neighbors.

Tasks:

Find all peak energy values
Compute sum of squares of peak values
Compute average of peak values
Return difference between max peak and min peak
If no peaks, return -1

Test Case 1

Input:
energy = [20, 40, 30, 60, 50]

Output:
Peaks = [40, 60]
Sum of squares = 5200
Average = 50
Difference = 20

Test Case 2

Input:
energy = [10, 20, 15, 25, 20, 30]

Output:
Peaks = [20, 25, 30]
Sum of squares = 1525
Average = 25
Difference = 10

Test Case 3

Input:
energy = [5]

Output:
Peaks = [5]
Sum of squares = 25
Average = 5
Difference = 0'''

n=int(input("enter size"))
arr=[]
peak=[]
sums=0
sq=1
avg=0
sum1=0
print("Enter the element one by one=")
for i in range(n):
    arr.append(int(input()))
peak_index=-1
for i in range(n):
    if i==0:
        if n==1 or arr[i]>arr[i+1]:
            peak_index=i
            peak.append(arr[i])
    elif i==n-1:
        if arr[i]>arr[i-1]:
            peak_index=i
            peak.append(arr[i])
    else:
        if arr[i]>arr[i+1] or arr[i]>arr[i-1]:
            peak_index=i
            peak.append(arr[i])
print("Peak list=",peak)
for x in peak:
     sq=x**2
     sum1+=x
     sums+=sq
     avg=sum1//len(peak)
print("Sum of squares=",sums)
print("Average=",avg)
max=peak[0]
min=peak[0]
for x in peak:
    if x>max:
        max=x
    if x<min:
        min=x
diff=max-min
print("Difference=",diff)
