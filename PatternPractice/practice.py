'''s=input("Enter the String:")
words=s.split()
for i in range(0,len(words),1):
     w=words[i]
     rev=""
     for j in range(len(w)-1,-1,-1):
         rev=rev+w[j]
     print(rev,end=" ")'''


s=input("Enter the string:")
words=s.split()
rev=""
for j in range(len(words)-1,-1,-1):
         rev=words[j]+rev
print(rev,end=" ")

