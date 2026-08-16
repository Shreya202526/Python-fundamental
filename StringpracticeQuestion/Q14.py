'''14Find the first occurrence of a character. S = "banana", Char = 'a' 1 (index)'''


s=input("Input:")
char=input("Char:")
temp=""
for i in range(len(s)):
    if char==s[i]:
        temp=i
        break
print("Index",temp)


s = input("Input: ")
char = input("Char: ")

print(s.find(char))