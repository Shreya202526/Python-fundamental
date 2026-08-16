'''1.Find the Longest Substring Without Repeating Characters
Cybersecurity Session Tracking System

A cybersecurity company monitors user session IDs generated during secure login sessions.

To detect suspicious repeated patterns, the company wants a Python program that 
finds the longest substring containing no repeated characters.

Input:
abcabcbb
Output:
abc'''

s=input("Enter : ")

ans=""
for i in s :
    temp=""

    for j in s :
        if i != j :
            temp+=i
            break
    # print(temp)
    
    if temp not in ans:
        ans+=temp


print(ans)

