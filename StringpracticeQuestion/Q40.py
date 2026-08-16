'''40 Search all occurrences of a word. S = "a b a b", Word = "b" 2, 6 (start indices)'''

s=input("Enter the String:")
char=input("Enter char")
found=True
for i in range(len(s)):
    if char==s[i]:
        if not found:
            print(",",end="")
        print(i,end="")
        found=False
