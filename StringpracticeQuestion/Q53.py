'''53 Remove all punctuation characters. S = "Hello, world!" "Hello world"'''
s=input("Enter the String=")
result=""
for i in range(len(s)):
     if s[i]>='a' and s[i]<='z' or s[i]>="0" and s[i]<="9" or   s[i]>='A' and s[i]<='Z' or s[i]==" ":
             result+=s[i]
print(result)