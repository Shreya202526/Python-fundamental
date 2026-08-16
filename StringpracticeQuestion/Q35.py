'''35 Find the first palindrome word. S = "this madam is here" "madam"'''
s=input("Enter the string")
new_string=s.split()
result=""
for x in new_string:
    if x==x[::-1]:
        result=x
print(result)