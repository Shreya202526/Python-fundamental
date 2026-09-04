'''65 Count palindromic substrings. S = "aaa" 6 (a, a, a, aa, aa, aaa)'''

s=input("enter the string=")
count=0
for i in range(len(s)):
    ch=s[i]
    a=""
    for j in range(i,len(s)):
        a=ch+s[j]
        b=a[::-1]
        if a==b:
            count+=1
print(count)


