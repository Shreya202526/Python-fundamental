'''78 Find the longest mirror-image substring at both ends. S = "aabccbaa" "aab"'''
s=input("Enter the String")
result=""
l=""
larg=0
for i in range(1):
    for j in range(i+1,len(s)):
        sub=s[i:j]
        print("Substring",sub)
        end=s[-len(sub):]
        rev=end[::-1]
        print("end",end)
        print("Mirror",rev)
        if sub==rev and len(sub)>len(l):
            result=sub
            larg=len(sub)
print(result)
