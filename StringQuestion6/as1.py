s=input("Enter the String : ")
s1=""
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
