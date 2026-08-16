'''51Extract only digits. S = "a1b2c3" "123"'''
s=input("Enter the string=")
result=""
for i in range(len(s)):

    #if s[i]!="a" and s[i]!="e" and s[i]!="i" and s[i]!="o" and s[i]!="u" and s[i]!="A" and s[i]!="E" and s[i]!="I" and s[i]!="O" and s[i]!="U" :
    if s[i]>"0" and s[i]<="9":
        result+=s[i]
print(result)