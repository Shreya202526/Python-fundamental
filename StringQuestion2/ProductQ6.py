'''6.

Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching'''


str1=input("Enter first product code=").upper()
str2=input("Enter second product code=").upper()
new_str1=""
new_str2=""
i=0
while i<len(str1):
      ch=str1[i]
      if ch>='A' and ch<='Z': 
         new_str1=new_str1+ch
      i=i+1
print("New String=",new_str1)
print(str1)
j=0
while j<len(str2):
      ch=str2[j]
      if ch>='A' and ch<='Z': 
         new_str2=new_str2+ch
      j=j+1
print("New String2",new_str2)
print(str2)
if len(new_str1)!=len(new_str2):
    print("Not matching")
else:
    visited=[]
    x=1
    i=0
    while i<len(new_str1):
          ch=new_str1[i]
          if ch not in visited:
            c1=0
            c2=0
            j=0
            while j<len(new_str1):
              if new_str1[j]==ch:
                 c1=c1+1
              j=j+1
            j=0
            while j<len(new_str2):
              if new_str2[j]==ch:
                 c2=c2+1
              j=j+1 
            if c1!=c2:
             x=0
             break
            visited.append(ch)
          i=i+1
if x==1:
   print("Both Codes are matching ")
else:
   print("Both Code are not matching")






