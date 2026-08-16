'''19Find the highest frequency character. S = "abracadabra" a'''

s=input("Enter the String ")
max=0
max_char=""
for x in s:
    c=0
    for y in s:
        if x==y:
            c+=1
            if c>max:
                max_char=x
print(max_char)