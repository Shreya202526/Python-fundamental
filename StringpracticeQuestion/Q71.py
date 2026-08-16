'''71 Print all substrings. S = "abc" "a, b, c, ab, bc, abc"'''

s=input("Enter the string")
c=0
substring=len(s)
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        sub=s[i:j]
        print(sub)
    