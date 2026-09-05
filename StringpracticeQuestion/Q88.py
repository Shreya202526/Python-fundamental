'''88 Rearrange a string so that identical characters are at least d distance apart. S = "aaabc", d = 2 "abaca"'''

s=input("Enter the string:")
d=int(input("distance: "))
iden=""
non_ide=""
result=[""]*len(s)
for x in s:
    if s.count(x)==1:
        iden+=x
    else:
        non_ide=x
print(iden)
print(non_ide)
i=0
while i<len(s):
    result[i]=non_ide
    i+=d
print(result)
j=0
for x in iden:
    while result[j]!="":
        j+=1
    result[j]=x
print(" ".join(result))

