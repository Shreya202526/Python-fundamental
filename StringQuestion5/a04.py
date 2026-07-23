'''4.

Find All Characters with Maximum Frequency
Website Traffic Analysis System

A web analytics company tracks user activity symbols in server logs.

The company wants to identify all characters having the maximum frequency in the given string.

Input:
aabbbccddd
Output
b d'''


s=input("Enter input:")
c=0 
for i in s:
    count=0
    for j in s:
        if i==j:
         count+=1
    if count>c :
        c=count

print(c)
ans=c 
c=0       
for i in s:
    count=0
    x=0
    y=0
    for j in range():
        if i==j:
         count+=1
    if ans==count :
       x=1
    if x==1:
       print(i,end=" ")
       x=0   
       
        


