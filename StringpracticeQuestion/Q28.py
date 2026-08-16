'''28Count occurrences of a word. S = "
", Word = "word" 3'''


s=input("Enter the string")
word=input("Enter the word")
count=0
for i in range(len(s)-len(word)+1):
    match=1
    for j in range(len(word)):
        if s[i+j]!=word[j]:
         match=0
         break
    if match==1:
        count+=1
print(count)


