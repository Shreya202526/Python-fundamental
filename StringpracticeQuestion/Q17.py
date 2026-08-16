'''17Remove occurrences of a character. S = "banana", Char = 'a', Remove All "bnn'''

s=input("Enter the string")
char=input("Enter the string")
count=""
for x in s:
    if char!=x:
        count+=x
print(count)