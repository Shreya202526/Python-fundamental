s=input("Enter the String:")
result=""
for i in range(len(s)):
     if s[i]>='a' and s[i]<='z':
          result=result+chr(ord(s[i])-32)
          print("RESULT",result)
     else:
          result=result+chr(ord(s[i])+32)
          print("result",result)
print(result)
          