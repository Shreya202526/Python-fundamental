'''89 Remove 'b' and 'ac' from a string. S = "abacbb" "c" output=a'''

s=input("Enter the String:")
result=""
i=0
while i<len(s):
    if s[i]=="b":
        i+=1
    elif i+1<len(s) and s[i:i+2]=="ac":
       i+=2
    else:
      result+=s[i]
      i+=1
print(result)