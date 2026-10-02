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


'''print(ans)

s = input("Enter string: ")

longest = ""

for i in range(len(s)):
    current = ""

    for j in range(i, len(s)):
        if s[j] in current:
            break

        current += s[j]

    if len(current) > len(longest):
        longest = current

print(longest)'''



s=input("Enter the String : ")

s2=""
for i in range(0,len(s)):
    s1=""
    for j in range(i,len(s)):
        if s[j] not in s1:
            s1+=s[j]
        else:
            break 
    if len(s1)>len(s2):
        s2=s1
print(s2)    