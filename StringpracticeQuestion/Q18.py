'''18Replace occurrences of a character. S = "apple", Old='p', New='x' "axxle"'''
s=input("Enter the String")
old=input("Old:")
new=input("New:")
result=""
for x in s:
    if old==x:
        result+=new
    else:
        result+=x
print(result)