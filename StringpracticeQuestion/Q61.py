'''61 Count total alphabets, digits, and special characters. S = "a1b!c2" Alphabets: 3, Digits: 2, Special: 1'''
s=input("Enter the string=")
char=0
digit=0
sp=0
for i in range(len(s)):
    ch=s[i]
    if ch>="a" and ch<="z" or ch>="A" and ch<="Z":
        char+=1
    elif ch>="0" and ch<="9":
        digit+=1
    else:
        sp+=1
print(f"Alphabets:{char}, Digits:{digit}, Special:{sp}")