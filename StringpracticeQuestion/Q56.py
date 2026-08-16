'''56Reverse only consonants. S = "apple" "eplpa"'''
s=input("enter the string:")
vol=""
result=""
for i in range(len(s)):
    ch=s[i]
    if ch!="a" and ch!="e" and ch!="i" and ch!="o" and ch!="u":
        vol+=ch
print(vol)
vol2=vol[::-1]
j=0
for i in range(len(s)):
    ch=s[i]
    if ch!="a" and ch!="e" and ch!="i" and ch!="o" and ch!="u":
        result+=vol2[j]
        j+=1
    else:
        result+=ch
print(result)
