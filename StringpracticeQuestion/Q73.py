'''73 Find the longest palindromic substring. S = "babad" "bab" (or "aba")'''

s=input("Enter the string")
longest=""
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        sub=s[i:j]
        rev=sub[::-1]
        print("rev",rev)
        print("sub",sub)
        if sub==rev and len(rev)>=len(longest):
          longest=sub

print("longest",longest)
