'''52Remove all special characters. S = "a!@b#c" "abc"'''

s=input("enter the string=")
result=""
for i in range(len(s)):
    if s[i]>='a' and s[i]<='z' or s[i]>="0"and s[i]<="9":
         result+=s[i]
print(result)