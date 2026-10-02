'''# 4. Cloud Storage Duplicate File Name Resolver

A cloud storage company stores uploaded filenames from users.

Sometimes multiple duplicate filenames are uploaded.

The system should:

* Keep the first occurrence unchanged
* Add (1), (2), (3)... for duplicates

### Input:

text
file file image file image data


### Output:

text
file file(1) image file(2) image(1) data'''
'''
text="file file image file image data"

words=text.split()
count={}
ans=[]

for word in words:
    if word not in count:
        count[word]=0
        ans.append(word)
    else:
        count[word]+=1
        ans.append(word+f"({count[word]})")
print(" ".join(ans))

'''
    
s=input("Enter the String : ")
s1=""
word=s.split()
for i in word:
    word2=s1.split()
    print(word2)
    count=0
    for j in word2:
        if i==j:
            count+=1
            print(count)
    if count==0:
        s1+=i+" "
    else:
        s1+=i+" ("+ str( count )+") "            

print(s1)
