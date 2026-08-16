'''42 Check if two strings are equal without using equals(). S1 = "abc", S2 = "abc" TRUE'''


s1=input("enter the string1:")
s2=input("enter the string2:")
result=False
match=1
if len(s1)!=len(s2):
    print("Not equal")
else:
  for i in range(len(s1)):
      if s1[i]!=s2[i]:
          match=0
          break
  if match==1:
       result=True
print(result)
          
            

