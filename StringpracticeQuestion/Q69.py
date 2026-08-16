'''69 Count how many times 'life' appears in a string. S = "life is life" 2'''
s=input("Enter the string=")
s2=input("Enter count word")
c=0
new_string=s.split()
for i in range(len(new_string)):
    if new_string[i]==s2:
        c+=1
print(c)