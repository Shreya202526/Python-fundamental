'''67 Count how many times a substring appears. S = "abab", Sub = "ab" 2'''

s=input("enter the string=")
sub=input("enter the substring=")
c=0
for i in range(len(s)):
    ch=s[i]
    match=0
    for j in range(i+1,len(s)+1):
        if s[i:j]==sub:
         match=1
         break
    if match==1:
        c+=1
print(c)

s=input("enter the string=")
sub=input("enter the substring=")
c=0
for i in range(len(s)):
    ch=s[i]
    match=1
    for j in range(i+1,len(s)-len(sub)+1):
        if s[i+j]!=sub:
         match=0
         break
    if match==1:
        c+=1
print(c)

       