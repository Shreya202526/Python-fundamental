'''21Find the first non-repeating character. S = "aabbcde" c'''

s=input("Input:")
for x in s:
    c=0
    for y in s:
        if x==y:
           c+=1
    if c==1:
     print(x)
     break
else:
    print("All Repeated Character")