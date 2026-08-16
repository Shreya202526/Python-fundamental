
'''29 Remove occurrences of a word. S = "a test b test c", Word = "test", Remove All "a b c"'''

'''
s=input("Enter the String")
word=input("Enter the word")
result=""
i=0
while i<len(s)-len(word)+1:
    match=1
    j=0
    while j<len(word):
        if s[i+j]!=word[j]:
            match=0
            break
        j=j+1
    if match==1:
     i=i+len(word)
     if i<len(s) or s[i]==" ":
        i=i+1
    else:
     result+=s[i]
     i=i+1
    
while i<len(s):
   result+=s[i]
   i=i+1
print(result)
print(len(result))
'''

s=input("Enter the String:")
word=input("Enter word")
result=""
new_string=s.split()
for x in new_string:
   if word!=x:
      result+=x+" "
print(result)
          






