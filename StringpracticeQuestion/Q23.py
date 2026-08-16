
'''23 Print all characters that occur exactly twice. S = "aabbcdee" b', 'e'''

s=input("Input:")
temp=""
for x in s:
    c=0
    for y in s:
        if x==y:
           c+=1
    if c==2:
     if x not in temp:
      temp=temp+x+" "
print(temp)

    