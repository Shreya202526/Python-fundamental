'''24Check if all characters in a string are unique. S1 = "abc", S2 = "abca" S1: True, S2: False'''
s1='abc'
s2='abca'
result=""
count=0
unique=True
for i in s1:
     if i in result:
       count+=1
     else:
        result+=i
if count>=1:
    unique=False
print("S1:",unique)
print(result)
for i in s2:
     if i in result:
       count+=1
     else:
        result+=i
if count>=1:
    unique=False
print("S2:",unique)
print(result)
    

