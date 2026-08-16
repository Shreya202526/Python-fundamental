'''63Count frequency of each character. S = "aabcc" a: 2, b: 1, c: 2'''

s=input("enter the string=")
result=""
for i in range(len(s)):
    c=0
    if s[i] not in result:
        result+=s[i]
        for j in range(len(s)):
         if s[i]==s[j]:
            c+=1  
        print(s[i],":",c,end=" ")