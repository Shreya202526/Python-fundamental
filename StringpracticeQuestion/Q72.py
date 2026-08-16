'''72 Print all substrings of length n. S = "abc", n = 2 "ab, bc"'''

s=input("Enter the string")
n=int(input("Enter length of substring"))
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        sub=s[i:j]
        if len(sub)==n:
         print(sub)
