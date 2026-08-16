'''30Replace a word with another word. S = "old data", Old="old", New="new" "new data"'''

s=input("Enter the String:")
old=input("Old data:")
new=input("new data:")
result=""
new_string=s.split()
for x in new_string:
    if old==x:
        result+=new+" "
    else:
        result+=x+" "
print(result)