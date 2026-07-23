s=input("Enter the String=")
result=" "
i=0
while i<len(s):
      if i==0 or s[i-1]=="":
         if s[i]>='a' and s[i]<='z':
            result=result+chr(ord(s[i])-32)
         else:
            result=result+s[i]
      else:
           result=result+s[i]
      i=i+1
print(result)