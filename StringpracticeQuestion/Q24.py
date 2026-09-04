'''24Check if all characters in a string are unique. S1 = "abc", S2 = "abca" S1: True, S2: False'''


'''s=input("Enter the String: ")
new=""
for i in s:
    c=0
    for j in s:
        if i==j:
            c+=1
    if c==1:
        new+=i
if new=="":
    print("No unique Chracter")
else:
    print("unique character",new)'''

s=input("Enter the String: ")
new=""
unique=True
for i in s:
    c=0
    for j in s:
        if i==j:
            c+=1
    if c>1:
        unique=False
        break
print("unique character",unique)


