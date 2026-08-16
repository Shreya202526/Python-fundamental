'''50Remove all digits. S = "a1b2c3" "abc"'''
s=input("Enter the string=")
result=""
for i in range(len(s)):

    #if s[i]!="a" and s[i]!="e" and s[i]!="i" and s[i]!="o" and s[i]!="u" and s[i]!="A" and s[i]!="E" and s[i]!="I" and s[i]!="O" and s[i]!="U" :
    if s[i].isalpha():
        result+=s[i]
print(result)
