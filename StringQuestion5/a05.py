'''.
Cybercrime Log Analysis System

A cybersecurity company monitors encrypted login activity stored as character-based security logs.

During investigation, analysts need to identify the last character that repeats in the log sequence.
This helps detect the most recent duplicated activity pattern before a possible security breach.

Write a Python program to find the last repeating character in a given string.

If no repeating character exists, print:

No repeating character found
Input:
abccdbefga
Output:
a'''


s=input("Enter input:")
c=0 

for i in s:
    count=0
    for j in s:
        if i==j:
         count+=1
    if count>c:
        c = count       

stored = ""
for i in s:
    count = 0
    for j in s:
        if i == j:
            count += 1
    if count == c and i not in stored:
        print(i, end=" ")
        stored = stored + i

