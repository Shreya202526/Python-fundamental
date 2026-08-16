'''77 Find the longest substring that appears at both ends. S = "abracadabra" "abra"'''
s=input("Enter the String")
result=""
l=""
larg=0
for i in range(1):
    for j in range(i+1,len(s)):
        sub=s[i:j]
        print("Substring",sub)
        end=s[-len(sub):]
        print("end",end)
        if sub==end and len(sub)>len(l):
            result=sub
            larg=len(sub)
print(result)

