'''43 Check if two strings are rotations of each other. S1 = "abcde", S2 = "cdeab" TRUE

s1=input("Enter the 1st string1:")
s2=input("Enter the 2nd string:")
s3=s1+s1
result=0
print(s3)  
for i in range(len(s3)):
    found=0
    for j in range(len(s2)):
     if s2==s3[i:j]:     
        found=1 
    if found==1:
       result=1
       break

print(result)

'''
s1=input("Enter the 1st string1:")
s2=input("Enter the 2nd string:")
l=len(s1)
result=False
new_str1=""
new_str2=""
for i in range(len(s1)//2,l):
    new_str1+=s1[i]
    print(new_str1)
for j in range(0,len(s1)//2):
    new_str2+=s1[j]
    print(new_str2)
s3=new_str1+new_str2
print(s3)
match=1
for k in range(len(s3)):
    if s3[k]!=s2[k]:
      match=0
      break
if match==1:
    result=True
print(result)

