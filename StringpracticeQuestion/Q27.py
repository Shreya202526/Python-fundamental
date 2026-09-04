
'''
27Find the last occurrence of a word. S = "Test this test", Word = "test" 15 (index)'''

s=input("Enter the String")
word=input("Enter the string")
count=0
result=""
for i in range(len(s)-len(word)+1):
    match=1
    for j in range(len(word)):
        if s[i+j]!=word[j]:
           match=0
           break
    if match==1:
       result=i+(len(word)+1)
print(result)
    
