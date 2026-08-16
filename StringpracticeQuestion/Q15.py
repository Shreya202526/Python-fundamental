'''5Find the last occurrence of a character. S = "banana", Char = 'a' 5 (index)'''
s=input("Input:")
char=input("Char:")
temp=""
for i in range(len(s)):
    if char==s[i]:
        temp=i
print("Index",temp)


