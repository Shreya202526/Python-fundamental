'''16Count total occurrences of a character. S = "programming", Char = 'g' 2'''

s=input("Enter the string")
char=input("Enter the string")
count=0
for x in s:
    if char==x:
        count+=1
print(count)