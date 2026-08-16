'''55Reverse only vowels. S = "hello" "holle"'''
s=input("enter the string:")
vol=""
result=""
for i in range(len(s)):
    ch=s[i]
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        vol+=ch
print(vol)
vol2=vol[::-1]
j=0
for i in range(len(s)):
    ch=s[i]
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        result+=vol2[j]
        j+=1
    else:
        result+=ch
print(result)
