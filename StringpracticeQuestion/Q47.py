'''47 Check if one string is a substring of another using only concatenation. S1 = "CDAB", 
S2 = "ABCD" S1 is substring of S2S2 (ABCDABCD) → True
'''

s1=input("Enter the str1")
s2=input("Enter the str2")
s3=s2+s2
substring=False
for i in range(len(s3)-len(s1)+1):
    match=1
    for j in range(len(s1)):
        if s3[i+j]!=s1[j]:
            match=0
            break
    if match==1:
        substring=True
print(substring)