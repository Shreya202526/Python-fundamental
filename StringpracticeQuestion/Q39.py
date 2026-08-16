'''39Search all occurrences of a character. S = "banana", Char = 'a' 1, 3, 5 (indices)'''

s=input("Enter the String:")
char=input("Enter char")
found=True
for i in range(len(s)):
    if char==s[i]:
        if not found:
            print(",",end="")
        print(i,end="")
        found=False
