'''Reverse each word. S = "cat dog" "tac god"'''

s=input("Enter the string:")
new_string=s.split()
result=""
for x in new_string:
    result+=x[::-1]+" "
print(result)