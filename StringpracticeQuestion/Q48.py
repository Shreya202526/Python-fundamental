'''48
Remove all vowels. S = "aeiou XYZ" " XYZ"'''

s=input("Enter the string=")
result=""
for i in range(len(s)):

    #if s[i]!="a" and s[i]!="e" and s[i]!="i" and s[i]!="o" and s[i]!="u" and s[i]!="A" and s[i]!="E" and s[i]!="I" and s[i]!="O" and s[i]!="U" :
    if s[i] not in "aeiouAEIOU" :
        result+=s[i]
print(result)
