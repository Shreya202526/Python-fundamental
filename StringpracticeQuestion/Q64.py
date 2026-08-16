'''64Count frequency of each vowel. S = "programming" o: 1, a: 1 (e, i, u: 0)'''
s=input("enter the string=")
result=""
for i in range(len(s)):
    ch=s[i]
    c=0
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
     if s[i] not in result:
        result+=s[i]
        for j in range(len(s)):
         if s[i]==s[j]:
            c+=1  
        if c>=1:
         print(s[i],":",c,end=" ")

