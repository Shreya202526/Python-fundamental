'''4.

Find All Characters with Maximum Frequency
Website Traffic Analysis System

A web analytics company tracks user activity symbols in server logs.

The company wants to identify all characters having the maximum frequency in the given string.

Input:
aabbbccddd
Output
b d'''


s=input("Input:")
c=0
for i in s:
    count=0
    for j in s:
        if i==j:
            count+=1
    if count>c:
        c=count
        print(count)
stored=""
for i in s:
    count=0
    for j in s:
        if i==j:
            count=count+1
    if count==c and i not in stored:
        print(i,end=" ")
        stored=stored+i
       
        


