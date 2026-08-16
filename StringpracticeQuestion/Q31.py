'''31 Remove duplicate words. S = "the cat and the dog" "the cat and dog"'''
s=input("Enter the string")
new_str=s.split()
result=""
for x in new_str:
    if x not in result:
        result+=x+" "
print(result)