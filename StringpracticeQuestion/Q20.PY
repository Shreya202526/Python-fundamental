'''20Find the lowest frequency character. S = "aabbcde" c', 'd', 'e' (any one or all)'''

s=input("Enter the String ")
min=len(s)
min_count=""
for x in s:
    c=0
    for y in s:
        if x==y:
           c+=1
    if c<min:
       min=c
       min_count=x
for x in s:
    c=0
    for y in s:
        if x==y:
           c+=1
    if c==min:
       min_count=x
       print(min_count,end=" ")
