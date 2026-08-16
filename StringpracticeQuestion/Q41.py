'''41 Check if a string contains a substring (without using contains()). S1 = "Hello", Sub = "ell" TRUE'''
s=input("Enter the string")
sub=input("Enter sub")
found=False
for i in range(len(s)):
    match=True
    for j in range(len(s)-len(sub)+1):
     if s[i+j]!=sub[j]:
        match=False
        break
    if match==True:
       found=True
       break
print(found)
     

