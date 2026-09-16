'''90 Remove adjacent duplicates recursively. S = "azxxzy" "ay'''

s=input("enter the string: ")
result=[]
i=1
while i<len(s):
    if s[i-1]==s[i]:
        i=1
    else:
      s=s[:i]+s[i+2:]
      i+=1
print("".join(s))
