'''74 Find the longest substring without repeating characters. S = "abcabcbb" "abc"'''

s=input("Enter the String:")
longest=""
l=0
for i in range(len(s)):
    temp=""
    for j in range(i,len(s)):
        if s[j] in temp:
            break
        temp+=s[j]
        if len(temp)>l:
            l=len(temp)
            longest=temp
print(l)
print(longest)
