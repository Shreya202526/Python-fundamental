'''22Find the last repeating character. S = "abracadabra" r'''

s=input("Input:")
temp=""
for x in s:
    c=0
    for y in s:
        if x==y:
           c+=1
    if c>1:
     temp=x
     
print(temp)

    